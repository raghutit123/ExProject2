# Generated by Django 3.0.3 on 2021-08-22 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(max_length=50)),
                ('second_name', models.CharField(max_length=52)),
                ('image', models.ImageField(default='', upload_to='myapp/images')),
            ],
        ),
    ]
