# Generated by Django 3.1.4 on 2021-01-22 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20210122_1900'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post_model',
            name='id',
        ),
        migrations.AddField(
            model_name='post_model',
            name='post_id',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
    ]
