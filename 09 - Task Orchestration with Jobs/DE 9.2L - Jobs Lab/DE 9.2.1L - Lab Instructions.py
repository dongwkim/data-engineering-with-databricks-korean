# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md <i18n value="51f698bd-880b-4a85-b187-9b96d8c2cf18"/>
# MAGIC 
# MAGIC # Lab: Databricks로 작업 오케스트레이션
# MAGIC 
# MAGIC 이 실습에서는 다음으로 구성된 멀티태스킹 작업을 구성합니다.
# MAGIC * 스토리지 디렉토리에 새로운 데이터를 저장하는 노트북
# MAGIC * 여러개의 테이블을 통해 이 데이터를 처리하는 델타 라이브 테이블 파이프라인
# MAGIC * 이 파이프라인에서 생성된 골드 테이블과 DLT에서 출력되는 다양한 지표를 쿼리하는 노트북
# MAGIC 
# MAGIC ## 학습 목표
# MAGIC 이 실습을 마치면 다음을 수행할 수 있습니다.
# MAGIC * Databricks 작업에서 노트북을 작업으로 예약
# MAGIC * Databricks 작업에서 DLT 파이프라인을 작업으로 예약
# MAGIC * Databricks Workflows UI를 사용하여 작업 간의 선형 종속성 구성

# COMMAND ----------

# MAGIC %run ../../Includes/Classroom-Setup-09.2.1L

# COMMAND ----------

# MAGIC %md <i18n value="b7163714-376c-41fd-8e38-80a7247fa923"/>
# MAGIC 
# MAGIC 
# MAGIC ## 초기 데이터 적재
# MAGIC 
# MAGIC 계속하기 전에 일부 데이터로 랜딩 존을 시드하십시오. 나중에 추가 데이터를 가져오려면 이 명령을 다시 실행합니다.

# COMMAND ----------

DA.data_factory.load()

# COMMAND ----------

# MAGIC %md <i18n value="6bc33560-37f4-4f91-910d-669a1708ba66"/>
# MAGIC 
# MAGIC ## 파이프라인 생성 및 구성
# MAGIC 
# MAGIC 여기에서 만드는 파이프라인은 이전 단원의 파이프라인과 거의 동일합니다.
# MAGIC 
# MAGIC 이 단원에서는 스케줄된 작업의 일부로 사용합니다.
# MAGIC 
# MAGIC 다음 셀을 실행하여 다음 구성 단계에서 사용될 값을 인쇄하십시오.

# COMMAND ----------

DA.print_pipeline_config()

# COMMAND ----------

# MAGIC 
# MAGIC 
# MAGIC %md <i18n value="71b010a3-80be-4909-9b44-6f68029f16c0"/>
# MAGIC 
# MAGIC ## 파이프라인 생성 및 구성
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
# MAGIC | #3            | **`source`** | 상단 셀에서 제공된 **Source** |
# MAGIC 
# MAGIC 3. 마지막으로, **Create** 클릭.
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"> **Note**: 이 파이프라인은 이 레슨의 뒷부분에서 작업에 의해 실행될 것이므로 직접 실행하지는 않겠지만, 정말 빨리 테스트하고 싶다면 지금 **Start** 버튼을 클릭해도 됩니다.

# COMMAND ----------

DA.validate_pipeline_config()

# COMMAND ----------

# MAGIC %md <i18n value="f98768ac-cbcc-42a2-8c51-ffdc3778aa11"/>
# MAGIC 
# MAGIC 
# MAGIC ## 노트북 작업 예약
# MAGIC 
# MAGIC 작업 UI를 사용하여 여러 태스크로 워크로드를 오케스트레이션하는 경우 항상 단일 태스크를 예약하는 것으로 시작합니다.
# MAGIC 
# MAGIC 시작하기 전에 다음 셀을 실행하여 이 단계에서 사용된 값을 가져옵니다.

# COMMAND ----------

DA.print_job_config()

# COMMAND ----------

# MAGIC %md <i18n value = "fab2a427-5d5a-4a82-8947-c809d815c2a3"/>
# MAGIC 
# MAGIC 여기서는 첫 번째 노트북을 스케줄링하는 것으로 시작합니다.
# MAGIC 
# MAGIC 단계 :
# MAGIC 1. 사이드 바에서 **Workflows** 버튼을 클릭하십시오.
# MAGIC 1. **Jobs** 탭을 선택하십시오.
# MAGIC 1. 파란색 **Create Job** 버튼을 클릭하십시오
# MAGIC 1. 태스크 구성 :
# MAGIC      1. 작업 이름에 대해 **Batch-Job** 를 입력하십시오
# MAGIC      1. **Type** 에서 **Notebook** 을 선택하십시오.
# MAGIC      1. **Source** 에서 **Workspace** 를 선택하십시오.
# MAGIC      1. **Path** 의 경우 위의 셀에 제공된 값 **Batch Notebook Path** 를 지정하십시오.
# MAGIC      1. **Existing All Purpose Clusters** 아래 **Cluster** 드롭 다운에서 클러스터를 선택하십시오.
# MAGIC      1. **Create** 를 클릭하십시오.
# MAGIC 1. 화면의 왼쪽 상단에서 위의 셀에 제공된 **`Job Name`** 값을 사용하여 작업의 이름을 지정하십시오 (태스크가 아님).
# MAGIC 1. 파란색 **Run now** 오른쪽 상단의 버튼을 클릭하여 작업을 시작하십시오.

# COMMAND ----------

# MAGIC %md <i18n value="1ab345ce-dff4-4a99-ad45-209793ddc581"/>
# MAGIC 
# MAGIC ## DLT 파이프 라인을 태스크로 스케줄링
# MAGIC 
# MAGIC 이 단계에서는 이전 셀에서 구성한 작업이 성공한 후에 실행될 DLT 파이프 라인을 추가합니다.
# MAGIC 
# MAGIC 단계 :
# MAGIC 1. **Tasks** 탭을 클릭하십시오.
# MAGIC 1. 화면 중앙 하단에 **+** 가있는 큰 파란색 원을 클릭하여 새 작업을 추가하십시오.
# MAGIC 1. 작업 구성 :
# MAGIC      1. 작업 이름에 대해 **DLT** 를 입력하십시오
# MAGIC      1. **Type** 을 위해 **Delta Live Table pipeline** 을 선택하십시오.
# MAGIC      1. **pipeline** 의 경우 이전에 구성했던 DLT 파이프 라인을 선택하십시오 <br/>
# MAGIC      1. **Depends on** 은 이전에 정의 된 작업 **Batch-Job** 이 기본값으로 정의됩니다. 
# MAGIC      1. 파란색 **Create task** 버튼을 클릭하십시오
# MAGIC 
# MAGIC 이제 2 개의 상자와 그 사이의 아래쪽 화살표가 있는 화면이 표시됩니다.
# MAGIC 
# MAGIC 여러분의  **`Batch-Job`** 작업은 상단에 있으며 **`dlt`** 작업으로 이어집니다.

# COMMAND ----------

# MAGIC %md <i18n value="dd4e16c5-1842-4642-8159-117cfc84d4b4"/>
# MAGIC 
# MAGIC ## 추가 노트북 작업을 스케줄링 하십시오
# MAGIC 
# MAGIC DLT 파이프 라인에 정의된 일부 DLT메트릭과 골드 테이블을 쿼리하는 추가 노트북이 제공되어 있습니다.
# MAGIC 
# MAGIC 우리는 이것을 우리의 파이프라인 작업에서 최종 작업으로 추가 할 것입니다.
# MAGIC 
# MAGIC 단계 :
# MAGIC 1. 화면 중앙 하단에 **+**가있는 큰 파란색 원을 클릭하여 새 작업을 추가하십시오.
# MAGIC 단계 :
# MAGIC 1. 작업 구성 :
# MAGIC      1. 작업 이름에 대해 **Query-Results** 를 입력하십시오
# MAGIC      1. **Type** 을 위해 **Notebook** 을 선택하십시오.
# MAGIC      1. **Path** 의 경우 위의 셀에 제공된 **Query Notebook Path** 값을 선택하십시오.
# MAGIC      1. **Existing All Purpose Clusters** 아래 **Cluster** 드롭 다운에서 클러스터를 선택하십시오.
# MAGIC      1. **Depends on**은 이전에 정의 된 작업에 대한 기본값으로 표시됩니다.
# MAGIC      1. 파란색 **Create task** 버튼을 클릭하십시오
# MAGIC     
# MAGIC 이 작업을 실행하려면 화면 오른쪽 상단에있는 파란색 **Run now** 버튼을 클릭하십시오.
# MAGIC 
# MAGIC 화면 상단 **Runs** 탭을 클릭 후 시각적으로 작업 진행 상황을 추적 할 수 있습니다.
# MAGIC 
# MAGIC 모든 작업이 성공하면 각 작업의 내용을 검토하여 결과값을 확인하십시오.

# COMMAND ----------

DA.validate_job_config()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
