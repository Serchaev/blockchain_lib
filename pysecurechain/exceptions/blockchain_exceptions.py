class BlockAttributeTypeError(Exception):
    """incorrect definition of block class attributes."""

    def __str__(self):
        return "invalid attribute data type is specified."


class BlockAttributeKeyError(Exception):
    """incorrect definition of block class attributes."""

    def __str__(self):
        return "invalid attribute key is specified."
