# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md 
# MAGIC <i18n value="48031791-53af-4737-8c15-280e45fb9226"/>
# MAGIC 
# MAGIC # 노트북 기초
# MAGIC 
# MAGIC 노트북은 Databricks에서 대화형으로 코드를 개발하고 실행하는 기본 수단입니다. 이 단원에서는 Databricks 노트북 작업에 대한 기본적인 소개를 제공합니다.
# MAGIC 
# MAGIC 이전에 Databricks 에서 노트북을 사용했지만 Databricks Repos에서 노트북을 처음 실행한다면 기본 기능이 동일하다는 것을 알 수 있습니다. 다음 단원에서는 Databricks Repos가 노트북에 추가하는 몇 가지 기능을 검토합니다.
# MAGIC 
# MAGIC ## 학습 목표
# MAGIC 이 단원을 마치면 다음을 수행할 수 있습니다.
# MAGIC * 클러스터에 노트북 연결
# MAGIC * 노트북에서 셀 실행
# MAGIC * 노트북 언어 설정
# MAGIC * 매직 커맨드 설명 및 사용
# MAGIC * SQL 셀 생성 및 실행
# MAGIC * Python 셀 생성 및 실행
# MAGIC * 마크다운 셀 생성
# MAGIC * Databricks 노트북 내보내기
# MAGIC * Databricks 노트북 컬렉션 내보내기

# COMMAND ----------

# MAGIC %md <i18n value="96041d75-d411-45db-8add-986022e62159"/>
# MAGIC 
# MAGIC 
# MAGIC ## 클러스터에 노트북 붙이기
# MAGIC 
# MAGIC 이전 레슨에서 클러스터를 이미 배포했거나 관리자가 사용하도록 구성한 클러스터를 식별했어야 합니다.
# MAGIC 
# MAGIC 화면 상단의 이 노트북 이름 옆에 있는 드롭다운 목록을 사용하여 이 노트북을 클러스터에 연결합니다.
# MAGIC 
# MAGIC **참고**: 클러스터를 배포하는 데 몇 분 정도 걸릴 수 있습니다. 리소스가 배포되면 클러스터 이름 오른쪽에 녹색 화살표가 나타납니다. 클러스터 왼쪽에 단색 회색 원이 있는 경우 다음 지침을 따라야 합니다. 
# MAGIC <a href="$./DE 1.1 - Create and Manage Interactive Clusters"> 클러스터 시작하기</a>.

# COMMAND ----------



# COMMAND ----------

# MAGIC %md <i18n value="9f021e76-692f-4df7-8e80-fec41d03c719"/>
# MAGIC 
# MAGIC ## 노트북 기초
# MAGIC 
# MAGIC 노트북은 코드의 셀 단위 실행을 제공합니다. 노트북에서 여러 언어를 혼합할 수 있습니다. 사용자는 플롯, 이미지 및 마크다운 텍스트를 추가하여 코드를 향상시킬 수 있습니다.
# MAGIC 
# MAGIC 노트북은 학습 도구로 설계되었습니다. 노트북은 Databricks를 사용하여 프로덕션 코드로 쉽게 배포할 수 있을 뿐만 아니라 데이터 탐색, 보고 및 대시보드 작성을 위한 강력한 도구 집합을 제공할 수 있습니다.
# MAGIC 
# MAGIC ### Cell 실행하기
# MAGIC * 다음 옵션 중 하나를 사용하여 아래 셀을 실행합니다.
# MAGIC    * **CTRL+ENTER** 또는 **CTRL+RETURN**
# MAGIC    * **SHIFT+ENTER** 또는 **SHIFT+RETURN** 셀을 실행하고 다음 셀로 이동
# MAGIC    * 여기에 표시된 대로 **Run Cell**, **Run All Above** 또는 **Run All Below** 사용<br/><img style="box-shadow: 5px 5px 5px 0px rgba(0,0,0,0.25); border: 1px solid rgba(0,0,0,0.25);" src="https://files.training.databricks.com/images/notebook-cell-run-cmd.png"/>

# COMMAND ----------

print("I'm running Python!")

# COMMAND ----------



# COMMAND ----------



# COMMAND ----------



# COMMAND ----------

# MAGIC %md <i18n value="cea571b2-8a27-495f-a1ee-7e270d688d62"/>
# MAGIC 
# MAGIC 
# MAGIC **NOTE**: 셀별 코드 실행은 셀이 여러 번 또는 순서 없이 실행될 수 있음을 의미합니다. 명시적으로 지시하지 않는 한, 이 과정의 노트북은 위에서 아래로 한 번에 한 셀씩 항상 실행되도록 되어 있다고 가정해야 합니다. 오류가 발생하면 문제 해결을 시도하기 전에 오류가 의도적인 학습 순간이 아닌지 확인하기 위해 셀 앞뒤의 텍스트를 읽어야 합니다. 대부분의 오류는 누락된 노트북의 이전 셀을 실행하거나 위에서부터 전체 노트북을 다시 실행하여 해결할 수 있습니다.

# COMMAND ----------

# MAGIC %md <i18n value="702cb769-7d37-4b1a-8131-292f37d4c8e6"/>
# MAGIC 
# MAGIC 
# MAGIC ### 기본 노트북 언어 설정
# MAGIC 
# MAGIC 노트북의 현재 기본 언어가 Python으로 설정되어 있기 때문에 위의 셀은 Python 명령을 실행합니다.
# MAGIC 
# MAGIC Databricks 노트북은 Python, SQL, Scala 및 R을 지원합니다. 노트북을 만들 때 언어를 선택할 수 있지만 언제든지 변경할 수 있습니다.
# MAGIC 
# MAGIC 기본 언어는 페이지 상단의 노트북 제목 바로 오른쪽에 나타납니다. 이 과정에서는 SQL과 Python 노트북을 함께 사용합니다.
# MAGIC 
# MAGIC 이 노트북의 기본 언어를 SQL로 변경하겠습니다.
# MAGIC 
# MAGIC 단계:
# MAGIC * 화면 상단 노트북 제목 옆 **Python** 클릭
# MAGIC * 팝업되는 UI의 드롭다운 목록에서 **SQL** 선택
# MAGIC 
# MAGIC **참고**: 이 셀 바로 앞의 셀에 <strong><code>&#37;python</code></strong>이라는 새 줄이 표시되어야 합니다. 잠시 후에 이에 대해 논의하겠습니다.

# COMMAND ----------

# MAGIC %md <i18n value="0e12c7f2-4169-40d6-b065-5b6e1454ae2a"/>
# MAGIC 
# MAGIC 
# MAGIC ### SQL 셀 생성하고 실행하기 
# MAGIC 
# MAGIC * 이 셀을 선택 하고 키보드의 **B** 버튼을 눌러 아래에 새 셀을 만듭니다.
# MAGIC * 다음 코드를 아래 셀에 복사한 후 셀을 실행합니다.
# MAGIC 
# MAGIC **`%sql`**<br/>
# MAGIC **`SELECT "I'm running SQL!"`**
# MAGIC 
# MAGIC **NOTE**: GUI 옵션 및 키보드 단축키를 포함하여 셀을 추가, 이동 및 삭제하는 다양한 방법이 있습니다. 자세한 사항은 <a href="https://docs.databricks.com/notebooks/notebooks-use.html#develop-notebooks" target="_blank">문서</a> 를 참고하세요

# COMMAND ----------

# MAGIC %md 
# MAGIC 
# MAGIC <i18n value="828d14d2-a661-45e4-a555-0b86896c31d4"/>
# MAGIC 
# MAGIC ## 매직 커맨드
# MAGIC * 매직 커맨드는 Databricks 노트북에만 적용됩니다.
# MAGIC * 유사한 노트북 제품에서 볼 수 있는 매직 커맨드와 매우 유사합니다.
# MAGIC * 이들은 노트북의 언어에 관계없이 동일한 결과를 제공하는 내장된 명령입니다.
# MAGIC * 셀 시작 부분의 퍼센트(%) 기호는 매직 커맨드를 나타냅니다.
# MAGIC    * 셀당 하나의 매직 커맨드를 가질 수 있습니다.
# MAGIC    * 매직 커맨드는 셀의 첫 번째 항목이어야 합니다.

# COMMAND ----------

# MAGIC %md <i18n value="19380cb5-20d3-4bd6-abd6-ae09082f2451"/>
# MAGIC 
# MAGIC 
# MAGIC ### Language Magics
# MAGIC 매직 명령을 사용하면 노트북의 기본 언어 이외의 언어로 코드를 실행할 수 있습니다. 이 과정에서는 다음과 같은 언어 매직을 볼 수 있습니다.
# MAGIC * <strong><code>&#37;python</code></strong>
# MAGIC * <strong><code>&#37;sql</code></strong>
# MAGIC 
# MAGIC 현재 설정된 노트북 유형에 대한 언어 마법을 추가할 필요가 없습니다.
# MAGIC 
# MAGIC 위에서 노트북 언어를 Python에서 SQL로 변경했을 때 Python으로 작성된 기존 셀에 <strong><code>&#37;python</code></strong> 명령이 추가되었습니다.
# MAGIC 
# MAGIC **NOTE**: 노트북의 기본 언어를 지속적으로 변경하는 대신 기본 언어를 기본 언어로 유지하고 다른 언어로 코드를 실행하는 데 필요한 언어 매직만 사용해야 합니다.

# COMMAND ----------

print("Hello Python!")

# COMMAND ----------

# MAGIC %sql
# MAGIC 
# MAGIC select "Hello SQL!"

# COMMAND ----------

# MAGIC %md <i18n value="81f29d75-0c8f-47d3-a052-7664f3e2bc83"/>
# MAGIC 
# MAGIC 
# MAGIC 
# MAGIC ### Markdown
# MAGIC 
# MAGIC 마법 명령 **%md**를 사용하면 셀에서 Markdown을 렌더링할 수 있습니다.
# MAGIC * 편집을 시작하려면 이 셀을 두 번 클릭합니다.
# MAGIC * 그런 다음 **`Esc`**를 눌러 편집을 중지합니다.
# MAGIC 
# MAGIC # Title One
# MAGIC ## Title Two
# MAGIC ### Title Three
# MAGIC 
# MAGIC 이것은 기본 텍스트 입니다.
# MAGIC 
# MAGIC 이것은 **굵은** 단어가 포함된 텍스트입니다.
# MAGIC 
# MAGIC *기울임꼴* 단어가 포함된 텍스트입니다.
# MAGIC 
# MAGIC 이것은 순차 리스트 입니다
# MAGIC 1. once
# MAGIC 1. two
# MAGIC 1. three
# MAGIC 
# MAGIC 이것은 리스트 입니다. 
# MAGIC * apples
# MAGIC * peaches
# MAGIC * bananas
# MAGIC 
# MAGIC Links/Embedded HTML: <a href="https://en.wikipedia.org/wiki/Markdown" target="_blank">Markdown - Wikipedia</a>
# MAGIC 
# MAGIC 이미지:
# MAGIC ![Spark Engines](https://files.training.databricks.com/images/Apache-Spark-Logo_TM_200px.png)
# MAGIC 
# MAGIC 테이블 포맷:
# MAGIC 
# MAGIC | name   | value |
# MAGIC |--------|-------|
# MAGIC | Yi     | 1     |
# MAGIC | Ali    | 2     |
# MAGIC | Selina | 3     |

# COMMAND ----------

# MAGIC %md <i18n value="8bdf271e-346f-4ec8-b49c-a7593a5f1f6c"/>
# MAGIC 
# MAGIC 
# MAGIC ### %run
# MAGIC * 마법 명령 **%run**을 사용하여 노트북에서 다른 노트북을 실행할 수 있습니다.
# MAGIC * 실행할 노트북은 상대 경로로 지정됩니다.
# MAGIC * 참조된 노트북은 현재 노트북의 일부인 것처럼 실행되므로 호출 노트북에서 temporary views 및 기타 로컬 변수 선언을 사용할 수 있습니다.

# COMMAND ----------

# MAGIC %md <i18n value="739cd1b9-dac7-40f7-8c33-9a3c91eec348"/>
# MAGIC 
# MAGIC 
# MAGIC 다음 셀의 주석을 해제하고 실행하면 다음 오류가 발생합니다:<br/>
# MAGIC **`Error in SQL statement: AnalysisException: Table or view not found: demo_tmp_vw`**

# COMMAND ----------

# MAGIC %sql
# MAGIC -- SELECT * FROM demo_tmp_vw

# COMMAND ----------

# MAGIC %md <i18n value="d9e357e2-f605-4aae-be7d-9254361e2147"/>
# MAGIC 
# MAGIC 그러나 우리는 그것을 선언할 수 있고 소수의 다른 변수와 함수가 이 셀을 실행할 수 있습니다:

# COMMAND ----------

# MAGIC %run ../Includes/Classroom-Setup-01.2

# COMMAND ----------

# MAGIC %md <i18n value="e7a9c7ec-1d61-42d6-91c9-ece07d2aa2a3"/>
# MAGIC 
# MAGIC 우리가 참조한 **`../Includes/Classroom-Setup-01.2`** 노트북에는 **`demo_temp_vw`** 임시 뷰를 생성할 뿐만 아니라 데이터베이스를 생성하고 **`USE`**하는 로직이 포함되어 있습니다.
# MAGIC 
# MAGIC 이제 다음 쿼리를 사용하여 현재 노트북 세션에서 이 temporary view를 사용할 수 있음을 알 수 있습니다.

# COMMAND ----------

# MAGIC %sql 
# MAGIC SELECT * FROM demo_tmp_vw

# COMMAND ----------

# MAGIC %md <i18n value="fd9afa7b-7efd-421e-9a22-61e7d6533a52"/>
# MAGIC 
# MAGIC 과정 전반에 걸쳐 이 "setup" 노트북 패턴을 사용하여 수업 및 실습을 위한 환경을 구성할 것입니다.
# MAGIC 
# MAGIC 이러한 "제공된" 변수, 함수 및 기타 개체는 **`DBAcademyHelper`**의 인스턴스인 **`DA`** 개체의 일부이므로 쉽게 식별할 수 있어야 합니다.
# MAGIC 
# MAGIC 이를 염두에 두고 대부분의 수업에서는 사용자 이름에서 파생된 변수를 사용하여 파일과 데이터베이스를 구성합니다.
# MAGIC 
# MAGIC 이 패턴을 사용하면 공유 작업 공간에서 다른 사용자와의 충돌을 피할 수 있습니다.
# MAGIC 
# MAGIC 아래 셀은 Python을 사용하여 이전에 이 노트북의 설정 스크립트에 정의된 변수 중 일부를 출력합니다.

# COMMAND ----------

print(f"DA:                   {DA}")
print(f"DA.username:          {DA.username}")
print(f"DA.paths.working_dir: {DA.paths.working_dir}")
print(f"DA.schema_name:       {DA.schema_name}")

# COMMAND ----------

# MAGIC %md <i18n value="f28a5e07-c955-460c-8779-6eb3f7306b19"/>
# MAGIC 
# MAGIC 이 외에도 이러한 동일한 변수가 SQL 문에서 사용할 수 있도록 SQL 컨텍스트에 "주입"됩니다.
# MAGIC 
# MAGIC 나중에 이에 대해 자세히 설명하겠지만 다음 셀에서 간단한 예를 볼 수 있습니다.
# MAGIC 
# MAGIC <img src="https://files.training.databricks.com/images/icon_note_32.png"> 위 아래 두 예제에서 **`da`**와 **`DA`**라는 단어의 대소문자가 미묘하지만 중요한 차이가 있음에 유의하십시오.

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT '${da.username}' AS current_username,
# MAGIC        '${da.paths.working_dir}' AS working_directory,
# MAGIC        '${da.schema_name}' as schema_name

# COMMAND ----------

# MAGIC %md <i18n value="cf6ff3b4-2f4b-4fed-9d56-1e5f1b4fbb83"/>
# MAGIC 
# MAGIC 
# MAGIC ## Databricks Utilities
# MAGIC 
# MAGIC Databricks 노트북은 환경 구성 및 상호 작용을 위한 다양한 유틸리티 명령을 제공합니다. <a href="https://docs.databricks.com/user-guide/dev-tools/dbutils.html" target="_blank">dbutils 문서</a>
# MAGIC 
# MAGIC 이 과정에서 종종 **`dbutils.fs.ls()`**를 사용하여 Python 셀에서 파일 디렉토리를 나열할 것입니다.

# COMMAND ----------

path = f"{DA.paths.datasets}"
dbutils.fs.ls(path)

# COMMAND ----------

# MAGIC %md <i18n value="b58df4d5-09b7-4a63-89d8-69363d32e37b"/>
# MAGIC 
# MAGIC 
# MAGIC ## display()
# MAGIC 
# MAGIC 셀에서 SQL 쿼리를 실행할 때 결과는 항상 렌더링된 표 형식으로 표시됩니다.
# MAGIC 
# MAGIC Python 셀에서 반환한 테이블 형식 데이터가 있는 경우 **`display`** 를 호출하여 동일한 유형의 미리보기를 얻을 수 있습니다.
# MAGIC 
# MAGIC 여기서 파일 시스템의 이전 list 명령을 **`display`** 로 래핑합니다.

# COMMAND ----------

path = f"{DA.paths.datasets}"
files = dbutils.fs.ls(path)
display(files)

# COMMAND ----------

# MAGIC %md <i18n value="4ee5258a-3c18-47d5-823c-01596b4787c4"/>
# MAGIC 
# MAGIC **`display()`** 명령에는 다음과 같은 기능과 제한 사항이 있습니다.
# MAGIC * 결과 미리보기는 1000개 레코드로 제한됨
# MAGIC * 결과 데이터를 CSV로 다운로드할 수 있는 버튼 제공
# MAGIC * 렌더링 플롯 허용

# COMMAND ----------

# MAGIC %md <i18n value="b1e79003-3240-4a4e-84e3-a7902f969631"/>
# MAGIC 
# MAGIC 
# MAGIC ## Downloading Notebooks
# MAGIC 
# MAGIC 개별 노트북 또는 노트북 컬렉션을 다운로드하기 위한 다양한 옵션이 있습니다.
# MAGIC 
# MAGIC 여기에서 이 노트북과 이 과정의 모든 노트북 모음을 다운로드하는 프로세스를 진행합니다.
# MAGIC 
# MAGIC ### 단일 노트북 다운로드
# MAGIC 
# MAGIC 단계:
# MAGIC * 노트북 상단의 클러스터 선택 오른쪽에 있는 **File** 옵션을 클릭합니다.
# MAGIC * 표시되는 메뉴에서 **Export** 위로 마우스를 가져간 다음 **Source file**을 선택합니다.
# MAGIC 
# MAGIC 노트북이 개인 노트북으로 다운로드됩니다. 현재 노트북 이름으로 이름이 지정되고 기본 언어에 대한 파일 확장자를 갖습니다. 파일 편집기로 이 노트북을 열고 Databricks 노트북의 원시 콘텐츠를 볼 수 있습니다.
# MAGIC 
# MAGIC 이러한 소스 파일은 모든 Databricks 작업 영역에 업로드할 수 있습니다.
# MAGIC 
# MAGIC ### 노트북 컬렉션 다운로드 
# MAGIC 
# MAGIC **NOTE**: 다음 지침에서는 **Repos**를 사용하여 이러한 자료를 가져온 것으로 가정합니다.
# MAGIC 
# MAGIC 단계:
# MAGIC * 왼쪽 사이드바에서 ![](https://files.training.databricks.com/images/repos-icon.png) **Repos**를 클릭합니다.
# MAGIC    * 이것은 이 노트북에 대한 상위 디렉토리의 미리보기를 제공해야 합니다.
# MAGIC * 화면 중앙 부근의 디렉토리 미리보기 왼쪽에 왼쪽 화살표(<)가 있어야 합니다. 파일 계층 구조에서 위로 이동하려면 이것을 클릭하십시오.
# MAGIC * **Data Engineering with Databricks**라는 디렉터리가 표시되어야 합니다. 아래쪽 화살표를 클릭하여 메뉴를 불러옵니다.
# MAGIC * 메뉴에서 **Export** 위로 마우스를 가져간 다음 **DBC Archive**를 선택합니다.
# MAGIC 
# MAGIC 다운로드되는 DBC(Databricks Cloud) 파일에는 이 과정의 디렉터리 및 노트북 모음이 압축되어 포함되어 있습니다. 사용자는 이러한 DBC 파일을 로컬에서 편집하려고 시도해서는 안 되지만 Databricks 작업 영역에 안전하게 업로드하여 노트북 콘텐츠를 이동하거나 공유할 수 있습니다.
# MAGIC 
# MAGIC **NOTE**: DBC 컬렉션을 다운로드할 때 결과 미리 보기 및 플롯도 내보냅니다. 반면 Source file 형태로 노트북 다운로드 시 코드만 저장됩니다.

# COMMAND ----------

# MAGIC %md <i18n value="37f4f2b0-5f6e-45d6-9ee4-3f90348f8277"/>
# MAGIC 
# MAGIC 
# MAGIC ## Learning More
# MAGIC 
# MAGIC Databricks 플랫폼 및 노트북의 다양한 기능에 대해 자세히 알아보려면 설명서를 살펴보는 것이 좋습니다.
# MAGIC * <a href="https://docs.databricks.com/user-guide/index.html#user-guide" target="_blank">User Guide</a>
# MAGIC * <a href="https://docs.databricks.com/user-guide/getting-started.html" target="_blank">Getting Started with Databricks</a>
# MAGIC * <a href="https://docs.databricks.com/user-guide/notebooks/index.html" target="_blank">User Guide / Notebooks</a>
# MAGIC * <a href="https://docs.databricks.com/notebooks/notebooks-manage.html#notebook-external-formats" target="_blank">Importing notebooks - Supported Formats</a>
# MAGIC * <a href="https://docs.databricks.com/repos/index.html" target="_blank">Repos</a>
# MAGIC * <a href="https://docs.databricks.com/administration-guide/index.html#administration-guide" target="_blank">Administration Guide</a>
# MAGIC * <a href="https://docs.databricks.com/user-guide/clusters/index.html" target="_blank">Cluster Configuration</a>
# MAGIC * <a href="https://docs.databricks.com/api/latest/index.html#rest-api-2-0" target="_blank">REST API</a>
# MAGIC * <a href="https://docs.databricks.com/release-notes/index.html#release-notes" target="_blank">Release Notes</a>

# COMMAND ----------

# MAGIC %md <i18n value="b3cc4b2f-a3ee-4602-bee8-b2b8fad2684a"/>
# MAGIC 
# MAGIC 
# MAGIC ## One more note! 
# MAGIC 
# MAGIC 각 단원이 끝나면 **`DA.cleanup()`** 명령이 표시됩니다.
# MAGIC 
# MAGIC 이 방법은 작업 공간을 깨끗하게 유지하고 각 레슨의 불변성을 유지하기 위해 레슨별 데이터베이스와 작업 디렉토리를 삭제합니다.
# MAGIC 
# MAGIC 다음 셀을 실행하여 이 학습과 연관된 테이블 및 파일을 삭제하십시오.

# COMMAND ----------

DA.cleanup()

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
