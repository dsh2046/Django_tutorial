1. 自定义user profile
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)
    gender = models.CharField(choices=(('male', 'male'), ('female', 'female')), default='male', max_length=6)
    address = models.CharField(default='', max_length=100)
    mobile = models.CharField(null=True, blank=True, max_length=10)

    class Meta:
        verbose_name = 'UserInfo'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username
        
注意：需要在settings.py中添加：

AUTH_USER_MODEL = 'users.UserProfile'
