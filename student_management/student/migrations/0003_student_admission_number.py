# Generated by Django 5.1.3 on 2024-11-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_student_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]