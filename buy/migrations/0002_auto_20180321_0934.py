# Generated by Django 2.0.3 on 2018-03-21 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Iniciada em'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='buy',
            name='status',
            field=models.CharField(choices=[('open', 'Aberta'), ('close', 'Fechada')], default='close', max_length=5),
        ),
        migrations.AddField(
            model_name='buy',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizada em'),
        ),
    ]