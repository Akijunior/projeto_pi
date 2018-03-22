# Generated by Django 2.0.3 on 2018-03-22 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0008_auto_20180321_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buy',
            name='status',
            field=models.CharField(choices=[('open', 'Aberta'), ('closed', 'Fechada')], default='closed', max_length=5),
        ),
        migrations.AlterField(
            model_name='item',
            name='amount',
            field=models.FloatField(default=0, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='item',
            name='gear',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='core.Gear', verbose_name='peça'),
        ),
        migrations.AlterField(
            model_name='pay',
            name='total_value',
            field=models.FloatField(blank=True, null=True, verbose_name='Valor total do pagamento'),
        ),
    ]