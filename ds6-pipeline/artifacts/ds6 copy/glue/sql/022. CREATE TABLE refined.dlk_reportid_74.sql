CREATE TABLE IF NOT EXISTS "stg-dlk-sbx-ds6-refined-db".dlk_reportid_74
WITH (table_type = 'ICEBERG',
      format = 'ORC', 
      write_compression ='ZSTD',
      location = 's3://stg-dlk-sbx-ds-6-refined/iceberg/dlk_reportid_74/', 
      is_external = false,
--      partitioning = ARRAY['month(dt)'],
      vacuum_min_snapshots_to_keep = 10,
      vacuum_max_snapshot_age_seconds = 604800
   )
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
    AND email NOT LIKE '%@straumann.com%'
    AND email NOT LIKE '%@im-systems.de%'
    AND email NOT LIKE '%@anthogyr.com%'
    AND email NOT LIKE '%@medentika.de%'
    AND email NOT LIKE '%@imsssde.de%'
    AND email NOT LIKE '%@ims.de%'
    AND email NOT LIKE '%@user.de%'
    AND email NOT LIKE '%@test.de%'
    AND email NOT LIKE '%@neodent.com%'
    AND email NOT LIKE '%@dental-wings.com%'
    AND email NOT LIKE '%@clearcorrect.com%'
    AND email NOT LIKE '%@private.ch%'
    AND email NOT LIKE '%@ch.ch%'
    AND email NOT LIKE '%@im-de.de%'
    AND email NOT LIKE '%@registrationtest.com%'
    AND email NOT LIKE '%@test562.it%'
    AND email NOT LIKE '%@rebelartistry.com%'
    AND email NOT LIKE '%@wearehackerone.com%'
    AND email NOT IN ('testuser@yahoo.com',
                        'testing@six-group.com',
                        'test@multi.de',
                        'test.victim@example.com',
                        'pegnevsales@aol.com',
                        'tomasz.dzierzewicz@rebelartistry.com',
                        'zejnilos@gmail.com',
                        'aurinko_paistaa@registrationtest.com',
                        'fmbarani@gmail.com',
                        'TEST@gmail.com')
;
