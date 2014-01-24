# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from analytics import analytics

@login_required
@user_passes_test(lambda u: u.is_staff)
def show_analytics(request):
	return render(request,'analytics/main.html',{'analytics':analytics.get()})


