from django.db import models

# Create your models here.

# Create your models here.
class Books(models.Model):
    Book = models.TextField(default="Django-tutorial")
    Book_id = models.TextField(default="100")
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "book"


