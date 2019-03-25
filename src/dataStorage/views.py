from django.shortcuts import render ,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q

from .forms import ReviewForm
from .models import Review
# Create your views here.

def index(request):
	return redirect('home')

@csrf_exempt
def home(request):
    if request.user.is_authenticated:
        user = request.user.username
        #print(request.user.username)
        context = {
            'user' : user,
        }
    else:
        context = {}
    return render(request, 'home.html', context)

@login_required
@csrf_exempt
def addPost(request):
    if request.method == 'POST':
        print(request.POST)
        print(request.user.username)
    form = ReviewForm(request.POST or None)
    if request.user.is_authenticated:
        user = request.user.username
        #print(request.user.username)
        context = {
            'user' : user,
            'form' : form
        }
    else:
        context = {
            #'user' : user,
            'form' : form
        }
    if form.is_valid():
        form.save()
    return render(request, 'review.html', context)
