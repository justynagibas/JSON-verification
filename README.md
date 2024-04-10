# JSON-verification

This project contain verification of given input JSON in format AWS::IAM::Role Policy.
It provides complete solution from loading file from given path, through JSON parsing and schema validation, to checking the 'Resource' field of JSON file.

Project is part of Remitly evaluation process.

## Dependencies
- `jsonschema`: Used for JSON schema validation.

```bash
pip install jsonschema
```

## JSON Schema
The JSON schema used for validation can be found in 'json_schema.py'. Currently, it matches basic requirements of AWS:IAMRole Policy format and can be easily adjusted to meet more specific requirements.

## Running
You can run solution using command line or setup and configure it in your desired work environment.  
**To run function/tests from command line ensure you are in a project directory (JSON-verification).**

### Running Function
 
```bash
 python verification.py "path/to/your/json"
```

Example
```bash
 python verification.py "./test_cases/resource_false.json"
```
### Running Unittest

```bash
python -m unittest
```

## Expected Results
List of expected outputs with of json_check function form 'verification.py' and conditions:
 - logical False - JSON match AWS::IAM::Role Policy format and 'Resource' field contains a single asterisk,
 - logical True - JSON match AWS:IAM:Roel Policy format and 'Resource' field not contains a single asterisk or 'Resource' field is not in JSON (as valid policy contains either 'Resource' or 'NotResource' field),
 - FileNotFound exception - incorrect path to file,
 - JSONDecodeError exception - loaded file is not a valid JSON,
 - ValidationError exception - JSON is not in AWS:IAM:Role Policy format.



