#!/usr/bin/python3
"""This is the module of the User class"""

import models


class User(models.base_model.BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
