# Generated by Django 3.2.12 on 2022-11-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_rename_projects_project_projects_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='name',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
