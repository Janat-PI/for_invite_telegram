from typing import Any

import pandas as pd

from excel_read.abstracts import AbstractReader
from excel_read.helper import file_path
from excel_read.validators import Validate


class User:

    validate = Validate()
    
    def __init__(self, name: str, phone) -> None:
        self.name = name
        self.phone = self.validate.validate_number(phone)

    def __repr__(self) -> str:
        return f"{self.__class__} {self.name} {self.phone}"

    def __str__(self) -> str:
        return f"{self.name} {self.phone}"


class ReaderExcel(AbstractReader):

    def __init__(self, path: file_path):
        self._path = path

    def read(self, columns: list[str] | None = None) -> pd.DataFrame:
        """
        it's methods read file and return Pandas object
        :params colums: it's list on columns
        """
        data = pd.read_excel(self._path)
        return self.read_helper(data, columns)

    def write(self):
        pass

    def custom_read(self, data: pd, columns: list[str] | None) -> dict[int, str]:
        new_data = self.read_helper(data, columns)
        return new_data.to_dict()
    
    @staticmethod
    def read_helper(data: pd, columns: list[str] | None) -> pd.DataFrame:
        if columns:
            new_data = pd.DataFrame(data, columns=columns)
        else:
            new_data = pd.DataFrame(data)
        return new_data
    
    # @classmethod
    # def check_path(cls, path):
    #     try:
    #         with open(path) as file:
    #             return path
    #     except FileNotFoundError as e:
    #         print(e)
    #         # raise FileNotFoundError("file not found!!!")


class Converter():

    def __init__(self, new_data: dict, index, columns, data):
        self._new_data = new_data
        self._index = index
        self._columns = columns
        self._data = data


    def generate_to_new_dict(self, choice: Any) -> list[User] | Any:
        """
        it is function return dict for choice data
        """
        match choice:
            case self._index:
                return self._new_data[self._index]
            case self._columns:
                return self._new_data[self._columns]
            case self._data:
                new_obj: list[User] = []
                for obj in  self._new_data[self._data]:
                    name, phone = obj
                    new_obj.append(User(name=name, phone=phone))
                return new_obj
            case _:
                return []


