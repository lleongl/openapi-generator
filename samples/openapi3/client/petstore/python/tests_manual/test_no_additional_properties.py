# coding: utf-8

"""
    OpenAPI Petstore

    This spec is mainly for testing Petstore server and contains fake endpoints, models. Please do not use this for any other purpose. Special characters: \" \\  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""

import decimal
import unittest

from petstore_api.model.no_additional_properties import NoAdditionalProperties
from petstore_api import schemas

class TestNoAdditionalProperties(unittest.TestCase):
    """NoAdditionalProperties unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testNoAdditionalProperties(self):
        """Test NoAdditionalProperties"""

        # works with only required
        inst = NoAdditionalProperties(id=1)
        id_by_items = inst["id"]
        assert id_by_items == 1
        assert isinstance(id_by_items, (schemas.Int64Schema, decimal.Decimal))
        id_by_property = inst.id
        assert id_by_property == 1
        assert isinstance(id_by_property, (schemas.Int64Schema, decimal.Decimal))
        with self.assertRaises(AttributeError):
            inst.petId
        with self.assertRaises(KeyError):
            inst["petId"]
        assert inst.get_item_oapg("petId") is schemas.unset

        # works with required + optional
        inst = NoAdditionalProperties(id=1, petId=2)

        # needs required
        # TODO cast this to ApiTypeError?
        with self.assertRaisesRegex(
            TypeError,
            r"missing 1 required keyword-only argument: 'id'"
        ):
            NoAdditionalProperties(petId=2)

        # may not be passed additional properties
        # TODO cast this to ApiTypeError?
        with self.assertRaisesRegex(
            TypeError,
            r"got an unexpected keyword argument 'invalidArg'"
        ):
            NoAdditionalProperties(id=2, invalidArg=2)

        # plural example
        # TODO cast this to ApiTypeError?
        with self.assertRaisesRegex(
            TypeError,
            r"got an unexpected keyword argument 'firstInvalidArg'"
        ):
            NoAdditionalProperties(id=2, firstInvalidArg=1, secondInvalidArg=1)


if __name__ == '__main__':
    unittest.main()
