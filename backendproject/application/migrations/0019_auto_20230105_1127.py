# Generated by Django 3.2.12 on 2023-01-05 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_table_project'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_story',
            name='Epic',
        ),
        migrations.RemoveField(
            model_name='user_story',
            name='Role',
        ),
        migrations.RemoveField(
            model_name='user_story',
            name='what',
        ),
        migrations.RemoveField(
            model_name='user_story',
            name='why',
        ),
        migrations.AddField(
            model_name='user_story',
            name='User_story',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]