# Manual Testing

**The site was built, tested and validated on the Chrome browser only.**

<h2 align="left"><img src="docs/pictures/chrome.jpg"></h2>


---

## Supported Browsers and Screen Sizes

Bootstrap v4.6 was used for building the site - see the [supported browsers and devices](https://getbootstrap.com/docs/4.6/getting-started/browsers-devices/)

* Bootstrap is compatible with:
    - Chrome 45+
    - Firefox 38+
    - Safari 9+
    - Opera 30+
    - Edge 12+
    - IE 10+
    - Android 4.4+
    - iOS 9+

### Mobile devices

Generally speaking, Bootstrap supports the latest versions of each major platform’s default browsers. Note that proxy browsers (such as Opera Mini, Opera Mobile’s Turbo mode, UC Browser Mini, Amazon Silk) are not supported.

<h2 align="left"><img src="docs/pictures/bootstrap-mobile.jpg"></h2>

### Desktop browsers

Similarly, the latest versions of most desktop browsers are supported.

<h2 align="left"><img src="docs/pictures/bootstrap-desktop.jpg"></h2>

---

## Testing Against User Stories

"**_As a user, I would like to_** _____________________________"

- *add, update or delete items from shopping bag*
    - All users are able to view, add, edit or delete their own bag items:
        - View
        <h2 align="left"><img src="docs/testing/user/bag-view.jpg"></h2>
        - Add
        <h2 align="left"><img src="docs/testing/user/bag-add.jpg"></h2>
        - Delete
        <h2 align="left"><img src="docs/testing/user/bag-delete.jpg"></h2>
        - Edit
        <h2 align="left"><img src="docs/testing/user/bag-edit.jpg"></h2>

- *keep my information secure*
    - Users need to register with a unique username and password in order to create a profile page. This profile page is a history of their prior orders. 

    <h2 align="left"><img src="docs/testing/user/register.jpg"></h2>

    - Security is provided by the [**django-allauth**](https://django-allauth.readthedocs.io/en/latest/) app. The *allauth* app is stored in the root *templates* folder of the project.

    <h2 align="left"><img src="docs/testing/user/defense.jpg"></h2>

- *use the site without logging in*
    - Users can buy items, without registering or logging in:

    <h2 align="left"><img src="docs/testing/user/buy.jpg"></h2>

- *order and pay for products*

    <h2 align="left"><img src="docs/testing/user/pay.jpg"></h2>

- *as a logged in user, see my order history*

    <h2 align="left"><img src="docs/testing/user/history.jpg"></h2>

---

## Test Cases

These cases are included in order to help the next developer understand the design of the site and how to extend it. They document the look and functionality of each page. All pages and features will function and look the same whether on desktop, tablet or mobile, except for the 

- absence of the branding **Click**Collect and *hamburger* menu for mobiles and some tablets

    <h2 align="left"><img src="docs/testing/testcases/nav-hamburger.jpg"></h2>

    When the menu icon is selected, it reveals a sliding down panel listing the menu options. Select an option to navigate to the appropriate page.

    <h2 align="left"><img src="docs/testing/testcases/nav-mobile.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/nav-tablet.jpg"></h2>


- number of product cards displayed across the screen:
    - desktops tend to show four cards across

    <h2 align="left"><img src="docs/testing/testcases/products-desktop.jpg"></h2>

    - tablets tend to show two cards across

    <h2 align="left"><img src="docs/testing/testcases/products-tablet.jpg"></h2>
    
    - mobiles tend to show one card across

    <h2 align="left"><img src="docs/testing/testcases/products-mobile.jpg"></h2>


### Test Case Logs

The defensive programming is included with the [**django-allauth**](https://django-allauth.readthedocs.io/en/latest/) in order to build a more secure app. This is an integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

The following logs detail the testing carried out:

---

#### Top Header Section

<h2 align="left"><img src="docs/testing/testcases/top-header-06.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-01-top-header-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-01-top-header-2.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-01-top-header-3.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/top-header-01.jpg"></h2>

    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/top-header-03.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/top-header-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/top-header-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/top-header-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/top-header-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/top-header-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/top-header-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/top-header-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/top-header-12.jpg"></h2>

    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/top-header-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/top-header-14.jpg"></h2>

    - Step 15
    <h2 align="left"><img src="docs/testing/testcases/top-header-15.jpg"></h2>

    - Step 16
    <h2 align="left"><img src="docs/testing/testcases/top-header-16.jpg"></h2>

    - Step 17
    <h2 align="left"><img src="docs/testing/testcases/top-header-17.jpg"></h2>

    - Step 18
    <h2 align="left"><img src="docs/testing/testcases/top-header-18.jpg"></h2>

    - Step 19
    <h2 align="left"><img src="docs/testing/testcases/top-header-19.jpg"></h2>

    - Step 20
    <h2 align="left"><img src="docs/testing/testcases/top-header-20.jpg"></h2>

    - Step 21
    <h2 align="left"><img src="docs/testing/testcases/top-header-21.jpg"></h2>

    - Step 22
    <h2 align="left"><img src="docs/testing/testcases/top-header-22.jpg"></h2>

    - Step 23
    <h2 align="left"><img src="docs/testing/testcases/top-header-23a.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/top-header-23.jpg"></h2>

    - Step 24
    <h2 align="left"><img src="docs/testing/testcases/top-header-24.jpg"></h2>

    - Step 25
    <h2 align="left"><img src="docs/testing/testcases/top-header-25.jpg"></h2>

    - Step 26
    <h2 align="left"><img src="docs/testing/testcases/top-header-26.jpg"></h2>

    - Step 27
    <h2 align="left"><img src="docs/testing/testcases/top-header-27.jpg"></h2>

    - Step 28
    <h2 align="left"><img src="docs/testing/testcases/top-header-28.jpg"></h2>

    - Step 29
    <h2 align="left"><img src="docs/testing/testcases/top-header-29.jpg"></h2>

    - Step 30
    <h2 align="left"><img src="docs/testing/testcases/top-header-30.jpg"></h2>

---

#### Home Page

<h2 align="left"><img src="docs/testing/testcases/home-01.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-02-home.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/home-01.jpg"></h2>

    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/home-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/home-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/home-06.jpg"></h2>

---

#### Products Page

<h2 align="left"><img src="docs/testing/testcases/products-03.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-03-products-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-03-products-2.jpg"></h2>

- Screenshots

    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/products-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/products-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/products-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/products-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/products-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/products-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/products-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/products-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/products-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/products-12.jpg"></h2>

    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/products-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/products-14.jpg"></h2>

    - Step 15
    <h2 align="left"><img src="docs/testing/testcases/products-15.jpg"></h2>

    - Step 17
    <h2 align="left"><img src="docs/testing/testcases/products-17.jpg"></h2>

    - Step 18
    <h2 align="left"><img src="docs/testing/testcases/products-18.jpg"></h2>

    - Step 19
    <h2 align="left"><img src="docs/testing/testcases/products-19.jpg"></h2>

    - Step 20
    <h2 align="left"><img src="docs/testing/testcases/products-20.jpg"></h2>

    - Step 21
    <h2 align="left"><img src="docs/testing/testcases/products-21.jpg"></h2>

---

#### Product Detail Page

<h2 align="left"><img src="docs/testing/testcases/product-detail-04.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-04-product-detail-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-04-product-detail-2.jpg"></h2>

- Screenshots

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/product-detail-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/product-detail-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/product-detail-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/product-detail-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/product-detail-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/product-detail-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/product-detail-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/product-detail-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/product-detail-12.jpg"></h2>

    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/product-detail-13.jpg"></h2>

---

#### Shopping Bag Page

<h2 align="left"><img src="docs/testing/testcases/bag-03.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-05-bag-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-05-bag-2.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/bag-01.jpg"></h2>

    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/bag-03.jpg"></h2>
    
    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/bag-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/bag-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/bag-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/bag-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/bag-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/bag-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/bag-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/bag-11.jpg"></h2>

---

#### Checkout Page

<h2 align="left"><img src="docs/testing/testcases/checkout-04.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-06-checkout-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-06-checkout-2.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-06-checkout-3.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-06-checkout-4.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/checkout-01.jpg"></h2>

    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/checkout-03.jpg"></h2>
    
    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/checkout-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/checkout-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/checkout-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/checkout-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/checkout-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/checkout-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/checkout-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/checkout-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/checkout-12.jpg"></h2>

    - Step 13a
    <h2 align="left"><img src="docs/testing/testcases/checkout-13a.jpg"></h2>

    - Step 13b
    <h2 align="left"><img src="docs/testing/testcases/checkout-13b.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/checkout-14.jpg"></h2>

    - Step 15a
    <h2 align="left"><img src="docs/testing/testcases/checkout-15a.jpg"></h2>

    - Step 15b
    <h2 align="left"><img src="docs/testing/testcases/checkout-15b.jpg"></h2>

    - Step 15c
    <h2 align="left"><img src="docs/testing/testcases/checkout-15c.jpg"></h2>

    - Step 15d
    <h2 align="left"><img src="docs/testing/testcases/checkout-15d.jpg"></h2>

    - Step 15e
    <h2 align="left"><img src="docs/testing/testcases/checkout-15e.jpg"></h2>

    - Step 15f
    <h2 align="left"><img src="docs/testing/testcases/checkout-15f.jpg"></h2>

    - Step 16
    <h2 align="left"><img src="docs/testing/testcases/checkout-16.jpg"></h2>

    - Step 17
    <h2 align="left"><img src="docs/testing/testcases/checkout-17.jpg"></h2>

    - Step 18a
    <h2 align="left"><img src="docs/testing/testcases/checkout-18a.jpg"></h2>

    - Step 18b
    <h2 align="left"><img src="docs/testing/testcases/checkout-18b.jpg"></h2>

    - Step 19a
    <h2 align="left"><img src="docs/testing/testcases/checkout-19a.jpg"></h2>

    - Step 19b
    <h2 align="left"><img src="docs/testing/testcases/checkout-19b.jpg"></h2>

    - Step 20a
    <h2 align="left"><img src="docs/testing/testcases/checkout-20a.jpg"></h2>

    - Step 20b
    <h2 align="left"><img src="docs/testing/testcases/checkout-20b.jpg"></h2>

    - Step 21
    <h2 align="left"><img src="docs/testing/testcases/checkout-21.jpg"></h2>

    - Step 22
    <h2 align="left"><img src="docs/testing/testcases/checkout-22.jpg"></h2>

    - Step 23
    <h2 align="left"><img src="docs/testing/testcases/checkout-23.jpg"></h2>
    
    - Step 24
    <h2 align="left"><img src="docs/testing/testcases/checkout-24.jpg"></h2>

    - Step 25
    <h2 align="left"><img src="docs/testing/testcases/checkout-25.jpg"></h2>

---

#### Sign Up (Register) Page

<h2 align="left"><img src="docs/testing/testcases/register-03.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-07-register-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-07-register-2.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-07-register-3.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/register-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/register-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/register-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/register-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/register-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/register-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/register-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/register-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/register-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/register-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/register-12.jpg"></h2>

    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/register-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/register-14.jpg"></h2>

    - Step 15
    <h2 align="left"><img src="docs/testing/testcases/register-15.jpg"></h2>

    - Step 16
    <h2 align="left"><img src="docs/testing/testcases/register-16.jpg"></h2>

    - Step 17
    <h2 align="left"><img src="docs/testing/testcases/register-17.jpg"></h2>

    - Step 18
    <h2 align="left"><img src="docs/testing/testcases/register-18.jpg"></h2>

    - Step 19a
    <h2 align="left"><img src="docs/testing/testcases/register-19a.jpg"></h2>

    - Step 19b
    <h2 align="left"><img src="docs/testing/testcases/register-19b.jpg"></h2>

    - Step 20
    <h2 align="left"><img src="docs/testing/testcases/register-20.jpg"></h2>

    - Step 21
    <h2 align="left"><img src="docs/testing/testcases/register-21.jpg"></h2>

    - Step 22
    <h2 align="left"><img src="docs/testing/testcases/register-22.jpg"></h2>

    - Step 23
    <h2 align="left"><img src="docs/testing/testcases/register-23.jpg"></h2>

    - Step 24
    <h2 align="left"><img src="docs/testing/testcases/register-24.jpg"></h2>

---

#### Sign In (Login) Page

<h2 align="left"><img src="docs/testing/testcases/login-03.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-08-login-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-08-login-2.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-08-login-3.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/login-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/login-03.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/login-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/login-06.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/login-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/login-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/login-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/login-12.jpg"></h2>

    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/login-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/login-14.jpg"></h2>

    - Step 16
    <h2 align="left"><img src="docs/testing/testcases/login-16.jpg"></h2>

    - Step 17
    <h2 align="left"><img src="docs/testing/testcases/login-17.jpg"></h2>

    - Step 18
    <h2 align="left"><img src="docs/testing/testcases/login-18.jpg"></h2>

    - Step 19
    <h2 align="left"><img src="docs/testing/testcases/login-19.jpg"></h2>

    - Step 20
    <h2 align="left"><img src="docs/testing/testcases/login-20.jpg"></h2>

    - Step 21
    <h2 align="left"><img src="docs/testing/testcases/login-21.jpg"></h2>

    - Step 22
    <h2 align="left"><img src="docs/testing/testcases/login-22.jpg"></h2>

    - Step 23
    <h2 align="left"><img src="docs/testing/testcases/login-01.jpg"></h2>

---

#### Profile Page

Due to having exceeded 85% of the monthly usage limit for the S3 AWS Free Tier in one week, the rest of the testing will be carried out on Localhost rather than on Heroku.

<h2 align="left"><img src="docs/testing/testcases/profile-05.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-09-profile-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-09-profile-2.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-09-profile-3.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-09-profile-4.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/profile-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/profile-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/profile-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/profile-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/profile-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/profile-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/profile-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/profile-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/profile-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/profile-11.jpg"></h2>
    
    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/profile-12.jpg"></h2>
    
    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/profile-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/profile-14.jpg"></h2>

    - Step 15
    <h2 align="left"><img src="docs/testing/testcases/profile-15.jpg"></h2>

    - Step 16
    <h2 align="left"><img src="docs/testing/testcases/profile-16.jpg"></h2>

    - Step 17
    <h2 align="left"><img src="docs/testing/testcases/profile-17.jpg"></h2>

    - Step 18
    <h2 align="left"><img src="docs/testing/testcases/profile-18.jpg"></h2>

    - Step 19
    <h2 align="left"><img src="docs/testing/testcases/profile-19.jpg"></h2>

    - Step 20
    <h2 align="left"><img src="docs/testing/testcases/profile-20.jpg"></h2>

    - Step 21
    <h2 align="left"><img src="docs/testing/testcases/profile-21.jpg"></h2>
    
    - Step 22
    <h2 align="left"><img src="docs/testing/testcases/profile-22.jpg"></h2>
    
    - Step 23
    <h2 align="left"><img src="docs/testing/testcases/profile-23.jpg"></h2>

    - Step 24
    <h2 align="left"><img src="docs/testing/testcases/profile-24.jpg"></h2>

    - Step 25
    <h2 align="left"><img src="docs/testing/testcases/profile-25.jpg"></h2>

    - Step 26
    <h2 align="left"><img src="docs/testing/testcases/profile-26.jpg"></h2>

    - Step 27
    <h2 align="left"><img src="docs/testing/testcases/profile-27.jpg"></h2>

    - Step 28
    <h2 align="left"><img src="docs/testing/testcases/profile-28.jpg"></h2>

    - Step 29
    <h2 align="left"><img src="docs/testing/testcases/profile-29.jpg"></h2>

    - Step 30
    <h2 align="left"><img src="docs/testing/testcases/profile-30.jpg"></h2>

    - Step 31
    <h2 align="left"><img src="docs/testing/testcases/profile-31.jpg"></h2>
    
    - Step 32
    <h2 align="left"><img src="docs/testing/testcases/profile-32.jpg"></h2>
    
    - Step 33
    <h2 align="left"><img src="docs/testing/testcases/profile-33.jpg"></h2>

    - Step 34
    <h2 align="left"><img src="docs/testing/testcases/profile-34.jpg"></h2>

    - Step 35
    <h2 align="left"><img src="docs/testing/testcases/profile-35.jpg"></h2>

---

#### Product Management: Product Add Page (ADMIN login)

<h2 align="left"><img src="docs/testing/testcases/productadd-03.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-10-productadd-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-10-productadd-2.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/productadd-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/productadd-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/productadd-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/productadd-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/productadd-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/productadd-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/productadd-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/productadd-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/productadd-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/productadd-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/productadd-12.jpg"></h2>
    
    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/productadd-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/productadd-14.jpg"></h2>

    - Step 15
    <h2 align="left"><img src="docs/testing/testcases/productadd-15.jpg"></h2>

---

#### Product Management: Product Edit Page (ADMIN login)

<h2 align="left"><img src="docs/testing/testcases/productedit-03.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-11-productedit-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-11-productedit-2.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/productedit-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/productedit-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/productedit-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/productedit-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/productedit-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/productedit-07.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/productedit-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/productedit-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/productedit-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/productedit-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/productedit-12.jpg"></h2>
    
    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/productedit-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/productedit-14.jpg"></h2>

    - Step 15
    <h2 align="left"><img src="docs/testing/testcases/productedit-15.jpg"></h2>

    - Step 16
    <h2 align="left"><img src="docs/testing/testcases/productedit-16.jpg"></h2>

---

#### Sign Out Page (Logout)

<h2 align="left"><img src="docs/testing/testcases/logout-03.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-12-logout-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-12-logout-2.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/logout-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/logout-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/logout-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/logout-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/logout-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/logout-06.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/logout-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/logout-09.jpg"></h2>

---

#### Subscribe to Newsletter Page

<h2 align="left"><img src="docs/testing/testcases/subscribe-04.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-13-subscribe-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-13-subscribe-2.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/subscribe-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/subscribe-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/subscribe-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/subscribe-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/subscribe-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/subscribe-06.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/subscribe-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/subscribe-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/subscribe-10.jpg"></h2>

    - Step 11
    <h2 align="left"><img src="docs/testing/testcases/subscribe-11.jpg"></h2>

    - Step 12
    <h2 align="left"><img src="docs/testing/testcases/subscribe-12.jpg"></h2>

    - Step 13
    <h2 align="left"><img src="docs/testing/testcases/subscribe-13.jpg"></h2>

    - Step 14
    <h2 align="left"><img src="docs/testing/testcases/subscribe-14.jpg"></h2>

    - Step 15
    <h2 align="left"><img src="docs/testing/testcases/subscribe-15.jpg"></h2>

    - Step 16
    <h2 align="left"><img src="docs/testing/testcases/subscribe-16.jpg"></h2>

    - Step 17
    <h2 align="left"><img src="docs/testing/testcases/subscribe-17.jpg"></h2>

    - Step 18
    <h2 align="left"><img src="docs/testing/testcases/subscribe-18.jpg"></h2>

    - Step 19
    <h2 align="left"><img src="docs/testing/testcases/subscribe-19.jpg"></h2>

    - Step 20
    <h2 align="left"><img src="docs/testing/testcases/subscribe-20.jpg"></h2>

---

#### Blog Pages

<h2 align="left"><img src="docs/testing/testcases/blog-04.jpg"></h2>

- Results

    <h2 align="left"><img src="docs/testing/testcases/testcase-14-blog-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/testcases/testcase-14-blog-2.jpg"></h2>

- Screenshots

    - Step 1
    <h2 align="left"><img src="docs/testing/testcases/blog-01.jpg"></h2>
    
    - Step 3
    <h2 align="left"><img src="docs/testing/testcases/blog-03.jpg"></h2>

    - Step 4
    <h2 align="left"><img src="docs/testing/testcases/blog-04.jpg"></h2>

    - Step 5
    <h2 align="left"><img src="docs/testing/testcases/blog-05.jpg"></h2>

    - Step 6
    <h2 align="left"><img src="docs/testing/testcases/blog-06.jpg"></h2>

    - Step 7
    <h2 align="left"><img src="docs/testing/testcases/blog-06.jpg"></h2>

    - Step 8
    <h2 align="left"><img src="docs/testing/testcases/blog-08.jpg"></h2>

    - Step 9
    <h2 align="left"><img src="docs/testing/testcases/blog-09.jpg"></h2>

    - Step 10
    <h2 align="left"><img src="docs/testing/testcases/blog-10.jpg"></h2>


---

[Test Case Template](https://www.guru99.com/download-sample-test-case-template-with-explanation-of-important-fields.html) provided by Thomas Hamilton on GURU99

---

## Code Validation

### HTML

0 errors and 1 warning were detected by [W3C](https://validator.w3.org/#validate_by_input) Validation for pages:

- [bag.html PDF report](docs/testing/validation/w3c-html-bag.pdf)

- [post_detail.html PDF report](docs/testing/validation/w3c-html-postdetail.pdf)
- [post_list.html PDF report](docs/testing/validation/w3c-html-postlist.pdf)

- [checkout_success.html PDF report](docs/testing/validation/w3c-html-checkoutsuccess.pdf)
- [checkout.html PDF report ](docs/testing/validation/w3c-html-checkout.pdf) <code> 1 warning</code>


- [index.html PDF report](docs/testing/validation/w3c-html-index.pdf)

- [add_product.html PDF report](docs/testing/validation/w3c-html-productadd.pdf)
- [edit_product.html PDF report](docs/testing/validation/w3c-html-productedit.pdf)
- [product_detail.html PDF report](docs/testing/validation/w3c-html-productdetail.pdf)
- [products.html PDF report](docs/testing/validation/w3c-html-products.pdf)

- [profile.html PDF report](docs/testing/validation/w3c-html-profile.pdf)

- [subscribe.html PDF report](docs/testing/validation/w3c-html-subscribe.pdf)

- [signup.html PDF report](docs/testing/validation/w3c-html-signup.pdf)
- [verification_sent.html PDF report](docs/testing/validation/w3c-html-verificationsent.pdf)
- [email_confirm.html PDF report](docs/testing/validation/w3c-html-emailconfirm.pdf)

- [login.html PDF report](docs/testing/validation/w3c-html-signin.pdf)
- [logout.html PDF report](docs/testing/validation/w3c-html-signout.pdf)

- [password_reset.html PDF report](docs/testing/validation/w3c-html-passwordreset.pdf)
- [password_reset_done.html PDF report](docs/testing/validation/w3c-html-passwordresetdone.pdf)
- [password_reset_from_key.html PDF report](docs/testing/validation/w3c-html-passwordresetkey.pdf)
- [password_reset_from_key_done.html PDF report](docs/testing/validation/w3c-html-passwordresetkeydone.pdf)

- [404.html PDF report](docs/testing/validation/w3c-html-404.pdf)
- [500.html PDF report](docs/testing/validation/w3c-html-500.pdf)

<h2 align="left"><img src="docs/testing/validation/w3c-html.jpg"></h2>

### CSS

0 errors and 0 warnings were detected by [Jigsaw (W3C)](https://jigsaw.w3.org/css-validator/#validate_by_input) Validation for:

- [base.css PDF report](docs/testing/validation/w3c-css-base.pdf)
- [blog.css PDF report](docs/testing/validation/w3c-css-blog.pdf)
- [checkout.css PDF report](docs/testing/validation/w3c-css-checkout.pdf)
- [profile.css PDF report](docs/testing/validation/w3c-css-profile.pdf)
- [subscribe.css PDF report](docs/testing/validation/w3c-css-subscribe.pdf)

<h2 align="left"><img src="docs/testing/validation/w3c-css.jpg"></h2>

### JavaScript and jQuery

0 errors and 7 warnings were detected by [JSHint](https://jshint.com/) for:

- [stripe_element.js PDF report](docs/testing/validation/js-stripeelement.pdf)
- [countryfield.js PDF report](docs/testing/validation/js-countryfield.pdf)
- [HTML jQuery PDF report ](docs/testing/validation/js-html-jquery.pdf) <code> 7 warnings</code>

<h2 align="left"><img src="docs/testing/validation/jshint.jpg"></h2>

### Python

0 errors and 5 warnings were detected by [CI Python Linter](https://pep8ci.herokuapp.com/) for: 

- custom_storages.py

<h2 align="left"><img src="docs/testing/validation/py-customstorages.jpg"></h2>

- manage.py

<h2 align="left"><img src="docs/testing/validation/py-manage.jpg"></h2>

- bag/
    - apps.py
    <h2 align="left"><img src="docs/testing/validation/py-bag-apps.jpg"></h2>

    - contexts.py
    <h2 align="left"><img src="docs/testing/validation/py-bag-contexts.jpg"></h2>

    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-bag-urls.jpg"></h2>

    - views.py
    <h2 align="left"><img src="docs/testing/validation/py-bag-views.jpg"></h2>

    - templatetags/bag_tools.py
    <h2 align="left"><img src="docs/testing/validation/py-bag-tools.jpg"></h2>

- blog/
    - admin.py
    <h2 align="left"><img src="docs/testing/validation/py-blog-admin.jpg"></h2>

    - apps.py
    <h2 align="left"><img src="docs/testing/validation/py-blog-apps.jpg"></h2>

    - models.py
    <h2 align="left"><img src="docs/testing/validation/py-blog-models.jpg"></h2>

    - tests.py
    <h2 align="left"><img src="docs/testing/validation/py-blog-tests.jpg"></h2>

    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-blog-urls.jpg"></h2>

    - views.py
    <h2 align="left"><img src="docs/testing/validation/py-blog-views.jpg"></h2>

- checkout/
    - admin.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-admin.jpg"></h2>

    - apps.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-apps.jpg"></h2>

    - forms.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-forms.jpg"></h2>

    - models.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-models.jpg"></h2>

    - signals.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-signals.jpg"></h2>

    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-urls.jpg"></h2>

    - views.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-views.jpg"></h2>

    - webhook_handler.py
    <h2 align="left"><img src="docs/testing/validation/py-checkout-webhookhandler.jpg"></h2>

    - webhooks.py  <code> 1 warning</code>
    <h2 align="left"><img src="docs/testing/validation/py-checkout-webhooks.jpg"></h2>

- click_collect/
    - settings.py  <code> 4 warnings</code>
    <h2 align="left"><img src="docs/testing/validation/py-clickcollect-settings.jpg"></h2>

    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-clickcollect-urls.jpg"></h2>

- home/
    - apps.py
    <h2 align="left"><img src="docs/testing/validation/py-home-apps.jpg"></h2>

    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-home-urls.jpg"></h2>

    - views.py
    <h2 align="left"><img src="docs/testing/validation/py-home-views.jpg"></h2>

- products/
    - admin.py
    <h2 align="left"><img src="docs/testing/validation/py-products-admin.jpg"></h2>

    - apps.py
    <h2 align="left"><img src="docs/testing/validation/py-products-apps.jpg"></h2>

    - forms.py
    <h2 align="left"><img src="docs/testing/validation/py-products-forms.jpg"></h2>

    - models.py
    <h2 align="left"><img src="docs/testing/validation/py-products-models.jpg"></h2>

    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-products-urls.jpg"></h2>

    - views.py
    <h2 align="left"><img src="docs/testing/validation/py-products-views.jpg"></h2>

    - widgets.py
    <h2 align="left"><img src="docs/testing/validation/py-products-widgets.jpg"></h2>

- profiles/
    - apps.py
    <h2 align="left"><img src="docs/testing/validation/py-profiles-apps.jpg"></h2>

    - forms.py
    <h2 align="left"><img src="docs/testing/validation/py-profiles-forms.jpg"></h2>

    - models.py
    <h2 align="left"><img src="docs/testing/validation/py-profiles-models.jpg"></h2>
    
    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-profiles-urls.jpg"></h2>

    - views.py
    <h2 align="left"><img src="docs/testing/validation/py-profiles-views.jpg"></h2>

- subscribe/
    - admin.py
    <h2 align="left"><img src="docs/testing/validation/py-subscribe-admin.jpg"></h2>

    - apps.py
    <h2 align="left"><img src="docs/testing/validation/py-subscribe-apps.jpg"></h2>

    - forms.py
    <h2 align="left"><img src="docs/testing/validation/py-subscribe-forms.jpg"></h2>

    - models.py
    <h2 align="left"><img src="docs/testing/validation/py-subscribe-models.jpg"></h2>

    - urls.py
    <h2 align="left"><img src="docs/testing/validation/py-subscribe-urls.jpg"></h2>

    - views.py
    <h2 align="left"><img src="docs/testing/validation/py-subscribe-views.jpg"></h2>

---

## Site Audit

### Desktop audits

Many of the audit issues are caused by use of third party frameworks and libraries e.g. Bootstrap, jQuery, FontAwesome, Stripe, etc. See the PDF reports for more details.

* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) average scores:

    <h2 align="left"><img src="docs/testing/audit/lighthouse-avg-desk.jpg"></h2>

    Full PDF reports:
    - [bag.html PDF report](docs/testing/audit/lighthouse-desk-bag.pdf)

    - [post_detail.html PDF report](docs/testing/audit/lighthouse-desk-postdetail.pdf)
    - [post_list.html PDF report](docs/testing/audit/lighthouse-desk-postlist.pdf)

    - [checkout_success.html PDF report](docs/testing/audit/lighthouse-desk-checkoutsuccess.pdf)
    - [checkout.html PDF report](docs/testing/audit/lighthouse-desk-checkout.pdf)

    - [index.html PDF report](docs/testing/audit/lighthouse-desk-index.pdf)

    - [add_product.html PDF report](docs/testing/audit/lighthouse-desk-addproduct.pdf)
    - [edit_product.html PDF report](docs/testing/audit/lighthouse-desk-editproduct.pdf)
    - [product_detail.html PDF report](docs/testing/audit/lighthouse-desk-productdetail.pdf)
    - [products.html PDF report](docs/testing/audit/lighthouse-desk-products.pdf)
    
    - [profile.html PDF report](docs/testing/audit/lighthouse-desk-profile.pdf)

    - [subscribe.html PDF report](docs/testing/audit/lighthouse-desk-subscribe.pdf)

    - [email_confirm.html PDF report](docs/testing/audit/lighthouse-desk-emailconfirm.pdf)
    - [login.html PDF report](docs/testing/audit/lighthouse-desk-login.pdf)
    - [logout.html PDF report](docs/testing/audit/lighthouse-desk-logout.pdf)
    - [password_reset_done.html PDF report](docs/testing/audit/lighthouse-desk-passwordresetdone.pdf)
    - [password_reset.html PDF report](docs/testing/audit/lighthouse-desk-passwordreset.pdf)
    - [password_reset_from_key.html PDF report](docs/testing/audit/lighthouse-desk-passwordresetkey.pdf)
    - [password_reset_from_key.html PDF report](docs/testing/audit/lighthouse-desk-passwordresetkeydone.pdf)
    - [signup.html PDF report](docs/testing/audit/lighthouse-desk-signup.pdf)
    - [verification_sent.html PDF report](docs/testing/audit/lighthouse-desk-verificationsent.pdf)

### Mobile audits

* [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview/) average scores:

    <h2 align="left"><img src="docs/testing/audit/lighthouse-avg-mob.jpg"></h2>

    Full PDF reports:
    - [bag.html PDF report](docs/testing/audit/lighthouse-mob-bag.pdf)

    - [post_detail.html PDF report](docs/testing/audit/lighthouse-mob-postdetail.pdf)
    - [post_list.html PDF report](docs/testing/audit/lighthouse-mob-postlist.pdf)

    - [checkout_success.html PDF report](docs/testing/audit/lighthouse-mob-checkoutsuccess.pdf)
    - [checkout.html PDF report](docs/testing/audit/lighthouse-mob-checkout.pdf)

    - [index.html PDF report](docs/testing/audit/lighthouse-mob-index.pdf)

    - [add_product.html PDF report](docs/testing/audit/lighthouse-mob-addproduct.pdf)
    - [edit_product.html PDF report](docs/testing/audit/lighthouse-mob-editproduct.pdf)
    - [product_detail.html PDF report](docs/testing/audit/lighthouse-mob-productdetail.pdf)
    - [products.html PDF report](docs/testing/audit/lighthouse-mob-products.pdf)
    
    - [profile.html PDF report](docs/testing/audit/lighthouse-mob-profile.pdf)

    - [subscribe.html PDF report](docs/testing/audit/lighthouse-mob-subscribe.pdf)

    - [email_confirm.html PDF report](docs/testing/audit/lighthouse-mob-emailconfirm.pdf)
    - [login.html PDF report](docs/testing/audit/lighthouse-mob-login.pdf)
    - [logout.html PDF report](docs/testing/audit/lighthouse-mob-logout.pdf)
    - [password_reset_done.html PDF report](docs/testing/audit/lighthouse-mob-passwordresetdone.pdf)
    - [password_reset.html PDF report](docs/testing/audit/lighthouse-mob-passwordreset.pdf)
    - [password_reset_from_key.html PDF report](docs/testing/audit/lighthouse-mob-passwordresetkey.pdf)
    - [password_reset_from_key.html PDF report](docs/testing/audit/lighthouse-mob-passwordresetkeydone.pdf)
    - [signup.html PDF report](docs/testing/audit/lighthouse-mob-signup.pdf)
    - [verification_sent.html PDF report](docs/testing/audit/lighthouse-mob-verificationsent.pdf)

---

## Compatibility

The majority of testing and validation was carried out on the Chrome browser with a Windows 10 desktop, but to ensure that a broad range of users can successfully use this site, it was also tested with other browsers in both desktop and mobile configuration.

- Chrome v.114
- Edge v.115
- Firefox v.106
- Safari v.13
- Opera v.99

The results are shown below in a testing matrix:

<h2 align="left"><img src="docs/testing/audit/compatibility.jpg"></h2>

The original Excel version created by Tim Nelson, can be found [here](https://github.com/TravelTimN/ci-milestone04-dcd/blob/main/app/testing/testing-ci-milestone04-dcd.xlsx).

---

## Bugs Found

1. Missing product images

    - When the site was first deployed to Heroku, the drinks product images were missing.

    <h2 align="left"><img src="docs/testing/bugs/bug-01-1.jpg"></h2>

    - Error message for ```href``` link: *This XML file does not appear to...*

    <h2 align="left"><img src="docs/testing/bugs/bug-01-2.jpg"></h2>

    - The images were incorrectly named in the products section of the Django Administration dashboard.

    <h2 align="left"><img src="docs/testing/bugs/bug-01-3.jpg"></h2>

    - Solved by correctly naming the images in Django Admin

    <h2 align="left"><img src="docs/testing/bugs/bug-01-soln.jpg"></h2>

2. Favicon not displaying on Heroku

    <h2 align="left"><img src="docs/testing/bugs/bug-02-1.jpg"></h2>

    - Heroku was returning a 404 response because it could not find the favicon on Amazon S3.

    <h2 align="left"><img src="docs/testing/bugs/bug-02-2.jpg"></h2>

    - Solved by moving the favicon into the root static folder.

    <h2 align="left"><img src="docs/testing/bugs/bug-02-soln.jpg"></h2>

3. Misaligned page titles and horizontal rules

    <h2 align="left"><img src="docs/testing/bugs/bug-03.jpg"></h2>

    - Solved by ensuring all titles were centred.

    <h2 align="left"><img src="docs/testing/bugs/bug-03-soln.jpg"></h2>

4. Future features for the app were visible

    - Some future features (new arrivals, clearance, deals) not required at the moment were still showing in the product manage section.

    <h2 align="left"><img src="docs/testing/bugs/bug-04.jpg"></h2>

    - Solved by adding CSS to not display those options.

    <h2 align="left"><img src="docs/testing/bugs/bug-04-soln.jpg"></h2>

5. No minimum text length for input fields

    - The card details form has no minimum text length rules for the phone number and address fields.

    <h2 align="left"><img src="docs/testing/bugs/bug-05-1.jpg"></h2>
    <h2 align="left"><img src="docs/testing/bugs/bug-05-2.jpg"></h2>

    - No action required. It was decided that for the real world there was no need to change this. For card payment validation, the user must input their correct address. An incorrect address is an indicator of an attempted fraudulent payment and the transaction will fail.

6. Missing form labels

    - During the Lighthouse audit, some form elements had missing labels which are useful for accessibility.

    <h2 align="left"><img src="docs/testing/bugs/bug-06.jpg"></h2>

    - Solved by adding aria labels.

    <h2 align="left"><img src="docs/testing/bugs/bug-06-soln.jpg"></h2>

7. Link does not have a discernible name

    - The Facebook icon on the red banner had no label.

    <h2 align="left"><img src="docs/testing/bugs/bug-07.jpg"></h2>

    - Solved by adding an aria label to the ```<a></a>``` tag

    <h2 align="left"><img src="docs/testing/bugs/bug-07-soln.jpg"></h2>

8. Colour contrast insufficient

    - The shade of blue originally used for text links was not dark enough to contrast against the site's white background.

    <h2 align="left"><img src="docs/testing/bugs/bug-08.jpg"></h2>

    - Solved by changing the link colour from Bootstrap's *info* shade to dark blue #00008b.

    <h2 align="left"><img src="docs/testing/bugs/bug-08-soln.jpg"></h2>

9. No label for *My Account* icon

    <h2 align="left"><img src="docs/testing/bugs/bug-09.jpg"></h2>

    - Solved by adding an aria label.

    <h2 align="left"><img src="docs/testing/bugs/bug-09-soln.jpg"></h2>

10. Issue with AUTH_PASSWORD_VALIDATORS setting

    <h2 align="left"><img src="docs/testing/bugs/bug-10.jpg"></h2>

    - During the Flake8 validation check, warnings were displayed for lines which were too long in settings.py. An attempt to fix this issue resulted in configuration errors.
    
    - Debug = True:
    <h2 align="left"><img src="docs/testing/bugs/bug-10-1.jpg"></h2>

    - Debug = False:
    <h2 align="left"><img src="docs/testing/bugs/bug-10-2.jpg"></h2>

    - Solved by returning the code back to it's original form and removing the line continuation slash.

    <h2 align="left"><img src="docs/testing/bugs/bug-10-soln.jpg"></h2>

---

## Known Issues

This error was removed by running the site on Chrome in Incognito mode.

<h2 align="left"><img src="docs/testing/bugs/bug-00.jpg"></h2>

Stack Overflow user [Chrostip Schaejn](https://stackoverflow.com/questions/72494154/a-listener-indicated-an-asynchronous-response-by-returning-true-but-the-messag) advised that this error was cause by various Chrome extensions.

---

# Automated Testing 

## Unit Testing Using ChatGPT

The interest in using **ChatGPT** from [OpenAI](https://openai.com/) for testing has been inspired by two recent demonstrations that I attended, one by Amazon with Code Whisperer and the other by Microsoft with Copilot. I am sure that these features will very soon become embedded in the developer's life. I was not going to include automated testing due to time constraints, but these tests were generated by ChatGPT in a matter of seconds without much input from me. Scary or mindblowingly amazing? I'll let you decide.

I decided to generate these tests for the Blog app files *models.py* and *urls.py*. The test code was added to the app's **test.py** file in this directory:

<h2 align="left"><img src="docs/testing/unittests/chatgpt-13.jpg"></h2>

### Conversation with ChatGPT

<h2 align="left"><img src="docs/testing/unittests/chatgpt-01.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-02.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-03.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-04.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-05.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-06.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-07.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-08.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-09.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-10.jpg"></h2>
<h2 align="left"><img src="docs/testing/unittests/chatgpt-11.jpg"></h2>

### Running the Tests

The tests were run by typing into the terminal:
```
python manage.py test blog
``` 

#### Test Result - PASSED

<h2 align="left"><img src="docs/testing/unittests/chatgpt-12.jpg"></h2>

---
