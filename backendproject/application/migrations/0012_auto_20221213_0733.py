# Generated by Django 3.2.12 on 2022-12-13 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_crud_epic_project_roles_table_user_story'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserStory_Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
        migrations.RenameField(
            model_name='epic',
            old_name='Role_R',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='role',
            old_name='Project_P',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='user_story',
            old_name='Project_ID',
            new_name='Project',
        ),
        migrations.RenameField(
            model_name='user_story',
            old_name='Role_ID',
            new_name='Role',
        ),
        migrations.RemoveField(
            model_name='table',
            name='Project_ID',
        ),
        migrations.AddField(
            model_name='user_story',
            name='Epic',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='application.epic'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='CRUD',
        ),
        migrations.AddField(
            model_name='userstory_table',
            name='Table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.table'),
        ),
        migrations.AddField(
            model_name='userstory_table',
            name='User_Story',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.user_story'),
        ),
    ]
