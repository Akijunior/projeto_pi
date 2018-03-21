# Generated by Django 2.0.3 on 2018-03-21 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_auto_20180321_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='buy',
            name='amount_items',
            field=models.IntegerField(default=0, verbose_name='Quantidade de itens'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='buy',
            name='status',
            field=models.CharField(choices=[('open', 'Aberta'), ('closed', 'Fechada')], default='closed', max_length=5),
        ),
    ]