import re


class BrazilianPhone:
    def __init__(self, phone):
        if self.validate(phone):
            self.number = phone
        else:
            raise ValueError("Número incorreto")

    @staticmethod
    def validate(phone):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        # pattern = "[0-9]{2,3}[0-9]{2}[0-9]{4,5}[0-9]{4}"
        answer = re.findall(pattern, phone)
        return True if answer else False

    def fortmat_number(self):
        pattern = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        result = re.search(pattern, self.number)
        return f"+{result.group(1)}({result.group(2)})({result.group(3)})({result.group(4)})"
