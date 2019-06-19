# Generated by Django 2.0.2 on 2019-05-06 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_usertrueandfalse_user_subject_sum_nums'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usertrueandfalse',
            name='right_num',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='正确率'),
        ),
        migrations.AlterField(
            model_name='usertrueandfalse',
            name='wrong_num',
            field=models.FloatField(blank=True, default=0, null=True, verbose_name='错误率'),
        ),
    ]