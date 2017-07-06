from django.views.generic.base import View   # urls.py:  url(r'^login/', LoginView.as_view(), name='login')

class LoginView(View):
    def get(self, request):
        return render(request, 'login.html', {})

    def post(self, request):
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html', {'username': username})
        else:
            return render(request, 'login.html', {})
        
  
