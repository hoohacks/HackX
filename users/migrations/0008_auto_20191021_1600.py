# Generated by Django 2.2.6 on 2019-10-21 16:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20191011_0241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='mentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mentor_tickets', to=settings.AUTH_USER_MODEL),
        ),
    ]