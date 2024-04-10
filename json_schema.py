# json schema of AWS:IAM:Role Policy
aws_iam_role_policy_schema = {
    "type": "object",
    "properties": {
        "PolicyName": {"type": "string",
                       "minLength": 1,
                       "maxLength": 128
                       },
        "PolicyDocument": {
            "type": "object",
            "properties": {
                "Version": {"type": "string"},
                "Id": {"type": "string"},
                "Statement": {
                    "type": "array",
                    "items": {"type": "object",
                              "properties": {
                                  "Sid": {"type": "string"},
                                  "Effect": {"type": "string"},
                                  "Principal": {"oneOf": [
                                      {"type": "string"},
                                      {"type": "object"}
                                  ], },
                                  "NotPrincipal": {"oneOf": [
                                      {"type": "string"},
                                      {"type": "object"}
                                  ], },
                                  "Action": {"oneOf": [
                                      {"type": "string"},
                                      {
                                          "type": "array",
                                          "items": {
                                              "type": "string"
                                          }
                                      }
                                  ]},
                                  "NotAction": {"oneOf": [
                                      {"type": "string"},
                                      {
                                          "type": "array",
                                          "items": {
                                              "type": "string"
                                          }
                                      }
                                  ]},
                                  "Resource": {"oneOf": [
                                      {"type": "string"},
                                      {
                                          "type": "array",
                                          "items": {
                                              "type": "string"
                                          }
                                      }
                                  ]},
                                  "NotResource": {"oneOf": [
                                      {"type": "string"},
                                      {
                                          "type": "array",
                                          "items": {
                                              "type": "string"
                                          }
                                      }
                                  ]},
                                  "Condition": {"type": "object"}
                              },
                              "required": ["Effect"],

                              "allOf": [
                                  {
                                      "oneOf": [
                                          {"required": ["Action"]},
                                          {"required": ["NotAction"]}
                                      ]

                                  },
                                  {
                                      "oneOf": [
                                          {"required": ["Resource"]},
                                          {"required": ["NotResource"]}
                                      ]

                                  }
                              ]

                              }
                }
            },
            "required": ["Version", "Statement"]
        }
    },
    "required": ["PolicyName", "PolicyDocument"]
}
