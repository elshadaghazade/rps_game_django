from django.shortcuts import render, redirect
from random import choice

def check_value(user_choice, server_choice):
    if user_choice == 'r' and server_choice == 'p':
        return 2
    if user_choice == 'p' and server_choice == 'r':
        return 1
    if user_choice == 'r' and server_choice == 's':
        return 1
    if user_choice == 's' and server_choice == 'r':
        return 2
    if user_choice == 's' and server_choice == 'p':
        return 1
    if user_choice == 'p' and server_choice == 's':
        return 2
    else:
        return 3



def play(request):
    variants = ['r', 'p', 's']
    server_choice = choice(variants)
    user_choice = None
    context = {
        'server_choice': server_choice
    }

    if 'wins' not in request.session:
        request.session['wins'] = 0
    if 'loses' not in request.session:
        request.session['loses'] = 0
    
    if 'draws' not in request.session:
        request.session['draws'] = 0

    if not request.session.get('is_logged_in'):
        return redirect('authentication')
    else:
        if request.method == 'POST':
            user_choice = request.POST.get('user_choice')
            context['user_choice'] = user_choice
        
        result = check_value(user_choice, server_choice)
        if result == 1:
            context['game_state'] = 'You won!'
            request.session['wins'] += 1
        elif result == 2:
            context['game_state'] = 'You are loser!'
            request.session['loses'] += 1
        elif result == 3:
            context['game_state'] = 'Draw'
            request.session['draws'] += 1



        
        return render(request, "play.html", context)

def authenticate(request):
    context  = {}

    if request.method == 'POST':
        request.session['first_name'] = request.POST.get('first_name')
        request.session['last_name'] = request.POST.get('last_name')
        request.session['is_logged_in'] = True
        
        return redirect('play')
    elif request.method == 'GET':
        if request.session.get('is_logged_in'):
            return redirect('play')

        
    return render(request, 'authenticate.html', context)


def logout(request):
    request.session.clear()

    return redirect('authentication')


def statistics(request):
    if not request.session.get('is_logged_in'):
        return redirect('authentication')

    return render(request, 'statistics.html')