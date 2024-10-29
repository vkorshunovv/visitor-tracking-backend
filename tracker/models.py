from django.db import models

class Visitor(models.Model):
    ip = models.GenericIPAddressField()
    user_agent = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.ip} at {self.timestamp}"
    