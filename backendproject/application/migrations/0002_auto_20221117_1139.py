# Generated by Django 3.2.12 on 2022-11-17 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='officeuse',
            old_name='Table_CRUD',
            new_name='CRUD_NAME',
        ),
        migrations.RenameField(
            model_name='officeuse',
            old_name='Project_name',
            new_name='Projects',
        ),
        migrations.RenameField(
            model_name='officeuse',
            old_name='Table_Purpose',
            new_name='Purpose',
        ),
        migrations.RenameField(
            model_name='officeuse',
            old_name='Table_name',
            new_name='Table_Name',
        ),
    ]
