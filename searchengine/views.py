from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import PasswordResetForm

# Create your views here.

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

# def changePassword(request):
# 	if request.method == 'POST':
# 		form = PasswordResetForm(request.user, request.POST)
# 		if form.is_valid():
# 			print('--> Sending reset password mail')
# 			return render(request, 'registration/password_reset_done.html')
# 		else:
# 			print('--> Reset password Form not valid.')
# 			return render(request, 'registration/password_reset_done.html')
# 	else:
# 		print('--> Reset password Form start.')
# 		form = PasswordResetForm
# 		return render(request, 'registration/password_reset_form.html', {
#         'form': form
#     })

def profile(request):
	return render(request, 'userProfile.html')





