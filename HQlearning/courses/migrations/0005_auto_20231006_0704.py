# Generated by Django 2.2.19 on 2023-10-06 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0004_auto_20231006_0652'),
    ]

    operations = [
        migrations.CreateModel(
            name='Learning_Lessons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done', models.BooleanField()),
                ('lesson', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='courses.Lesson', verbose_name='Урок')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to=settings.AUTH_USER_MODEL, verbose_name='Ученик')),
            ],
            options={
                'verbose_name': 'Пройденный урок',
                'verbose_name_plural': 'Пройденные уроки',
            },
        ),
        migrations.AddConstraint(
            model_name='learning_lessons',
            constraint=models.UniqueConstraint(fields=('user', 'lesson'), name='unique_lesson'),
        ),
    ]
