
locals {
  dest_config = jsonencode([
    {
      connectorType : "S3",
      destinationConnectorProperties : {
        "S3" : {
          "bucketName" : var.dest_bucket_name,
          "s3OutputFormatConfig" : {
            "fileType" : "JSON",
            "prefixConfig" : {
              "prefixType" : "PATH",
              "prefixFormat" : "HOUR",
              "pathPrefixHierarchy" : [
                "SCHEMA_VERSION",
                "EXECUTION_ID"
              ]
            },
            "aggregationConfig" : {
              "aggregationType" : "None",
              "targetFileSize" : 384
            }
          }
        }
      }
    }
  ])

  marketing_dest_config = jsonencode([
    {
      connectorType : "S3",
      destinationConnectorProperties : {
        "S3" : {
          "bucketName" : var.dest_bucket_name,
          "s3OutputFormatConfig" : {
            "fileType" : "PARQUET",
            "prefixConfig" : {
              "prefixType" : "PATH",
              "prefixFormat" : "HOUR",
              "pathPrefixHierarchy" : [
                "SCHEMA_VERSION",
                "EXECUTION_ID"
              ]
            },
            "aggregationConfig" : {
              "aggregationType" : "None",
              "targetFileSize" : 384
            }
          }
        }
      }
    }
  ])
}
