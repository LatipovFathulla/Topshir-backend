# Generated by Django 3.2.19 on 2023-05-30 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0015_contactmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactmodel',
            name='start_studying',
            field=models.CharField(choices=[('', 'When would you like to start studying?'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027')], max_length=10),
        ),
    ]
