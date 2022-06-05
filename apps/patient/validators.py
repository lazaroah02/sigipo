from typing import Any

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator
from django.utils.translation import gettext_lazy as _


class IdentityCardValidator(BaseValidator):
    message = _(
        "Asegúrese que el valor tiene %(limit_value_1)s o %(limit_value_2)s caracteres (tiene %(show_value)s)."
    )
    code = "two_values_min_length"

    def __init__(self, limit_value_1: Any, limit_value_2: Any) -> None:
        self.limit_value_1 = limit_value_1
        self.limit_value_2 = limit_value_2

    def __call__(self, value):
        cleaned = self.clean(value)
        limit_value_1 = (
            self.limit_value_1() if callable(self.limit_value_1) else self.limit_value_1
        )
        limit_value_2 = (
            self.limit_value_2() if callable(self.limit_value_2) else self.limit_value_2
        )
        params = {
            "limit_value_1": limit_value_1,
            "limit_value_2": limit_value_2,
            "show_value": cleaned,
            "value": value,
        }
        if not (
            self.compare(cleaned, limit_value_1) or self.compare(cleaned, limit_value_2)
        ):
            raise ValidationError(self.message, code=self.code, params=params)

    def compare(self, a, b):
        return a == b

    def clean(self, x):
        return len(x)


def only_numbers_validator(value: str) -> bool:
    """Validate if value is a number."""
    try:
        int(value)
        return True
    except ValueError:
        raise ValidationError(
            _("%(value)s no es un número"),
            params={"value": value},
        )
