CREATE TABLE IF NOT EXISTS "stg-dlk-sbx-ds6-refined-db".dlk_reportid_74
AS
SELECT DISTINCT
      "user unique id"                      AS "user.iduser"
    , "profession code"                     AS "user_profession_code"
    , "professional specialization"         AS "user_professional_specialization"
    , "country code"                        AS "user_country_code"
    , "course unique id"                    AS "course.uidcourse"
    , "course enrollment status"            AS "enrollment.status"
    , "enrollment date"                     AS "enrollment.date_inscr"
    , "external course number"              AS course_external_course_number
    , "course type"                         AS "course.course_type"
    , "course name"                         AS "course.name"
    , "user creation date"                  AS "user.register_date"
    , "course internal id"                  AS "course.course_internal_id"
FROM
    "stg-dlk-sbx-ds6-raw-db".docebo_users_courses_csv_gzip
WHERE "user unique id" IS NOT NULL
AND "course internal id" IS NOT NULL
;
