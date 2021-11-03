# Generated by Django 2.2.5 on 2021-10-29 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookID', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('authors', models.CharField(max_length=120)),
                ('average_rating', models.FloatField()),
                ('isbn', models.IntegerField()),
                ('language_code', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='my_images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(default='pic.jpg', upload_to='pics')),
                ('username', models.CharField(max_length=100)),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
