# Generated by Django 3.2 on 2023-06-14 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Movies', '0002_alter_reviewmodel_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentmodel',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]