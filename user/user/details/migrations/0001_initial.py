# Generated by Django 4.2.3 on 2023-08-01 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=200, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_of_birth', models.DateField()),
                ('status', models.BooleanField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='details.user')),
            ],
        ),
    ]
