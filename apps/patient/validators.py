from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


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
