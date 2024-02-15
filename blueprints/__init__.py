from .browsing import api as browsing
from .oauth import api as oauthflow
from .search import api as search
from .lyrics import api as lyrics
from .dlp import api as dlp

blueprints = [
    oauthflow,
    search,
    browsing,
    dlp,
    lyrics
]