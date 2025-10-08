"""
FastPusher - A fast and efficient push notification library
"""

__version__ = "0.0.1"
__author__ = "FastPusherUZ"
__email__ = "fastpusheruz@gmail.com"
__description__ = "A fast and efficient push notification library"

from .exceptions import (
    AuthenticationError,
    ChannelNotFoundError,
    ConnectionError,
    FastPusherError,
    RateLimitError,
    ValidationError,
)
from .pusher import FastPusher

__all__ = [
    "FastPusher",
    "FastPusherError",
    "ConnectionError",
    "AuthenticationError",
    "ValidationError",
    "RateLimitError",
    "ChannelNotFoundError",
]
