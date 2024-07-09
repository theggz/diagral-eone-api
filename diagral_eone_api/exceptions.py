"""Diagral e-one Cloud API exceptions."""

class DiagralCloudError(Exception):
    """Base class for Diagral Cloud errors."""


class CloudConnectionError(DiagralCloudError):
    """Exception raised when an error happend when connecting to the API."""


class BadRequestError(DiagralCloudError):
    """Exception raised when the request is invalid."""


class AuthorizationError(DiagralCloudError):
    """Exception raised when authorization is not provided or has expired."""


class TooManyRequestsError(DiagralCloudError):
    """Exception raised when too many requests have been made."""


class MissingFieldResponseError(DiagralCloudError):
    """Exception raised when a field is missing in the response."""
    