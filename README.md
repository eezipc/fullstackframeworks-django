
## Eezi Motorcycles
* Eezi Motorcycles is a site created for Code Institute Milestone 4.
* The main purpose of the site is to provide parts and accessories for a Motorcycle.
* A user can order any item in the store. (There is no need to create an account)
* A user can also register an account and then they are able to order an item and view their orders.
* A user can also register an account and then they are able to Create a profile, view their profile, Update their profile or Delete their profile.
* The site can also be maintained by a site manager. A manager can add new items to the store, update details on existing items or delete items from the store.
* A site main admin can do the same as a site manager as well as create user profiles, assign privileges and delete profiles or orders.

## Technologies
Django
Python
HTML
CSS
jquery
bootstrap
Postgrl

## Deployment
The deployed link for the site is: <https://eezimotorcycles.herokuapp.com/>


## User Experience(UX)

The site has multiple pages as outlined below:
* base.html - This page is the template for all other pages.
* basket.html - This is where a user can view items in their basket.
* checkout.html - This is where a user can pay for their products and checkout.
* confirmcheckout.html - This page provides a confirmation of a users booking.
* contact.html - This is where a user can use a contact form to email the company.
* edit_product.html - This is where an admin can edit an existing product.
* index.html - The main page giving an outline of the purpose of the site.
* new_product.html - This is where an admin can add a new product to the store.
* privacy.html - This is where a user can view the company privacy policy.
* shopping.html - This is where a user can view various products in the store.
* shopping_detail.html - This is where a user can view information about a single item.
* success.html - This is where a user is diverted to when subscribing or contacting the company.
* terms.html - This is where a user can view the company's terms and conditions.
* update_products.html - This is where a manager can update existing products in the store.
* userprofile.html - This is where a user can view, edit or delete their profile.
* allauth - This is where a user can register, login and reset their password.



## User goals

* As a customer, I want to be able to order a product without having to create an account.
* As a customer, I want to able to register an account.
* As a customer, I want to be able to view multiple or single products.
* As a customer, I want to be able to contact the company.
* As a customer, I want to be able to view, update or delete my profile.
* As a customer, I want to see all previous orders in my profile.
* As a customer, I want to see clearly see prices.
* As a customer, I want to see clearly see total prices in the basket before checkout.
* As a customer, I want to see special offers.
* As a customer, I want to search for products by filtering.
* As a customer, I want to be able to search for a product by name.
* As a customer, I want to be able to choose the quantity of items to buy.
* As a customer, I want to be able to add or remove items in the cart.
* As a customer, I want to be able to feel secure when entering payment information.
* As a customer, I want to receive an email when a profile is created.
* As a customer, I want to receive an email when an order is created.
* As a customer, I want to clearly see an outcome whether the order is successful or not.

* As a manager, I want to be able to create an account.
* As a manager, I want to be able easily log in or out.
* As a manager, I want to be able to reset a password.
* As a manager, I want to be able to receive an email when an account has been created.
* As a manager, I want to be able to view all customers order history.
* As a manager, I want to be able to edit or delete an existing product.
* As a manager, I want to be able to add a new product.



## Design choices

The design is simple with clear layouts providing easy access to order a product, contact the company and view all services and prices.


## Balsamiq

* Balsamiq mockups are in the folder called "Documentation".
* I kept quite close to the original plans. Although the project did grow as I started to build.

## Header and navigation bar

* There is a logo on the top left with link to home page. Visible on all screens.
* Menu resizes for small devices. 
* There is a search bar on this navbar.
* There is a second navbar that hides when the user scrolls. The menu is hidden on mobile.

## Home page (index.html)

* There is a carousel with links to parts, gear and accessories.
* There is a special offer carousel with links to various products.
* There are more links underneath to parts, gear and accessories.

## Products (shopping.html)

* This is where a user can view all or filtered products.

## Product (shopping_detail.html)

* Here a user can view a single product in more detail.
* A user can add the item or multiples of that item to the shopping basket.

## Basket (basket.html)

* A user can see items in the basket (if any)
* A user can continue to checkout or edit the basket or continue shopping.

## Checkout (checkout.html)

* A user can fill out their details and credit card info on the left side (desktop view)
* A user can view items in the basket on the right side (desktop view)
* A user can update quantity in the basket or delete items from the basket.
* A user can also continue shopping.
* A user also has an option to login or create an account to save the order details in their account.

## Confirmcheckout (confirmcheckout.html)

* A user can view details of their order
* A user can also continue shopping.

## Register

* The register page has a simple form for a user to create a user profile.

## Userprofile

* When a user creates a profile on the register page, they are automatically logged in and forwarded to the profile page.
* The user can view or update their profile.
* This page is only available to users who have created a profile and logged in.


## Login

* Contains a simple form with email address and password inputs
* Also contains an option to register

## Contact

* The form has the address and phone number on the side.
* The form contains five inputs; first name, last name, email, reason and message.
* The form uses formkeep.

## Success (success.html)

* This is a simple confirmation page that shows when a user books a service.

## Edit Product (edit_product.html)

* This page allows an admin to edit a product.
* This section is only available to registered admin users.

## New Product (new_product.html)

* This page allows an admin to add a new product.
* This section is only available to registered admin users.


## Footer

* The footer contains links to privacy, terms, contact, subscribe, register and login.
* The footer also contains social media icon links for Facebook & Twitter.
* The links change depending on whether a user is logged in.
* When not logged in, the footer shows the login and register links. When logged in, the footer shows the profile and logout links.
* The footer also contains a copyright notice.

## Future features

* I would have liked to add an Amazon or Ebay api to the site.
* I would also have liked to add multiple images for each product.

## Tools


* Gitpod - https://gitpod.ie/ - as a code editer and version control.
* Github - https://github.com/ - to share and store code 
* Heroku - https://heroku.com/ - for hosting the application and deployment
* MongoDB https://www.mongodb.com - database for the website

## Libraries and frameworks

* Bootstrap https://getbootstrap.com/ - for layout and responsive design
* Font Awesome - https://fontawesome.com - Icons
* emailJs - emailjs.com - App for the contact form.
* Datepicker - https://forum.webflow.com/t/simple-datepicker-100-working/73398 

## Languages

* HTML
* CSS
* Javascript
* Python 3.8

## Testing

* Site was tested on Windows 10 pc, 2 x android phones, iPhone 8, iPad mini, Android 10" tablet, Dell 13" laptop, Mac 13" laptop. 
* Site was tested on Chrome, Firefox, Edge, Canary, Safari.
* Site was also tested on Browserstack: www.browserstack.com
* Site was tested with https://validator.w3.org
* Site was tested by https://jigsaw.w3.org/css-validator/
* Python code was checked by http://pep8online.com/
* There are a few errors but the code seems fine. 

## Deployment

This application can run on Gitpod or Heroku

## Deploy to Heroku

1:  Create a requirements.txt file using the terminal command pip freeze > requirements.txt.

2:   Create a Procfile with the terminal command echo web: python app.py > Procfile.

3:  Type git add and git commit the new requirements and Procfile .

4:  Create a new app on the Heroku website by clicking the "New" button in your dashboard. Give it a name and set the region to Europe.

5:  From the heroku dashboard of your newly created application, click on "Deploy" > "Deployment method" and select GitHub.

6:  Confirm the linking of the heroku app to the correct GitHub repository.

7:   In the heroku dashboard for the application, click on "Settings" > "Reveal Config Vars".

8:  Set the following config vars:

Key 	Value
DEBUG 	FALSE
IP 	0.0.0.0
MONGO_URI 	mongodb+srv://<username>:<password>@doggiecluster.wtitg.mongodb.net/<dbname>?retryWrites=true&w=majority
PORT 	5000
SECRET_KEY 	<your_secret_key>

9:  In the heroku dashboard, click "Deploy".

10: In the "Manual Deployment" section, made sure the master branch is selected and then click "Deploy Branch".

11: The site is now successfully deployed.

## Credits
* 
## Media

* All images are provided by www.unsplash.com and www.pexels.com 
* Alot of the product images and text was taken from https://www.xlmoto.ie

## Code

* Most of the code was learnt from Youtube, Udemy and Le Wagon.
* The Code Institute lessons on Django were excellent. Although they had set a low standard.
* All credit for the videos must go to czk8780: https://github.com/ckz8780
* Got alot of help from stackexchange https://stackexchange.com/
* Some of the code for the back to top button came from here 
* Alot of inspiration from Bootstrap: https://www.getbootstrap.com
* Alot of help from W3Schools: https://www.W3Schools.com
