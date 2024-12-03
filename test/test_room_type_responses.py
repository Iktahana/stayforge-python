# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from stayforge.models.room_type_responses import RoomTypeResponses

class TestRoomTypeResponses(unittest.TestCase):
    """RoomTypeResponses unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RoomTypeResponses:
        """Test RoomTypeResponses
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RoomTypeResponses`
        """
        model = RoomTypeResponses()
        if include_optional:
            return RoomTypeResponses(
                data = [
                    stayforge.models.room_type.RoomType(
                        id = '674f82faacd14a354445d55d', 
                        create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        description = '', 
                        price = '', 
                        price_policy = '', 
                        price_max = '', 
                        price_min = '', )
                    ],
                detail = 'Successfully.',
                status = 56,
                used_time = 1.337,
                stayforge = stayforge.models.stayforge.Stayforge(
                    ver = '1.0.0', )
            )
        else:
            return RoomTypeResponses(
                data = [
                    stayforge.models.room_type.RoomType(
                        id = '674f82faacd14a354445d55d', 
                        create_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        update_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        name = '', 
                        description = '', 
                        price = '', 
                        price_policy = '', 
                        price_max = '', 
                        price_min = '', )
                    ],
        )
        """

    def testRoomTypeResponses(self):
        """Test RoomTypeResponses"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
