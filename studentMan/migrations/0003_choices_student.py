# Generated by Django 4.0.3 on 2022-06-02 07:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('studentMan', '0002_choices_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='choices',
            name='student',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='studentMan.student'),
        ),
    ]
