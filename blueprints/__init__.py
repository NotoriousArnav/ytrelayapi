from .oauth import api as oauthflow
from .search import api as search
from .browsing import api as browsing

blueprints = [
    oauthflow,
    search,
    browsing
]