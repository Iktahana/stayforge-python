# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge) ![PyPI Downloads](https://img.shields.io/pypi/dm/stayforge) ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.room import Room

class TestRoom(unittest.TestCase):
    """Room unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Room:
        """Test Room
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Room`
        """
        model = Room()
        if include_optional:
            return Room(
                id = '675012f213e02d3d0e9ca0a6',
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                key_id = '675012f213e02d3d0e9ca0a9',
                room_type_id = '675012f213e02d3d0e9ca0aa',
                number = '',
                priority = 56
            )
        else:
            return Room(
                create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                number = '',
                priority = 56,
        )
        """

    def testRoom(self):
        """Test Room"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
