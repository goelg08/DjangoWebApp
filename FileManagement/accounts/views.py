from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.core.files.storage import FileSystemStorage

# Create your views here.
def login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		
		user = auth.authenticate(username=username, password=password)
		
		if user is not None:
			auth.login(request, user)
			return redirect("upload")
		else:
			messages.info(request,"Invalid credentials")
			return redirect('login')
	else:
		return render(request, 'login.html')
		
def logout(request):
	auth.logout(request)
	return redirect("/")
	

def register(request):

	if request.method == 'POST':
		firstname = request.POST['firstname']
		lastname = request.POST['lastname']
		username = request.POST['username']
		email = request.POST['email']
		password = request.POST['password']
		confirmpassword = request.POST['confirmpassword']
		
		if username=='':
			messages.info(request, 'Please provide Username')
			return redirect('register')
		elif password=='':
			messages.info(request, 'Please provide password')
			return redirect('register')
		elif password==confirmpassword:
			if User.objects.filter(username=username).exists():
				messages.info(request, 'Username Taken')
				return redirect('register')
			elif User.objects.filter(email=email).exists():
				messages.info(request, 'Email Taken')
				return redirect('register')
			else:
				user = User.objects.create_user(username=username, password=password, email=email, first_name=firstname, last_name=lastname)
				user.save();
				messages.info(request, 'User Created')
				return redirect('login')
		else:
			messages.info(request, 'Password Not Matching')
			return redirect('register')
		return redirect('/')
	else:
		return render(request, 'register.html')

		
def upload(request):
	if request.method == 'POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		fs.save(uploaded_file.name, uploaded_file)
	return render(request,'upload.html')