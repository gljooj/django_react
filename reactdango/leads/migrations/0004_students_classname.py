# Generated by Django 3.1.3 on 2020-11-30 21:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0003_remove_students_classname'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='classname',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='leads.classname'),
        ),
    ]
