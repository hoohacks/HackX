# Generated by Django 2.2.6 on 2019-10-22 18:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('judging', '0001_initial'),
        ('users', '0008_auto_20191021_1600'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_judge',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='user',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='judging.Organization'),
        ),
        migrations.AddField(
            model_name='user',
            name='sd_offset',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=9),
        ),
    ]
