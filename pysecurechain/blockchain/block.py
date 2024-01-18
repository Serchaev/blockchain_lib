import hashlib
import time
from typing import Optional, Any

from pysecurechain.exceptions import BlockAttributeTypeError, BlockAttributeKeyError


class Block:
    """Block, a single component unit of the blockchain."""

    __attrs = {
        "index": int,
        "segment_id": str,
        "timestamp": float,
        "data": list,
        "previous_hash": str,
        "actual_hash": str,
    }

    @classmethod
    def __validate_attrs(cls, key: str, value: Any) -> None:
        """Checking the data types of class attributes."""
        if not isinstance(value, cls.__attrs[key]):
            raise TypeError

    def __calculate_hash(self) -> str:
        """Calculating the hash function for self block of the blockchain."""

        sha = hashlib.sha256()
        sha.update(
            "".join([str(value) for value in self.__dict__.values()]).encode("utf-8")
        )
        return sha.hexdigest()

    def __setattr__(self, key, value):
        if key in self.__attrs:
            try:
                self.__validate_attrs(key, value)
            except TypeError:
                raise BlockAttributeTypeError
            else:
                return object.__setattr__(self, key, value)
        raise BlockAttributeKeyError

    def __init__(
        self,
        index: int,
        segment_id: str,
        previous_hash: str,
        data: Optional[list] = None,
        timestamp: Optional[float] = None,
    ):
        self.index = index
        self.segment_id = segment_id
        self.previous_hash = previous_hash
        self.data = [] if data is None else data
        self.timestamp = time.time() if timestamp is None else timestamp
        self.actual_hash = self.__calculate_hash()

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        attrs = ", ".join([f"{key}={value}" for key, value in self.__dict__.items()])
        return f"{self.__class__.__name__}({attrs})"
