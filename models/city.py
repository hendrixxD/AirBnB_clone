#!/usr/bin/python3
"""City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """public class attribute

    state_id = "" -> str [it will be State.id]
    name = "" -> str
    """

    state_id = ""
    name = ""
