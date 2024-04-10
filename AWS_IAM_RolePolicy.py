from json_schema import aws_iam_role_policy_schema
from jsonschema import validate


class AWSIAMRolePolicy:
    def __init__(self, input_json: dict):
        # check if loaded JSON is in AWS::IAM::Role Policy format
        if self.__validate_schema__(input_json, aws_iam_role_policy_schema):
            self.json = input_json

    def __validate_schema__(self, input_json: dict, expected_schema: dict) -> bool:
        """Check if input_json schema match AWS::IAM::RolePolicy schema."""
        # raise ValidationError if input JSON is not in expected format
        validate(instance=input_json, schema=expected_schema)
        return True

    def verify_resource_field(self) -> bool:
        """Method verifying if input JSON contains single asterisk in Resource field"""
        # As there is not specified what should be returned as multiple Statements are present I assume that there is no such Policy.
        # If there will be, there is a need to iterate through all the Statement fields in the Policy and check if any or all of the Resource fields contain a single asterisk.
        if "Resource" in self.json["PolicyDocument"]["Statement"][0].keys():
            resource = self.json["PolicyDocument"]["Statement"][0]["Resource"]
            if resource == "*":
                return False
        return True
