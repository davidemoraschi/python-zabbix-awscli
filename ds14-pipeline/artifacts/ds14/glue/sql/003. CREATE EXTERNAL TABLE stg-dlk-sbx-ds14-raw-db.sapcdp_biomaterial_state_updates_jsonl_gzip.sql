CREATE EXTERNAL TABLE IF NOT EXISTS `stg-dlk-sbx-ds14-raw-db`.sapcdp_biomaterial_state_updates_jsonl_gzip 
(
`contactId` string
,`eventType` string
,`eventAttributes` string
)
ROW FORMAT SERDE 'org.openx.data.jsonserde.JsonSerDe'
LOCATION 's3://stg-dlk-sbx-ds-14-raw/events_feed/events_jsonl_gzip/BIOMATERIAL_STATE_UPDATE'
;
