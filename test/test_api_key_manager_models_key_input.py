# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.api_key_manager_models_key_input import ApiKeyManagerModelsKeyInput

class TestApiKeyManagerModelsKeyInput(unittest.TestCase):
    """ApiKeyManagerModelsKeyInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ApiKeyManagerModelsKeyInput:
        """Test ApiKeyManagerModelsKeyInput
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ApiKeyManagerModelsKeyInput`
        """
        model = ApiKeyManagerModelsKeyInput()
        if include_optional:
            return ApiKeyManagerModelsKeyInput(
                url = '',
                num = '',
                effective_at = '2024-12-03T22:15:22.763294Z',
                ineffective_at = '2024-12-04T22:15:22.763326Z'
            )
        else:
            return ApiKeyManagerModelsKeyInput(
                url = '',
        )
        """

    def testApiKeyManagerModelsKeyInput(self):
        """Test ApiKeyManagerModelsKeyInput"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
