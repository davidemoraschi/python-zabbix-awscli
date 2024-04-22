CREATE TABLE IF NOT EXISTS "stg-dlk-sbx-ds6-refined-db".dlk_reportid_75
WITH (table_type = 'ICEBERG',
      format = 'ORC', 
      write_compression ='ZSTD',
      location = 's3://stg-dlk-sbx-ds-6-refined/iceberg/dlk_reportid_75/', 
      is_external = false,
--      partitioning = ARRAY['month(dt)'],
      vacuum_min_snapshots_to_keep = 10,
      vacuum_max_snapshot_age_seconds = 604800
   )
AS
SELECT
    "external course number"        AS "course_external_course_number"
    , "course internal id"          AS "course.course_internal_id"
FROM
    "stg-dlk-sbx-ds6-raw-db".docebo_users_courses_csv_gzip
WHERE
    "course internal id" IS NOT NULL
;
