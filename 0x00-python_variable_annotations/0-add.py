#!/usr/bin/env python3

"""
This module defines the Student class.
"""


class Student:
    """
    This class represents a student.
    """

    def __init__(self, first_name: str, last_name: str, age: int, location: str):
        """
        Initialize a new Student object.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
            location (str): The location of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
