# Generated by Django 3.2.2 on 2021-05-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homework_1', '0003_university_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]