from django.db import models
from datetime import datetime,timedelta
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.



class Books(models.Model):

    category= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biography'),
        ('fiction', 'Fiction'),
        ('fantasy', 'Fantasy'),
        ('science', 'Science'),
        ('novel', 'Novel')
    ]

    booktitle = models.CharField(max_length=50, null=True,blank=False)
    isbn = models.CharField(max_length=10, null=True,blank=False,unique=True)
    author = models.CharField(max_length=30)
    bookcategory = models.CharField(choices=category, max_length=30, default= 'Education')

    def __str__(self):
        return self.booktitle

def get_expiry():
    return datetime.today() + timedelta(days=30)


class Issuebook(models.Model):
    book_title = models.ForeignKey(Books,max_length=50,on_delete=models.CASCADE)
    borrowed_by = models.ForeignKey(User, max_length=30, on_delete=models.CASCADE)
    date_borrowed = models.DateField(auto_now = True)
    return_date = models.DateField(default = get_expiry)
    
    # def __str__(self):
    #     return self.date_borrowed
    
