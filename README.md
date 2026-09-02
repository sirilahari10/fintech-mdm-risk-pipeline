#  Fintech Data Pipeline: MDM & Overdraft Risk Modeling
An end-to-end data pipeline orchestrating Identity Resolution (MDM) using PySpark, and dimensional risk modeling using Snowflake, dbt, and Apache Airflow. 

* **MDM Layer (PySpark):** Performs fuzzy matching to resolve fragmented member identities across legacy banking systems without O(N²) cartesian explosions.
* **Warehouse Layer (Snowflake & dbt):** Transforms resolved identities and daily transactions into a Star Schema, calculating 7-day rolling spend velocities for overdraft risk prediction.
* **Governance Layer:** Utilizes Snowflake Dynamic Data Masking to hide PII (SSN, Email) from unauthorized roles.
