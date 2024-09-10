# your_app/middleware.py

class DebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"User: {request.user}, Authenticated: {request.user.is_authenticated}")
        response = self.get_response(request)
        return response
