# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md <i18n value="2eb97b71-b2ab-4b68-afdc-1663ec49e9d4"/>
# MAGIC 
# MAGIC # Lab: SQL Notebook을 Delta Live 테이블로 마이그레이션
# MAGIC 
# MAGIC 이 노트북은 Lab 실습의 전체 구조를 설명하고, 랩 환경을 구성하고, 시뮬레이션된 데이터 스트리밍을 제공하고, 완료되면 정리를 수행합니다. 이와 같은 노트북은 일반적으로 프로덕션 파이프라인 시나리오에서 필요하지 않습니다.
# MAGIC 
# MAGIC ## 학습 목표
# MAGIC 이 실습을 마치면 다음을 수행할 수 있습니다.
# MAGIC * 기존 데이터 파이프라인을 델타 라이브 테이블로 변환

# COMMAND ----------

# MAGIC %md <i18n value="782da0e9-5fc2-4deb-b7a4-939af49e38ed"/>
# MAGIC 
# MAGIC 
# MAGIC ## 사용되는 데이터 셋
# MAGIC 
# MAGIC 이 데모는 인위적으로 생성된 단순화된 의료 데이터를 사용합니다. 두 데이터 세트의 스키마는 다음과 같습니다. 다양한 단계에서 이러한 스키마를 조작할 것입니다.
# MAGIC 
# MAGIC #### Recordings
# MAGIC 기본 데이터 세트는 JSON 형식으로 제공되는 의료 기기의 심박수 기록을 사용합니다.
# MAGIC 
# MAGIC | Field | Type |
# MAGIC | --- | --- |
# MAGIC | device_id | int |
# MAGIC | mrn | long |
# MAGIC | time | double |
# MAGIC | heartrate | double |
# MAGIC 
# MAGIC #### PII
# MAGIC 이러한 데이터는 나중에 이름으로 환자를 식별하기 위해 외부 시스템에 저장된 환자 정보의 정적 테이블과 결합됩니다.
# MAGIC 
# MAGIC | Field | Type |
# MAGIC | --- | --- |
# MAGIC | mrn | long |
# MAGIC | name | string |

# COMMAND ----------

# MAGIC %md <i18n value="b691e21b-24a5-46bc-97d8-a43e9ae6e268"/>
# MAGIC 
# MAGIC 
# MAGIC ## 시작하기
# MAGIC 
# MAGIC 랩 환경을 구성하려면 다음 셀을 실행하여 시작하십시오.

# COMMAND ----------

# MAGIC %run ../../Includes/Classroom-Setup-08.2.1L

# COMMAND ----------

# MAGIC %md <i18n value="c68290ac-56ad-4d6e-afec-b0a61c35386f"/>
# MAGIC 
# MAGIC 
# MAGIC ## 초기 데이터 적재
# MAGIC 진행하기 전에 더 많은 데이터로 랜딩 존을 시드하십시오.
# MAGIC 
# MAGIC 나중에 추가 데이터를 가져오려면 이 명령을 다시 실행합니다.

# COMMAND ----------

DA.data_factory.load()

# COMMAND ----------

# MAGIC %md <i18n value="7cb98302-06c2-4384-bdf7-2260cbf2662d"/>
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
# MAGIC | #3.           | **`source`**.       | 상단 셀에서 제공된 **source** | 
# MAGIC 
# MAGIC 마지막으로, **Create** 클릭.

# COMMAND ----------

DA.validate_pipeline_config()

# COMMAND ----------

# MAGIC %md <i18n value="3340e93d-1fad-4549-bf79-ec239b1d59d4"/>
# MAGIC 
# MAGIC ## DLT 파이프라인 노트북 열어서 완료 하기
# MAGIC 
# MAGIC 여러분은 궁극적으로 파이프라인으로 배포하게될 노트북 [DE 8.2.2L - Migrating a SQL Pipeline to DLT Lab]($./DE 8.2.2L - Migrating a SQL Pipeline to DLT Lab),<br/> 에서 작업을 수행합니다.
# MAGIC 노트북을 열고 제공된 가이드라인에 따라 <br/> 이전 섹션에서 작업한 것과 유사한 다중 홉 아키텍처를 구현합니다.

# COMMAND ----------

# MAGIC %md <i18n value="90a66079-16f8-4503-ab48-840cbdd07914"/>
# MAGIC 
# MAGIC 
# MAGIC ## 파이프라인 수행하기
# MAGIC 
# MAGIC 여러 실행에서 동일한 클러스터를 재사용하여 개발 수명 주기를 가속화하는 **Development** 모드를 선택하세요.<br/>
# MAGIC 개발 모드는 작업이 실패하면 자동 재시도를 끕니다.
# MAGIC 
# MAGIC **Start**을 클릭하여 테이블에 대한 첫 번째 업데이트를 시작합니다.
# MAGIC 
# MAGIC Delta Live Tables는 필요한 모든 인프라를 자동으로 배포하고 모든 데이터 세트 간의 종속성을 해결합니다.
# MAGIC 
# MAGIC **NOTE**: 첫 번째 테이블 업데이트는 인프라가 배포되고 테이블관의 관계를 구성하기 때문에 몇 분 정도 걸릴 수 있습니다.

# COMMAND ----------

# MAGIC %md <i18n value="d1797d22-692c-43ce-b146-1e0248e65da3"/>
# MAGIC 
# MAGIC 
# MAGIC ## 개발 모드에서 코드 문제 해결
# MAGIC 
# MAGIC 파이프라인이 처음 실패하더라도 절망하지 마십시오. Delta Live Tables는 개발 중이며 여러분들이 코드를 수정할때마다 오류 메시지는 항상 개선되고 있습니다.
# MAGIC 
# MAGIC 테이블 간의 관계는 DAG로 매핑되기 때문에 데이터 세트를 찾을 수 없다는 오류 메시지가 표시되는 경우가 많습니다.
# MAGIC 
# MAGIC 아래에서 DAG를 살펴보겠습니다.
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/dlt-dag.png">
# MAGIC 
# MAGIC 오류 메시지 **`Dataset not found: 'recordings_parsed'`**가 표시되면 몇 가지 원인이 있을 수 있습니다.
# MAGIC 1. **`recordings_parsed`** 를 정의하는 문법이 유효하지 않습니다.
# MAGIC 1. **`recordings_bronze`** 에서 읽는 오류가 있습니다.
# MAGIC 1. **`recordings_parsed`** 또는 **`recordings_bronze`** 에 오타가 있습니다.
# MAGIC 
# MAGIC 원인을 식별하는 가장 안전한 방법은 초기 수집 테이블에서 시작하여 반복적으로 테이블/뷰 정의를 DAG에 다시 추가하는 것입니다. 나중에 테이블/뷰 정의를 간단히 주석 처리하고 실행 사이에 주석 처리를 제거할 수 있습니다.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
