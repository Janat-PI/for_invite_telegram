from typing import TypeAlias, NamedTuple, Any
from dataclasses import dataclass


file_path: TypeAlias = str
phone: TypeAlias = str


class ReadKeys(NamedTuple):
    index: Any
    columns: Any
    data: Any


# @dataclass(slots=True, frozen=True)
# class User:
#     name: str
#     phone: str







