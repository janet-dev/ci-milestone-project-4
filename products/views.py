"""
The code utilizes Django models to manage products and categories,
along with forms for adding/editing products. It also uses Django's
messages framework to display success, error, and info messages to users.
The views 'add_product', 'edit_product', and 'delete_product' require
user authentication, ensuring only superusers can perform these actions.
"""

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    A view to show all products, including sorting and search queries -
    This view displays all products in the store, supporting sorting and
    search queries. It retrieves the products from the database, sorts them
    based on user-provided parameters, filters products based on categories
    and search queries, and renders the 'products/products.html' template
    with the filtered products.
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "You didn't enter any search criteria!")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    A view to show individual product details -
    This view displays the details of an individual product.
    It retrieves the product based on the provided product_id from
    the database and renders the 'products/product_detail.html'
    template with the product details.
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """
    Add a product to the store -
    This view allows the site owner (superuser) to add a new product
    to the store. It processes the product form data, saves the new
    product to the database, and redirects to the product detail page
    upon successful addition.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owner can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to add product. Please ensure the form is valid.'
            )
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """
    Edit a product in the store -
    This view allows the site owner (superuser) to edit an existing
    product in the store. It retrieves the product based on the provided
    product_id, processes the updated form data, and saves the changes
    to the database. Upon successful update, it redirects to the product
    detail page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(
                request,
                'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """
    Delete a product from the store -
    This view allows the site owner (superuser) to delete a product
    from the store. It retrieves the product based on the provided
    product_id, deletes it from the database, and redirects to the
    product listing page.
    """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site owner can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
