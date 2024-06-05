from django.db import models
from django.contrib.auth.models import User


class Component(models.Model):

    NAME_COMP_CHOICES = [
        ('Процессор', 'Процессор'),
        ('Видеокарта', 'Видеокарта'),
        ('Оперативная память', 'Оперативная память'),
        ('Память', 'Память'),
        ('Материнская плата', 'Материнская плата'),
        ('Блок питания', 'Блок питания'),
        ('корпус', 'корпус')
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=NAME_COMP_CHOICES, null=True, blank=True)
    characteristics = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    compatible_with = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.name


class PCBuild(models.Model):
    CATEGORY_CHOICES = [
        ('Игровой', 'Игровой'),
        ('Офисный', 'Офисный'),
        ('Для дома', 'Для дома'),
        ('Профессиональный', 'Профессиональный'),
        ('Пользовательский', 'Пользовательский'),
    ]

    processor = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='pcbuild_processor')
    graphics_card = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='pcbuild_graphics_card')
    ram = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='pcbuild_ram')
    memory = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='pcbuild_memory')
    motherboard = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='pcbuild_motherboard')
    power_unit = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='pcbuild_power_unit')
    frame = models.ForeignKey(Component, on_delete=models.CASCADE, related_name='pcbuild_frame')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_price(self):
        total_price = (
                self.processor.price +
                self.graphics_card.price +
                self.ram.price +
                self.memory.price +
                self.motherboard.price +
                self.power_unit.price +
                self.frame.price
        )
        return total_price

    def save(self, *args, **kwargs):
        self.price = self.calculate_price()
        super().save(*args, **kwargs)



class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    pc_build = models.ForeignKey(PCBuild, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)


