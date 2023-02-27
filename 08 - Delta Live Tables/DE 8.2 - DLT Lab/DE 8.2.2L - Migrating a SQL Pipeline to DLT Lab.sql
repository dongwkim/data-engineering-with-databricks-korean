-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC 
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>

-- COMMAND ----------

-- MAGIC %md <i18n value="cffedc4f-a6a4-4412-8193-46a7a8a6a213"/>
-- MAGIC 
-- MAGIC 
-- MAGIC # Lab : SQL 파이프라인을 델타 라이브 테이블로 마이그레이션
-- MAGIC 
-- MAGIC 이 노트북은 SQL을 사용하여 DLT 파이프라인을 구현하기 위해 작성됩니다.
-- MAGIC 
-- MAGIC **의도된** 것은 대화식으로 실행되는 것이 아니라 변경을 완료한 후 파이프라인으로 배포되는 것입니다.
-- MAGIC 
-- MAGIC 이 노트를 작성하는 데 도움이 되도록 <a href="https://docs.databricks.com/data-engineering/delta-live-tables/delta-live-tables-language-ref.html#sql " target="_blank">DLT 구문 문서</a>를 참고 하세요

-- COMMAND ----------

-- MAGIC %md <i18n value="01e06565-56e7-4581-8833-14bc0db8c281"/>
-- MAGIC 
-- MAGIC 
-- MAGIC ## Bronze Table 선언
-- MAGIC 
-- MAGIC 
-- MAGIC 시뮬레이션된 클라우드 소스에서 오토 로더를 사용하여 JSON 데이터를 점진적으로 수집하는 브론즈 테이블 **`recordings_bronze`** 를 선언합니다. 소스 위치는 이미 인수로 제공됩니다. 이 값을 사용하는 방법은 아래 셀에 설명되어 있습니다.
-- MAGIC 
-- MAGIC 이전에 했던 것처럼 두 개의 추가 컬럼을 포함합니다.
-- MAGIC * **`current_timestamp()`** 에 의해 반환된 타임스탬프를 기록하는 **`receipt_time`**
-- MAGIC * **`input_file_name()`** 에 의해 획득된 **`source_file`**

-- COMMAND ----------

-- TODO
CREATE <FILL-IN>
AS SELECT <FILL-IN>
  FROM cloud_files("${source}", "json", map("cloudFiles.schemaHints", "time DOUBLE, mrn INTEGER"))

-- COMMAND ----------

-- MAGIC %md <i18n value="57422f74-b830-4abb-b4a9-969d0ab90be6"/>
-- MAGIC 
-- MAGIC 
-- MAGIC ### PII File
-- MAGIC 
-- MAGIC 유사한 CTAS 구문을 사용하여 *healthcare/patient* 데이터 세트에 있는 CSV 데이터에 라이브 **테이블**을 만듭니다.
-- MAGIC 
-- MAGIC 이 소스에 대해 자동 로더를 올바르게 구성하려면 다음 추가 매개변수를 지정해야 합니다.
-- MAGIC 
-- MAGIC | option | value |
-- MAGIC | --- | --- |
-- MAGIC | **`header`** | **`true`** |
-- MAGIC | **`cloudFiles.inferColumnTypes`** | **`true`** |
-- MAGIC 
-- MAGIC <img src="https://files.training.databricks.com/images/icon_note_24.png"/> CSV 를 위한 AutoLoader 매개변수 구성은 <a href="https://docs.databricks.com/spark/latest/structured-streaming/auto-loader-csv.html" target="_blank">여기</a> 를 참고하세요.

-- COMMAND ----------

-- TODO
CREATE <FILL-IN> pii
AS SELECT *
  FROM cloud_files("${datasets_path}/healthcare/patient", "csv", map(<FILL-IN>))

-- COMMAND ----------

-- MAGIC %md <i18n value="3573b6a4-233a-4f23-a002-aab072eb5096"/>
-- MAGIC 
-- MAGIC 
-- MAGIC ## Silver Tables 선언
-- MAGIC 
-- MAGIC 실버 테이블 **`recordings_enriched`** 는 다음 필드로 구성됩니다:
-- MAGIC 
-- MAGIC | Field | Type |
-- MAGIC | --- | --- |
-- MAGIC | **`device_id`** | **`INTEGER`** |
-- MAGIC | **`mrn`** | **`LONG`** |
-- MAGIC | **`heartrate`** | **`DOUBLE`** |
-- MAGIC | **`time`** | **`TIMESTAMP`** (아래에 예시 제공) |
-- MAGIC | **`name`** | **`STRING`** |
-- MAGIC 
-- MAGIC 또한 이 쿼리는 환자의 이름을 얻기 위해 공통 **`mrn`** 필드의 **`pii`** 테이블과 내부 조인을 통해 데이터를 보강해야 합니다.
-- MAGIC 
-- MAGIC 잘못된 **`심박수`**(즉, 0보다 크지 않음)가 있는 레코드를 삭제하는 제약을 적용하여 품질 관리를 구현합니다.

-- COMMAND ----------

-- TODO
CREATE OR REFRESH STREAMING LIVE TABLE recordings_enriched
  (<FILL-IN add a constraint to drop records when heartrate ! > 0>)
AS SELECT 
  CAST(<FILL-IN>) device_id, 
  <FILL-IN mrn>, 
  <FILL-IN heartrate>, 
  CAST(FROM_UNIXTIME(DOUBLE(time), 'yyyy-MM-dd HH:mm:ss') AS TIMESTAMP) time 
  FROM STREAM(live.recordings_bronze)
  <FILL-IN specify an inner join with the pii table on the mrn field>

-- COMMAND ----------

-- MAGIC %md <i18n value="3b9309a8-9e1d-46a2-a0eb-e95fe698d23b"/>
-- MAGIC 
-- MAGIC 
-- MAGIC ## Gold Table
-- MAGIC 
-- MAGIC **`daily_patient_avg`** 골드 테이블 생성,  **`mrn`**, **`name`**, **`date`**  컬럼을 기준으로  **`recordings_enriched`** 를 집계
-- MAGIC 
-- MAGIC | Column name | Value |
-- MAGIC | --- | --- |
-- MAGIC | **`mrn`** | 소스 테이블에서 **`mrn`** |
-- MAGIC | **`name`** | 소스 테이블에서 **`name`**  |
-- MAGIC | **`avg_heartrate`** |  **`heartrate`** 의 평균 |
-- MAGIC | **`date`** |  **`time`** 에서 날짜 추출 |

-- COMMAND ----------

-- TODO
CREATE <FILL-IN> daily_patient_avg
  COMMENT <FILL-IN insert comment here>
AS SELECT <FILL-IN>

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
