# Generated by Django 4.0.4 on 2022-04-19 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_alter_loginuser_user_id_alter_loginuser_user_pw'),
    ]

    operations = [
        migrations.AddField(
            model_name='loginuser',
            name='age',
            field=models.IntegerField(default=20, verbose_name='나이'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='birth_day',
            field=models.DateField(null=True, verbose_name='생년월일'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='email',
            field=models.CharField(default=False, max_length=255, verbose_name='이메일 주소'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='gender',
            field=models.CharField(default='male', max_length=6, verbose_name='성별'),
        ),
        migrations.AddField(
            model_name='loginuser',
            name='name',
            field=models.CharField(default=False, max_length=20, verbose_name='이름'),
        ),
        migrations.AlterField(
            model_name='loginuser',
            name='user_pw',
            field=models.CharField(default=False, max_length=255),
        ),
    ]
