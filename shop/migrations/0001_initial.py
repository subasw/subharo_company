# Generated by Django 2.2.7 on 2019-11-10 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='about/')),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('hotline', models.IntegerField()),
                ('email_address', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10000)),
                ('slug', models.SlugField(unique=True)),
                ('featured', models.BooleanField(default=False)),
                ('category', models.CharField(choices=[('T', 'toys'), ('G', 'gift'), ('E', 'electric'), ('H', 'household'), ('F', 'furniture'), ('S', 'stationary')], max_length=1)),
                ('image', models.ImageField(blank=True, null=True, upload_to='items/')),
            ],
        ),
    ]