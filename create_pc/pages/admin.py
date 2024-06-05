from django.contrib import admin
from .models import *
from .forms import PCBuildForm



@admin.register(Component)
class ComponentAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'category', 'price', 'compatible_with_list']
    search_fields = ['name']

    def compatible_with_list(self, obj):
        return ", ".join([comp.name for comp in obj.compatible_with.all()])

    compatible_with_list.short_description = 'Совместим с'

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == 'compatible_with':
            kwargs['queryset'] = Component.objects.exclude(pk=request.resolver_match.kwargs.get('object_id', None))
        return super().formfield_for_manytomany(db_field, request, **kwargs)

@admin.register(PCBuild)
class PCBuildAdmin(admin.ModelAdmin):
    form = PCBuildForm
    list_display = ['pk', 'get_processor', 'get_graphics_card', 'get_ram', 'get_memory', 'get_motherboard', 'get_power_unit', 'get_frame', 'price', 'category']
    list_filter = ['category']

    def get_processor(self, obj):
        return obj.processor.name

    def get_graphics_card(self, obj):
        return obj.graphics_card.name

    def get_ram(self, obj):
        return obj.ram.name

    def get_memory(self, obj):
        return obj.memory.name

    def get_motherboard(self, obj):
        return obj.motherboard.name

    def get_power_unit(self, obj):
        return obj.power_unit.name

    def get_frame(self, obj):
        return obj.frame.name

    get_processor.short_description = 'Процессор'
    get_graphics_card.short_description = 'Видеокарта'
    get_ram.short_description = 'Оперативная память'
    get_memory.short_description = 'Память'
    get_motherboard.short_description = 'Материнская плата'
    get_power_unit.short_description = 'Блок питания'
    get_frame.short_description = 'Корпус'

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user', 'pc_build', 'price']
