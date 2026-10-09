"""Typed FotMob client for the Crawlora hosted API."""

from .platform import FotMobClient, AsyncFotMobClient
from .client import CrawloraClientError, CrawloraError, CrawloraNetworkError, CrawloraServerError
from .operations import OPERATION_COUNT, OPERATION_IDS, PLATFORM

Client = FotMobClient
AsyncClient = AsyncFotMobClient
__version__ = '0.1.6'
DISPLAY_NAME = 'FotMob'
PLATFORM = 'fotmob'
CONTRACT_REVISION = 'sha256:d40e5ee2b400b1b40b5ca6998063cde26b6bb3e7f84da679b5047d26380f3fa1'

__all__ = [
    "FotMobClient", "AsyncFotMobClient", "Client", "AsyncClient",
    "CrawloraError", "CrawloraClientError", "CrawloraServerError", "CrawloraNetworkError",
    "DISPLAY_NAME", "PLATFORM", "CONTRACT_REVISION", "OPERATION_COUNT", "OPERATION_IDS", "__version__",
]
