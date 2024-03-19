CREATE EXTERNAL TABLE IF NOT EXISTS `stg-dlk-sbx-ds6-raw-db`.docebo_users_training_material_csv_gzip 
    (
         `Username`                                                 string
        ,`Account code`                                             string
        ,`Aligner Experience LEVEL`                                 string
        ,`ARE you a Speaker Mentor OR KOL FOR ClearCorrect`         string
        ,`ARE you a Straumann Employee`                             string
        ,`ARE you an AGD (Academy OF GENERAL Dentistry) MEMBER`     string
        ,`ARE you licensed IN the state OF Vermont`                 string
        ,`ARE you part OF a DSO (Dental Service Organization)`      string
        ,`Branch Name`                                              string
        ,`Branch PATH`                                              string
        ,`Branches Codes`                                           string
        ,`Cidade`                                                   string
        ,`City`                                                     string
        ,`City 1`                                                   string
        ,`Company city`                                             string
        ,`Company house number`                                     string
        ,`Company name`                                             string
        ,`Company name 2`                                           string
        ,`Company state`                                            string
        ,`Company Street`                                           string
        ,`Company Zip code`                                         string
        ,`Country`                                                  string
        ,`Country code`                                             string
        ,`Deactivated`                                              string
        ,`Direct Manager`                                           string
        ,`DSO MEMBER Code`                                          string
        ,`Email`                                                    string
        ,`Email Validation Status`                                  string
        ,`Endereço`                                                 string
        ,`Especialidade`                                            string
        ,`Estado`                                                   string
        ,`FIRST Name`                                               string
        ,`FULL Name`                                                string
        ,`House Number`                                             string
        ,`IF Other Enter Country`                                   string
        ,`IF Other Enter Your DSO Name Here`                        string
        ,`IF Yes Enter AGD Number`                                  string
        ,`IF Yes Enter NPI #`                                       string
        ,`IF Yes Enter Straumann Customer #`                        string
        ,`LAST Name`                                                string
        ,`License # - enter N / A IF NOT applicable`                string
        ,`License # - STMGR`                                        string
        ,`License # CA - STMGR`                                     string
        ,`License State - STMGR`                                    string
        ,`License State CA - STMGR`                                 string
        ,`Memeberships`                                             string
        ,`My FIRST Implant`                                         string
        ,`Nome Completo`                                            string
        ,`NPI # - STMGR`                                            string
        ,`NPI (NATIONAL Provider Identifier) #`                     string
        ,`Número de celular`                                        string
        ,`Ocupação`                                                 string
        ,`Organization customer number`                             string
        ,`País`                                                     string
        ,`Phone Number`                                             string
        ,`Profession code`                                          string
        ,`Professional Specialization`                              string
        ,`Registration Number:`                                     string
        ,`Specialty / Profession`                                   string
        ,`Specialty / Profession - Enter Other`                     string
        ,`State`                                                    string
        ,`State OF Licensure`                                       string
        ,`State / Province`                                         string
        ,`Straumann Customer #`                                     string
        ,`Street AND house number - required FOR AGD members`       string
        ,`Street Name`                                              string
        ,`Title`                                                    string
        ,`Training Program Neodent`                                 string
        ,`Training Program Straumann`                               string
        ,`USER Creation Date`                                       string
        ,`USER Expiration Date`                                     string
        ,`USER LAST Access Date`                                    string
        ,`USER LEVEL`                                               string
        ,`USER Suspension Date`                                     string
        ,`USER UNIQUE ID`                                           string
        ,`Young Professional`                                       string
        ,`Zip Code`                                                 string
        ,`ZIP code 1`                                               string
        ,`Course Name`                                              string
        ,`Actual Total 1`                                           string
        ,`Actual Total 2`                                           string
        ,`AGD Subject Code`                                         string
        ,`Allocation Category 1`                                    string
        ,`Allocation Category 2`                                    string
        ,`Budget Category 1`                                        string
        ,`Budget Category 2`                                        string
        ,`Budget Item Name 1`                                       string
        ,`Budget Item Name 2`                                       string
        ,`CDE Hours`                                                string
        ,`Course Category`                                          string
        ,`Course Category Code`                                     string
        ,`Course code`                                              string
        ,`Course Creation Date`                                     string
        ,`Course duration`                                          string
        ,`Course END date`                                          string
        ,`Course has expired`                                       string
        ,`Course Internal ID`                                       string
        ,`Course location`                                          string
        ,`Course START Date`                                        string
        ,`Course Status`                                            string
        ,`Course TYPE`                                              string
        ,`Course UNIQUE ID`                                         string
        ,`Credits (CEUs)`                                           string
        ,`Duration`                                                 string
        ,`EXTERNAL Course Number`                                   string
        ,`Instructor`                                               string
        ,`LANGUAGE`                                                 string
        ,`Learning Plan Name`                                       string
        ,`Program Format`                                           string
        ,`Speaker 1`                                                string
        ,`Verification Code`                                        string
        ,`Verification Code AGD`                                    string
        ,`Bookmark`                                                 string
        ,`Training Material Title`                                  string
        ,`Attempt Date`                                             string
        ,`FIRST attempt`                                            string
        ,`Training Material LAST Completion Date`                   string
        ,`Training Material Score`                                  string
        ,`Training Material Status`                                 string
        ,`Training Material TYPE`                                   string
        ,`Training Material Version`                                string
        ,`Completion Date`                                          string
        ,`Enrollment Date`                                          string
    )
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES 
('separatorChar' = ',', 'quoteChar' = '"', 'escapeChar' = '\\')
LOCATION 's3://stg-dlk-sbx-ds-6-raw/docebo_feed/Users_Training_Material'
TBLPROPERTIES ('skip.header.line.count' = '1', 'classification'='csv')
;
