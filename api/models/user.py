from djongo import models

class User(models.Model):
    _id = models.ObjectIdField()
    username = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"I'm {self.username}"