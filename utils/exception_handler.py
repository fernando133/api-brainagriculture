# utils/exception_handler.py
from rest_framework.views import exception_handler
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response:
        logger.error(f"Exceção: {exc} | Contexto: {context}")
    return response
