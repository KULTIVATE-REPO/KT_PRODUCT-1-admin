# Generated by Django 3.2.12 on 2022-12-09 10:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20221125_0704'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_Name', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Role_Name', models.CharField(max_length=150)),
                ('Project_P', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.project')),
            ],
        ),
        migrations.CreateModel(
            name='User_story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.TextField()),
                ('why', models.TextField()),
                ('Project_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.project')),
                ('Role_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.roles')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Table_Name', models.CharField(max_length=250)),
                ('Purpose', models.TextField()),
                ('Project_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.project')),
            ],
        ),
        migrations.CreateModel(
            name='Epic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Epic', models.CharField(max_length=150)),
                ('Role_R', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.project')),
            ],
        ),
        migrations.CreateModel(
            name='CRUD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CRUD_NAME', models.CharField(max_length=150)),
                ('Table_T', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.table')),
            ],
        ),
    ]
