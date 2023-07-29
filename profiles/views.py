from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """Display the user's profile -
    This view displays the user's profile. It requires the user to be
    logged in (@login_required). It retrieves the user's UserProfile
    using get_object_or_404, and then handles the profile update if the
    request method is POST. If the form is valid, it saves the updated
    profile data and displays a success message. If the form is not valid,
    it displays an error message. The view also displays the user's
    order history and renders the 'profiles/profile.html' template
    with relevant data.
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """
    This view displays a past confirmation for a specific order
    identified by the order_number. It retrieves the order using
    get_object_or_404 and displays an info message indicating that
    it is a past confirmation with the order number.
    The view renders the 'checkout/checkout_success.html' template
    with the order details, indicating that it is accessed
    from the user profile page.
    """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)
