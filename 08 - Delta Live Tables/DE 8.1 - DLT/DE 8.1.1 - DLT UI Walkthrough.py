# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md <i18n value="1fb32f72-2ccc-4206-98d9-907287fc3262"/>
# MAGIC 
# MAGIC 
# MAGIC # Delta Live Tables UI 사용하기
# MAGIC 
# MAGIC 이 데모에서는 DLT UI를 살펴봅니다.
# MAGIC 
# MAGIC 
# MAGIC ## 학습 목표
# MAGIC 이 단원을 마치면 다음을 수행할 수 있습니다:
# MAGIC * DLT 파이프라인 배포
# MAGIC * 결과 DAG 탐색
# MAGIC * 파이프라인 업데이트 실행
# MAGIC * 지표 살펴보기

# COMMAND ----------

# MAGIC %md <i18n value="c950ed75-9a93-4340-a82c-e00505222d15"/>
# MAGIC 
# MAGIC 
# MAGIC ## 환경 설정 
# MAGIC 
# MAGIC 다음 셀은 이 데모를 재설정하도록 구성됩니다.

# COMMAND ----------

# MAGIC %run ../../Includes/Classroom-Setup-08.1.1

# COMMAND ----------

# MAGIC %md <i18n value="0a719ade-b4b5-49b5-89bf-8fc2b0b7d63c"/>
# MAGIC 
# MAGIC 
# MAGIC 다음 구성 단계에서 사용될 값을 인쇄하려면 다음 셀을 실행하십시오.

# COMMAND ----------

DA.print_pipeline_config()

# COMMAND ----------

# MAGIC %md <i18n value="71b010a3-80be-4909-9b44-6f68029f16c0"/>
# MAGIC 
# MAGIC ## 파이프라인 생성
# MAGIC 
# MAGIC 이 섹션에서는 코스웨어와 함께 제공된 노트북을 사용하여 파이프라인을 생성합니다. 다음 레슨에서 노트북의 내용을 살펴보겠습니다.
# MAGIC 
# MAGIC 단계:
# MAGIC 1. 사이드바에서 **Workflows** 버튼을 클릭하고 **Delta Live Tables** 탭을 클릭한 다음 **Create Pipeline**을 클릭합니다.
# MAGIC 2. 아래 지정된 파이프라인 설정을 구성합니다.
# MAGIC 
# MAGIC    **참고:** 설정 중 일부를 구성하려면 위의 셀 출력에 제공된 값이 필요합니다.
# MAGIC    
# MAGIC 
# MAGIC | Setting | Instructions |
# MAGIC |--|--|
# MAGIC | Pipeline name | 상단 셀에 출력된 **Pipeline Name** 값 |
# MAGIC | Product edition |  **Advanced** 선택 |
# MAGIC | Pipeline mode | **Triggered** 선택|
# MAGIC | Cluster policy | 상단 셀에 출력된 **Policy** 값 |
# MAGIC | Notebook libraries | 상단 셀에 출력된 **Notebook Path** 를 붙여넣거나, Navigator 를 통해서 검색 |
# MAGIC | Storage location | 상단 셀에 출력된 **Storage Location** 붙여넣기 |
# MAGIC | Target schema | 상단 셀에 출력된 **Target** 데이터베이스 이름 붙여넣기 |
# MAGIC | Cluster mode | auto scaling 을 disable 하기 위한  **Fixed size** 선택  |
# MAGIC | Workers |  Single Node cluster를 사용하기 위해 **0** 입력  |
# MAGIC | Photon Acceleration | 사용 하기 위해서 Check  |
# MAGIC | Configuration | 추가 세팅 확인하기 위해서 **Advanced** 클릭 <br> **Add Configuration**를 클릭하여 아래 표의 #1번 행에 대한 **Key** 및 **Value**를 입력.<br>**Add Configuration**를 클릭하여 아래 표에서 #2번 행의 **Key** 및 **Value** 를 입력 |
# MAGIC | Channel |  현재 runtime 버젼을 사용하기 위해서 **Current** 선택  |
# MAGIC 
# MAGIC | Configuration | Key                 | Value                                      |
# MAGIC | ------------- | ------------------- | ------------------------------------------ |
# MAGIC | #1            | **`spark.master`**  | **`local[*]`**                             |
# MAGIC | #2            | **`datasets_path`** | 상단 셀에서 제공된 **Datasets Path** |
# MAGIC 
# MAGIC 마지막으로, **Create** 클릭.
# MAGIC 
# MAGIC 
# MAGIC 파이프라인 설정에 대한 몇 가지 참고 사항:
# MAGIC 
# MAGIC - **Pipeline mode** - 이것은 파이프라인이 실행되는 방법을 지정합니다. 대기 시간 및 비용 요구 사항에 따라 모드를 선택합니다
# MAGIC   - `Triggered` 파이프라인은 한 번 실행된 후 다음 수동 또는 예약 업데이트까지 종료된 상태로 유지됩니다.
# MAGIC   - `Continuous` 파이프라인은 지속적으로 실행되어 새로운 데이터가 도착하면 수집합니다.
# MAGIC - **Notebook libraries** - 지금 문서는 표준 Databricks Notebook이지만 SQL 구문은 DLT 테이블 선언에 특화되어 있습니다. 다음 연습에서 구문을 살펴보겠습니다.
# MAGIC - **Storage location** - 이 선택적 필드를 통해 사용자는 파이프라인 실행과 관련된 로그, 테이블 및 기타 정보를 저장할 위치를 지정할 수 있습니다. 지정하지 않으면 DLT가 자동으로 디렉토리를 생성합니다.
# MAGIC - **Target** - 이 선택적 필드를 지정하지 않으면 테이블이 메타스토어에 등록되지 않습니다. 하지만 DBFS에서 계속 사용할 수 있습니다. 해당 옵션에 대한 상세 정보는 <a href="https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-user-guide.html#publish-tables" target="_blank">문서</a> 를 확인하세요.
# MAGIC - **Cluster mode**, **Min Workers**, **Max Workers** - 해당 필드는 파이프라인을 처리하는 기본 클러스터의 Worker 구성을 제어합니다. 본 실습에서는 작업자 수를 0으로 설정합니다. 이는 위에서 정의한 **spark.master** 매개 변수와 함께 작동하여 클러스터를 단일 노드 클러스터로 구성합니다..

# COMMAND ----------

DA.validate_pipeline_config()

# COMMAND ----------

# MAGIC %md <i18n value="a7e4b2fc-83a1-4509-8269-9a4c5791de21"/>
# MAGIC 
# MAGIC 
# MAGIC ## Pipeline 실행
# MAGIC 
# MAGIC 파이프라인이 생성되면 이제 파이프라인을 실행합니다.
# MAGIC 
# MAGIC 1. **Development**을 선택하여 개발 모드에서 파이프라인을 실행합니다.
# MAGIC    * 개발 모드는 클러스터를 재사용하고(실행할 때마다 새 클러스터를 만드는 것과 반대로) 오류를 쉽게 식별하고 오류를 수정할 수 있도록 재시도를 비활성화하여 보다 신속한 반복 개발을 제공합니다.
# MAGIC    * 이 기능에 대한 자세한 내용은  <a href="https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-user-guide.html#optimize-execution" target="_blank" >문서</a>를 참조하십시오.
# MAGIC 2. **Start**을 클릭합니다.
# MAGIC 
# MAGIC 클러스터가 프로비저닝되는 동안 초기 실행은 몇 분 정도 걸립니다.

# COMMAND ----------

# MAGIC %md <i18n value="4b92f93e-7a7f-4169-a1d2-9df3ac440674"/>
# MAGIC 
# MAGIC 
# MAGIC ## DAG 탐색
# MAGIC 
# MAGIC 파이프라인이 완료되면 실행 흐름이 그래프로 표시됩니다.
# MAGIC 
# MAGIC 테이블을 선택하면 세부 정보를 검토합니다.
# MAGIC 
# MAGIC **sales_orders_cleaned**를 선택합니다. **Data Quality** 섹션에 보고된 결과를 확인하십시오. 이 흐름에는 데이터에 대한 기대치가 선언되어 있으므로 해당 메트릭이 여기에서 추적됩니다. 위반 레코드가 결과에 포함될 수 있도록 허용하는 방식으로 제약 조건이 선언되기 때문에 레코드가 삭제되지 않습니다. 해당 부분은 다음 실습에서 더 자세히 다룰 것입니다.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
