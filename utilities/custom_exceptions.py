"""Custom exceptions"""


class RequestError(Exception):
    """Custom exception for the API requests error"""
    def __init__(self, request):
        message = f"status: {request.status_code}. URL: {request.url}\n{request.text}"
        super().__init__(message)
