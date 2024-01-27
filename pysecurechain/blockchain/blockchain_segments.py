from abc import ABC, abstractmethod
from typing import Any, Union, Mapping, Iterable

from pysecurechain.exceptions import (
    BlockchainAttributeTypeError,
    BlockchainAttributeKeyError,
)


class BlockchainSegmentInterface(ABC):
    @abstractmethod
    def _BlockchainSegment__create_genesis_block(self):
        pass

    @abstractmethod
    def add_transactions(self, transactions: Union[Mapping, Iterable[Mapping]]):
        pass

    @abstractmethod
    def register_transactions(self):
        pass


class BlockchainSegment(BlockchainSegmentInterface):
    __slots__ = ["segment_id", "unconfirmed_transactions"]

    __attrs = {
        "segment_id": str,
        "unconfirmed_transactions": list,
    }

    @classmethod
    def __validate_attrs(cls, key: str, value: Any) -> None:
        """Checking the data types of class attributes."""
        if not isinstance(value, cls.__attrs[key]):
            raise TypeError

    def __setattr__(self, key, value):
        if key in self.__attrs:
            try:
                self.__validate_attrs(key, value)
            except TypeError:
                raise BlockchainAttributeTypeError
            else:
                return object.__setattr__(self, key, value)
        raise BlockchainAttributeKeyError

    def __init__(self, segment_id: str, transactions: list = None):
        self.segment_id = segment_id
        self.unconfirmed_transactions = [] if transactions is None else transactions
