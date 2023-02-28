# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md <i18n value="36722caa-e827-436b-8c45-3e85619fd2d0"/>
# MAGIC 
# MAGIC 
# MAGIC # Databricks Workflows 작업 오케스트레이션
# MAGIC 
# MAGIC Databricks 작업 UI에 대한 새로운 업데이트에는 작업의 일부로 여러 작업을 예약하는 기능이 추가되어 Databricks 작업이 대부분의 프로덕션 워크로드에 대한 오케스트레이션을 완전히 처리할 수 있습니다.
# MAGIC 
# MAGIC 여기서는 노트북 작업을 트리거된 독립 실행형 작업으로 예약하는 단계를 검토한 다음 DLT 파이프라인을 사용하여 후속 작업을 추가합니다.
# MAGIC 
# MAGIC ## 학습 목표
# MAGIC 이 단원을 마치면 다음을 수행할 수 있습니다.
# MAGIC * Databricks 워크플로 작업에서 노트북 작업 예약
# MAGIC * 클러스터 유형 간의 작업 예약 옵션 및 차이점 설명
# MAGIC * 작업 실행을 검토하여 진행 상황을 추적하고 결과를 확인합니다.
# MAGIC * Databricks 워크플로 작업에서 DLT 파이프라인 작업 예약
# MAGIC * Databricks Workflows UI를 사용하여 작업 간의 종속성 구성

# COMMAND ----------

# MAGIC %run ../../Includes/Classroom-Setup-09.1.1

# COMMAND ----------

# MAGIC %md <i18n value="f1dc94ee-1f34-40b1-b2ba-49de9801b0d1"/>
# MAGIC 
# MAGIC 
# MAGIC ## 파이프라인 생성 및 구성
# MAGIC 여기에서 만드는 데이터 파이프라인은 이전 단원의 파이프라인과 거의 동일합니다.
# MAGIC 
# MAGIC 이 단원에서는스케줄링된 작업의 일부로 이전 파이프라인을 사용합니다.
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
# MAGIC 
# MAGIC 3. 마지막으로, **Create** 클릭.
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"> **Note**: 이 파이프라인은 이 레슨의 뒷부분에서 작업에 의해 실행될 것이므로 직접 실행하지는 않겠지만, 정말 빨리 테스트하고 싶다면 지금 **Start** 버튼을 클릭해도 됩니다.

# COMMAND ----------

DA.validate_pipeline_config()

# COMMAND ----------

# MAGIC %md <i18n value="ed9ed553-77e7-4ff2-a9dc-12466e30c994"/>
# MAGIC 
# MAGIC ## 노트북 작업 예약
# MAGIC 
# MAGIC 작업 UI를 사용하여 여러 작업으로 워크로드를 오케스트레이션하는 경우 항상 단일 태스크를 스켸줄링하는 것으로 시작합니다.
# MAGIC 
# MAGIC 시작하기 전에 다음 셀을 실행하여 이 단계에서 사용된 값을 가져옵니다.

# COMMAND ----------

DA.print_job_config_task_reset()

# COMMAND ----------

# MAGIC %md <i18n value="8c3c501e-0334-412a-91b3-bf250dfe8856"/>
# MAGIC 
# MAGIC 여기에서 다음 노트북을 예약하는 것부터 시작하겠습니다.
# MAGIC 
# MAGIC 단계:
# MAGIC 1. 사이드바에서 **Workflows** 버튼을 클릭하고 **Jobs** 탭을 클릭한 다음 **Create Job** 버튼을 클릭합니다.
# MAGIC 2. 아래에 지정된 대로 작업 및 태스크를 구성합니다. 이 단계에서는 위의 셀 출력에 제공된 값이 필요합니다.
# MAGIC 
# MAGIC 
# MAGIC | Setting | Instructions |
# MAGIC |--|--|
# MAGIC | Task name |  **Reset** 입력 |
# MAGIC | Type | **Notebook** 선택|
# MAGIC | Source | **Workspace** 선택|
# MAGIC | Path | 네비게이터를 사용하여 위에 제공된 **Reset Notebook Path**을 선택하거나 입력합니다.  |
# MAGIC | Cluster | 드롭다운 메뉴의 **Existing All Purpose Clusters**에서 클러스터를 선택합니다. |
# MAGIC | Job name | 화면 왼쪽 상단에 위에 제공된 **Job Name**을 입력하여 작업 이름을 추가합니다(태스크가 아님). |
# MAGIC 
# MAGIC <br>
# MAGIC 
# MAGIC 3. **Create** 버튼 클릭.
# MAGIC 4. 오른쪽 상단에 있는 파란색 **Run now** 버튼을 클릭하여 작업을 시작합니다. 
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"> **Note**: all-purpose cluster를 선택하면 이것이 all-purpose cluster로 청구되는 방식에 대한 경고가 표시됩니다. 프로덕션 작업은 항상 워크로드에 적합한 크기의 새 작업 클러스터에 대해 예약되어야 합니다. 이는 훨씬 더 낮은 요금으로 청구되기 때문입니다. 

# COMMAND ----------

DA.validate_job_v1_config()

# COMMAND ----------

# MAGIC %md <i18n value="8ebdf7c7-4b4a-49a9-b9d4-25dff82ed169"/>
# MAGIC 
# MAGIC ## Databricks 작업의 Cron 예약
# MAGIC 
# MAGIC Jobs UI 오른쪽의 **Job Details** 섹션 바로 아래에 **Trigger** 섹션이 있습니다.
# MAGIC 
# MAGIC 일정 옵션을 탐색하려면 **Add Trigger** 버튼을 선택합니다.
# MAGIC 
# MAGIC **Trigger type**을 **None (Manual)** 에서 **Scheduled** 으로 변경하면 크론 예약 UI가 나타납니다.
# MAGIC 
# MAGIC 이 UI는 작업의 시간순 일정을 설정하기 위한 광범위한 옵션을 제공합니다. UI로 구성된 설정은 cron 구문으로 출력될 수도 있으며, UI로 사용할 수 없는 사용자 지정 구성이 필요한 경우 편집할 수 있습니다.
# MAGIC 
# MAGIC 지금은 작업을 **Manual** 예약으로 설정해 둡니다. 작업 세부 정보로 돌아가려면 **Cancel**를 선택하세요.

# COMMAND ----------

# MAGIC %md <i18n value="50665a01-dd6c-4767-b8ef-56ee02dbd9db"/>
# MAGIC 
# MAGIC ## Review Run
# MAGIC 
# MAGIC 현재 구성된 단일 노트북은 단일 노트북만 예약할 수 있었던 레거시 Databricks 작업 UI와 동일한 성능을 제공합니다.
# MAGIC 
# MAGIC 작업 실행을 검토하려면
# MAGIC 1. 화면 왼쪽 상단에서 **Runs** 탭을 선택합니다(현재 **Tasks** 탭에 있어야 함).
# MAGIC 1. **Start time** 컬럼 아래의 타임스탬프 필드를 클릭하여 출력 세부 정보를 엽니다.
# MAGIC 1. **작업이 계속 실행 중인 경우** **`Succeeded`** 또는 **`Pending`** 의 **Status**와 함께 노트북의 활성 상태가 표시됩니다. . **작업이 완료된** 경우  **`Succeeded`** 또는 **`Failed`**의 **Status**와 함께 노트북의 전체 실행이 표시됩니다.
# MAGIC   
# MAGIC 노트북은 매직 명령 **`%run`** 을 사용하여 상대 경로를 사용하여 추가 노트북을 호출합니다. 
# MAGIC 
# MAGIC 예약된 노트북의 실제 결과는 새 작업 및 파이프라인에 대한 환경을 재설정하는 것입니다.

# COMMAND ----------

# MAGIC %md <i18n value="3dbff1a3-1c13-46f9-91c4-55aefb95be20"/>
# MAGIC 
# MAGIC 
# MAGIC ## DLT 파이프라인을 작업으로 예약
# MAGIC 
# MAGIC 이 단계에서는 이 강의 시작 부분에서 구성한 작업이 성공한 후 실행할 DLT 파이프라인을 추가합니다.
# MAGIC 
# MAGIC 단계:
# MAGIC 1. 화면 왼쪽 상단에 현재 선택된 **Runs** 탭이 표시됩니다. **Taks** 탭을 클릭합니다.
# MAGIC 1. 화면 중앙 하단에 **+** 가 있는 큰 파란색 원을 클릭하여 새 작업을 추가합니다.
# MAGIC 1. 작업을 구성합니다.
# MAGIC      1. 작업 이름에 **DLT** 입력
# MAGIC      1. **Tyle**에서 **Delta Live Tables pipiline** 을 선택합니다.
# MAGIC      1. **Pipeline** 에서 이 연습에서 이전에 구성한 DLT 파이프라인을 선택합니다.<br/>
# MAGIC      1. **Depends on** 필드는 이전에 정의한 작업인 **Reset**으로 기본 설정됩니다. 이 값은 그대로 둡니다.
# MAGIC      1. 파란색 **Create task** 버튼을 클릭합니다.
# MAGIC 
# MAGIC 이제 2개의 상자와 그 사이에 아래쪽 화살표가 있는 화면이 표시됩니다.
# MAGIC 
# MAGIC **`Reset`** 작업이 맨 위에 있고 **`DLT`** 작업으로 이어집니다.
# MAGIC 
# MAGIC 이 시각화는 이러한 작업 간의 종속성을 나타냅니다.
# MAGIC 
# MAGIC **Run now** 을 클릭하여 작업을 실행합니다.
# MAGIC 
# MAGIC **Note**: 작업 및 파이프라인에 대한 인프라가 배포될 때까지 몇 분 정도 기다려야 할 수 있습니다.

# COMMAND ----------

DA.validate_job_v2_config()

# COMMAND ----------

# MAGIC %md <i18n value="4fecba69-f1cf-4413-8bc6-7b50d32b2456"/>
# MAGIC 
# MAGIC ## 다중 작업 실행 결과 검토
# MAGIC 
# MAGIC 상단의 **Runs** 탭을 다시 선택한 다음 작업 완료가 화면 아래 테이블에 표 형태로 표시됩니다
# MAGIC 
# MAGIC 작업에 대한 시각화는 실시간으로 업데이트되어 현재 실행 중인 작업을 반영하고 작업 실패가 발생하면 색상이 변경됩니다.
# MAGIC 
# MAGIC 태스크 상자를 클릭하면 UI에 예약된 노트북이 렌더링됩니다.
# MAGIC 
# MAGIC 이는 이전 Databricks 작업 UI 위에 추가된 오케스트레이션 계층으로 생각할 수 있습니다. CLI 또는 REST API로 작업을 예약하는 워크로드가 있는 경우 <a href="https://docs.databricks.com/dev-tools/api/latest/jobs.html" target="_blank">JSON 작업에 대한 결과를 구성하고 가져오는 데 사용되는 데이터 구조는 UI와 유사합니다.</a>
# MAGIC 
# MAGIC **NOTE**: 현재 작업으로 예약된 DLT 파이프라인은 Runs GUI에서 결과를 직접 렌더링하지 않습니다. 대신 예약된 파이프라인에 대한 DLT 파이프라인 GUI로 다시 안내됩니다.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
