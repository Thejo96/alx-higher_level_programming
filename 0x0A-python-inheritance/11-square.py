#!/usr/bin/python3
"""
Module for Square class.
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class that inherits from Rectangle.
    """

    def __init__(self, size):
        """
        Initializes a Square object with a given size.

        Args:
            size (int): The size of the square.

            Raises:
            ValueError: If size is not a positive integer.
            """
            self.integer_validator("size", size)
            super().__init__(size, size)

            def __str__(self):
                """
                Returns a string representation of the Square.

                Returns:
                str: A string in the format "[Square] <width>/<height>"
                """
                return "[Square] {}/{}".format(self.__width, self.__height)

            def area(self):
                """
                Calculates the area of the Square.

                Returns:
                int: The area of the square.
                """
                return self.__width * self.__height

            def integer_validator(self, name, value):
                """
                Validates that a given value is a positive integer.

                Args:
                    name (str): The name of the value being validated.
                    value (int): The value to be validated.

                    Raises:
                    ValueError: If value is not a positive integer.
                    """
                    if type(value) is not int:
                    raise TypeError("{} must be an integer".format(name))
                    if value <= 0:
                    raise ValueError("{} must be > 0".format(name))

                    if __name__ == "__main__":
                    s = Square(13)
                    print(s)
                    print(s.area())
