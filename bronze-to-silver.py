# Databricks notebook source
# MAGIC %md
# MAGIC ## Doing transformation for all tables
# MAGIC 
# MAGIC ## إجراء تحويل لجميع الجداول

# COMMAND ----------

# Initialize an empty list to store table names
table_name = []

# List all files in the specified directory and extract table names
for i in dbutils.fs.ls('mnt/bronze/SalesLT/'):
    print(i.name)  # Print the name of each file or directory
    table_name.append(i.name.split('/')[0])  # Extract and append the table name to the list

# COMMAND ----------

# Display the list of table names
table_name

# COMMAND ----------

# Import necessary functions and types from PySpark
from pyspark.sql.functions import from_utc_timestamp, date_format
from pyspark.sql.types import TimestampType

# Loop through each table name to perform transformations
for i in table_name:
    # Construct the file path for the parquet file of the current table
    path = '/mnt/bronze/SalesLT/' + i + '/' + i + '.parquet'
    
    # Read the parquet file into a DataFrame
    df = spark.read.format('parquet').load(path)
    
    # Get the list of columns in the DataFrame
    column = df.columns

    # Loop through each column to check for date columns
    for col in column:
        # Check if the column name contains "Date" or "date"
        if "Date" in col or "date" in col:
            # Convert the UTC timestamp to local timezone and format it to "yyyy-MM-dd"
            df = df.withColumn(col, date_format(from_utc_timestamp(df[col].cast(TimestampType()), "UTC"), "yyyy-MM-dd"))

    # Construct the output path for saving the transformed DataFrame
    output_path = '/mnt/silver/SalesLT/' + i + '/'
    
    # Write the transformed DataFrame to Delta format, overwriting any existing data
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

# Display the final DataFrame (for the last processed table)
display(df)

# COMMAND ----------
