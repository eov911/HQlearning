from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator
from django.db.models import UniqueConstraint

User = get_user_model()


class Lesson(models.Model):
    name = models.TextField()
    link = models.TextField()
    duration = models.PositiveIntegerField(
        'Длительность урока',
        validators=(MinValueValidator(1, message='Минимальное значение 1!'),)
    )

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.TextField()
    owner = models.ForeignKey(User,
                              on_delete=models.CASCADE,
                              related_name='courses')
    lessons = models.ManyToManyField(
        Lesson,
        related_name='recipes',
        verbose_name='уроки'

    )

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'

    def __str__(self):
        return self.name

class Subscribe(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='subscribes',
        verbose_name='Ученик',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='subscribes',
        verbose_name='Курс',
    )

    class Meta:
        verbose_name = 'Курсы'
        verbose_name_plural = 'Курсы'
        constraints = [
            UniqueConstraint(fields=['user', 'course'],
                             name='unique_course')
        ]

    def __str__(self):
        return f'{self.user} подписался на курс "{self.recipe}".'
