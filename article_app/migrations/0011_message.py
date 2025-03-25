# Generated by Django 5.1.7 on 2025-03-25 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article_app', '0010_alter_comment_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('body', models.TextField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
