# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.stayforge import Stayforge

class TestStayforge(unittest.TestCase):
    """Stayforge unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Stayforge:
        """Test Stayforge
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Stayforge`
        """
        model = Stayforge()
        if include_optional:
            return Stayforge(
                ver = '1.0.0'
            )
        else:
            return Stayforge(
        )
        """

    def testStayforge(self):
        """Test Stayforge"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
