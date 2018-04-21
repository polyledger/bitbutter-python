# coding: utf-8
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals


class BitbutterError(Exception):
    """Base error class for all exceptions raised in this library.

    Will never be raised naked; more specific subclasses of this exception
    will be raised when appropriate.
    """


class APIError(BitbutterError):
    """Raised for errors related to interacting with the Bitbutter API."""

    def __init__(self, response, message):
        self.status_code = response.status_code
        self.response = response
        self.message = message or ''
        self.request = getattr(response, 'request', None)

    def __str__(self):
        return self.message


class BadRequestError(APIError): pass
class UnauthorizedError(APIError): pass
class ForbiddenError(APIError): pass
class NotFoundError(APIError): pass
class InternalServerError(APIError): pass


def build_api_error(response, blob=None):
    """
    Helper method for creating errors and attaching HTTP response/request
    details to them.
    """
    blob = blob or response.json()
    error_message = blob['error']
    error_class = (_status_code_to_class.get(response.status_code, APIError))
    return error_class(response, error_message)


_status_code_to_class = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    500: InternalServerError
  }
