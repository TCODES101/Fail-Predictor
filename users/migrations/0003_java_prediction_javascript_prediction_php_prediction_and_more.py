# Generated by Django 4.2.5 on 2023-10-03 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_students_clubs_alter_students_units'),
    ]

    operations = [
        migrations.AddField(
            model_name='java',
            name='prediction',
            field=models.CharField(default='NULL', max_length=4),
        ),
        migrations.AddField(
            model_name='javascript',
            name='prediction',
            field=models.CharField(default='NULL', max_length=4),
        ),
        migrations.AddField(
            model_name='php',
            name='prediction',
            field=models.CharField(default='NULL', max_length=4),
        ),
        migrations.AddField(
            model_name='python',
            name='prediction',
            field=models.CharField(default='NULL', max_length=4),
        ),
        migrations.AddField(
            model_name='sql',
            name='prediction',
            field=models.CharField(default='NULL', max_length=4),
        ),
    ]
