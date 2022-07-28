from excel_read.abstracts import AbstractValidate

from excel_read.helper import phone


class Validate(AbstractValidate):

    def validate_number(self, phone_num: phone) -> phone:
        if "|" in str(phone_num):
            return "".join(phone_num.split("|")[0])
        return phone_num
