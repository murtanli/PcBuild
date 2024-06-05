from django import forms
from .models import PCBuild, Component

class ComponentChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return f"{obj.name} ({obj.category}, {obj.price} руб.)"

class PCBuildForm(forms.ModelForm):
    processor = ComponentChoiceField(queryset=Component.objects.filter(category='Процессор'))
    graphics_card = ComponentChoiceField(queryset=Component.objects.filter(category='Видеокарта'))
    ram = ComponentChoiceField(queryset=Component.objects.filter(category='Оперативная память'))
    memory = ComponentChoiceField(queryset=Component.objects.filter(category='Память'))
    motherboard = ComponentChoiceField(queryset=Component.objects.filter(category='Материнская плата'))
    power_unit = ComponentChoiceField(queryset=Component.objects.filter(category='Блок питания'))
    frame = ComponentChoiceField(queryset=Component.objects.filter(category='корпус'))

    class Meta:
        model = PCBuild
        fields = '__all__'