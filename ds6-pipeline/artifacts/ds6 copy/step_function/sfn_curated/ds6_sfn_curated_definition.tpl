{
    "StartAt": "run_glue_job_refined_to_curated",
    "States": {
      "run_glue_job_refined_to_curated": {
          "Type": "Task",
          "Resource": "arn:aws:states:::glue:startJobRun.sync",
          "Parameters": {
              "JobName": "${glue_job_name}"
          },
          "ResultPath": "$.glue_job_run",
          "Next": "StartCrawler"
      },
      "StartCrawler": {
        "Type": "Task",
        "Parameters": {
            "Name": "${crawler_name}"
        },
        "Resource": "arn:aws:states:::aws-sdk:glue:startCrawler",
        "Retry": [
            {
                "ErrorEquals": [
                    "Glue.EntityNotFoundException"
                ],
                "BackoffRate": 1,
                "IntervalSeconds": 1,
                "MaxAttempts": 0,
                "Comment": "EntityNotFoundException - Fail immediately"
            },
            {
                "ErrorEquals": [
                    "Glue.CrawlerRunningException"
                ],
                "BackoffRate": 1,
                "IntervalSeconds": 1,
                "MaxAttempts": 0
            }
        ],
        "Next": "GetCrawler",
        "ResultPath": "$.response.start_crawler",
        "Catch": [
            {
                "ErrorEquals": [
                    "Glue.CrawlerRunningException"
                ],
                "Next": "GetCrawler",
                "Comment": "Crawler Already Running, just continue to monitor",
                "ResultPath": "$.response.start_crawler"
            }
        ]
      },
      "GetCrawler": {
          "Type": "Task",
          "Parameters": {
              "Name": "${crawler_name}"
          },
          "Resource": "arn:aws:states:::aws-sdk:glue:getCrawler",
          "ResultPath": "$.response.get_crawler",
          "Retry": [
              {
                  "ErrorEquals": [
                      "States.ALL"
                  ],
                  "BackoffRate": 2,
                  "IntervalSeconds": 1,
                  "MaxAttempts": 8
              }
          ],
          "Next": "Is Running?"
      },
      "Is Running?": {
          "Type": "Choice",
          "Choices": [
              {
                  "Or": [
                      {
                          "Variable": "$.response.get_crawler.Crawler.State",
                          "StringEquals": "RUNNING"
                      },
                      {
                          "Variable": "$.response.get_crawler.Crawler.State",
                          "StringEquals": "STOPPING"
                      }
                  ],
                  "Next": "Wait for Crawler To Complete"
              }
          ],
          "Default": "CheckCrawlerStatus"
      },
      "Wait for Crawler To Complete": {
          "Type": "Wait",
          "Seconds": 5,
          "Next": "GetCrawler"
      },
      "CheckCrawlerStatus": {
        "Type": "Choice",
        "Choices": [
            {
                "Variable": "$.response.get_crawler.Crawler.LastCrawl.Status",
                "StringEquals": "FAILED",
                "Next": "CrawlerFailed"
            }
        ],
        "Default": "CrawlerSucceeded"
      },
      "CrawlerSucceeded": {
        "Type": "Pass",
        "End": true
      },
      "CrawlerFailed": {
        "Type": "Fail",
        "Error": "CrawlerFailedError",
        "Cause": "The crawler failed."
      }
    }
  }