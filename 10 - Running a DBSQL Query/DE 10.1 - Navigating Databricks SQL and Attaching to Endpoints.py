# Databricks notebook source
# MAGIC %md-sandbox
# MAGIC 
# MAGIC <div style="text-align: center; line-height: 0; padding-top: 9px;">
# MAGIC   <img src="https://databricks.com/wp-content/uploads/2018/03/db-academy-rgb-1200px.png" alt="Databricks Learning" style="width: 600px">
# MAGIC </div>

# COMMAND ----------

# MAGIC %md <i18n value="cbd3eef7-fc50-4393-bed5-44d7711f8052"/>
# MAGIC 
# MAGIC 
# MAGIC # Databricks SQL 탐색 및 SQL Warehouse에 연결
# MAGIC 
# MAGIC * Databricks SQL로 이동
# MAGIC    * 사이드바(Databricks 로고 바로 아래)의 작업 공간 옵션에서 SQL이 선택되어 있는지 확인하십시오.
# MAGIC * SQL Warehouses 가 켜져 있고 액세스 가능한지 확인
# MAGIC    * 사이드바에서 SQL Warehouses를 선택해서 이동합니다.
# MAGIC    * SQL 웨어하우스가 존재하고 **`Running`** 상태인 경우 해당 SQL 웨어하우스를 사용합니다.
# MAGIC    * SQL 웨어하우스가 존재하지만 **`Stopped`** 인 경우 이 옵션이 있으면 **`Start`** 버튼을 클릭합니다(**참고**: 사용 가능한 가장 작은 SQL 웨어하우스 시작).
# MAGIC    * SQL 웨어하우스가 없고 옵션이 있는 경우 **`Create SQL Warehouse`** 을 클릭합니다. SQL 웨어하우스에 인식할 수 있는 이름을 지정하고 클러스터 크기를 2X-Small로 설정합니다. 다른 모든 옵션은 기본값으로 둡니다.
# MAGIC    * SQL 웨어하우스를 만들거나 연결할 방법이 없는 경우 계속하려면 작업 영역 관리자에게 연락하여 Databricks SQL의 컴퓨팅 리소스에 대한 액세스 권한을 요청해야 합니다.
# MAGIC * Databricks SQL의 홈 페이지로 이동
# MAGIC    * 측면 탐색 모음 상단의 Databricks 로고를 클릭합니다.
# MAGIC * **샘플 대시보드**를 찾아 **`Visit gallery`** 을 클릭합니다.
# MAGIC * **Retail Revenue & Supply Chain** 옵션 옆에 있는 **`Import`** 를 클릭합니다.
# MAGIC    * 사용 가능한 SQL 웨어하우스가 있다고 가정하면 대시보드가 로드되고 즉시 결과가 표시됩니다.
# MAGIC    * 오른쪽 상단에서 **Refresh**을 클릭합니다(기본 데이터는 변경되지 않았지만 변경 사항을 선택하는 데 사용되는 버튼임).
# MAGIC 
# MAGIC # DBSQL Dashboard 업데이트
# MAGIC 
# MAGIC 
# MAGIC * 사이드바 탐색기를 사용하여 **Dashboards** 를 찾습니다.
# MAGIC    * 방금 로드한 샘플 대시보드를 찾습니다. 이름은 **Retail Revenue & Supply Chain**이어야 하며 **`Created By`** 필드 아래에 사용자 이름이 있어야 합니다. **NOTE**: 오른쪽에 있는 **내 대시보드** 옵션은 작업 영역에서 다른 대시보드를 필터링하는 바로 가기 역할을 할 수 있습니다.
# MAGIC    * 대시보드 이름을 클릭하면 볼 수 있습니다.
# MAGIC * **Shifts in Pricing Priorities** 를 구성하는 쿼리 보기
# MAGIC    * 플롯 위로 마우스를 가져갑니다. 세 개의 수직 점이 나타나야 합니다. 이것을 클릭
# MAGIC    * 표시되는 메뉴에서 **View Query**를 선택합니다.
# MAGIC * 이 플롯을 채우는 데 사용된 SQL 코드를 검토합니다.
# MAGIC    * 소스 테이블을 식별하기 위해 3계층 네임스페이스가 사용됩니다. 이것은 Unity Catalog에서 지원할 새로운 기능입니다.
# MAGIC    * 화면 왼쪽 상단의 **`Run`** 을 클릭하면 쿼리 결과를 미리 볼 수 있습니다.
# MAGIC * 시각화 검토
# MAGIC    * 쿼리 아래에서 **Results** 라는 탭을 선택해야 합니다. 플롯의 미리보기로 전환하려면 **Price by Priority over Time** 을 클릭하세요.
# MAGIC    * 시각화 설정을 검토하려면 **Price by Priority over Time** 탭 옆의 아래 꺽쇠 버튼을 눌러서 **Edit**  을 클릭하세요.
# MAGIC    * 설정 변경이 시각화에 미치는 영향 알아보기
# MAGIC    * 변경 사항을 적용하려면 **Save** 을 클릭하십시오. 그렇지 않으면 **Cancel** 를 클릭합니다.
# MAGIC * 쿼리 편집기로 돌아가 시각화 이름 오른쪽에 있는 + 를 눌러서  **Visualization** 버튼을 클릭합니다.
# MAGIC    * **Visualization type** 을 Bar 로 선택합니다.
# MAGIC    * **X Column** 을 **`Date`** 로 설정
# MAGIC    * **Y Column**을 **`Total Price`** 로 설정
# MAGIC    * **Group by** **`Priority`**
# MAGIC    * **Stacking**을 **`Stack`** 으로 설정
# MAGIC    * 다른 모든 설정은 기본값으로 두십시오.
# MAGIC    * **Save** 를 클릭합니다.
# MAGIC * 쿼리 편집기로 돌아가서 이 시각화의 기본 이름을 클릭하여 편집합니다. **Bar 1** 탭을 클릭해서 시각화 이름을 **`Stacked Price`**로 변경
# MAGIC * 방금 변경한 시각화 이름 오른쪽에 있는 아래 꺽쇠를 클릭합니다.
# MAGIC    * 메뉴에서 **Add to Dashbaord** 선택
# MAGIC    * **`Retail Revenue & Supply Chain`** 대시보드 선택
# MAGIC 
# MAGIC 
# MAGIC # 새로운 쿼리 생성
# MAGIC 
# MAGIC 
# MAGIC * 사이드바를 사용하여 **SQL Editor**로 이동합니다.
# MAGIC *  + 버튼을 클릭해서 **`Create Query`** 메뉴를 클릭합니다.
# MAGIC * SQL 웨어하우스에 연결되어 있는지 확인하십시오. **Schema Browser** 에서 현재 메타스토어를 클릭하고 **`samples`**를 선택합니다.
# MAGIC    * **`tpch`** 데이터베이스 선택
# MAGIC    * 스키마 미리보기를 보려면 **`partsupp`** 테이블을 클릭하십시오.
# MAGIC    * **`partsupp`** 테이블 이름 위로 마우스를 가져간 상태에서 **>>** 버튼을 클릭하여 쿼리 텍스트에 테이블 이름을 삽입합니다.
# MAGIC * 첫 번째 쿼리 작성:
# MAGIC    * **`SELECT * FROM`** 마지막 단계에서 가져온 전체 이름을 사용하여 **`partsupp`** 테이블; 결과를 미리 보려면 **실행**을 클릭하세요.
# MAGIC    * 이 쿼리를 **`GROUP BY ps_partkey`** 로 수정하고 **`ps_partkey`** 및 **`sum(ps_availqty)`** 을 반환합니다. 결과를 미리 보려면 **실행**을 클릭하세요.
# MAGIC    * 두 번째 열의 별칭을 **`total_availqty`** 로 지정하고 쿼리를 다시 실행하도록 쿼리를 업데이트합니다.
# MAGIC * 쿼리 저장
# MAGIC    * 화면 오른쪽 상단 **실행** 옆 **저장** 버튼 클릭
# MAGIC    * 쿼리에 기억할 이름을 지정하십시오.
# MAGIC * 대시보드에 쿼리 추가
# MAGIC    * Results 탭 옆의 아래 꺽쇠 클릭
# MAGIC    * **Add to dashboard** 를 클릭합니다.
# MAGIC    * **`Retail Revenue & Supply Chain`** 대시보드 선택
# MAGIC * 이 변경 사항을 보려면 대시보드로 돌아가십시오.
# MAGIC    * 시각화 구성을 변경하려면 화면 오른쪽 상단에 있는 세 개의 수직 버튼을 클릭하십시오. 표시되는 메뉴에서 **Edit** 을 클릭하면 시각화를 끌어서 크기를 조정할 수 있습니다.

# COMMAND ----------

# MAGIC %md-sandbox
# MAGIC &copy; 2023 Databricks, Inc. All rights reserved.<br/>
# MAGIC Apache, Apache Spark, Spark and the Spark logo are trademarks of the <a href="https://www.apache.org/">Apache Software Foundation</a>.<br/>
# MAGIC <br/>
# MAGIC <a href="https://databricks.com/privacy-policy">Privacy Policy</a> | <a href="https://databricks.com/terms-of-use">Terms of Use</a> | <a href="https://help.databricks.com/">Support</a>
