from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.


def index(request):
	return render(request,'home.html')

def Register(request):
	if request.method=='POST':
		username=request.POST['username']
		email=request.POST['email']
		password=request.POST['password']
		confirm_password=request.POST['confirm_password']

		if password==confirm_password:
			if User.objects.filter(username=username).exists():
				messages.info(request,"username already Taken")
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request,"Email already Taken")
				return redirect('register')
			else:
				user=User.objects.create_user(username=username,email=email,password=password)
				user.save()
				print("user created sucessfully!!")
				messages.success(request, 'Registration successful! Please log in.')
				return redirect('login')
		else:
			messages.info(request,"Password Does Not Match")
			return redirect('register')
		
	else:
		return render(request,'register.html')

def user_login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        # Ensure that email and password are not None
        if username and password:
            user = auth.authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('homepage')  # Redirect to the homepage or dashboard
            else:
                messages.info(request, "Invalid credentials")  # Use error message for better visibility
        else:
            messages.info(request, "Both fields are required.")  # Handle empty fields

    # Return the login page for both GET requests and POST requests that fail
    return render(request, 'login.html')

def Logout(request):
	auth.logout(request)
	return redirect('login')