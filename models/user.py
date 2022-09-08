#!/usr/bin/python3
"""class user that inherits from BaseModel"""

from models.base_model import BaseModel


class User(BaseModel):
    """ User Data File """
    email = "" -> str
    password = "" -> str
    first_name = "" -> str
    last_name = "" -> str
