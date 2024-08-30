from django.db import models
from django.contrib.auth.models import User

class BotGroup(models.Model):
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=50, choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram')], default='Facebook')
    url = models.URLField()
    added_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Bot(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    images = models.ImageField(upload_to='bot_images/', null=True, blank=True)
    groups = models.ManyToManyField('BotGroup')
    bot_platform = models.CharField(
        max_length=50,
        choices=[('Facebook', 'Facebook'), ('Instagram', 'Instagram')],
        default='Facebook'
    )
    send_opt = models.CharField(
        max_length=50,
        choices=[('all_days', 'All Days'), ('selected_days', 'Selected Days'), ('day', 'One Day per Week')],
        default='all_days'
    )
    send_time = models.TimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
