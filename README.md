# PORTFOLIO PROJECT for ALX SE Africa

## app-Secrets

<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/app_logo.png" alt="app-Secret Logo" style="width: 100px;">

<strong>app-Secrets</strong> as envisaged is an online System that will be designed for users to note or write down certain occurrences or future plans they would love to keep secret and confidential. It is a simple app meant to fulfill the portfolio project requirements for ALX Software Engineering Foundational stage and may likely be used for fun purposes.

From this project, users will have little "Logged Out Experience" and the routes that can be assessed by the user or customer includes:

- The landing page
- The About page
- Login Page
- Registration Page
- Users' Profile

### DEVELOPMENT TOOLS

To develop this application, we have to state some tools that will be used for the software development:

- Django
- MySQL DBMS
- Bootstrap CSS library
- JQuery JavaScript library

First we will create a virtual environment where Django will be installed.

But we need to have Python and Virtual Environment installed

### Install virtual Environment

```shell
$ sudo apt update
$ sudo apt upgrade -y
$ sudo apt install virtualenv -y
```

### Creating a Virtual Environment

```shell
$ virtualenv .secrets
```

### Activating the virtual Environment

```shell
# on a unix based operating system

$ source .secrets/bin/activate
(.secrets) /home/nerd $

# on a windows based operating system
.secrets\Scripts\activate.bat
(.secrets) C:\Users\nerd>
```

### Deactivating a Virtual Environment

```shell
(.secrets) /home/nerd $ deactivate
```

### INSTALLING DEPENDENCIES

We have the following dependencies saved in a file called requirements.txt:

- asgiref==3.7.2
- crispy-bootstrap4==2023.1
- Django==4.2.9
- django-crispy-forms==2.1
- mysqlclient==2.2.4
- pillow==10.2.0
- sqlparse==0.4.4
- typing_extensions==4.9.0

> this was achieved using
>
> ```shell
> (.secrets) /home/nerd $ pip freeze > requirements.txt
> ```

To install all these requirements do the following:

- Activate the virtual environment

```shell
/home/nerd $ source .secrets/bin/activate

(.secrets) /home/nerd $
```

- Install the dependencies

```shell
(.secrets) /home/nerd $ pip install -r requirements.txt
```

### RUNNING THE APPLICATION
As regards this project, the completed and fully functional application will be hosted on a live server. But in the interim and at the time of writing the documentation, we will be running the application from the local or development machine and using `DEBUG = True` so as to see how the program goes

#### Starting The Application

<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/run_app.png" alt="Run Application Image">

#### Landing Page

<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/landing_page.png" alt="Application Landing Page Image">

The landing page can be accessed only in a logged out state. When the user is logged in, his/her profile becomes the index page.

#### About/Contact Page

<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/about.png" alt="About Page Image">
<br>
<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/contact.png" alt="Contact Page Image">

The About page and the contact page can be accessed both from the logged out scene or logged in scene.

#### Signup/Signin Page

<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/register.png" alt="Register Page Image">
<br>
<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/login.png" alt="Login Page Image">


#### Authenticated Page for Logged In Users

<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/logged_in.png" alt="Authenticated User Page Image">

When a user is successfully authenticated and logged in, his home page becomes the profile page with a list of all his secrets. The page is paginated also to go the last of first secrets as well as scroll through the lists of secrets page after page.


#### Adding A New Secret

<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/add_post.png" alt="Add Secret Image">
<br>
<img src="https://github.com/Sampul-CodeMine/app-secrets/blob/main/screenshots/post_added.png" alt="Secret Added Image">

To add a new secret, a user clicks on the New Secret from the menu bar, a page is displayed for you to enter the details of the secrets. When your entry is complete, click on the <b>Save Secret</b> button to save the secret and it will redirect you to your profile home page with a message that post is added.




---

### AUTHORS

> Dukeson Ehigboria - [Github](https://github.com/Sampul-CodeMine) / [Twitter](https://twitter.com/Sampul_CodeMine)
>

### License

Public Domain. No copy write protection.

