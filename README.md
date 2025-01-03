<h2 align="left"><img src="docs/pictures/am-i-responsive.jpg"></h2>

## Project Purpose

This is a Code Institute student project for Milestone 4, built to satisfy the requirements for the EKC Training Diploma (Level 5) in [Web Application Development](https://www.ekcgroup.ac.uk/ashford-college/computing/web-application-development-diploma-level-5). 

This project has been created in order to provide a community CRUD application on a deployed interactive website. The project was built using **Gitpod**. 

The information has been presented in a way that ensures the users achieve their goals of:
* understanding what the site's function is
* understanding how to create, read, update and delete their own records or posts
* being able to register, log in and log out of this community site

The site also enhances the owner's goals by:
* showcasing their database design skills
* showcasing their Python programming skills
* showcasing their Django skills
* showcasing their back-end development skills by allowing users to change data in a PostgreSQL relational database with the aid of the Django web-framework.


## Project Requirements

* The technologies used were HTML, CSS, **Python, Django and PostgreSQL**.
* This interactive back-end project contains pages to enable users to create, read, update and delete user records in a relational database
* This README.md file explains what the project does and the value it provides for the users
* Version control is provided by Git and GitHub
* External code, libraries, templates, images, information, etc. will be listed in the **Credits**, at the bottom of this README.
* This project is deployed via **Heroku**. The code stored in a GitHub repository, whilst the data is stored in the relational PostgreSQL database hosted by **ElephantSQL**.

---

<h1 align="left">Django Web App with PostgreSQL: ClickCollect</h1>

![Python](https://img.shields.io/static/v1?label=Python&message=3.8.12&color=blue&logo=python&logoColor=ffffff)
![Django](https://img.shields.io/static/v1?label=Django&message=3.2.19&color=yellow&logo=django)
![PostgreSQL](https://img.shields.io/static/v1?label=PostgreSQL&message=11.19&color=blue&logo=postgresql&logoColor=ffffff)

[View the app deployed on Heroku.](https://clickcollect-app-be0648f4f2c3.herokuapp.com/)

[View the demo video on YouTube.](https://youtu.be/CBwUq8s2ZSY)

The aim of the project is to provide a supplementary app for local hospitality businesses offering a food takeaway service. Whilst many of these business offer an online table booking service, they do not have a select, pay and collect (or delivery) facility for takeaway food.

This site is created for my friend Jason Firth who owns the [**Luca Loves PIZZA**](https://www.lucalovespizza.co.uk/) mobile takeaway service for Warwickshire and the West Midlands. He travels with his pizza van to local events and festivals. Jason usually operates the service by himself and at the moment mainly takes orders via WhatsApp messenger, but it would make life easier if this part of the business could be automated. 

This app is inspired by [Zari Restaurant](https://www.zarirestaurant.co.uk/indian-takeaway-in-crawley/) in Crawley, West Sussex. I used their online takeaway facility many times, whilst working away. I would order my meal, pay for it and select a time slot for collection on the way home.

The site is designed to be responsive and accessible on a range of devices, making it easy to use for potential users.

<h2 align="left"><img src="docs/pictures/jason-pizza-van.jpg"></h2>

---

## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Owner Goals**](#owner-goals)
    - [**Design**](#design)
    - [**Wireframes**](#wireframes)
    - [**Relational Database**](#relational-database)

---
2. [**Features**](#features)
    - [**Current Features**](#current-features)
    - [**Future Features**](#future-features)

---
3. [**Technologies Used**](#technologies-used)
    - [**Design Tools**](#design-tools)
    - [**Front-End**](#front-end)
    - [**Back-End**](#back-end)
    - [**Validation and Evaluation**](#validation-and-evaluation)

---
4. [**Manual Testing**](TESTING.md)
    - [**Supported Browsers and Screen Sizes**](TESTING.md/#supported-browsers-and-screen-sizes)
    - [**Testing Against User Stories**](TESTING.md/#testing-against-user-stories)
    - [**Test Cases**](TESTING.md/#test-cases)
    - [**Code Validation**](TESTING.md/#code-validation)
    - [**Site Audit**](TESTING.md/#site-audit)
    - [**Compatibility**](TESTING.md/#compatibility)
    - [**Bugs Found**](TESTING.md/#bugs-found)
    - [**Known Issues**](TESTING.md/#known-issues)

---
5. [**Automated Testing**](TESTING.md/#automated-testing)
    - [**Unit Testing Using ChatGPT**](TESTING.md/#unit-testing-using-chatgpt)

---
6. [**Deployment**](DEPLOYMENT.md)
    - [**Local Deployment**](DEPLOYMENT.md/#local-deployment)
    - [**Remote Deployment**](DEPLOYMENT.md/#remote-deployment)

---
7. [**Credits**](#credits)
    - [**Media**](#media)
    - [**Code**](#code)
    - [**Acknowledgements**](#acknowledgements)

---

## UX

### User stories

:white_check_mark: *denotes current features*

"**_As a user, I would like to_** _____________________________"

- :white_check_mark: *add, update or delete items from shopping bag*.
- :white_check_mark: *keep my information secure*.
- :white_check_mark: *order and pay for products*.
- :white_check_mark: *see my order history*.
- :white_check_mark: *use the site without logging in*.
- :white_check_mark: *subscribe to a newsletter*.
- :white_check_mark: *view the site owner's blog*.


### Owner goals

"**_As an owner, I would like to_** _____________________________"

- :white_check_mark: *build a Django app*.
- :white_check_mark: *allow users to store their data via the app*.
- :white_check_mark: *build a bolt-on ecommerce app to assist local food businesses, which do not have a takeaway order and payment section*.
- :white_check_mark: *build an app to be visually attractive*.

### Design

#### The CRUD App

- This app was influenced by the Code Institute full stack e-commerce tutorial for [Boutique-Ado](https://github.com/ckz8780/boutique_ado_v1), by [Chris Z](https://github.com/ckz8780).

- What is a CRUD app? This type of app allows the user to create, read, update and delete records or posts in a database via graphical interface. In this case the PostgreSQL database is hosted by [ElephantSQL](https://www.elephantsql.com/) and as the app is developed with [Python 3.8](https://www.python.org/downloads/release/python-3811/), the graphical interface is provided by HTML5 and the mini-framework, [Django 3.2](https://docs.djangoproject.com/en/4.2/releases/3.2.19/) with [Bootstrap v4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/).

- Why this app? Many restaurants have a takeaway service where customers can order over the telephone, but surprisingly very few offer an online order, payment and delivery/collection service. With the arrival of the pandemic and the shortage of hospitality staff, may establishments would benefit from such a service. Many local businesses are on a strict budget, so this app is designed to be a bolt-on feature built by ClickCollect for use with any restaurant website. This particular site was designed for a mobile pizza van service located in the West Midlands. The business owner's photographs are used to display the products for sale. A search facility on keywords allows the user to search though the products on offer. The site does not require login, but profile and checkout pages do. All products are visible to every one, but only the site owner (superuser) can add, edit or delete the the product details. 

- View the project design flowchart to see which Django apps are associated with which templates of the app:

<h2 align="left"><img src="docs/pictures/design-site.jpg"></h2>


#### Framework

- [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) is popular framework for building responsive, mobile-first sites, with jsDelivr and a template starter page..
- [jQuery 3.5.1](https://code.jquery.com/jquery/) was used for minimal JavaScript programming.
- [Django 3.2.19](https://docs.djangoproject.com/en/4.2/releases/3.2.19/) is a web framework used to render the back-end Python with the front-end Bootstrap.

#### Colour Scheme

The following Bootstrap [colour scheme](https://getbootstrap.com/docs/4.6/utilities/colors/) was chosen for simplicity, readability and lends itself nicely to the subject of multi-coloured flame baked pizzas.

<h2 align="left"><img src="docs/pictures/colours.jpg"></h2>

#### Typography

Bootstrap v4.6 uses [native font stack](https://getbootstrap.com/docs/4.6/content/typography/) that selects the best font-family for each OS and device. For a more inclusive and accessible type scale, it uses the browser’s default root font-size (typically 16px) so visitors can customize their browser defaults as needed.

#### Imagery

In general, all pages have the Bootstrap white background with dark grey or black text. Added splashes of colour are provided by the Bootstrap red colour class '.bg-danger', hex: #DC3545.


### Wireframes

View the wireframes PDF [here](docs/ux/wireframe-mp4.pdf).

The pages contain the same functionality and look the same on every device, with the exception to the menus and the number of product cards displayed across the screen.

#### Tablet 

- Home

<h2 align="left"><img src="docs/ux/tablet-home.jpg"></h2>

- Navigation

<h2 align="left"><img src="docs/ux/tablet-mobile-nav.jpg"></h2>

- Navigation (Logged In)

<h2 align="left"><img src="docs/ux/tablet-mobile-logged-in.jpg"></h2>

- Products

<h2 align="left"><img src="docs/ux/tablet-products.jpg"></h2>

- Product Details

<h2 align="left"><img src="docs/ux/tablet-product-details.jpg"></h2>

- Product Add (Admin Login Only)

<h2 align="left"><img src="docs/ux/tablet-product-add.jpg"></h2>

- Product Edit (Admin Login Only)

<h2 align="left"><img src="docs/ux/tablet-product-edit.jpg"></h2>

- Shopping Bag

<h2 align="left"><img src="docs/ux/tablet-shopping-bag.jpg"></h2>

- Checkout

<h2 align="left"><img src="docs/ux/tablet-checkout.jpg"></h2>

- Checkout Success

<h2 align="left"><img src="docs/ux/tablet-checkout-success.jpg"></h2>

- Blog

<h2 align="left"><img src="docs/ux/tablet-blog.jpg"></h2>

- Blog Article

<h2 align="left"><img src="docs/ux/tablet-blog-article.jpg"></h2>

- Newspaper Subscription

<h2 align="left"><img src="docs/ux/tablet-subscribe.jpg"></h2>

- Sign Up / Register

<h2 align="left"><img src="docs/ux/tablet-signup.jpg"></h2>

- Sign In / Login

<h2 align="left"><img src="docs/ux/tablet-signin.jpg"></h2>

- Profile (User/Admin Login)

<h2 align="left"><img src="docs/ux/tablet-profile.jpg"></h2>

- Sign Out / Logout

<h2 align="left"><img src="docs/ux/tablet-signout.jpg"></h2>


#### Desktop

- Home

<h2 align="left"><img src="docs/ux/desktop-home.jpg"></h2>

- Navigation

<h2 align="left"><img src="docs/ux/desktop-nav.jpg"></h2>

- Navigation (Logged In)

<h2 align="left"><img src="docs/ux/desktop-logged-in.jpg"></h2>

- Products

<h2 align="left"><img src="docs/ux/desktop-products.jpg"></h2>

- Profile (User/Admin Login)

<h2 align="left"><img src="docs/ux/desktop-profile.jpg"></h2>

- Other Pages - same as for tablet

#### Mobile

- Home

<h2 align="left"><img src="docs/ux/mobile-home.jpg"></h2>

- Products

<h2 align="left"><img src="docs/ux/mobile-products.jpg"></h2>

- Product Details

<h2 align="left"><img src="docs/ux/mobile-product-details.jpg"></h2>

- Shopping Bag

<h2 align="left"><img src="docs/ux/mobile-shopping-bag.jpg"></h2>

- Other Pages - same as for tablet

### Relational Database

This projects uses [ElephantSQL](https://www.elephantsql.com/) which offers PostgreSQL as a service.

<h2 align="left"><img src="docs/pictures/db-version.jpg"></h2>

Database Entity Relationship Diagram (PostgreSQL)

<h2 align="left"><img src="docs/pictures/db-erd.jpg"></h2>

#### Database Tables

In Django, data is created in objects called Models, which are actually tables in a database. The following are the custom built models for this app. Models generated by *allauth* or *Django Admin* are not covered here.

<h2 align="left"><img src="docs/pictures/db-models.jpg"></h2>

**Blog Model**

The Post model has the following fields:

- title: A character field (CharField) for the title of the blog post with a maximum length of 200 characters. It must be unique.

- slug: A slug field (SlugField) used in URLs to represent the post with a maximum length of 200 characters. It must be unique.

- author: A foreign key field (ForeignKey) that relates the blog post to a user from the User model. The on_delete=models.CASCADE specifies that if the related user is deleted, all their blog posts will also be deleted. The related_name='blog_posts' provides a reverse relation for the user model.

- updated_on: A DateTime field (DateTimeField) that automatically updates whenever the post is modified.

- content: A TextField that holds the content of the blog post.

- created_on: A DateTime field that automatically records the date and time when the post is created.

- status: An Integer field (IntegerField) that represents the status of the post, with two choices: "Draft" (status=0) and "Publish" (status=1). The default value is set to "Draft".

The Post model also defines a nested class Meta, where the ordering of the blog posts is set to be in descending order of the created_on field.

Finally, the ```__str__``` method is defined to return the title of the blog post as a string representation when the object is referenced.

**Checkout Models**

This Python code defines two models for handling orders and order line items in a Django web application:

- Order model: This model represents an order made by a user. It includes various fields for storing order details such as order_number, user_profile, full_name, email, phone_number, country, postcode, town_or_city, street_address1, street_address2, county, date, delivery_cost, order_total, grand_total, original_bag, and stripe_pid. The model also defines methods for generating a random order number, updating the total amount of the order (including delivery costs), and overriding the save method to set the order number if it hasn't been set already.

- OrderLineItem model: This model represents individual line items in an order. It contains fields like order, product, product_mod, quantity, and lineitem_total. The model includes a save method to set the line item total based on the product price and quantity, and it updates the order total accordingly.

These models are related through foreign keys, and they facilitate storing and managing order data for the web application. The ```__str__``` methods in both models provide string representations of the order and line items when referenced.

**Products Models**

This Python code defines two models, Category and Product, for handling categories and products in a Django web application:

- Category model: This model represents product categories. It has fields for name and friendly_name. The name field stores the name of the category, and the friendly_name field stores an optional user-friendly name for the category. The model provides a method get_friendly_name() to return the friendly name if available. The ```__str__``` method returns the name of the category as its string representation.

- Product model: This model represents individual products in the web application. It includes fields such as category, sku, name, description, has_mods, price, rating, image_url, and image. The category field is a foreign key that links the product to a category from the Category model. The ```__str__``` method returns the name of the product as its string representation.

Both models utilize Django's models.Model class for defining the fields and behavior. They help in managing category and product data and establishing relationships between products and their categories.

**Profiles Model**

This Python code defines a UserProfile model and a signal receiver function to create or update user profiles when a new user is created or an existing user is saved.

- UserProfile model: This model represents a user profile and contains fields for maintaining default delivery information, including user, default_phone_number, default_street_address1, default_street_address2, default_town_or_city, default_county, default_postcode, and default_country. The user field is a one-to-one relationship with the Django User model to associate each user with their profile. The __str__ method returns the username of the associated user as its string representation.

- create_or_update_user_profile signal receiver: This function is connected to the post_save signal of the User model. When a new user is created, it automatically creates a corresponding UserProfile instance. For existing users, it updates the UserProfile instance to ensure it stays synchronized with the associated user.

The code effectively sets up a one-to-one relationship between the User model and the UserProfile model, allowing each user to have a profile with default delivery information and order history. The signal receiver ensures that user profiles are created or updated as needed when user instances are saved.

**Subscribe Model**

This Python code defines a Django model named SubscribedUsers to store information about subscribed users. The model includes the following fields:

- name: A character field with a maximum length of 50 characters to store the name of the subscribed user.

- email: An email field with a maximum length of 254 characters and marked as unique=True to ensure each email is unique in the database. It stores the email address of the subscribed user.

- created_date: A DateTime field with the default value set to the current date and time using timezone.now. It represents the date and time when the user's subscription was created.

The ```__str__``` method is defined to return the email address of the subscribed user as its string representation. This model is suitable for maintaining a list of subscribed users with their names, email addresses, and the date when they subscribed.

---

## Features

### Current Features

* This app consists of the following pages (no login required):
    - Home
    - Products
    - Product Details
    - Shopping Bag
    - Checkout
    - Checkout Success
    - Blog List
    - Blog Article
    - Newspaper Subscription
    - Sign Up
    - Sign In

* User/admin logged in pages for:
    - Profile
    - Password Reset
    - Sign Out

* Additional admin (superuser) only pages for:
    - Add Product
    - Edit Product

* And a further set of in-built Django admin pages for user and app management

<h2 align="left"><img src="docs/pictures/admin-django.jpg"></h2>
 
#### Navigation :compass:

Navigation section will be the default responsive Bootstrap one.

* Desktops

   The main menu items in bold:

    - **ClickCollect** branding for navigation to the **Home** page
    - **Search** our site box
    - **My Account** with dropdown menu for:
        - Register
        - Login
        - Product Manage (Administrator Only)
        - My Profile (User Login)
        - Logout (User Login)
    - **Shopping Bag**

    will be inline with the Search box and fixed across the top of the screen. Underneath will be *Product* and *More* menu items:

    - **All Products** with dropdown menu for:
        - By Price
        - By Rating
        - By Category
        - All Products
    - **Pizza & Calzone** with dropdown menu for:
        - Meat
        - Vegetarian
        - Vegan
        - All Pizza
    - **Drinks** with dropdown menu for:
        - Cold drinks
        - Hot Drinks
        - All Drinks
    - **More...** with dropdown menu for:
        - Our Blog
        - Subscribe 
    
    which will be inline and fixed just above the red *FOLLOW US* on Facebook banner. 
    
    All dropdown menu items will have dark grey text on a white background and on hover, a light grey backgound.

* Mobiles 
    - will feature the collapsed Bootstrap navigation with a hamburger icon inline along the top of the screen with:

        - **Search** icon with dropdown search box
        - **My Account** with dropdown menu for:
            - Register
            - Login
            - Product Manage (Administrator only)
            - My Profile (User Login)
            - Logout (User Login)
        - **Shopping Bag** 

    - selecting the hamburger icon will reveal a dropdown menu with black text on a white background:

        - **All Products** with dropdown menu for:
            - By Price
            - By Rating
            - By Category
            - All Products
        - **Pizza & Calzone** with dropdown menu for:
            - Meat
            - Vegetarian
            - Vegan
            - All Pizza
        - **Drinks** with dropdown menu for:
            - Cold drinks
            - Hot Drinks
            - All Drinks
        - **More...** with dropdown menu for:
            - Our blog
            - Subscribe 

#### Home Page :house:

Anyone (guest, member, administrator) can view this page which features a hero image with a call to action **ORDER NOW** button.

#### Products :books:

The products are displayed as cards containing the item image with the following summary:
- item name
- price
- category
- rating out of 5

Clicking the image will take the user to the product detail page. This page also contains a **Sort By** box for ordering the items.

Only the **administrator** can view the links to **Edit** (blue) or **Delete** (red) a product.

<h2 align="left"><img src="docs/pictures/admin-edit-delete.jpg"></h2>

#### Product Detail :pizza:

Only the selected product is displayed with a larger image and the same details. In addition the following is seen:
- item description
- quantity adjustment box
- **add to bag** button
- **keep shopping** button

#### Product Manage - Add :pizza::heavy_plus_sign:

Only the **administrator** can view this page which contains the add product form. 

The following fields are displayed: (```*``` mandatory)
- category dropdown select
- sku
- name*
- description*
- price*
- rating
- image url

with the buttons:
- select image
- cancel
- add product

#### Product Manage - Edit :pencil2:

Only the **administrator** can view this page which contains the edit product form. 

The following fields are displayed: (```*``` mandatory)
- category dropdown select
- sku
- name*
- description*
- price*
- rating
- image url

with the buttons:
- select image
- cancel
- add product

#### Shopping Bag :handbag:

Users can see which items they have added to their bag. Here, they can: 
- view the grand total
- update the item quantity
- remove the item
- keep shopping
- proceed to secure checkout

#### Checkout with Stripe Payment :credit_card:

Checkout is completed via secure [Stripe Payments](https://stripe.com/en-gb/payments). Users fill in their card details and have the option to save their details in their profile. Payment success is issued via a checkout success page and email confirmation, whereas failure is notified by red text underneath the card number.

#### Checkout Success :heavy_check_mark:

Logged-in users can view a past order page from their profile, with the following information:
- email address used for order confirmation
- order information
- order details
- credit card address
- billing information

#### Our Blog :writing_hand:

Blog contains a list of articles displayed in reverse chronological order. Selecting the **READ MORE** button takes the user to the more informative current **blog article**.

#### Newsletter Subscription :email:

Anyone can subscribe to the business newsletter email which keeps users updated on future events.

#### Sign Up :bust_in_silhouette::heavy_plus_sign:

Anybody can *register* for free and create a unique profile to store their own order history.

#### Sign In :bust_in_silhouette:

This facility is created using the [Django-allauth package](https://django-allauth.readthedocs.io/en/latest/index.html) built on top of [Django's own authentication and authorisation framework](https://docs.djangoproject.com/en/3.2/topics/auth/default/). This provides a comprehensive set of tools to handle user authentication and registration in Django projects. 

It is important that unauthorised users are denied access to certain pages. Personal profile pages contain credit/debit card address details, full name, phone number and email address - information that should be protected. At the moment, this app does not show users the names of other users - this makes it difficult to attempt access to personal accounts. @login_required decorators are used to ensure only logged in users have access to appropriate pages.

The administration pages for the site owner are protected from other users by creating a superuser account during project installation. A flag is used in the database to indicate if a certain registered user is a superuser/admin. This method is much better than creating a superuser with username of *admin*, which gives hackers half the information required - they only have to guess the password. 

See the [Testcases](TESTING.md/#test-cases) section for how the defensive programming is implemented.

#### Profile :lock:

An inbuilt Django decorator protects user profiles. Only the current logged-in user can view the **past order detail** page - which is actually the same page as **checkout success**, or update default address information. 

#### Sign Out :point_right:

This is a separate page where the user either confirms to signing out or cancels the action. 

#### 404 Page :no_entry:

This page replaces the standard Django **Page Not Found** with one matching the site design and a **Go Home** button.

#### 500 Page :warning:

This page replaces the standard Django **Internal Server Error** page with one matching the site design and a **Go Home** button.

### Future Features

- Allow users to 'rate' or 'like' products
- Allow users to register via social media accounts - this is provide in the app but due to time constraints is not yet activated
- Add special offers and discounted items
- Send out an actual newsletter email
- Offer a delivery service when the business expands to a certain level
- Let the customer choose a time slot for collection
- Offer dietry requirement options

---

## Technologies Used

* Cloud developer platform from [Gitpod](https://www.gitpod.io/).
* IDE integrated into Gitpod from [Visual Studio Code](https://code.visualstudio.com/).
* Debugging assisted by [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/).
* Version control integrated into Gitpod from [Git](https://git-scm.com/).

### Design Tools

* Wireframes from [Balsamiq](https://balsamiq.com/).
* Native font stack from [Bootstrap](https://getbootstrap.com/docs/4.6/content/reboot/#native-font-stack).
* Colour palette generated by [Bootstrap](https://getbootstrap.com/docs/4.6/utilities/colors/).
* Icon library and toolkit from [Font Awesome 5](https://fontawesome.com/).
* Online photo editor from [Pixlr](https://pixlr.com/x/).
* Stock photos from [Unsplash](https://unsplash.com).
* Product photos from [Jason Firth](https://www.facebook.com/people/Luca-Loves-Pizza/100075726265051/)
* Showcasing the site on different devices by [Bytes](https://ui.dev/amiresponsive)
* Paint from [Microsoft](https://apps.microsoft.com/store/detail/paint/9PCFS5B6T72H?hl=en-us&gl=us)
* Snip and Sketch from [Microsoft](https://apps.microsoft.com/store/detail/snipping-tool/9MZ95KL8MR0L?hl=en-gb&gl=gb)
* PDF Reader from [Adobe Acrobat Reader](https://www.adobe.com/uk/)
* Flowchart by [diagrams.net/draw.io](https://www.diagrams.net/)
* PostgreSQL ERD created by [DbSchema](https://dbschema.com/)
* Python code summaries and test files generated by ChatGPT from [OpenAI](https://openai.com/)
* Demo video for YouTube created on [Clipchamp](https://app.clipchamp.com/)

### Front-End

- ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) as the base for markup text.
- ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS) for custom styling the site.
- ![jQuery 3.5.1](https://img.shields.io/static/v1?label=jQuery&message=3.5.1&color=0769AD&logo=jquery&logoColor=ffffff)
    - [jQuery 3.5.1](https://code.jquery.com/jquery/) for JavaScript functionality.
- ![Bootstrap 4.6](https://img.shields.io/static/v1?label=Bootstrap&message=4.6&color=ee6e73)
    - [Bootstrap 4.6](https://getbootstrap.com/docs/4.6/getting-started/introduction/) is a popular framework for building responsive, mobile-first sites.

### Back-End

- ![Python](https://img.shields.io/static/v1?label=Python&message=3.8.12&color=blue&logo=python&logoColor=ffffff)
    - [Python 3.8.12](https://www.python.org/) is a high-level, general-purpose programming language.
- ![Django](https://img.shields.io/static/v1?label=Django&message=3.2.19&color=yellow&logo=django)
    - [Django 3.2.19](https://docs.djangoproject.com/en/4.2/releases/3.2.19/) is a web framework written in Python.
- ![Django-allauth](https://img.shields.io/static/v1?label=Django-allauth&message=0.41.0&color=orange&logo=django-allauth)
    - [Django-allauth 0.41.0](https://django-allauth.readthedocs.io/en/latest/) for authentication and authorisation.
- ![Heroku](https://img.shields.io/static/v1?label=Heroku&message=PaaS&color=430098&logo=heroku)
    - [Heroku](https://www.heroku.com) is used as *"Platform as a Service"* (PaaS) for app hosting.
- ![PostgreSQL](https://img.shields.io/static/v1?label=PostgreSQL&message=11.19&color=blue&logo=postgresql&logoColor=ffffff)
    - [PostgreSQL](https://www.postgresql.org/) is used as a relational database plugin via Heroku.

### Validation and Evaluation

* HTML validation from [W3C](https://validator.w3.org/#validate_by_input)
* CSS validation from [Jigsaw (W3C)](https://jigsaw.w3.org/css-validator/)
* Python validation from [CI Python Linter](https://pep8ci.herokuapp.com/)
* Tool For Style Guide Enforcement from [Flake8](https://flake8.pycqa.org/en/latest/)
* JavaScript validation from [JSHint](https://jshint.com/)
* Site audit by [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/)
* Temporary email account for testing from [Temp Mail](https://temp-mail.org/en/)

---

## Project Testing

See the document [TESTING.md](TESTING.md) for the code validation, site evaluation and manual tests.

---

## Deployment

See the document [DEPLOYMENT.md](DEPLOYMENT.md) for local and Heroku deployment.

---

## Credits

A huge thank you to the following people and organisations, because without you, the website would not have been produced in it's present form.

### From the Course

Heroku deployment instructions from Code Institute graduate [Joy Zadan](https://github.com/JoyZadan/shop-kbeauty/blob/main/DEPLOYMENT.md)

Readme styling from Tim Nelson's project [Unicorn Attractor](https://github.com/TravelTimN/ci-milestone05-fsfw)

Markdown Cheatsheet from [Adam Pritchard](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet#html)

### Media

Favicon created on [favicon.cc](https://www.favicon.cc/)

Emoji shortcodes from [Ikatyang](https://github.com/ikatyang/emoji-cheat-sheet/blob/master/README.md) on GitHub

GitHub static badges from [Shields.io](https://shields.io/badges)

### Code

Although this project is the work of the author, the code is based on the [Boutique Ado Tutorial](https://github.com/Code-Institute-Solutions/boutique_ado_v1) by Chris Z for Code Institute.

Other code sourced from or inspired by others have references embedded as links throughout this document and indicated by the active blue text links.

The Blog App code is based on the Djangocentral tutorial [Building A Blog Application With Django](https://djangocentral.com/building-a-blog-application-with-django/) by Abhijeet Pal

Subscription page code based on the Python Lessons tutorial [Introduction no Subscribers and Newsletter #18](https://www.youtube.com/watch?v=wl4Yxo5_Cgw) by Rokas Liuberskis

---

## Acknowledgements

Rachel Furlong - [EKC Training](https://ekcgroup.ac.uk/business-units/ekc-training) Course Facilitator, for generous support and advice.

Rohit Sharma - [Code Institute](https://codeinstitute.net/) Mentor, for the continuous feedback and guidance in industry standards.
