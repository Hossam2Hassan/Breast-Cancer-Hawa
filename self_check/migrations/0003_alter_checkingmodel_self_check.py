# Generated by Django 4.0.4 on 2022-04-22 01:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('self_check', '0002_alter_checkingmodel_self_check'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checkingmodel',
            name='self_check',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='self_check.self_checkmodel'),
            preserve_default=False,
        ),
    ]
