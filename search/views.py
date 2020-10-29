from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm
from django.db.models.query_utils import Q
from django.core.files.storage import FileSystemStorage
from django.conf import settings

#Elastic Search Utils
from .es_test import eSearch
from .es_client_service import eSearchNormalRetrieve, eSearchAdvancedRetrieve, eSearchIndexData

#Py Utils
import mimetypes

# Create your views here.

UserModel = get_user_model()
from .forms import SignUpForm, UserForm, ProfileForm

#signup
def signup(request):
    context = {}
    form = SignUpForm(request.POST or None)
    if request.method == "POST":
        if User.objects.filter(email=request.POST['email']).exists():
            messages.error(request, "Unsuccessful registration, Email Already Exists. Please use a different email." )
        elif form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            sendActivationEmail(request, user, form)
            #login(request, user)
            #messages.success(request, "Please confirm your email address to complete the registration" )
            return render(request, 'accounts/register_account.html',context={'user':user})
        messages.error(request, "Unsuccessful registration, Invalid Information." )
    context['signup_form']=form
    return render(request,'accounts/signup.html',context)

#--- https://www.ordinarycoders.com/blog/article/django-user-register-login-logout
#--- https://www.ordinarycoders.com/blog/article/django-password-reset
def sendActivationEmail(request, user, form):
    current_site = get_current_site(request)
    mail_subject = 'Activate your Eye of Sauron account.'
    message = render_to_string('accounts/account_activation.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
    })
    to_email = form.cleaned_data.get('email')
    email = EmailMessage(
                mail_subject, message, to=[to_email]
    )
    email.send()

# activate
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        print(user)
        print(default_token_generator.check_token(user, token))
        return HttpResponse('Activation link is invalid!')

#login
def login_c(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if not user.is_active:
                messages.error(request, "You are not a registered user. Please confirm the email before login")
            elif user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('index')
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="accounts/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("index")

#index
@login_required
def index(request):
    return render(request,'search/home.html')

#Test Elastic Search
@login_required
def etest(request):
    results=[]
    name_term=""
    gender_term=""
    if request.POST.get('name') and request.POST.get('gender'):
        #print("--> Both name and gender found")
        name_term=request.POST['name']
        gender_term=request.POST['gender']
    elif request.POST.get('name'):
        #print("--> Name found")
        name_term=request.POST['name']
    elif request.POST.get('gender'):
        #print("--> Gender found")
        gender_term=request.POST['gender']
    search_term = name_term or gender_term
    print(request.POST.keys())
    results = eSearch(firstName=name_term, gender=gender_term)
    #print(results)
    context={
        'results': results,
        'count': len(results),
        'search_term': search_term
    }
    return render(request,'search/etest.html', context=context)


#advanced search
@login_required
def advanced_search(request):
    results=[]
    imgPatentID=""
    imgDescription=""
    imgObject=""
    imgAspect=""
    if request.method == "POST":
        if request.POST.get('img-patentID'):
            imgPatentID=request.POST['img-patentID']
        if request.POST.get('img-desc'):
            imgDescription=request.POST['img-desc']
        if request.POST.get('img-obj'):
            imgObject=request.POST['img-obj']
        if request.POST.get('img-aspect'):
            imgAspect=request.POST['img-aspect']
        print(request.POST.keys())
        #retrieve results from elastic search
        results = eSearchAdvancedRetrieve(imgPatentID, imgDescription, imgObject, imgAspect)
    search_term = imgPatentID or imgDescription or imgObject or imgAspect
    print('--> Search Term: ',search_term)
    context = {
        'results': results,
        'count': len(results),
        'search_term': search_term
    }
    return render(request,'search/advanced.html', context=context)

#advanced search
@login_required
def search(request):
    results=[]
    search_term=""
    if request.method == "POST":
        search_term = request.POST['img-search-string']
        results = eSearchNormalRetrieve(search_term)
    print('--> Search Term: ',search_term)
    context = {
        'results': results,
        'count': len(results),
        'search_term': search_term
    }
    return render(request,'search/search.html', context=context)


def checkFiletype(fileName):
    mimetypes.init()
    mimestart = mimetypes.guess_type(fileName)[0]
    if mimestart != None:
        mimestart = mimestart.split('/')[0]
        if mimestart == 'image':
            return True
        return False

#index new data
@login_required
def indexData(request):
    index = False
    if request.method == 'POST':
        imgfile = request.FILES['img-file']
        if checkFiletype(imgfile.name):
            fs = FileSystemStorage(location=settings.IMAGE_DATA_ROOT)
            imgName = request.POST['img-patentID']+'-D000'+request.POST['img-figId']+'.png'
            filename = fs.save(imgName, imgfile)
            if eSearchIndexData(request.POST):
                index = True
                messages.info(request, "Data successfully indexed.") 
            else:
                messages.error(request, "Error in indexing data.")
        else:
            messages.error(request, "Please upload only an image file. ('png','jpeg','jpg')")
    context = {
        'index' : index
    }
    return render(request,'search/newImagePatent.html', context=context)

#profile
@login_required
def getProfileDetails(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid():
            user_form.save()
            messages.success(request,('Your profile was successfully updated!'))
        elif profile_form.is_valid():
            profile_form.save()
            messages.success(request,('Your wishlist was successfully updated!'))
        else:
            messages.error(request,('Unable to complete request'))
        return redirect ("/accounts/profile")
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request=request, template_name="accounts/profile.html", context={"user":request.user, "user_form":user_form, "profile_form":profile_form })
    #return render(request,'accounts/profile.html',context={})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts/profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'passwords/password_change.html', {
        'form': form
    })

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Eye of Sauron | Password Reset Requested"
					email_template_name = "passwords/password_reset_email.html"
					c = {
					"email":user.email,
					'domain':get_current_site(request).domain,
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, None , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("/password_reset/done/")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="passwords/password_reset.html", context={"password_reset_form":password_reset_form})
