# Generated by Django 5.0 on 2024-02-09 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module1', '0002_alter_register_phonenumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('comment', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
    ]
