from djongo import models
from api.models.user import User

class Audit(models.Model):
    _id = models.ObjectIdField()
    user = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"I'm an audit log of {self.user}"