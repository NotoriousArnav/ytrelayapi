from .oauth import api as oauthflow
from .search import api as search

blueprints = [
    oauthflow,
    search
]