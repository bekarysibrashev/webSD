# Generated by Django 4.1.1 on 2022-09-18 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewText',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, verbose_name='Тема')),
                ('info', models.CharField(max_length=1000, verbose_name='Заголовок')),
            ],
        ),
    ]