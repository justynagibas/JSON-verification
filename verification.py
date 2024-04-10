import json
import sys
from AWS_IAM_RolePolicy import AWSIAMRolePolicy


def json_check(json_path: str) -> bool:
    with open(json_path) as json_file:
        json_data = json.load(json_file)
    aws_role_policy = AWSIAMRolePolicy(json_data)
    return aws_role_policy.verify_resource_field()


if __name__ == "__main__":
    print(json_check(sys.argv[1]))
