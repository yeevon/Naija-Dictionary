# Generated by Django 4.2.3 on 2023-07-19 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_dictionaryentry_table_alter_usercomments_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictionaryentry',
            name='origin_language',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='dictionaryentry',
            name='word',
            field=models.CharField(max_length=255),
        ),
    ]
