# Generated by Django 4.2.13 on 2024-06-09 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('description', models.TextField()),
                ('photo', models.FileField(blank=True, null=True, upload_to='files')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.category')),
                ('instructor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('video', models.FileField(blank=True, null=True, upload_to='files')),
                ('description', models.TextField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
            ],
        ),
        migrations.CreateModel(
            name='MyCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.FloatField()),
                ('course', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='courses.course')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.profile')),
            ],
        ),
    ]
