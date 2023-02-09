from datetime import datetime

class Cell:
    __color_map = {
        0: "white",
        1: "black",
        2: "red",
        3: "green",
        4: "blue",
        5: "yellow",
        6: "purple"
    }
    def __init__(self, value=None, color=0):
        self._value = value
        self._color = color

    def __repr__(self):
        return str(self._value)

    def set_value(self, value):
        self._value = str(value)

    def set_color(self, color):
        if self.__color_map.get(color) is not None:
            self._color = str(color)
        else:
            return "Enter valid color"

    def get_value(self):
        return self._value

    def get_color(self):
        return self._color

    def to_int(self):
        try:
            return int(self._value)
        except (ValueError, TypeError):
            return 'Can not convert to int'

    def to_double(self):
        try:
            return float(self._value)
        except (ValueError, TypeError):
            return 'Can not convert to double'

    def to_date(self):
        try:
            return datetime.strptime(self._value, '%d/%m/%y')
        except (ValueError, TypeError):
            return 'Can not convert to Date'

    def reset(self):
        self._value = None
        self._color = 0



