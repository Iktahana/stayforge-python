# coding: utf-8

# flake8: noqa

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


__version__ = "0.0.0-bbf4dd5"

# import apis into sdk package
from stayforge.api.branches_api import BranchesApi
from stayforge.api.key_manager_api import KeyManagerApi
from stayforge.api.models_manager_api import ModelsManagerApi
from stayforge.api.orders_api import OrdersApi
from stayforge.api.room_types_api import RoomTypesApi
from stayforge.api.rooms_api import RoomsApi
from stayforge.api.webhooks_manager_api import WebhooksManagerApi

# import ApiClient
from stayforge.api_response import ApiResponse
from stayforge.api_client import ApiClient
from stayforge.configuration import Configuration
from stayforge.exceptions import OpenApiException
from stayforge.exceptions import ApiTypeError
from stayforge.exceptions import ApiValueError
from stayforge.exceptions import ApiKeyError
from stayforge.exceptions import ApiAttributeError
from stayforge.exceptions import ApiException

# import models into sdk package
from stayforge.models.api_branch_models_key import ApiBranchModelsKey
from stayforge.models.api_branch_models_key_input import ApiBranchModelsKeyInput
from stayforge.models.api_branch_view_key_responses import ApiBranchViewKeyResponses
from stayforge.models.api_key_manager_models_key import ApiKeyManagerModelsKey
from stayforge.models.api_key_manager_models_key_input import ApiKeyManagerModelsKeyInput
from stayforge.models.api_key_manager_view_key_responses import ApiKeyManagerViewKeyResponses
from stayforge.models.guest import Guest
from stayforge.models.http_validation_error import HTTPValidationError
from stayforge.models.id_document import IDDocument
from stayforge.models.models_manager import ModelsManager
from stayforge.models.models_manager_input import ModelsManagerInput
from stayforge.models.models_manager_responses import ModelsManagerResponses
from stayforge.models.order import Order
from stayforge.models.order_input import OrderInput
from stayforge.models.order_responses import OrderResponses
from stayforge.models.photocopy import Photocopy
from stayforge.models.price import Price
from stayforge.models.price_max import PriceMax
from stayforge.models.price_min import PriceMin
from stayforge.models.room import Room
from stayforge.models.room_input import RoomInput
from stayforge.models.room_responses import RoomResponses
from stayforge.models.room_type import RoomType
from stayforge.models.room_type_input import RoomTypeInput
from stayforge.models.room_type_responses import RoomTypeResponses
from stayforge.models.stayforge import Stayforge
from stayforge.models.validation_error import ValidationError
from stayforge.models.validation_error_loc_inner import ValidationErrorLocInner
from stayforge.models.webhooks_manager import WebhooksManager
from stayforge.models.webhooks_manager_input import WebhooksManagerInput
from stayforge.models.webhooks_manager_responses import WebhooksManagerResponses
