#!/usr/bin/python3
"""This is the Module of the Review class"""

import models

class Review(models.base_model.BaseModel):
    place_id = ""
    user_id = ""
    text = ""
