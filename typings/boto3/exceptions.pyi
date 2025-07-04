"""
This type stub file was generated by pyright.
"""

import botocore.exceptions

class Boto3Error(Exception):
    """Base class for all Boto3 errors."""
    ...


class ResourceLoadException(Boto3Error):
    ...


class NoVersionFound(Boto3Error):
    ...


class UnknownAPIVersionError(Boto3Error, botocore.exceptions.DataNotFoundError):
    def __init__(self, service_name, bad_api_version, available_api_versions) -> None:
        ...
    


class ResourceNotExistsError(Boto3Error, botocore.exceptions.DataNotFoundError):
    """Raised when you attempt to create a resource that does not exist."""
    def __init__(self, service_name, available_services, has_low_level_client) -> None:
        ...
    


class RetriesExceededError(Boto3Error):
    def __init__(self, last_exception, msg=...) -> None:
        ...
    


class S3TransferFailedError(Boto3Error):
    ...


class S3UploadFailedError(Boto3Error):
    ...


class DynamoDBOperationNotSupportedError(Boto3Error):
    """Raised for operations that are not supported for an operand."""
    def __init__(self, operation, value) -> None:
        ...
    


DynanmoDBOperationNotSupportedError = DynamoDBOperationNotSupportedError
class DynamoDBNeedsConditionError(Boto3Error):
    """Raised when input is not a condition"""
    def __init__(self, value) -> None:
        ...
    


class DynamoDBNeedsKeyConditionError(Boto3Error):
    ...


class PythonDeprecationWarning(Warning):
    """
    Python version being used is scheduled to become unsupported
    in an future release. See warning for specifics.
    """
    ...


