from django.utils.timezone import now
import logging

logger = logging.getLogger(__name__)

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = now()
        response = self.get_response(request)
        end_time = now()

        logger.info(
            f"Request: {request.method} {request.path}, "
            f"Response: {response.status_code}, "
            f"Duration: {(end_time - start_time).total_seconds()} seconds"
        )

        return response
