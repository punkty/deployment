from django.shortcuts import render, redirect
from django.contrib import messages
from models import User, Doodle

def session_check(request):
    if 'user' in request.session:
        return True
    else:
        return False

def index(request):
    if session_check(request):
        return redirect('wall')
    else:
        return render(request,'index.html')

def login_reg(request):
    if request.POST['action'] == 'register':
        result = User.objects.validate_reg(request)

    elif request.POST['action'] == 'login':
        result = User.objects.validate_login(request)

    if result[0] == False:
        print_errors(request, result[1])
        return redirect('/')

    return log_user_in(request, result[1])

def print_errors(request, error_list):
    for error in error_list:
        messages.add_message(request, messages.INFO, error)

def log_user_in(request, user):
    request.session['user'] = {
        'user_id': user.id,
        'first_name': user.first_name
    }

    return redirect('wall')

def doodle(request):
    if not session_check(request):
        return redirect('index')

    result = Doodle.objects.post_doodle(request)

    if result:
        print_errors(request, result)

    return redirect('wall')

def destroy(request, id):
    if not session_check(request):
        return redirect('index')
    else:
        Doodle.objects.destroy_doodle(request, id)

        return redirect('wall')

def wall(request):
    if not session_check(request):
        return redirect('index')

    context = {
        'doodles': Doodle.objects.all()[::-1]
    }

    return render(request, 'wall.html', context)

def logout(request):
    request.session.clear()

    return redirect('index')
