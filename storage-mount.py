# Databricks notebook source

# Define configuration settings for Azure Data Lake Storage
# تعريف إعدادات التكوين لتخزين بيانات Azure Data Lake
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",  # Specify the authentication type as Custom Access Token
  # تحديد نوع المصادقة كـ Custom Access Token
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")  # Get the token provider class name from Spark configuration
  # الحصول على اسم فئة موفر الرمز من إعدادات Spark
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
# يمكن أن تضيف <directory-name> إلى URI المصدر لنقطة التحميل الخاصة بك اختيارياً.
# Mount the Bronze layer of the Azure Data Lake Storage
# تحميل الطبقة البرونزية من تخزين بيانات Azure Data Lake
dbutils.fs.mount(
  source = "abfss://bronze@mrkdatalakegen2.dfs.core.windows.net/",  # Source URI for the Bronze layer
  # URI المصدر للطبقة البرونزية
  mount_point = "/mnt/bronze",  # Mount point in Databricks file system
  # نقطة التحميل في نظام ملفات Databricks
  extra_configs = configs)  # Pass the configuration settings
  # تمرير إعدادات التكوين

# COMMAND ----------
# List the contents of the SalesLT directory in the mounted Bronze layer
# عرض محتويات دليل SalesLT في الطبقة البرونزية المحملة
dbutils.fs.ls("/mnt/bronze/SalesLT/")  # Display files and directories under /mnt/bronze/SalesLT/
# عرض الملفات والدلائل تحت /mnt/bronze/SalesLT/

# COMMAND ----------

# Define configuration settings for Azure Data Lake Storage again for the Silver layer
# تعريف إعدادات التكوين لتخزين بيانات Azure Data Lake مرة أخرى للطبقة الفضية
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",  # Specify the authentication type as Custom Access Token
  # تحديد نوع المصادقة كـ Custom Access Token
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")  # Get the token provider class name from Spark configuration
  # الحصول على اسم فئة موفر الرمز من إعدادات Spark
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
# يمكن أن تضيف <directory-name> إلى URI المصدر لنقطة التحميل الخاصة بك اختيارياً.
# Mount the Silver layer of the Azure Data Lake Storage
# تحميل الطبقة الفضية من تخزين بيانات Azure Data Lake
dbutils.fs.mount(
  source = "abfss://silver@mrkdatalakegen2.dfs.core.windows.net/",  # Source URI for the Silver layer
  # URI المصدر للطبقة الفضية
  mount_point = "/mnt/silver",  # Mount point in Databricks file system
  # نقطة التحميل في نظام ملفات Databricks
  extra_configs = configs)  # Pass the configuration settings
  # تمرير إعدادات التكوين

# COMMAND ----------

# Define configuration settings for Azure Data Lake Storage again for the Gold layer
# تعريف إعدادات التكوين لتخزين بيانات Azure Data Lake مرة أخرى للطبقة الذهبية
configs = {
  "fs.azure.account.auth.type": "CustomAccessToken",  # Specify the authentication type as Custom Access Token
  # تحديد نوع المصادقة كـ Custom Access Token
  "fs.azure.account.custom.token.provider.class": spark.conf.get("spark.databricks.passthrough.adls.gen2.tokenProviderClassName")  # Get the token provider class name from Spark configuration
  # الحصول على اسم فئة موفر الرمز من إعدادات Spark
}

# Optionally, you can add <directory-name> to the source URI of your mount point.
# يمكن أن تضيف <directory-name> إلى URI المصدر لنقطة التحميل الخاصة بك اختيارياً.
# Mount the Gold layer of the Azure Data Lake Storage
# تحميل الطبقة الذهبية من تخزين بيانات Azure Data Lake
dbutils.fs.mount(
  source = "abfss://gold@mrkdatalakegen2.dfs.core.windows.net/",  # Source URI for the Gold layer
  # URI المصدر للطبقة الذهبية
  mount_point = "/mnt/gold",  # Mount point in Databricks file system
  # نقطة التحميل في نظام ملفات Databricks
  extra_configs = configs)  # Pass the configuration settings
  # تمرير إعدادات التكوين

# COMMAND ----------
