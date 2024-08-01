#!/usr/bin/python3
"""
views
"""

from flask import Blueprint

app_views = Blueprint('/api/v1', __name__, url_prefix="/api/v1")

# Import other view modules here
from api.v1.views.index import *

