from django.shortcuts import render

# Create your views here.

def landing_page (request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email,password)

    return render(request,'landing_page.html')
