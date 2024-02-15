from .browsing import api as browsing
from .oauth import api as oauthflow
from .search import api as search
from .lyrics import api as lyrics
from .dlp import api as dlp

"""Blueprints for API Routes
Register your APIs here in the `blueprint` list.
"""

blueprints = [
    oauthflow,
    search,
    browsing,
    dlp,
    lyrics
]