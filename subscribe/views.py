from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

from .models import SubscribedUsers
from .forms import SubscribeForm


def subscribe(request):
    """
    Renders a form to allow guests to subscribe to a newsletter

    Credit:
    Django Tutorial - Introduction no Subscribers and Newsletter #18
    by Rokas Liuberskis
    https://www.youtube.com/watch?v=wl4Yxo5_Cgw
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
