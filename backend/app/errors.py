"""
This module contains error handlers for the app.
"""
from fastapi import HTTPException, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse

from app.app import app
from app.utils.exceptions import (InvalidCredentialsException, NotFoundException, UserCannotBeLoggedInException,
                                  ValidationException)


@app.exception_handler(exc_class_or_status_code=UserCannotBeLoggedInException)
async def handle_user_cannot_be_logged_in_exception(request: Request,
                                                    exception: UserCannotBeLoggedInException) -> JSONResponse:
    """
    Handle UserCannotBeLoggedInException.

    Args:
        request (Request): Request object.
        exception (UserCannotBeLoggedInException): UserCannotBeLoggedInException object.

    Returns:
        JSONResponse: JSONResponse object.
    """
    return JSONResponse(status_code=status.HTTP_400_BAD_REQUEST,
                        content={
                            'message': exception.message,
                            'error': 'Bad Request'
                        })


@app.exception_handler(exc_class_or_status_code=InvalidCredentialsException)
@app.exception_handler(exc_class_or_status_code=status.HTTP_401_UNAUTHORIZED)
async def handle_invalid_credentials_exception(request: Request,
                                               exception: InvalidCredentialsException | HTTPException) -> JSONResponse:
    """
    Handle InvalidCredentialsException and 401 error.

    Args:
        request (Request): Request object.
        exception (InvalidCredentialsException | HTTPException): InvalidCredentialsException or HTTPException object.

    Returns:
        JSONResponse: JSONResponse object.
    """
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED,
                        content={
                            'message': 'Invalid credentials. Please try again.',
                            'error': 'Unauthorized'
                        })


@app.exception_handler(exc_class_or_status_code=NotFoundException)
async def handle_not_found_exception(request: Request, exception: NotFoundException) -> JSONResponse:
    """
    Handle resource NotFoundException.

    Args:
        request (Request): Request object.
        exception (NotFoundException): NotFoundException object.

    Returns:
        JSONResponse: JSONResponse object.
    """
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={
                            'message': exception.message,
                            'error': 'Not Found'
                        })


@app.exception_handler(exc_class_or_status_code=status.HTTP_404_NOT_FOUND)
async def handle_404_error(request: Request, exception: HTTPException) -> JSONResponse:
    """
    Handle 404 error.

    Args:
        request (Request): Request object.
        exception (HTTPException): HTTPException object.

    Returns:
        JSONResponse: JSONResponse object.
    """
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND,
                        content={
                            'message': f'Cannot {request.method} {request.url.path}',
                            'error': 'Not Found'
                        })


@app.exception_handler(exc_class_or_status_code=status.HTTP_405_METHOD_NOT_ALLOWED)
async def handle_method_not_allowed_exception(request: Request, exception: HTTPException) -> JSONResponse:
    """
    Handle 405 error.

    Args:
        request (Request): Request object.
        exception (HTTPException): HTTPException object.

    Returns:
        JSONResponse: JSONResponse object.
    """
    return JSONResponse(status_code=status.HTTP_405_METHOD_NOT_ALLOWED,
                        content={
                            'message': f'Cannot {request.method} {request.url.path}',
                            'error': 'Method Not Allowed'
                        })


@app.exception_handler(exc_class_or_status_code=ValidationException)
@app.exception_handler(exc_class_or_status_code=RequestValidationError)
async def handle_validation_exception(request: Request,
                                      exception: ValidationException | RequestValidationError) -> JSONResponse:
    """
    Handle ValidationException and Pydantic ValidationError.

    Args:
        request (Request): Request object.
        exception (ValidationException

    Returns:
        JSONResponse: JSONResponse object.
    """
    if isinstance(exception, ValidationException):
        message = exception.message

    elif isinstance(exception, RequestValidationError):
        message = exception.errors()[0]

    return JSONResponse(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                        content={
                            'message': message,
                            'error': 'Validation Error'
                        })
