from django.db import models
from django.contrib.auth.models import User

class BMIRecord(models.Model):
    height = models.FloatField(help_text="身高 (公分)")
    weight = models.FloatField(help_text="體重 (公斤)")
    age = models.IntegerField(help_text="年齡", null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[("male", "Male"), ("female", "Female")],
        null=True,
        blank=True
    )
    bmi = models.FloatField(null=True, blank=True)   # 前端計算後傳入
    bmr = models.FloatField(null=True, blank=True)   # 前端計算後傳入
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - BMI: {self.bmi if self.bmi else 'N/A'}, BMR: {self.bmr if self.bmr else 'N/A'}"
