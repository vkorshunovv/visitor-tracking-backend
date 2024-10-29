from .models import Visitor

class VisitorTrackingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        ip = request.META.get('REMOTE_ADDR')    
        user_agent = request.META.get('HTTP_USER_AGENT', '')
        
        #Save visitor data
        if ip:
            Visitor.objects.create(ip=ip, user_agent=user_agent)
            
        response= self.get_response(request)
        return response    