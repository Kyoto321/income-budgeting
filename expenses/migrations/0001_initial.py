# Generated by Django 5.0.2 on 2024-03-05 10:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('ONLINE_SERVICES', 'ONLINE_SERVICES'), ('VACATION', 'VACATION'), ('GROCERIES', 'GROCERIES'), ('RENT', 'RENT'), ('CAR MORGAGE', 'CAR MORGAGE'), ('NETFLIX', 'NETFLIX'), ('OTHER', 'OTHER')], max_length=255)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10, max_length=255)),
                ('description', models.TextField(max_length=555)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]