from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .forms import SignUpForm, LoginForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password, check_password
from django.http import JsonResponse


# Create your views here.

def table(request):
    # return HttpResponse("Hello user")
    users = User.objects.all()
    return render(request, 'details/table.html', {'users': users})


def sign_up(request):
    if request.method == 'POST':

        users = User.objects.create(first_name=request.POST.get('first_name'),
                                    last_name=request.POST.get('last_name'),
                                    date_of_birth=request.POST.get('date_of_birth'),
                                    gender=request.POST.get('gender'),
                                    email=request.POST.get('email'),
                                    password=make_password(request.POST.get('password')),
                                    username=request.POST.get('username'),
                                    )
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
        return HttpResponse("Submitted Successfully")

        # return render(request, 'details/table.html',{'users': users})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def edit_user(request, id):
    users = User.objects.get(id=id)
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            users.first_name = form.cleaned_data['first_name']
            users.last_name = form.cleaned_data['last_name']
            users.email = form.cleaned_data['email']
            users.password = form.cleaned_data['password']
            users.date_of_birth = form.cleaned_data['date_of_birth']
            users.save()
            return redirect('table')
    else:
        form = SignUpForm(initial={
            'first_name': users.first_name,
            'last_name': users.last_name,
            'email': users.email,
            'password': users.password,
        })
    return render(request, 'edit_user.html', {'users': users, 'form': form, })
    # return render(request, 'edit_user.html')


def delete_user(request, id):
    print("Delete user view accessed.")
    users = User.objects.get(id=id)
    if request.method == 'POST':
        if request.is_ajax():
            print("12")
            users.delete()
            return HttpResponse('User deleted successfully.')
        else:
            users.delete()
            return redirect('table')

    return render(request, 'delete_user.html', {'users': users})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            print("1st if")
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            users = User.objects.get(username=username)
            print(users)

            if users is not None and check_password(password, users.password):
                print("if coming")
                login(request, users)
                return redirect('table')
            else:
                print("else-part")
                return HttpResponse("Invalid username or password.")
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

# def delete_item(request, item_id):
#     if request.method == 'POST' and request.is_ajax():
#         try:
#             # Delete the item using the item_id
#             # Add your deletion logic here
#
#             # Return success response
#             return JsonResponse({'success': True})
#         except Exception as e:
#             # Return failure response
#             return JsonResponse({'success': False, 'error': str(e)})
