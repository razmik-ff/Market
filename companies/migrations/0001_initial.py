# Generated by Django 4.2.2 on 2023-06-29 15:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(choices=[('Market', 'Market'), ('Restaurant', 'Restaurant'), ('Pharmacy', 'Pharmacy'), ('Flowers', 'Flowers'), ('Other', 'Other')], max_length=20)),
                ('address', models.CharField(max_length=200)),
                ('tel', models.CharField(max_length=25)),
                ('logo', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
