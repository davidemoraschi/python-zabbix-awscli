CREATE EXTERNAL TABLE IF NOT EXISTS `stg-dlk-sbx-ds6-raw-db`.docebo_groups_courses_csv_gzip 
    (
         `GROUP/Branch Name`                               string
        ,`Members`                                         string
        ,`Course Name`                                     string
        ,`Actual Total 1`                                  string
        ,`Actual Total 2`                                  string
        ,`AGD Subject Code`                                string
        ,`Allocation Category 1`                           string
        ,`Allocation Category 2`                           string
        ,`Budget Category 1`                               string
        ,`Budget Category 2`                               string
        ,`Budget Item Name 1`                              string
        ,`Budget Item Name 2`                              string
        ,`CDE Hours`                                       string
        ,`Course Category`                                 string
        ,`Course Category Code`                            string
        ,`Course code`                                     string
        ,`Course Creation Date`                            string
        ,`Course duration`                                 string
        ,`Course end date`                                 string
        ,`Course has expired`                              string
        ,`Course Internal ID`                              string
        ,`Course location`                                 string
        ,`Course Start Date`                               string
        ,`Course Status`                                   string
        ,`Course Type`                                     string
        ,`Course Unique ID`                                string
        ,`Credits (CEUs)`                                  string
        ,`Duration`                                        string
        ,`External Course Number`                          string
        ,`Instructor`                                      string
        ,`Language`                                        string
        ,`Learning Plan Name`                              string
        ,`Program Format`                                  string
        ,`Skills in course`                                string
        ,`Speaker 1`                                       string
        ,`Verification Code`                               string
        ,`Verification Code AGD`                           string
        ,`Completed User Status`                           string
        ,`Completed User Status %`                         string
        ,`In Progress User Status`                         string
        ,`In Progress User Status %`                       string
        ,`Not Started User Status`                         string
        ,`Not Started User Status %`                       string
        ,`Enrolled Users`                                  string
        ,`Session Time (min)`                              string
        ,`Training Material Time (sec)`                    string
    )
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES 
('separatorChar' = ',', 'quoteChar' = '"', 'escapeChar' = '\\')
LOCATION 's3://stg-dlk-sbx-ds-6-raw/docebo_feed/Groups_Courses'
TBLPROPERTIES ('skip.header.line.count' = '1')
;
