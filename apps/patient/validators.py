def only_numbers_validator(value: str) -> bool:
    """Validate if value is a number."""
    try:
        int(value)
        return True
    except ValueError:
        return False
