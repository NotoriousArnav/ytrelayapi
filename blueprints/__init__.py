from .oauth import api as oauthflow
from .search import api as search
from .browsing import api as browsing
from .dlp import api as dlp

blueprints = [
    oauthflow,
    search,
    browsing,
    dlp
]