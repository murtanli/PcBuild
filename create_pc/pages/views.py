import json

from django.contrib import messages
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt

from .models import *
def main_page(request):
    return render(request, 'main.html')

def search_page(request):

    all_pc = []
    context = {}
    filtered_pc_builds_data = []
    message = ''

    builds = PCBuild.objects.all()
    context = {
        'builds': builds
    }

    if request.method == 'POST':
        type_pc = request.POST.get('type_pc')
        cpu = request.POST.get('cpu')
        graphics_card = request.POST.get('grahpics_card')
        min_price = request.POST.get('min_price')
        max_price = request.POST.get('max_price')

        filters = {}

        if type_pc:
            filters['category'] = type_pc
        if cpu:
            filters['processor__name__icontains'] = cpu
        if graphics_card:
            filters['graphics_card__name__icontains'] = graphics_card
        if min_price:
            filters['price__gte'] = min_price
        if max_price:
            filters['price__lte'] = max_price

        results = PCBuild.objects.filter(**filters)
        context = {
            'builds': results
        }

    return render(request, 'deals.html', context=context)

def info_page(request):
    return render(request, 'info.html')

def configurator_page(request, pc_build_id):

    pc_build = PCBuild.objects.get(id=pc_build_id)

    cpus = Component.objects.filter(category='Процессор')
    graphics_cards = Component.objects.filter(category='Видеокарта')
    motherboards = Component.objects.filter(category='Материнская плата')
    rams = Component.objects.filter(category='Оперативная память')
    memorys = Component.objects.filter(category='Память')
    power_units = Component.objects.filter(category='Блок питания')
    frames = Component.objects.filter(category='корпус')

    context = {
        'pc_build': pc_build,
        'cpus': cpus,
        'graphics_cards': graphics_cards,
        'motherboards': motherboards,
        'rams': rams,
        'memorys': memorys,
        'power_units': power_units,
        'frames': frames,
    }
    return render(request, 'configurator.html', context=context)


@csrf_exempt
def place_order(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            # Пример создания заказа без сериализатора
            order = PCBuild()
            order.graphics_card = get_object_or_404(Component, id=data['graphics_card'])
            order.processor = get_object_or_404(Component, id=data['processor'])
            order.motherboard = get_object_or_404(Component, id=data['motherboard'])
            order.ram = get_object_or_404(Component, id=data['ram'])
            order.memory = get_object_or_404(Component, id=data['memory'])
            order.power_unit = get_object_or_404(Component, id=data['power_unit'])
            order.frame = get_object_or_404(Component, id=data['frame'])
            order.category = 'Пользовательский'
            order.save()

            cart = Cart()
            cart.user = request.user
            cart.pc_build = order
            cart.price = order.price
            cart.save()
            messages.success(request, 'Заказ оформлен!')
            return JsonResponse({'order_id': order.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request'}, status=400)

def logout_view(request):
    logout(request)
    return redirect('main_page')

def auth(request):
    if request.method == 'POST':
        login_username = request.POST.get('login')  # Переименуйте переменную login
        password = request.POST.get('password')
        user = authenticate(username=login_username, password=password)  # Используйте новое имя переменной
        if user is not None:
            login(request, user)
            return redirect('search_page')
        else:
            messages.error(request,'Неверный логин или пароль')

    return render(request, "auth.html", )

def sign_in(request):
    if request.method == 'POST':
        login_text = request.POST.get('login')
        password_text = request.POST.get('password')

        try:
            # Создаем пользователя
            user = User.objects.create_user(username=login_text, password=password_text)

            messages.success(request, 'Регистрация прошла успешно!')
            return redirect('auth')

        except:
            messages.error(request, 'Ошибка регистрации. Пользователь с таким логином уже существует.')

        return redirect('sign_in')

    else:
        return render(request, 'sign_in.html')

def order_pc(request, pc_build_id):
    pc_build = PCBuild.objects.get(id=pc_build_id)
    cart = Cart()
    cart.user = request.user
    cart.pc_build = pc_build
    cart.price = pc_build.price
    cart.save()
    messages.success(request, 'Заказ оформлен!')
    return redirect('search_page')