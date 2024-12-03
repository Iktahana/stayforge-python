# coding: utf-8

"""
    Stayforge API

    This is a basic API description.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from apis.orders_api import OrdersApi


class TestOrdersApi(unittest.TestCase):
    """OrdersApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrdersApi()

    def tearDown(self) -> None:
        pass

    def test_create_order_api_order_post(self) -> None:
        """Test case for create_order_api_order_post

        Create Order
        """
        pass

    def test_delete_order_api_order_delete_id_delete(self) -> None:
        """Test case for delete_order_api_order_delete_id_delete

        Delete Order
        """
        pass

    def test_get_order_by_id_api_order_id_get(self) -> None:
        """Test case for get_order_by_id_api_order_id_get

        Get Order By Id
        """
        pass

    def test_get_order_by_num_api_order_num_num_get(self) -> None:
        """Test case for get_order_by_num_api_order_num_num_get

        Get Order By Num
        """
        pass

    def test_get_order_types_api_order_order_types_get(self) -> None:
        """Test case for get_order_types_api_order_order_types_get

        Get Order Types
        """
        pass


if __name__ == '__main__':
    unittest.main()
