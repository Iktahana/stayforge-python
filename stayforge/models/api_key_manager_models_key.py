# coding: utf-8

"""
    Stayforge API

    ![Commit Activity](https://img.shields.io/github/commit-activity/m/tokujun-t/stayforge) ![Codecov](https://codecov.io/gh/tokujun-t/stayforge/branch/main/graph/badge.svg) ![PyPI Version](https://img.shields.io/pypi/v/stayforge)  ### SDK  - [Python SDK](https://github.com/tokujun-t/stayforge-python)  We provided SDKs (currently only the Python version is provided). Before deciding to call the API directly, you may wish to try the SDK to speed up your development.  ![GitHub Workflow Status](https://github.com/tokujun-t/Stayforge/actions/workflows/python-sdk.yml/badge.svg)   ### About Healthcheck  Healthcheck at `/api/healthcheck`. curl to check if the service is working.  ```shell curl -I http://<your service>/api/healthcheck ``` ### Some Links  GitHub Repo [https://github.com/tokujun-t/Stayforge](https://github.com/tokujun-t/Stayforge)  Wiki [https://github.com/tokujun-t/Stayforge/wiki](https://github.com/tokujun-t/Stayforge/wiki) 

    The version of the OpenAPI document: 1.0.0
    Contact: support@stayforge.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class ApiKeyManagerModelsKey(BaseModel):
    """
    ApiKeyManagerModelsKey
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default='676428619a4b5a54291891d9', description="Reference ID of the key.")
    create_at: Optional[datetime]
    update_at: Optional[datetime] = None
    url: StrictStr = Field(description="The name of the hotel key. By default, it combines a base name with a random town.")
    num: Optional[StrictStr] = Field(default='', description="Order number")
    effective_at: Optional[StrictStr] = Field(default='2024-12-19T14:06:25.805915Z', description="Effective at")
    ineffective_at: Optional[StrictStr] = Field(default='2024-12-20T14:06:25.805942Z', description="Ineffective at")
    __properties: ClassVar[List[str]] = ["id", "create_at", "update_at", "url", "num", "effective_at", "ineffective_at"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ApiKeyManagerModelsKey from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if create_at (nullable) is None
        # and model_fields_set contains the field
        if self.create_at is None and "create_at" in self.model_fields_set:
            _dict['create_at'] = None

        # set to None if update_at (nullable) is None
        # and model_fields_set contains the field
        if self.update_at is None and "update_at" in self.model_fields_set:
            _dict['update_at'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ApiKeyManagerModelsKey from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id") if obj.get("id") is not None else '676428619a4b5a54291891d9',
            "create_at": obj.get("create_at"),
            "update_at": obj.get("update_at"),
            "url": obj.get("url"),
            "num": obj.get("num") if obj.get("num") is not None else '',
            "effective_at": obj.get("effective_at") if obj.get("effective_at") is not None else '2024-12-19T14:06:25.805915Z',
            "ineffective_at": obj.get("ineffective_at") if obj.get("ineffective_at") is not None else '2024-12-20T14:06:25.805942Z'
        })
        return _obj


