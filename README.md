# **End-to-End Azure Data Engineering Pipeline**

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
![Resource group](https://github.com/user-attachments/assets/efdce2f3-ac53-44b0-8365-e21cb736a8e0)

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
- **Add this user and password as Key Vault secrets**:![like this](https://github.com/user-attachments/assets/82a7aa7e-0f56-4605-9ad1-643e0435ef12)
 

---

### **2. Azure Data Factory (ADF) Setup**
- **Orchestrate Data**: Use ADF to manage data movement and workflow automation.
- **Create Pipelines**: Set up pipelines to orchestrate Databricks transformations.
- **Configure Linked Services**: Set up connections to Azure SQL Database, Blob Storage, etc.
- **Data Flows**: Create and debug data flows for transformations and cleansing.
![Final look on ADF](https://github.com/user-attachments/assets/f625827f-ab85-46fe-93cd-3856cee735c5)
)

---

### **3. Azure Databricks Setup**
- **Create a Databricks Workspace**: Set up and configure a cluster for data processing.
- **Develop Python Notebooks**: Use PySpark to write and run notebooks that transform data between bronze, silver, and gold layers.
- **Integrate with ADF**: Link Databricks notebooks to ADF for orchestration and scheduling.
![Final look on databricks](https://github.com/user-attachments/assets/549b5820-bdfb-4a95-9ab2-6ceef4e37c7e)

---

### **4. Azure Synapse Analytics Setup**
- **Create Synapse Workspace**: Set up Synapse Analytics for big data processing and warehousing.
- **Data Warehousing**: Set up dedicated or serverless SQL pools to perform queries and transformations.
- **Run Queries**: Execute SQL queries to extract insights from the transformed data.
![Azure Synapse Analytics after setting the pipeline](https://github.com/user-attachments/assets/5efa0047-5fa2-42b2-9a02-fa989d11c2c3)

---

### **5. Power BI Setup**
- **Connect Power BI to Synapse**: Import data from Synapse Analytics into Power BI.
- **Design Reports**: Create interactive visualizations and dashboards that provide real-time insights.
- **Publish to Power BI Service**: Publish your reports for sharing and collaboration with stakeholders.
![PowerBI](https://github.com/user-attachments/assets/0b56a58c-721a-4a62-8e02-e0dd3e9f7198)

---

## **Conclusion**
This project demonstrates the full implementation of an **end-to-end data engineering pipeline** on Azure. It showcases how various Azure services can be combined to deliver a scalable, secure, and powerful data solution. By following the steps in this guide, you can replicate the solution in your own environment, customize it, and understand the overall data flow.

---

## **Additional Resources**
- [Azure Data Factory Documentation](https://learn.microsoft.com/en-us/azure/data-factory/)
- [Azure Databricks Documentation](https://learn.microsoft.com/en-us/azure/databricks/)
- [Azure Synapse Analytics Documentation](https://learn.microsoft.com/en-us/azure/synapse-analytics/)
- [Power BI Documentation](https://learn.microsoft.com/en-us/power-bi/)
