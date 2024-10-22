# **DEPI-Data-Warehouse-and-BI-Dashboard-for-Retail-ver1**

### **Overview**
This repository presents a comprehensive **end-to-end data engineering pipeline** built using **Azure services**. The project leverages **Azure Data Factory** for orchestration, **Azure Databricks** for data transformation using PySpark, **Azure Synapse Analytics** for data warehousing, and **Power BI** for visualization and reporting.



---

## **Project Structure**
The project components are as follows:

- **Key Vault**: Secures secrets and eliminates hard-coded security information.
- **Azure Storage Account**: Provides scalable cloud storage solutions.
- **Azure Data Factory (ADF)**: Orchestrates data movement and automates workflows.
- **Azure Databricks**: Transforms data, applying bronze-silver-gold transformations.
- **Azure Synapse Analytics**: Performs data warehousing and querying.
- **Power BI**: Visualizes data and delivers interactive reporting.


![01](https://github.com/user-attachments/assets/322a6cbb-21ae-49d7-901d-e4aa60a3efa6)

![02](https://github.com/user-attachments/assets/4304d3b3-4f72-44d1-bcf4-86c1014d4167)

![03](https://github.com/user-attachments/assets/2f45c3f7-6c4f-4e9c-a2a8-4cb36e1efc3d)



---

## **Prerequisites**
Before setting up the project, ensure you have the following:

- An Azure subscription with sufficient permissions.
- Access to Azure Data Factory, Databricks, Synapse Analytics, and Power BI.
- Basic understanding of Azure cloud services and data engineering concepts.

---

## **Getting Started**

### **1. Download and Restore AdventureWorksLT2017 Database**
- **Download the Database**: Get the AdventureWorksLT2017 database.
- **Restore the Database**: Follow the guide to restore the database on your SQL Server instance.
- **Setting User for login**: Copy the first two row from SQL Commands
- **Add this user and password as Key Vault secrets**:

![04](https://github.com/user-attachments/assets/f8454bc1-85ab-4ca6-9cb7-1af324d70d32)

![05](https://github.com/user-attachments/assets/3790df6f-bbe8-43f5-9e7e-3d4e98972479)

![06](https://github.com/user-attachments/assets/2d3bd1e6-e5c7-4a29-b897-9c256b213c25)

 

---

### **2. Azure Data Factory (ADF) Setup**
- **Orchestrate Data**: Use ADF to manage data movement and workflow automation.
- **Create Pipelines**: Set up pipelines to orchestrate Databricks transformations.
- **Configure Linked Services**: Set up connections to Azure SQL Database, Blob Storage, etc.
- **Data Flows**: Create and debug data flows for transformations and cleansing.

![07](https://github.com/user-attachments/assets/1811dbc2-25a9-4510-8543-19a89a7baece)

![08](https://github.com/user-attachments/assets/9472000c-449a-4771-9069-42e3c3b2d4b8)

![09](https://github.com/user-attachments/assets/3676c099-f545-4a69-95df-f70b04de010d)

![10](https://github.com/user-attachments/assets/d80a9d39-b277-4b9f-a59c-924779e48ea2)

![11](https://github.com/user-attachments/assets/b22dffb5-aad7-4f45-950a-9598b5b31446)

![12](https://github.com/user-attachments/assets/0c6e0bde-1a15-45c0-a0e4-85e0967db0eb)

![13](https://github.com/user-attachments/assets/b3a05c53-1301-4044-927d-16bf54e68e0b)

![14](https://github.com/user-attachments/assets/0eeb6259-5ef1-4628-bb8e-d94e232190cb)

![15](https://github.com/user-attachments/assets/4faf4108-e360-4d38-801f-89a601281eb8)

![16](https://github.com/user-attachments/assets/c51e03e7-3b0b-4f9d-b5ab-9cfe08f9d594)

![17](https://github.com/user-attachments/assets/b6093381-59bf-4d5d-a860-2348aa50f154)


---

### **3. Azure Databricks Setup**
- **Create a Databricks Workspace**: Set up and configure a cluster for data processing.
- **Develop Python Notebooks**: Use PySpark to write and run notebooks that transform data between bronze, silver, and gold layers.
- **Integrate with ADF**: Link Databricks notebooks to ADF for orchestration and scheduling.



---

### **4. Azure Synapse Analytics Setup**
- **Create Synapse Workspace**: Set up Synapse Analytics for big data processing and warehousing.
- **Data Warehousing**: Set up dedicated or serverless SQL pools to perform queries and transformations.
- **Run Queries**: Execute SQL queries to extract insights from the transformed data.



---

### **5. Power BI Setup**
- **Connect Power BI to Synapse**: Import data from Synapse Analytics into Power BI.
- **Design Reports**: Create interactive visualizations and dashboards that provide real-time insights.
- **Publish to Power BI Service**: Publish your reports for sharing and collaboration with stakeholders.



---

## **Conclusion**
This project demonstrates the full implementation of an **end-to-end data engineering pipeline** on Azure. It showcases how various Azure services can be combined to deliver a scalable, secure, and powerful data solution. By following the steps in this guide, you can replicate the solution in your own environment, customize it, and understand the overall data flow.

---

## **Additional Resources**
- [Azure Data Factory Documentation](https://learn.microsoft.com/en-us/azure/data-factory/)
- [Azure Databricks Documentation](https://learn.microsoft.com/en-us/azure/databricks/)
- [Azure Synapse Analytics Documentation](https://learn.microsoft.com/en-us/azure/synapse-analytics/)
- [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)
