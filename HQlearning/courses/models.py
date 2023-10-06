from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Course(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='courses')

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.TextField()
    link = models.TextField()
    duration = models.PositiveBigIntegerField()

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name
