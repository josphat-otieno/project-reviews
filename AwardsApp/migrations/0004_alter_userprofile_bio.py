# Generated by Django 3.2.5 on 2021-07-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AwardsApp', '0003_auto_20210719_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=255),
        ),
    ]
