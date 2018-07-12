from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default='default.png', blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, default=None)

#python manage.py makemagrations
#python manage.py migrate
#python manage.py runserver
#python manage.py startapp appname
#python manage.py shell
#python manage.py createsuperuser

    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:20] + '...'
