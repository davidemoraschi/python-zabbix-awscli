CREATE EXTERNAL TABLE IF NOT EXISTS `stg-dlk-sbx-ds6-raw-db`.docebo_user_session_csv_gzip 
    (
         `Username`                                                 string
        ,`Account code`                                             string
        ,`Aligner Experience Level`                                 string
        ,`Are you a Speaker Mentor or KOL for ClearCorrect`         string
        ,`Are you a Straumann Employee`                             string
        ,`Are you an AGD (Academy of General Dentistry) Member`     string
        ,`Are you licensed in the state of Vermont`                 string
        ,`Are you part of a DSO (Dental Service Organization)`      string
        ,`Branch Name`                                              string
        ,`Branch path`                                              string
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
        ,`DSO Member Code`                                          string
        ,`Email`                                                    string
        ,`Email Validation Status`                                  string
        ,`Endereço`                                                 string
        ,`Especialidade`                                            string
        ,`Estado`                                                   string
        ,`First Name`                                               string
        ,`Full Name`                                                string
        ,`House Number`                                             string
        ,`If Other Enter Country`                                   string
        ,`If Other Enter Your DSO Name Here`                        string
        ,`If Yes Enter AGD Number`                                  string
        ,`If Yes Enter NPI #`                                       string
        ,`If Yes Enter Straumann Customer #`                        string
        ,`Last Name`                                                string
        ,`License # - enter N/A if not applicable`                  string
        ,`License # - STMGR`                                        string
        ,`License # CA - STMGR`                                     string
        ,`License State - STMGR`                                    string
        ,`License State CA - STMGR`                                 string
        ,`Memeberships`                                             string
        ,`My First Implant`                                         string
        ,`Nome Completo`                                            string
        ,`NPI # - STMGR`                                            string
        ,`NPI (National Provider Identifier) #`                     string
        ,`Número de celular`                                        string
        ,`Ocupação`                                                 string
        ,`Organization customer number`                             string
        ,`País`                                                     string
        ,`Phone Number`                                             string
        ,`Profession code`                                          string
        ,`Professional Specialization`                              string
        ,`Registration Number:`                                     string
        ,`Specialty/Profession`                                     string
        ,`Specialty/Profession - Enter Other`                       string
        ,`State`                                                    string
        ,`State of Licensure`                                       string
        ,`State/Province`                                           string
        ,`Straumann Customer #`                                     string
        ,`Street and house number - required for AGD members`       string
        ,`Street Name`                                              string
        ,`Title`                                                    string
        ,`Training Program Neodent`                                 string
        ,`Training Program Straumann`                               string
        ,`User Creation Date`                                       string
        ,`User Expiration Date`                                     string
        ,`User Last Access Date`                                    string
        ,`User Level`                                               string
        ,`User Suspension Date`                                     string
        ,`User unique ID`                                           string
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
        ,`Course end date`                                          string
        ,`Course has expired`                                       string
        ,`Course Internal ID`                                       string
        ,`Course location`                                          string
        ,`Course Start Date`                                        string
        ,`Course Status`                                            string
        ,`Course Type`                                              string
        ,`Course Unique ID`                                         string
        ,`Credits (CEUs)`                                           string
        ,`Duration`                                                 string
        ,`External Course Number`                                   string
        ,`Instructor`                                               string
        ,`Language`                                                 string
        ,`Learning Plan Name`                                       string
        ,`Program Format`                                           string
        ,`Skills in course`                                         string
        ,`Speaker 1`                                                string
        ,`Verification Code`                                        string
        ,`Verification Code AGD`                                    string
        ,`Evaluation Score Base`                                    string
        ,`Program Format_1`                                         string
        ,`Program Format_1 1`                                       string
        ,`Session Attendance Type`                                  string
        ,`Session Code`                                             string
        ,`Session End Date`                                         string
        ,`Session Instructor Full Name`                             string
        ,`Session Instructor Username`                              string
        ,`Session Maximum Enrollments`                              string
        ,`Session Minimum Enrollments`                              string
        ,`Session Name`                                             string
        ,`Session Start Date`                                       string
        ,`Session Unique ID`                                        string
        ,`Time in Session`                                          string
        ,`Webinar Instructor_1`                                     string
        ,`Webinar Tool`                                             string
        ,`Webinar Tool Time in Session`                             string
        ,`Event Date`                                               string
        ,`Event Duration`                                           string
        ,`Event ID`                                                 string
        ,`Event Instructor Full Name`                               string
        ,`Event Instructor User Name`                               string
        ,`Event Name`                                               string
        ,`Event Start Date`                                         string
        ,`Event Time Zone`                                          string
        ,`Event Type`                                               string
        ,`Archive Date`                                             string
        ,`Archived Enrollment (Yes / No)`                           string
        ,`Attendance`                                               string
        ,`Completion Date`                                          string
        ,`Course Enrollment Status`                                 string
        ,`Enrollment Date`                                          string
        ,`Evaluation Status`                                        string
        ,`Event Attendance (Hours)`                                 string
        ,`Event Attendance (Status)`                                string
        ,`Instructor Feedback`                                      string
        ,`Learner evaluation`                                       string
        ,`Session Completion Date`                                  string
        ,`Session Enrollment Date`                                  string
        ,`Session Enrollment Status`                                string
        ,`User Course Level`                                        string    )
ROW FORMAT SERDE 'org.apache.hadoop.hive.serde2.OpenCSVSerde'
WITH SERDEPROPERTIES 
('separatorChar' = ',', 'quoteChar' = '"', 'escapeChar' = '\\')
LOCATION 's3://stg-dlk-sbx-ds-6-raw/docebo_feed/User_ILT_Session'
TBLPROPERTIES ('skip.header.line.count' = '1')
;
