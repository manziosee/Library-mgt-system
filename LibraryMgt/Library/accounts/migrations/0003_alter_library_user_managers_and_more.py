# Generated by Django 4.0.5 on 2022-08-02 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_library_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='library_user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='library_user',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='library_user',
            name='is_staff',
        ),
    ]