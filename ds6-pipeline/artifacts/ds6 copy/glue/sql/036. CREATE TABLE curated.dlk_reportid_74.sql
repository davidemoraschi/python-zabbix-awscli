CREATE TABLE IF NOT EXISTS "stg-dlk-sbx-cl-3-curated-db".dlk_reportid_74
WITH (table_type = 'ICEBERG',
      format = 'ORC', 
      write_compression ='ZSTD',
      location = 's3://stg-dlk-sbx-cl-3-curated/iceberg/dlk_reportid_74/', 
      is_external = false,
--      partitioning = ARRAY['month(dt)'],
      vacuum_min_snapshots_to_keep = 10,
      vacuum_max_snapshot_age_seconds = 604800
   )
AS
SELECT
    "user.iduser"
    , user_profession_code
    , user_professional_specialization
    , user_country_code
    , "course.uidcourse"
    , "enrollment.status"
    , "enrollment.date_inscr"
    , course_external_course_number
    , "course.course_type"
    , "course.name"
    , "user.register_date"
    , "course.course_internal_id"
FROM
    "stg-dlk-sbx-ds6-refined-db".dlk_reportid_74
;
