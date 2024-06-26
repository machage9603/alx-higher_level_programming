#!/usr/bin/python3

"""Create class Rectangle that defines a reactangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

        @property
        def width(self):
            """Retrieve attribute"""
            return self.__width

        @width.setter
        def width(self, value):
            """To set attribute"""
            if type(value) is not int:
                raise TypeError("width must be an intereger")
            if value < 0:
                raise ValueError("width must be >= 0")

            self.__width = value

            @property
            def height(self):
                """To retrieve attribute"""
                return self.__height

            @height.setter
            def height(self, value):
                """To set the attribute"""
                if type(value) is not int:
                    raise TypeError("height must b an intereger")
                if value < 0:
                    raise ValueError("height must be >= 0")

                self.__height = value
