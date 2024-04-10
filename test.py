import unittest
from verification import json_check
from json.decoder import JSONDecodeError
from jsonschema.exceptions import ValidationError


class TestJSONValidation(unittest.TestCase):

    def test_valid_input_single_asterisk(self):
        input_path = "./test_cases/resource_false.json"
        result = json_check(input_path)
        self.assertEqual(False, result)

    def test_valid_input_no_single_asterisk(self):
        input_path = "./test_cases/resource_true.json"
        result = json_check(input_path)
        self.assertEqual(True, result)

    def test_valid_input_not_resource(self):
        input_path = "./test_cases/not_resource.json"
        result = json_check(input_path)
        self.assertEqual(True, result)

    def test_not_valid_schema(self):
        input_path = "./test_cases/not_valid_schema.json"
        with self.assertRaises(ValidationError):
            json_check(input_path)

    def test_not_valid_json(self):
        input_path = "./test_cases/not_valid.json"
        with self.assertRaises(JSONDecodeError):
            json_check(input_path)