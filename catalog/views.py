from django.shortcuts import render


def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('name')
        print(f'{name}({phone}): {message}')
    return render(request, 'home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('name')
        print(f'{name}({phone}): {message}')
    return render(request, 'contacts.html')
