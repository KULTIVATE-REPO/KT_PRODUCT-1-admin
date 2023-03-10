# Generated by Django 3.2.12 on 2022-12-16 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0014_alter_userstory_table1_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('crud', models.CharField(blank=True, default=0, max_length=10, null=True)),
                ('Table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.table')),
                ('User_Story', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='application.user_story')),
            ],
        ),
    ]
