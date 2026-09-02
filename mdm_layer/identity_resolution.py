# Extracts member data, applies phonetic blocking, and fuzzy matches identities
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, soundex

spark = SparkSession.builder.appName("Fintech_MDM_Identity").getOrCreate()

# Load raw member data from data lake
df_raw = spark.read.parquet("s3://landing-zone/members/")

# Apply Phonetic Blocking to prevent Cartesian Explosion during joins
df_blocked = df_raw.withColumn("name_block", soundex(col("last_name")))

# (In production: proceed with fuzzy matching within blocks using Levenshtein distance)
df_blocked.write.mode("overwrite").parquet("s3://processed-zone/resolved_members/")
