# Databricks notebook source
# MAGIC %md
# MAGIC ## Doing transformation for all tables (Changing column names)
# MAGIC 
# MAGIC ## إجراء تحويل لجميع الجداول (تغيير أسماء الأعمدة)

# COMMAND ----------

# Initialize an empty list to store table names
# إنشاء قائمة فارغة لتخزين أسماء الجداول
table_name = []

# Loop through all files in the specified directory
# التكرار عبر جميع الملفات في الدليل المحدد
for i in dbutils.fs.ls('mnt/silver/SalesLT/'):
    print(i.name)  # Print the name of each file
    # Append the table name to the list, extracting it from the file path
    # إضافة اسم الجدول إلى القائمة، واستخراجه من مسار الملف
    table_name.append(i.name.split('/')[0])

# COMMAND ----------

# Display the list of table names
# عرض قائمة أسماء الجداول
table_name

# COMMAND ----------

# Loop through each table name to perform transformations
# التكرار عبر كل اسم جدول لتنفيذ التحويلات
for name in table_name:
    # Construct the full path to the current table
    # إنشاء المسار الكامل للجدول الحالي
    path = '/mnt/silver/SalesLT/' + name
    print(path)  # Print the full path of the current table
    
    # Read the table into a DataFrame using Delta format
    # قراءة الجدول إلى DataFrame باستخدام تنسيق Delta
    df = spark.read.format('delta').load(path)

    # Get the list of column names from the DataFrame
    # الحصول على قائمة بأسماء الأعمدة من DataFrame
    column_names = df.columns

    # Loop through each column name to rename it
    # التكرار عبر كل اسم عمود لإعادة تسميته
    for old_col_name in column_names:
        # Convert column name from ColumnName to Column_Name format
        # تحويل اسم العمود من صيغة ColumnName إلى صيغة Column_Name
        new_col_name = "".join(
            ["_" + char if char.isupper() and not old_col_name[i - 1].isupper() else char 
             for i, char in enumerate(old_col_name)]
        ).lstrip("_")  # Remove leading underscore if it exists
        
        # Change the column name using withColumnRenamed
        # تغيير اسم العمود باستخدام withColumnRenamed
        df = df.withColumnRenamed(old_col_name, new_col_name)

    # Construct the output path for the transformed table
    # إنشاء مسار الإخراج للجدول الذي تم تحويله
    output_path = '/mnt/gold/SalesLT/' + name + '/'
    
    # Write the transformed DataFrame to the specified output path
    # كتابة DataFrame المحوَّل إلى مسار الإخراج المحدد
    df.write.format('delta').mode("overwrite").save(output_path)

# COMMAND ----------

# Display the final DataFrame (optional)
# عرض DataFrame النهائي (اختياري)
display(df)

# COMMAND ----------
