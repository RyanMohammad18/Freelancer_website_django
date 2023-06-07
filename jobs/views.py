from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.urls import reverse_lazy
from jobs.models import Business, Freelancer
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.


def index(request):
    return HttpResponse("<h1>Freelancer_Website</h1>")


class FreelancerListView(ListView):
    model = Freelancer

class FreelancerDetailView(DetailView):
    model=Freelancer

class FreelancerCreateView(LoginRequiredMixin,CreateView):
    model =Freelancer
    fields = ['name','profile_pic','tagline','bio','website']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FreelancerCreateView, self).form_valid(form)
    

class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name','profile_pic','bio']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BusinessCreateView, self).form_valid(form)
    

@login_required
def handle_login(request):
    if request.user.get_freelancer() or request.user.get_business():
        return redirect(reverse_lazy('freelancer-list'))
    
    return render(request,'jobs/choose_account.html',{})