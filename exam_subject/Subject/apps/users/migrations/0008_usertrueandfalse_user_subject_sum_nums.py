# Generated by Django 2.0.2 on 2019-05-06 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_usertrueandfalse'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertrueandfalse',
            name='user_subject_sum_nums',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='答题总数'),
        ),
    ]