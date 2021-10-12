from django.shortcuts import render,get_object_or_404
from django.views.generic import CreateView,UpdateView,DetailView
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.urls import reverse_lazy,reverse
from django.contrib.auth.views import PasswordChangeView
from .forms import SignUpForm,PasswordChangingForm
from theblog.models import User,Post,Profile


# Create your views here.
class ShowProfileView(DetailView):
    model = Profile
    template_name = 'registration/users_profile.html'
    
    def get_context_data(self,*args,**kwargs):
        users = Profile.objects.all()
        context = super(ShowProfileView,self).get_context_data()
        page_user = get_object_or_404(Profile,id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context

class UserRegisterView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    ordering = ['fields']
    success_url = reverse_lazy('login')
    
class UserEditProfileView(UpdateView):
    model = Profile
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('profile')
    fields = ['bio','profile_pic','wb_url','insta_url','fb_url','whatsapp_url','twitter_url']

   

class CreateProfileView(CreateView):
    model = Profile
    template_name = 'registration/create_profile.html'
    #success_url = reverse_lazy('profile')
    fields = ['bio','profile_pic','wb_url','insta_url','fb_url','whatsapp_url','twitter_url']

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class settingsview(UpdateView):
    model = User
    template_name = 'registration/settings.html'
    success_url = reverse_lazy('home')
    fields = ['first_name','last_name','email']
    


class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('home')

def get_user_profile(request):
    profile = User.objects.filter(username=request.user)
    post_by_user = Post.objects.filter(author = request.user)
    total_posts = post_by_user.count()
    return render(request, 'registration/profile.html', {"profile":profile,'total_posts':total_posts})







