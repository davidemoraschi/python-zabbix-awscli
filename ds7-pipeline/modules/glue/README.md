1. Glue Data Catalog - to store metadata and schema information for data assets in the data lake
1.1. aws_glue_catalog_database - creates a Glue database

2. aws_glue_catalog_table - creates a Glue table within a database

3. Glue Crawlers - to automatically discover schema and metadata of data assets in the data lake 
2.1. aws_glue_crawler - creates a Glue crawler to crawl data from a data source and populate metadata into the Glue Data Catalog

4. Glue Jobs - to transform and process data using ETL jobs
3.1. aws_glue_job - creates a Glue job to run an ETL process on the data
