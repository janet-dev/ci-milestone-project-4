from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import SubscribedUsers
from .forms import SubscribeForm


def subscribe(request):
    """
    Renders a form to allow guests to subscribe to a newsletter 
    and provides user feedback via toasts
    """

    if request.method == "POST":
        subscribe_form = SubscribeForm(request.POST)

        if subscribe_form.is_valid():
            subscribe = subscribe_form.save()
            messages.success(request, "Successfully subscribed to newsletter.")
            return redirect('products')
        else:
            messages.error(request, "Form invalid, please try again.")
            return redirect('subscribe')
    else:
        subscribe_form = SubscribeForm()

    template = 'subscribe/subscribe.html'
    context = {
        'subscribe_form': subscribe_form,
    }

    return render(request, template, context)