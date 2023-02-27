-- Databricks notebook source
-- MAGIC %md-sandbox
-- MAGIC 
-- MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
-- MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
-- MAGIC </div>

-- COMMAND ----------

-- MAGIC %md <i18n value="7aa87ebc-24dd-4b39-bb02-7c59fa083a14"/>
-- MAGIC 
-- MAGIC 
-- MAGIC # Delta Tables 관리하기
-- MAGIC 
-- MAGIC SQL의 특징을 알고 있다면 데이터 레이크하우스에서 효과적으로 작업하는 데 필요한 많은 지식을 이미 가지고 있는 것입니다.
-- MAGIC 
-- MAGIC 이 노트북에서는 Databricks에서 SQL을 사용하여 데이터 및 테이블의 기본 조작을 살펴봅니다.
-- MAGIC 
-- MAGIC Delta Lake는 Databricks로 만든 모든 테이블의 기본 형식입니다. Databricks에서 SQL 문을 실행했다면 이미 Delta Lake로 작업하고 있을 확율이 높습니다
-- MAGIC 
-- MAGIC ## 학습 목표
-- MAGIC 이 단원을 마치면 다음을 수행할 수 있습니다.
-- MAGIC * Delta Lake 테이블 생성
-- MAGIC * Delta Lake 테이블의 쿼리 데이터
-- MAGIC * Delta Lake 테이블에서 레코드 삽입, 업데이트 및 삭제
-- MAGIC * Delta Lake로 upsert 문 작성
-- MAGIC * Delta Lake 테이블 삭제하기

-- COMMAND ----------

-- MAGIC %md <i18n value="add37b8c-6a95-423f-a09a-876e489ef17d"/>
-- MAGIC 
-- MAGIC 
-- MAGIC ## Run Setup
-- MAGIC 가장 먼저 할 일은 설정 스크립트를 실행하는 것입니다. 각 사용자로 범위가 지정된 사용자 이름, userhome 및 데이터베이스를 정의합니다.

-- COMMAND ----------

-- MAGIC %run ../Includes/Classroom-Setup-02.1

-- COMMAND ----------

-- MAGIC %md <i18n value="3b9c0755-bf72-480e-a836-18a4eceb97d2"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC ## Creating a Delta Table
-- MAGIC 
-- MAGIC Delta Lake로 테이블을 생성하기 위해 작성해야 하는 코드가 많지 않습니다. 과정 전반에 걸쳐 보게 될 Delta Lake 테이블을 만드는 방법에는 여러 가지가 있습니다. 가장 쉬운 방법 중 하나인 깡통 Delta Lake 테이블 등록부터 시작하겠습니다.
-- MAGIC 
-- MAGIC 
-- MAGIC 필요한 것: 
-- MAGIC - **`CREATE TABLE`** 문장
-- MAGIC - 테이블 이름 (아래 예제에서 **`students`** 사용)
-- MAGIC - 스키마
-- MAGIC 
-- MAGIC **NOTE:** Databricks Runtime 8.0 이상에서는 Delta Lake가 기본 형식이며 **`USING DELTA`**가 필요하지 않습니다.

-- COMMAND ----------

CREATE TABLE students
  (id INT, name STRING, value DOUBLE);

-- COMMAND ----------

-- MAGIC %md <i18n value="a00174f3-bbcd-4ee3-af0e-b8d4ccb58481"/>
-- MAGIC 
-- MAGIC 돌아가서 해당 셀을 다시 실행하려고 하면 오류가 발생합니다! 이것은 예상된 것입니다. 테이블이 이미 존재하기 때문에 오류가 발생합니다.
-- MAGIC 
-- MAGIC 테이블이 존재하는지 확인하는 추가 인수 **`IF NOT EXISTS`**를 추가할 수 있습니다. 이것은 오류를 회피할 것 입니다.

-- COMMAND ----------

CREATE TABLE IF NOT EXISTS students 
  (id INT, name STRING, value DOUBLE)

-- COMMAND ----------

-- MAGIC %md <i18n value="408b1c71-b26b-43c0-b144-d5e92064a5ac"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC ## 데이터 삽입
-- MAGIC 대부분의 경우 데이터는 다른 소스의 쿼리 결과로 테이블에 삽입됩니다.
-- MAGIC 
-- MAGIC 그러나 표준 SQL에서와 마찬가지로 여기에 표시된 대로 값을 직접 삽입할 수도 있습니다.

-- COMMAND ----------

INSERT INTO students VALUES (1, "Yve", 1.0);
INSERT INTO students VALUES (2, "Omar", 2.5);
INSERT INTO students VALUES (3, "Elia", 3.3);

-- COMMAND ----------

-- MAGIC %md <i18n value="853dd803-9f64-42d7-b5e8-5477ea61029e"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC 위의 셀에서 세 개의 별도 **`INSERT`** 문을 완료했습니다. 이들 각각은 자체 ACID 보장과 함께 별도의 트랜잭션으로 처리됩니다. 대부분의 경우 아래와 같이 단일 트랜잭션에 많은 레코드를 삽입합니다.

-- COMMAND ----------

INSERT INTO students
VALUES 
  (4, "Ted", 4.7),
  (5, "Tiffany", 5.5),
  (6, "Vini", 6.3)

-- COMMAND ----------

-- MAGIC %md <i18n value="7972982a-05be-46ce-954e-e9d29e3b7329"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC Databricks에는 **`COMMIT`** 키워드가 없습니다. 트랜잭션은 실행되는 즉시 실행되고 성공하면 커밋됩니다.

-- COMMAND ----------

-- MAGIC %md <i18n value="121bd36c-10c4-41fc-b730-2a6fb626c6af"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC ## Delta Table 조회하기
-- MAGIC 
-- MAGIC Delta Lake 테이블을 조회하는 것이 표준 **`SELECT`** 문을 사용하는 것만큼 쉽습니다.

-- COMMAND ----------

SELECT * FROM students

-- COMMAND ----------

-- MAGIC %md <i18n value="4ecaf351-d4a4-4803-8990-5864995287a4"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC 놀라운 점은 Delta Lake 테이블에 대한 모든 읽기가 **항상** 가장 최신 버전의 테이블을 반환하고 진행 중인 작업으로 인해 교착 상태가 발생하지 않도록 보장한다는 것입니다.
-- MAGIC 
-- MAGIC **요약**: 테이블 읽기는 다른 작업과 충돌할 수 없으며 최신 버전의 데이터는 레이크하우스를 쿼리할 수 있는 모든 클라이언트에서 즉시 사용할 수 있습니다. 모든 트랜잭션 정보는 데이터 파일과 함께 클라우드 개체 저장소에 저장되기 때문에 Delta Lake 테이블에 대한 동시 읽기는 클라우드 공급업체의 개체 저장소에 대한 엄격한 요청 수 제한에 의해서만 제한됩니다. (**참고**: 무한하지는 않지만 초당 최소 수천 번의 읽기입니다.)

-- COMMAND ----------

-- MAGIC %md <i18n value="8a379d8d-7c48-43b0-8e25-3e653d8d6e86"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC ## 레코드 업데이트
-- MAGIC 
-- MAGIC 레코드 업데이트는 원자성(Atomic) 보장도 제공합니다. 테이블의 현재 버전에 대한 스냅샷 읽기를 수행하고 **`WHERE`** 절과 일치하는 모든 필드를 찾은 다음 설명된 대로 변경 사항을 적용합니다.
-- MAGIC 
-- MAGIC 아래에서 이름이 문자 **T**로 시작하는 모든 학생을 찾고 **`value`** 열의 숫자에 1을 더합니다.

-- COMMAND ----------

UPDATE students 
SET value = value + 1
WHERE name LIKE "T%"

-- COMMAND ----------

-- MAGIC %md <i18n value="b307b3e7-5ed2-4df8-bdd5-6c25acfd072f"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC 변경 사항이 적용되었는지 확인하기위해서 테이블을 다시 쿼리하십시오.

-- COMMAND ----------

SELECT * FROM students

-- COMMAND ----------

-- MAGIC %md <i18n value="d581b9a2-f450-43dc-bff3-2ea9cc46ad4c"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC ## 레코드 삭제
-- MAGIC 
-- MAGIC 삭제도 원자성을 가지므로 데이터 레이크하우스에서 데이터를 제거할 때 부분적으로만 성공할 위험이 없습니다.
-- MAGIC 
-- MAGIC **`DELETE`** 문은 하나 이상의 레코드를 제거할 수 있지만 항상 단일 트랜잭션이 발생합니다.

-- COMMAND ----------

DELETE FROM students 
WHERE value > 6

-- COMMAND ----------

-- MAGIC %md <i18n value="b5b346b8-a3df-45f2-88a7-8cf8dea6d815"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC ## Merge 문 사용
-- MAGIC 
-- MAGIC 일부 SQL 시스템에는 업데이트, 삽입 및 기타 데이터 조작을 단일 명령으로 실행할 수 있는 upsert 개념이 있습니다.
-- MAGIC 
-- MAGIC Databricks는 **`MERGE`** 키워드를 사용하여 이 작업을 수행합니다.
-- MAGIC 
-- MAGIC CDC(변경 데이터 캡처) 피드에서 출력할 수 있는 4개의 레코드가 포함된 다음 Temp View 가 있다고 가정해 봅시다

-- COMMAND ----------

CREATE OR REPLACE TEMP VIEW updates(id, name, value, type) AS VALUES
  (2, "Omar", 15.2, "update"),
  (3, "", null, "delete"),
  (7, "Blue", 7.7, "insert"),
  (11, "Diya", 8.8, "update");
  
SELECT * FROM updates;

-- COMMAND ----------

-- MAGIC %md <i18n value="6fe009d5-513f-4b93-994f-1ae9a0f30a80"/>
-- MAGIC 
-- MAGIC 지금까지 본 구문을 사용하여 유형별로 이 보기에서 필터링하여 각각 레코드를 삽입, 업데이트 및 삭제하는 3개의 문을 작성할 수 있습니다. 그러나 이렇게 하면 3개의 개별 트랜잭션이 발생합니다. 이러한 트랜잭션 중 하나라도 실패하면 데이터가 유효하지 않은 상태로 남을 수 있습니다.
-- MAGIC 
-- MAGIC 대신 이러한 작업을 단일 원자 트랜잭션으로 결합하여 3가지 유형의 변경 사항을 함께 적용합니다.
-- MAGIC 
-- MAGIC **`MERGE`** 문에는 일치(ON 절)시킬 필드가 하나 이상 있어야 하며 각 **`WHEN MATCHED`** 또는 **`WHEN NOT MATCHED`** 절에는 원하는 만큼 추가 조건문이 있을 수 있습니다.
-- MAGIC 
-- MAGIC 여기에서 **`id`** 필드를 일치시킨 다음 **`type`** 필드를 필터링하여 레코드를 적절하게 업데이트, 삭제 또는 삽입합니다.

-- COMMAND ----------

MERGE INTO students b
USING updates u
ON b.id=u.id
WHEN MATCHED AND u.type = "update"
  THEN UPDATE SET *
WHEN MATCHED AND u.type = "delete"
  THEN DELETE
WHEN NOT MATCHED AND u.type = "insert"
  THEN INSERT *

-- COMMAND ----------

-- MAGIC %md <i18n value="77cee0a0-f94b-4016-a20b-08e4857d13db"/>
-- MAGIC 
-- MAGIC 3개의 레코드만 **`MERGE`** 문의 영향을 받았습니다. 업데이트 테이블의 레코드 중 하나는 학생 테이블에 일치하는 **`id`** 가 없지만 **`update`** 로 표시되었습니다. 사용자 지정 논리에 따라 이 레코드를 삽입하는 대신 무시했습니다.
-- MAGIC 
-- MAGIC 마지막 **`INSERT`** 절에 **`update`** 로 표시된 일치하지 않는 레코드를 포함하도록 위의 명령문을 어떻게 수정하시겠습니까?

-- COMMAND ----------

-- MAGIC %md <i18n value="4eca2c53-e457-4964-875e-d39d9205c3c6"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC ## 테이블 드롭
-- MAGIC 
-- MAGIC 대상 테이블에 대한 적절한 권한이 있다고 가정하면 **`DROP TABLE`** 명령을 사용하여 레이크하우스의 데이터를 영구적으로 삭제할 수 있습니다.
-- MAGIC 
-- MAGIC **NOTE**: 이 과정의 뒷부분에서 테이블 ACL(액세스 제어 목록) 및 기본 권한에 대해 설명합니다. 적절하게 구성된 레이크하우스에서 사용자는 프로덕션 테이블을 삭제할 수 **없어야** 합니다.

-- COMMAND ----------

DROP TABLE students

-- COMMAND ----------

-- MAGIC %md <i18n value="08cbbda5-96b2-4ae8-889f-b1f4c04d1496"/>
-- MAGIC 
-- MAGIC 
-- MAGIC 
-- MAGIC 다음 셀을 실행하여 이 학습과 연관된 테이블 및 파일을 삭제하십시오.

-- COMMAND ----------

-- MAGIC %python
-- MAGIC DA.cleanup()

-- COMMAND ----------

-- MAGIC %md-sandbox
-- MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
-- MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
-- MAGIC <br/>
-- MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
