-- Create a new login for SQL Server with the specified username and password
-- إنشاء تسجيل دخول جديد لـ SQL Server باستخدام اسم المستخدم وكلمة المرور المحددين
CREATE LOGIN <your username> WITH PASSWORD = 'your password';

-- Create a user associated with the login created above
-- إنشاء مستخدم مرتبط بتسجيل الدخول الذي تم إنشاؤه أعلاه
CREATE USER <your username> FOR LOGIN <your username>;

-- Query to select table names and schemas from the information_schema for the SalesLT schema
-- استعلام لاختيار أسماء الجداول والمخططات من information_schema لمخطط SalesLT
SELECT
    TABLE_NAME,        -- The name of the table
    TABLE_SCHEMA       -- The schema of the table
FROM 
    information_schema.TABLES
WHERE 
    table_schema = 'SalesLT'   -- Filter to only include tables from the SalesLT schema
AND
    table_type = 'BASE TABLE';  -- Ensure that only base tables are selected

-- Another query to get table names and schemas using sys.tables and sys.schemas
-- استعلام آخر للحصول على أسماء الجداول والمخططات باستخدام sys.tables و sys.schemas
SELECT 
    t.name,          -- Name of the table
    s.name           -- Name of the schema
FROM 
    sys.tables t     -- Alias for tables
INNER JOIN 
    sys.schemas s    -- Alias for schemas
ON 
    t.schema_id = s.schema_id  -- Join condition on schema_id
WHERE 
    s.name = 'SalesLT'; -- Filter to only include schemas named SalesLT

-- Use the specified database named gold_DB
-- استخدام قاعدة البيانات المحددة المسماة gold_DB
USE gold_DB;
GO

-- Create or alter a stored procedure named CreateSQLServerlessView_gold
-- إنشاء أو تعديل إجراء مخزن يسمى CreateSQLServerlessView_gold
CREATE OR ALTER PROCEDURE CreateSQLServerlessView_gold 
    @view_name NVARCHAR(100)  -- Parameter for the name of the view
AS 
BEGIN

    -- Declare a variable to hold the dynamic SQL statement
    -- إعلان متغير لتخزين جملة SQL الديناميكية
    DECLARE @sql VARCHAR(max);
    
    -- Construct the SQL statement to create or alter the view
    -- بناء جملة SQL لإنشاء أو تعديل العرض
    SET @sql = CONCAT(N'CREATE OR ALTER VIEW ', @view_name, ' AS 
    SELECT * FROM OPENROWSET(
        BULK ''https://<your datalake gen2 storage account name>.dfs.core.windows.net/gold/SalesLT/Address/'',
        FORMAT = ''DELTA''
    ) AS [result]');

    -- Execute the constructed SQL statement
    -- تنفيذ جملة SQL التي تم بناؤها
    EXEC (@sql);
END
GO
