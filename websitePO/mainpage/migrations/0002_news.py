# Generated by Django 4.1.1 on 2022-09-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50, verbose_name='Зголовок')),
                ('news', models.TextField(verbose_name='Новость')),
            ],
        ),
    ]
