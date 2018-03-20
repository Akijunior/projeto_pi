from django.db import models
from django.core.validators import MaxValueValidator


class Automaker(models.Model):
    name_descr = models.CharField("Nome da montadora", max_length=60)
    number = models.CharField('Telefone de contato', max_length=15, blank=True)
    email = models.CharField('E-mail', max_length=50, unique=True)

    def __str__(self):
        return self.name_descr


class Vehicle(models.Model):
    name_descr = models.CharField("Nome do veiculo", max_length=60)
    automaker = models.ForeignKey(Automaker, null=True, verbose_name='Montadora', related_name='veiculos',
                                  on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.automaker) + " - " + self.name_descr


class Modelo(models.Model):
    name_descr = models.CharField("Nome do modelo", max_length=60)
    vehicle = models.ForeignKey(Vehicle, verbose_name='Veiculo', related_name='modelo', on_delete=models.CASCADE)
    year = models.IntegerField(validators=[MaxValueValidator(3000)])

    def __str__(self):
        return str(self.vehicle) + " - " + self.name_descr + " " + str(self.year)


class Gear(models.Model):
    TYPE_GEAR_CHOICES = (
        ('acessórios', 'Acessórios'),
        ('pneus', 'Pneus, Rodas e Calotas'),
        ('iluminação', 'Faróis, Lanteras e iluminação'),
        ('midia', 'Som e Vídeo'),
        ('segurança', 'Alarmes e segurança'),
        ('grades', 'Para-choques e Grades'),
        ('motocicletas', 'Motocicletas'),
    )
    name_descr = models.CharField("Nome da peça", max_length=60)
    type_gear = models.CharField(max_length=20, choices=TYPE_GEAR_CHOICES, default='Sem tipo')
    modelo = models.ForeignKey(Modelo, null=True, related_name='pecas', on_delete=models.SET_NULL)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    amount = models.IntegerField('Quantidade em estoque', blank=True, default=0)
    views = models.IntegerField('Visualizações', blank=True, default=0)


    def __str__(self):
        return self.name_descr + " - " + self.type_gear + " " + str(self.modelo) + " = " + str(self.price)
