# Generated by Django 4.1.7 on 2023-03-15 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wave', '0004_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
