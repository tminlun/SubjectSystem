# Generated by Django 2.0.2 on 2019-05-05 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0009_examtime_exam_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='analysis',
            field=models.CharField(default='', max_length=500, verbose_name='解析'),
        ),
    ]