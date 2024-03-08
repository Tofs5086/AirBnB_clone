#!/usr/bin/python3
"""the module for Review class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """the class representing a Review."""
    place_id = ""
    user_id = ""
    text = ""
