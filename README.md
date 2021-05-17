```
A
Project Report On
```
##### “ Profanity Filter ”

Submitted in partial fulfilment of the requirements for the award of

###### T.E in (Computer Engineering)

```
By
Ms. MRUNMAYI PADWAL (Roll No. 46)
Ms. BHAGYASHREE PATHAK (Roll No. 48)
Ms. MRUGAKSHI THAKARE (Roll No. 67)
Mr. DIVYESH VISHWAKARMA (Roll No. 73)
```
```
Under the guidance of
```
###### Prof. Aruna Kamble

```
DEPARTMENT OF COMPUTER ENGINEERING
BHARATI VIDYAPEETH’S COLLEGE OF ENGINEERING
Sector-7, C.B.D. Belapur,
Navi Mumbai- 400614
Academic Year 2020 – 2021
```

###### BHARATI VIDYAPEETH

###### COLLEGE OF ENGINEERING

```
SECTOR – 7 C. B. D. BELAPUR
NAVI MUMBAI – 400 614
```
##### CERTIFICATE

```
This is to certify that,
The project entitled “ PROFANITY FILTER ” is a bonafide work of the
following students, submitted to the University of Mumbai in partial
fulfillment of the requirement for the award of the degree of
Undergraduate in Computer Engineering.
```
```
ROLL NO NAME OF THE STUDENT
46 MRUNMAYI PADWAL
48 BHAGYASHREE PATHAK
67 MRUGAKSHI THAKARE
73 DIVYESH VISHWAKARMA
```
```
PRINCIPAL
(Dr. Sandhya
Jadhav)
```
```
Head of Department
Computer Engineering
(Dr. D. R. Ingle)
```
**GUIDE
(Prof.Aruna Kamble)**


##### Project Synopsis Report Approval for T.E.

This project synopsis report entitled Profanity Filter by Bhagyashree,

Mrugakshi, Mrunmayi, Divyesh, is approved for the degree of Computer

Engineering.

```
Examiners
1.-------------------------------------------------
```
```
2.-------------------------------------------------
```
Date:

Place:


##### ACKNOWLEDGEMENT

The project “Profanity Filter” is creative work of many minds. A proper
synchronization between individual is must for any project to be completed
successfully. One cannot imagine the power of the force that guides us all and
neither can we succeed without acknowledging it.
We would like to express our gratitude to Principal Dr. Sandhya Jadhav and Dr.
D.R. Ignle , our Head of the department, Computer Engineering for encouraging
and inspiring us to carry out the project in the department lab. We would also
like to thank our Guide Prof. Aruna Kamble, Department of the Computer
Engineering for her expert guidance, encouragement and valuable suggestions
at every step.
We also would like to thank all the staff members Department of the Computer
Engineering for providing us with the required facilities and support towards the
completion of the project.
Last but not the least we are thankful to our parents and friends for their
constant Inspiration, encouragement and well wishes by which we have made a
challenging project.


##### TABLE OF CONTENTS

SR.NO
CHAPTER
PAGE NO.

```
1.
Introduction
6
1.1 Background Study 8
1.2 Problem Statement 10
```
```
2.
Aim and Objectives
11
```
```
3.
Architecture
13
```
```
4.
Tools and Techniques
18
```
```
5.
Algorithms
23
```
```
6.
Implementation
25
```
```
7.
Observation & Results
85
```
```
8.
Future Scope
90
```
```
9.
Conclusion
92
```
```
10.
References
94
```

# CHAPTER 1

# INTRODUCTION


##### 1. INTRODUCTION

In the context of this work we define profanity, curse, swear or taboo words, as
words used with offensive or vulgar intentions. Although swearing can be studied
in the context of multiple disciplines, from the computational perspective, it is
commonly associated with the automatic identification of abusive comments.
Most often the intent of profanity identification lays on censoring these words
or posts, but profanity is also tightly related with sentiment analysis and opinion
mining tasks , since it can adequately express certain emotions, mostly
negative. Its use seems to depend on several factors, such as gender, age and
social class.
How common is cursing on-line? Most pages of 16 year olds on MySpace, and
about 15% of pages of middle-aged people contained strong swearing. 9.28%
of comments in Yahoo! Buzz showed profanity. Out of 51 million tweets
in English, at least 7.73% of messages contained cursing , where swear words
represented 1.15% of all words seen — as frequent as first person plural pronouns
(we, us, our).

While profanity is a common occurrence on-line, correct spelling is not. Curse
words are not always written in the same way, a consequence of their use and
spread being more oral than written. Graphical diversity is also augmented by ac-
cidental misspellings or intended obfuscations.

Negative content can be problematic for sites wanting to expand their user base,
engage existing users, and foster a positive and collaborative community. Social
contracts and normative behaviors, however, are unique to specific socio-technical
systems. What is considered inappropriate in a given context is both site and
community specific. On many sites, community managers are primarily responsible
for the task of removing inappropriate content. However, the flood of user-generated
content on many sites quickly overwhelms community managers’ ability to
effectively manage it.


1.1 Background Study :

As more and more of the web has grown to include user-generated content, the
detection and management of inappropriate or objectionable content has
become an important task for web sites. One common technique is social
moderation, in which users themselves undertake the task of identifying and
flagging of profane or inappropriate responses. However these systems have
been only moderately successful, and suffer from potential collusion - flagging
can be used to indicate disagreement or dislike of a post that is not otherwise
inappropriate or profane. Instead of relying on social moderation, recent
proposals have been made to automate the detection of inappropriate or
abusive content.

Research in computer vision has given much attention to the related issue of
detecting inappropriate videos and images. Advances in this space have
largely included systems that detect “too much skin” in images and videos.
Other systems utilize textual metadata, while some combine the two; one such
system, WebGuard has reached 97.4% accuracy in detecting pornographic
web sites.

While many would argue that textual analysis is more tractable than visual
content analysis, this may be in part because of a general misunderstanding
about how difficult the problem of profanity detection is in real-world
contexts. Furthermore, text has a visual element that is socially understood.
Expressive forms such as emoticons and “ASCII art” use visual properties of
text, punctuation marks and symbols to mimic lexical units and thus convey
meaning, denote profanity and circumvent automatic filters. Such visual-for-
textual substitution is best illustrated through examples such as the use of “@”
in “@ss”.

Because of these misunderstandings, perhaps, comparatively little research has
focused on detecting inappropriate text in user-generated content systems. As
mentioned above, two groups have built systems to detect insults and
harassment in online forums and another has focused on cyberbullying of
teens, but even fewer have addressed the identification of profanity. Yoon et
al. built a system to detect newly coined profanities in Korean, in an attempt to
improve upon the failure of list-based systems to evolve along with profane
language. Due to the target audience being children, some have analyzed the
content of video game web sites and video games themselves to verify that
presented content meets ratings standards. However, work in this area does not
generally strive for automated analysis. Advancing our ability to detect and
remove profanity could have several significant, positive social consequences.
The growth of collaborative information products such as Wikipedia, Yahoo!


Answers, and Stack Overflow rely on the provision of interaction
environments that are supportive, productive, and meet the specific needs of
their user communities. Open-source software projects also rely on email lists
and forums to support the necessary community building, coordination, and
decision-making processes.

No automated system, by itself, can appropriately filter and manage ongoing
discourse and interaction so that it meets the needs of a particular topic,
domain, or user community. Indeed, research has illustrated the important role
of established community members for implicitly and explicitly
communicating language norms to new members. The enforcement of these
norms is often ad hoc, however. In large systems, the sheer volume of content
means ad hoc strategies often leave a large amount of profane or inappropriate
user-generated content undetected. The existence of such content can actually
fight against the positive influence of community managers and long-time
participants by setting a bad precedent that communicates to new users that
profanity and other negative content is acceptable [21]. Automated systems
that help community managers, moderators, and administrators to manage the
flood of user-generated content in these environments could help to promote
more productive large-scale collaboration and thus more valuable information
products.


1.2 Problem Statement :

1. TEXT
A profanity search and replace method. Returns the number of profane words
found and the submitted text with profane words replaced with symbol
provided. If the text is clean 0 (zero) is returned.

Arguments:
api_key (Required)
Your API application key.

text (Required)
The text you want checked for profanity.

replacesymbol (Required)
The symbol you want to replace each letter of the profane word with.

2. IMAGE
Our solution can be used to moderate or filter any web-hosted photo including
avatars, profile pictures, contest entries, photo album pics, etc.

By submitting the URL of the image, which consists of profane text, we return
the same image by blurring / by replacing the text in the image which contains
profane text by symbols.


# CHAPTER 2

# AIM & OBJECTIVE


##### 2. AIM & OBJECTIVE

###### Aim

To filter out profane, obscene and other unwanted content.

###### Objective

As user-generated Web content increases, the amount of inappropriate and/or objectionable
content also grows. Several scholarly communities are addressing how to detect and manage
such content: research in computer vision focuses on detection of inappropriate images,
natural language processing technology has advanced to recognize insults. However,
profanity detection systems remain flawed. Current list-based profanity detection systems
have two limitations. First, they are easy to circumvent and easily become stale–that is, they
cannot adapt to misspellings, abbreviations, and the fast pace of profane slang evolution.
Secondly, they offer a one-size fits all solution; they typically do not accommodate domain,
community and context specific needs. However, social settings have their own normative
behaviors–what is deemed acceptable in one community may not be in another. In this paper,
through analysis of comments from a social news site, we provide evidence that current
systems are performing poorly and evaluate the cases on which they fail. We then address
community differences regarding creation/tolerance of profanity and suggest a shift to more
contextually nuanced profanity detection systems.


# CHAPTER 3

# ARCHITECTURE


##### 3. ARCHITECTURE

The model schema explains the basic architecture of the project. The
architecture consists of 3 sections namely:

1. Profanity Text Filter Model Schema
2. Profane Image Filter Model Schema
3. API Model Schema

Let's discuss them in detail.

1. Profanity Text Filter Model Schema:

The model schema consists of the root called as the ProfaneList.
The profane list has 3 sub divisions:
a. Profane words
b. Date Created
c. Date Edited
Profane words when added newly to the database, first they are checked
that they are unique or not( non case sensitive). If they are unique then they are
automatically assigned date of Creation and Date of editing as the system date.


2. Profane Image Filter Model Schema:

The model schema for image consists of ProfaneImage as root.

The ProfaneImage has 3 sub divisions:

a. Image Input
b. Image Output
c. Date Edited
Similar to ext profanity filter model shema, this section takes one Input
Image and produces output. This model schema indirectly inherits from text
model schema. The date edited is the date of creation of the output image.


3. API Model Schema:

The API model schema consists of 2 things of which the root node is API
namely

a. Request
b. Response
c. Status
The request section keeps an account of the request that the api got from
the user.

The Response keeps an account of the response that has to be sent to the
user

The status represents the status of the request sent by the user

System Structure:

One can use the api to get results for the following things:

a. To filter just text
b. To filter just images
c. To filter both
Thus the system categorises requests in the following manner:


1. First The system identifies the type of request and categorises them as for
    images or for text or both. If the request type is valid the system returns a
    status response of 200 and proceeds to the next request or response cycle.
2. If the request is not of any of the above type then it returns either with
    404 , or no- response.


## CHAPTER 4

## TOOLS AND TECHNIQUES:


##### 4. TOOLS AND TECHNIQUES:

###### Tools:

Here’s a list of all the software tools used in the making of this project.

1. Python: Python is an interpreted high-level general-purpose programming
    language. Python's design philosophy emphasizes code readability with
    its notable use of significant indentation.
2. Django: Django is a Python-based free and open-source web framework
    that follows the model-template-views architectural pattern.
3. Niepage: Nicepage is a website builder software breaking limitations
    common for website builders with revolutionary freehand positioning.
    7000+ Free Templates
4. Bootstrap: Bootstrap is a free and open-source CSS framework directed at
    responsive, mobile-first front-end web development. It contains CSS- and
    JavaScript-based design templates for typography, forms, buttons,
    navigation, and other interface components.
5. Google Vision API: Derives Insights From Images With Google's
    Powerful Cloud Vision API.It has Innovative Machine Learning Products
    & Services for Developers & Data Scientists.
6. Pillow: Python Imaging Library is a free and open-source additional
    library for the Python programming language that adds support for
    opening, manipulating, and saving many different image file formats.
7. Heroku: Heroku is a cloud platform as a service supporting several
    programming languages. One of the first cloud platforms, Heroku has
    been in development since June 2007, when it supported only the Ruby
    programming language, but now supports Java, Node.js, Scala, Clojure,
    Python, PHP, and Go.
8. RapidAPI: RapidAPI's Enterprise Hub is an internal API Marketplace
    that is customized to match any company's brand, integrates seamlessly
    with internal systems.
9. LucidChart: Lucidchart is a web-based proprietary platform that allows
    users to collaborate on drawing, revising and sharing charts and diagrams.
10. Github: GitHub, Inc. is a provider of Internet hosting for software
    development and version control using Git. It offers the distributed


```
version control and source code management functionality of Git, plus its
own features.
```
###### Techniques:

There are several sub processes going on in the system altogether. So here are
the following significant processes that are running in the project’s system.

1. Filtering Profane Words From Text
2. Detecting and Blurring Profane words from an image
3. API request response handling.
Here is the detailed description and methodology of the process that are going
on.
1. Filtering Profane Words From Text:
Here’s the technique:
Explanation:
a. Initially all the profane words present in the database are imported
onto the views.py (the html response handling file)
b. Then the page loads and displays every element.
c. The page has an input field i the profanity text filter section of the
html page, which takes the input from the user.
d. Once the user inputs the data and clicks Check Profanity, then the
input data is read by the form fields named content and gets stored
in a variable.
e. Now the variable is converted into a list using the python method
“split()”
f. That list is then iterated over word to word. Then it categorises the
words as following types.
i. Only Alphanumeric Words
ii. Words with special symbol
g. Now it iterates over every alphanumeric word and checks if that
particular word is present in the database or not. If that word is in
the database then it is converted into stars and that starred word
replies the real word in the list at that same index. If the word is not
in the database then it's simply passed over and nothing is done to
that word.


```
h. If the word has some special symbols then that word is iterated
over each letter and checked if it makes a meaningful word or not,
if that word is present in the database then it is starred, else it is
passed and done with no changes at the exact same index.
i. The final list is then joined with spaces using the ‘.join()’ method.
And sent to the output field named context. The output then is
displayed to the user in the results box of text profanity.
```
2. Detecting and Blurring Profane words from an image:

Here’s the algorithm:

Explanation:

```
a. Initially the views.py loads the respective html page on the
browser.
b. In the image section of the webpage, the user needs to inputs
an image.
c. That imagefile is loaded onto the input field named filein
d. Then that image is loaded onto the google Vision Api
handler.
e. The vision api initially checks for the proper google
credentials and the api key.
f. If both the credentials and the api key is proper then an
image request is sent to google and a response is awaited,.
g. As soon as we get a positive response, we send a text
annotation request to google.
h. As we get the text annotation positive response, we store the
response in a variable same that was done in text profanity
filter
i. Then the Text profanity filter process runs. But instead of
staring out the word, we then generate a request to get the
coordinates of that word to google.
j. When we get the vertices of that word we crop that part of
the image.
k. Then we take the top left diagonal coordinate and bottom
right coordinate and pass it for the next process
```

```
l. When the diagonal vertices are passed to the pillow
library,then using the Gausian blur technique with a very
high radius, we blur that section of the image.
m. The final blurred section is then pasted on the initially
cropped image and the final output image is produced.(
Django keeps a track of dynamic nomenclature of the output
image file using the system date and time to name the output
image - So that every image has a unique name to avoid
overwriting)
n. Then the final image is passed out to the out-file variable and
displayed to the user as context of the webpage.
```
3. API request response handling.

This section handles all the requests among users, google and the
main server of the api. It also sends status reports.


# CHAPTER 5

# ALGORITHMS


##### 5. ALGORITHMS

###### TEXT FILTER:

1. Input a string from user
2. Store all the words of the string in a list
3. Make the words case-insensitive
4. Check if the word from the list is present in the database or not
5. If present, replace the characters of the word by “*”
6. Repeat step 4 until all the words from the list are checked
7. If the word is not present in the list, check if the word contains a special
    character or not
8. If it does, create a string variable “thatword’, and add all the characters
    (excluding special characters to the thatword).
9. If the value of thatword is present in the word and it is present in the
    database , then replace the letters of the word by “*”.
10 .Repeat the step 7,until all the words from the list are checked.
11. Join all the elements of the list into a string and return it

###### IMAGE FILTER:

1. Choose the Image to Upload
2. Read the image using Google cloud vision API
3. Request for TEXT_DETECTION for extracting the text
4. Store text annotations in a variable text
5. Convert the text into a list
6. Store the index of the profane word from the list in variable c
7. Using the index find the vertices of the bounding polygon of the profane
    word
8. Store the top-right x and y vertices and bottom-left x and y vertices of the
    bounding polygon in variables a1,a2,b1,b2 respectively
9. Using Pillow library, crop the image by passing the vertices a1,a2,b1,b2
10. Blur the cropped image
11. Paste the blurred image on the original image
12. Return the original image


# CHAPTER 6

# IMPLEMENTATION


##### 6. IMPLEMENTATION:

###### Main Process Flow Diagram:


Source Code:

Directory Structure:

Profanity_Filter:

| db.sqlite3

| list.txt

| manage.py

| README.md

|

+---cyber_bully_website

| | asgi.py

| | settings.py

| | urls.py

| | wsgi.py

| | __init__.py

| |

| \---__pycache__

| settings.cpython-39.pyc

| urls.cpython-39.pyc

| wsgi.cpython-39.pyc

| __init__.cpython-39.pyc

|

+---profanity_text

| | admin.py

| | apps.py

| | models.py

| | tests.py


| | urls.py

| | views.py

| | googleVision.py

| | __init__.py

| |

| +---migrations

| | | 0001_initial.py

| | | 0002_auto_20210417_2124.py

| | | __init__.py

| | |

| | \---__pycache__

| | 0001_initial.cpython-39.pyc

| | 0002_auto_20210417_2124.cpython-39.pyc

| | __init__.cpython-39.pyc

| |

| +---templates

| | \---profanity_text

| | Home.html

| | index.html

| | layout.html

| | save_cusswords.html

| |

| \---__pycache__

| admin.cpython-39.pyc

| models.cpython-39.pyc

| urls.cpython-39.pyc

| views.cpython-39.pyc


| __init__.cpython-39.pyc

|

+---profanity_text_api

| | admin.py

| | apps.py

| | models.py

| | tests.py

| | urls.py

| | views.py

| | __init__.py

| |

| +---migrations

| | | __init__.py

| | |

| | \---__pycache__

| | __init__.cpython-39.pyc

| |

| +---templates

| | \---profanity_text_api

| | API.html

| | index.html

| |

| \---__pycache__

| admin.cpython-39.pyc

| models.cpython-39.pyc

| urls.cpython-39.pyc

| views.cpython-39.pyc


| __init__.cpython-39.pyc

|

\---static

+---css

| API.css

| Home.css

| index.css

| nicepage.css

|

+---js

| jquery.js

| nicepage.js

|

\---media

image.jpg

favicon.ico

###### Settings.py

"""

Django settings for cyber_bully_website project.

Generated by 'django-admin startproject' using Django 3.1.6.

For more information on this file, see


https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see

https://docs.djangoproject.com/en/3.1/ref/settings/

"""

from pathlib import Path

import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production

# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = (Secret key hidden)

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [

'django.contrib.admin',

'django.contrib.auth',

'django.contrib.contenttypes',

'django.contrib.sessions',

'django.contrib.messages',

'django.contrib.staticfiles',

'profanity_text',

'profanity_text_api',

]

MIDDLEWARE = [

'django.middleware.security.SecurityMiddleware',

'django.contrib.sessions.middleware.SessionMiddleware',

'django.middleware.common.CommonMiddleware',

'django.middleware.csrf.CsrfViewMiddleware',

'django.contrib.auth.middleware.AuthenticationMiddleware',

'django.contrib.messages.middleware.MessageMiddleware',

'django.middleware.clickjacking.XFrameOptionsMiddleware',

]


ROOT_URLCONF = 'cyber_bully_website.urls'

TEMPLATES = [

{

'BACKEND': 'django.template.backends.django.DjangoTemplates',

'DIRS': [],

'APP_DIRS': True,

'OPTIONS': {

'context_processors': [

'django.template.context_processors.debug',

'django.template.context_processors.request',

'django.contrib.auth.context_processors.auth',

'django.contrib.messages.context_processors.messages',

],

},

},

]

WSGI_APPLICATION = 'cyber_bully_website.wsgi.application'

# Database


# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {

'default': {

'ENGINE': 'django.db.backends.sqlite3',

'NAME': BASE_DIR / 'db.sqlite3',

}

}

# Password validation

# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [

{

'NAME':
'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',

},

{

'NAME':
'django.contrib.auth.password_validation.MinimumLengthValidator',

},

{


'NAME':
'django.contrib.auth.password_validation.CommonPasswordValidator',

},

{

'NAME':
'django.contrib.auth.password_validation.NumericPasswordValidator',

},

]

# Internationalization

# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [

BASE_DIR/ "static",

]

# Media onfigurations

MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

###### Profanity_tex_website/urls.py:

"""cyber_bully_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

https://docs.djangoproject.com/en/3.1/topics/http/urls/

Examples:

Function views

1. Add an import: from my_app import views
2. Add a URL to urlpatterns: path('', views.home, name='home')

Class-based views

1. Add an import: from other_app.views import Home
2. Add a URL to urlpatterns: path('', Home.as_view(), name='home')


Including another URLconf

1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns: path('blog/', include('blog.urls'))

"""

from django.contrib import admin

from django.urls import include, path

# Static and media imports

from django.conf import settings

from django.conf.urls.static import static

# Url Patterns Here

urlpatterns = [

path('admin/', admin.site.urls),

path('profanity_text/', include('profanity_text.urls')),

path('profanity_text_api/', include('profanity_text_api.urls'))

] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG :

urlpatterns += static(settings.MEDIA_URL, document_root =
settings.MEDIA_ROOT)

Profanity_text/Templates/Profanity_Text/home.html

<!DOCTYPE html>

<html style="font-size: 16px;">


{% load static %}

<head>

<meta name="viewport" content="width=device-width, initial-scale=1.0">

<meta charset="utf-8">

<meta name="keywords" content="A faster and more efficient way to keep
user-generated content&nbsp;clean and safe.">

<meta name="description" content="">

<meta name="page_type" content="np-template-header-footer-from-plugin">

<title>Home</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-
beta3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-
eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwr
a6" crossorigin="anonymous">

<link rel="stylesheet" href="{% static 'css/nicepage.css' %}"
media="screen">

<link rel="stylesheet" href="{% static 'css/Home.css' %}" media="screen">

<script class="u-script" type="text/javascript" src="{% static 'js/jquery.js'
%}" defer=""></script>

<script class="u-script" type="text/javascript" src="{% static 'js/nicepage.js'
%}" defer=""></script>

<meta name="generator" content="Nicepage 3.11.0, nicepage.com">

<link id="u-theme-google-font" rel="stylesheet"
href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,4
00i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,600,600i,700,70
0i,800,800i">


<link id="u-page-google-font" rel="stylesheet"
href="https://fonts.googleapis.com/css?family=Lato:100,100i,300,300i,400,400i
,700,700i,900,900i">

<script type="application/ld+json">{

"@context": "http://schema.org",

"@type": "Organization",

"name": "",

"url": "index.html"

}</script>

<meta property="og:title" content="Home">

<meta property="og:type" content="website">

<meta name="theme-color" content="#478ac9">

<!-- <link rel="canonical" href="index.html"> -->

<meta property="og:url" content="index.html">

</head>

<body class="u-body u-overlap u-overlap-contrast"><header class="u-clearfix
u-grey-80 u-header u-header" id="sec-f45d"><div class="u-clearfix u-sheet u-
sheet-1">

<nav class="u-menu u-menu-dropdown u-offcanvas u-menu-1">

<div class="menu-collapse u-custom-font u-font-georgia" style="font-
size: 1.875rem; letter-spacing: 0px;">


<a class="u-button-style u-custom-left-right-menu-spacing u-custom-
padding-bottom u-custom-text-hover-color u-custom-top-bottom-menu-spacing
u-nav-link u-text-active-palette- 1 - base u-text-hover-palette- 2 - base" href="#">

<svg><use xmlns:xlink="http://www.w3.org/1999/xlink"
xlink:href="#menu-hamburger"></use></svg>

<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
xmlns:xlink="http://www.w3.org/1999/xlink"><defs><symbol id="menu-
hamburger" viewBox="0 0 16 16" style="width: 16px; height: 16px;"><rect
y="1" width="16" height="2"></rect><rect y="7" width="16"
height="2"></rect><rect y="13" width="16" height="2"></rect>

</symbol>

</defs></svg>

</a>

</div>

<div class="u-custom-menu u-nav-container">

<ul class="u-custom-font u-font-georgia u-nav u-unstyled u-nav-1"><li
class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-palette- 1 -
base u-text-hover-palette- 3 - light-2" href="{% url 'profanity_text:index' %}"
style="padding: 10px 30px;">Home</a>

</li><li class="u-nav-item"><a class="u-button-style u-nav-link u-text-active-
palette- 1 - base u-text-hover-palette- 3 - light-2" href="{% url
'profanity_text_api:index" style="padding: 10px 30px;">API</a>

</li></ul>

</div>

<div class="u-custom-menu u-nav-container-collapse">

<div class="u-black u-container-style u-inner-container-layout u-opacity
u-opacity-95 u-sidenav">


<div class="u-sidenav-overflow">

<div class="u-menu-close"></div>

<ul class="u-align-center u-nav u-popupmenu-items u-unstyled u-
nav-2"><li class="u-nav-item"><a class="u-button-style u-nav-link" href="{%
url 'profanity_text:index' %}" style="padding: 10px 40px;">Home</a>

</li><li class="u-nav-item"><a class="u-button-style u-nav-link" href="{% url
'profanity_text_api:index' %}" style="padding: 10px 40px;">API</a>

</li></ul>

</div>

</div>

<div class="u-black u-menu-overlay u-opacity u-opacity-70"></div>

</div>

</nav>

</div></header>

<section class="u-align-left u-clearfix u-image u-shading u-section-1"
id="sec-6147" data-image-width="1280" data-image-height="640">

<h1 class="u-custom-font u-font-georgia u-text u-text-1">ANTI-
PROFANE</h1>

<div class="u-align-center u-border-3 u-border-palette- 1 - dark-1 u-
container-style u-expanded-width u-group u-palette- 1 - light-3 u-group-1">

<div class="u-container-layout u-valign-middle-xl u-container-layout-1">

<h2 class="u-text u-text-2">A faster and more efficient way to keep user-
generated content&nbsp;clean and safe. </h2>

</div>

</div>


<h3 class="u-custom-font u-font-lato u-text u-text-body-alt-color u-text-
3">features :</h3>

<a href="https://nicepage.com/c/product-list-html-templates" class="u-
border-5 u-border-white u-btn u-btn-round u-button-style u-palette- 1 - light-1 u-
radius-6 u-text-black u-btn-1">API</a>

<a href="Home.html#sec-5cb6" data-page-id="92199917" class="u-border-
5 u-border-white u-btn u-btn-round u-button-style u-palette- 1 - light-1 u-radius- 6
u-text-black u-btn-2" target="_blank">

<span style="font-size: 1.25rem;">API <span style="font-size:
1.875rem;">

<span style="font-size: 2.25rem;"></span>

</span>

</span>

</a>

<a href="Home.html#sec-5cb6" data-page-id="92199917" class="u-border-
5 u-border-white u-btn u-btn-round u-button-style u-palette- 1 - light-1 u-radius- 6
u-text-black u-btn-3" target="_blank">PROFANITY fILTER<span style="font-
size: 1.25rem;">

<span style="font-size: 1.875rem;">

<span style="font-size: 2.25rem;"></span>

</span>

</span>

</a>

<a href="Home.html#sec-31f2" data-page-id="92199917" class="u-border-
6 u-border-custom-color-2 u-btn u-btn-round u-button-style u-palette- 1 - light- 2
u-radius-6 u-text-black u-btn-4">IMAGE MODERATION</a>


</section>

<section class="u-clearfix u-image u-shading u-section-2" id="sec-5cb6"
data-image-width="1280" data-image-height="640">

<div class="u-clearfix u-sheet u-valign-bottom-sm u-valign-middle-xl u-
sheet-1">

<div class="u-clearfix u-expanded-width-lg u-expanded-width-md u-
expanded-width-sm u-expanded-width-xl u-gutter-18 u-layout-wrap u-layout-
wrap-1">

<div class="u-layout">

<div class="u-layout-row">

<div class="u-align-left u-container-style u-layout-cell u-size-30 u-
white u-layout-cell-1">

<div class="u-container-layout u-valign-bottom-xs u-valign-top-lg u-
valign-top-xl u-container-layout-1">

<p class="u-text u-text-1">ENTER TEXT<span style="font-weight:
700;"></span>

</p>

<form action="/profanity_text/#scrollresult" method="post">

{% csrf_token %}

<div class="form-floating">

<textarea name="content" id="content" class="p-1 m-4"
placeholder="Leave a comment here" id="floatingTextarea" rows="20"
cols="60">{{ original }}</textarea>

<label for="floatingTextarea"></label>

</div>


<button type="submit" value="Check Profanity" class="btn btn-lg
btn-dark mx-4">Check Profanity</button>

</form>

</div>

</div>

<div class="u-container-style u-layout-cell u-size-30 u-layout-cell-2">

<div class="u-container-layout u-container-layout-2">

<h2 class="u-custom-font u-font-georgia u-text u-text-2"
id="scrollresult">PROFANITY FILTER<span style="font-weight:
700;"></span>

<br>

</h2>

<p class="u-text u-text-3">Converts profane text into Asterisk
(*)</p>

<div class="u-border-9 u-border-palette- 1 - base u-container-style u-
expanded-width-sm u-expanded-width-xs u-group u-white u-group-1">

<div class="u-container-layout u-container-layout-3">

<p class="u-text u-text-4" >FILTERED TEXT<span style="font-
weight: 700;"></span>

</p>

<h3>{{ result }}</h3>

</div>

</div>

</div>

</div>


</div>

</div>

</div>

</div>

</section>

<section class="u-clearfix u-image u-shading u-section-3" id="sec-31f2"
data-image-width="1280" data-image-height="640">

<div class="u-clearfix u-sheet u-valign-middle-md u-valign-middle-sm u-
sheet-1">

<div class="u-border-10 u-border-palette- 1 - base u-container-style u-
expanded-width-sm u-expanded-width-xs u-group u-shape-rectangle u-white u-
group-1">

<div class="u-container-layout u-container-layout-1">

<p class="u-text u-text-1">IMAGE AFTER MODERATION .......<br>

<br>

</p>

</div>

</div>

<div class="u-clearfix u-expanded-width-xs u-gutter-34 u-layout-wrap u-
layout-wrap-1">

<div class="u-layout">

<div class="u-layout-row">

<div class="u-container-style u-layout-cell u-palette- 1 - base u-shape-
rectangle u-size-60 u-layout-cell-1">


<div class="u-border-12 u-border-custom-color-3 u-container-layout
u-container-layout-2">

<p class="u-text u-text-2">

<span style="font-weight: 700;" class="u-text-body-
color">IMAGE MODERATION</span>

</p>

<p class="u-text u-text-3">INSERT IMAGE</p>

<a href="#" class="u-btn u-btn-round u-button-style u-hover-palette-
1 - light-2 u-palette- 1 - light-3 u-radius-6 u-btn-1">SUBMIT</a>

</div>

</div>

</div>

</div>

</div>

</div>

</section>

<footer class="u-align-left u-clearfix u-footer u-grey-80 u-footer" id="sec-
d02c"><div class="u-clearfix u-sheet u-sheet-1">

<p class="u-align-center u-text u-text-1">Copyright <span style="font-
size: 1.25rem;">

<span style="font-size: 1.5rem;"></span>

</span>Ⓒ Anti-Profane.All Rights Reserved.

</p>


</div></footer>

<section class="u-backlink u-clearfix u-grey-80">

<a class="u-link" href="https://nicepage.com/css-templates"
target="_blank">

<span>CSS Templates</span>

</a>

<p class="u-text">

<span>created with</span>

</p>

<a class="u-link" href="https://nicepage.com/html-website-builder"
target="_blank">

<span>Online HTML Editor</span>

</a>.

</section>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-
beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-
JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkL
tS3qm9Ekf" crossorigin="anonymous"></script>

</body>

</html>

Profanity_Text/admin.py

from django.contrib import admin

from .models import Cusslist


# Register your models here.

@admin.register(Cusslist)

class CusslistAdmin(admin.ModelAdmin):

list_display = ['cussword', 'created', 'edited']

search_fields = ['cussword']

###### Profanity_text/models.py

from django.db import models

# Create your models here.

class Cusslist(models.Model):

id = models.AutoField(primary_key=True)

cussword = models.CharField(max_length=100, unique=True)

created = models.DateTimeField(auto_now_add = True)

edited = models.DateTimeField(auto_now = True)

class Meta:

ordering = ['cussword']

def __str__(self):

return "Cusslist"


###### Profanity_Text/urls.py

from django.urls import path

from. import views

app_name = 'profanity_text'

# url patterns

urlpatterns = [

path("", views.index, name = 'index'),

path("cuss",views.save_cusswords,name='cuss'),

]

###### Profanity_Text/views.py

from django.shortcuts import render

from .models import Cusslist

import datetime

def convert_cuss_word_to_stars(a_word):

final_starred_word = "*" * len(a_word)

return final_starred_word

def check_for_special_character(a_word):

for j in a_word:

if j.isalpha()==False:


return True

def check_if_actually_a_cussword(a_word,cuss_words_list):

thatword=""

for k in a_word:

if k.isalpha()==True:

thatword+=k

if thatword in a_word and thatword in cuss_words_list:

return True

else:

return False

def check_special_character(a_string, cuss_words_list):

list_of_words_from_string = a_string.split()

for a_word in list_of_words_from_string:

if a_word.lower() in cuss_words_list:

list_of_words_from_string[list_of_words_from_string.index(a_word)]=convert
_cuss_word_to_stars(a_word)

else:


if check_for_special_character(a_word.lower())==True:

if
check_if_actually_a_cussword(a_word.lower(),cuss_words_list)==True:

list_of_words_from_string[list_of_words_from_string.index(a_word)] =
convert_cuss_word_to_stars(a_word)

return " ".join(list_of_words_from_string)

cuss_words_list=tuple(Cusslist.objects.all().values_list('cussword', flat=True))

# Create your views here.

def index(request):

result=""

user_input_string = ''

if request.method=="POST":

user_input_string = request.POST['content']

result = check_special_character(user_input_string, cuss_words_list)


context ={

"result":result,

"original": user_input_string

}

return render(request, 'profanity_text/Home.html', context)

def save_cusswords(request):

a_string = ""

if request.method == "POST":

a_string = request.POST['cuss']

list_of_cusswords = a_string.splitlines()

for a_word in list_of_cusswords:

a_cussword =
Cusslist.objects.create(cussword=a_word,created=datetime.datetime.now(),edite
d=datetime.datetime.now())

a_cussword.save()

return render(request,"profanity_text/save_cusswords.html")

###### Profanity_Text/Google Vision API.py

import os, io

from google.cloud import vision

# from google.cloud.vision import types

import pandas as pd


from PIL import Image,ImageFilter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'booming-coast-
313509 - bb494bed1251.json'

client=vision.ImageAnnotatorClient()

FILE_NAME= 'demoimage.jpg'

FOLDER_PATH=r'C:\Users\HP\Documents\miniproject_sem6'

with io.open (os.path.join(FOLDER_PATH,FILE_NAME),'rb') as image_file:

content=image_file.read()

image=vision.Image(content=content)

response=client.text_detection(image=image)

texts=response.text_annotations

print(texts)

a=(texts[0].description).split()

# print(a)

c=a.index("FOCUS")

# print(texts[c+1].bounding_poly)

# print(c)

# bounds=[]

a1=texts[c+1].bounding_poly.vertices[0].x


a2=texts[c+1].bounding_poly.vertices[0].y

b1=texts[c+1].bounding_poly.vertices[2].x

b2=texts[c+1].bounding_poly.vertices[2].y

ogimage=Image.open(r'C:\Users\HP\Documents\miniproject_sem6\demoimage.
jpg')

cropped_image=ogimage.crop((a1,a2,b1,b2))

# cropped_image.show()

blurred_image=cropped_image.filter(ImageFilter.GaussianBlur(radius=30))

ogimage.paste(blurred_image,(a1,a2,b1,b2))

ogimage.show()

###### static/Home.css

{% load static %}

.u-section-1 {

background-image: linear-gradient(0deg, rgba(0,0,0,0.3), rgba(0,0,0,0.3)),
url("/static/media/6f19c437ef861c3924cd28a85f71aaca7a8925c20a4a9fdd4465
69cf6aa3c893cb337d26d6397c7a0f852b352a3bdf7b947354c815aeb21b09ff7f_
1280.jpg");

min-height: 638px;

}

.u-section-1 .u-text-1 {


font-weight: 700;

margin: 143px calc(((100% - 1140 px) / 2) + 771px) 0 calc(((100% - 1140px) /
2) + -41px);

}

.u-section-1 .u-group-1 {

min-height: 56px;

background-image: none;

margin-top: 29px;

margin-bottom: 0;

}

.u-section-1 .u-container-layout-1 {

padding-left: 30px;

padding-right: 30px;

}

.u-section-1 .u-text-2 {

font-style: italic;

font-weight: normal;

margin: 0 -14px 0 -30px;

}

.u-section-1 .u-text-3 {

text-transform: uppercase;

font-weight: 700;

width: 171px;

margin: 39px auto 0;


}

.u-section-1 .u-btn-1 {

background-image: none;

font-size: 1.5rem;

font-weight: 700;

text-transform: none;

border-style: solid;

margin: 41px calc(((100% - 1140px) / 2) + -39px) 0 auto;

padding: 49px 139px 50px;

}

.u-section-1 .u-btn-2 {

background-image: none;

font-weight: normal;

text-transform: none;

font-size: 1rem;

margin: -119px auto 0 calc(((100% - 1140px) / 2) + 20px);

}

.u-section-1 .u-btn-3 {

border-style: solid;

font-weight: 700;

text-transform: uppercase;

font-size: 1.5rem;

background-image: none;

margin: -117px auto 0 calc(((100% - 1140px) / 2));


padding: 40px 49px 40px 48px;

}

.u-section-1 .u-btn-4 {

border-style: solid;

font-weight: 700;

text-transform: uppercase;

font-size: 1.5rem;

margin: -147px calc(((100% - 1140px) / 2) + 386px) 60px auto;

padding: 49px 35px 50px 33px;

}

@media (max-width: 1199px) {

.u-section-1 {

min-height: 847px;

}

.u-section-1 .u-text-1 {

width: auto;

margin-top: 269px;

margin-right: calc(((100% - 940px) / 2) + 562px);

margin-left: calc(((100% - 940px) / 2) + -34px);

}

.u-section-1 .u-group-1 {

min-height: 93px;

margin-top: 44px;


}

.u-section-1 .u-container-layout-1 {

padding-right: 38px;

}

.u-section-1 .u-text-2 {

width: auto;

margin-top: 9px;

margin-right: -48px;

}

.u-section-1 .u-text-3 {

margin-top: 60px;

}

.u-section-1 .u-btn-1 {

border-style: none;

text-transform: uppercase;

margin-top: 96px;

margin-right: calc(((100% - 940px) / 2) + -745px);

}

.u-section-1 .u-btn-2 {

border-style: solid;

font-weight: 700;

text-transform: uppercase;


font-size: 1.5rem;

margin-top: -185px;

margin-right: calc(((100% - 940px) / 2) + -33px);

margin-left: auto;

padding: 44px 143px 45px 141px;

}

.u-section-1 .u-btn-3 {

margin-top: -156px;

margin-left: calc(((100% - 940px) / 2) + -34px);

padding-top: 44px;

padding-bottom: 46px;

}

.u-section-1 .u-btn-4 {

margin-top: -157px;

margin-right: auto;

padding-top: 53px;

padding-right: 34px;

padding-bottom: 54px;

}

}

@media (max-width: 991px) {

.u-section-1 {

min-height: 1000px;

}


.u-section-1 .u-text-1 {

margin-top: 171px;

margin-right: calc(((100% - 720px) / 2) + 326px);

margin-left: calc(((100% - 720px) / 2) + -24px);

}

.u-section-1 .u-group-1 {

margin-top: 114px;

}

.u-section-1 .u-container-layout-1 {

padding-right: 30px;

padding-top: 0;

padding-bottom: 0;

}

.u-section-1 .u-text-2 {

margin-top: 0;

margin-right: 26px;

}

.u-section-1 .u-text-3 {

margin-top: -155px;

}

.u-section-1 .u-btn-1 {


margin-top: 543px;

margin-right: calc(((100% - 720px) / 2) + -9px);

padding-top: 0;

padding-bottom: 0;

}

.u-section-1 .u-btn-2 {

margin-top: -92px;

margin-right: calc(((100% - 720px) / 2) + -9px);

}

.u-section-1 .u-btn-3 {

margin-top: -481px;

margin-left: calc(((100% - 720px) / 2) + -24px);

}

.u-section-1 .u-btn-4 {

margin-top: 19px;

}

}

@media (max-width: 767px) {

.u-section-1 {

min-height: 982px;

}

.u-section-1 .u-text-1 {


margin-right: calc(((100% - 540px) / 2) + 151px);

margin-left: calc(((100% - 540px) / 2) + -24px);

}

.u-section-1 .u-group-1 {

margin-top: 96px;

}

.u-section-1 .u-container-layout-1 {

padding-left: 10px;

padding-right: 10px;

}

.u-section-1 .u-text-2 {

margin-left: -11px;

margin-right: -11px;

}

.u-section-1 .u-text-3 {

width: auto;

margin-top: -153px;

margin-right: calc(((100% - 540px) / 2) + 393px);

margin-left: calc(((100% - 540px) / 2) + -24px);

}

.u-section-1 .u-btn-1 {

margin-top: 539px;


margin-right: calc(((100% - 540px) / 2) + -17px);

}

.u-section-1 .u-btn-2 {

margin-right: calc(((100% - 540px) / 2) + -17px);

}

.u-section-1 .u-btn-3 {

margin-top: -491px;

margin-left: calc(((100% - 540px) / 2) + -24px);

}

.u-section-1 .u-btn-4 {

margin-top: 24px;

margin-left: calc(((100% - 540px) / 2) + 59px);

}

}

@media (max-width: 575px) {

.u-section-1 {

min-height: 932px;

}

.u-section-1 .u-text-1 {

margin-left: calc(((100% - 340px) / 2));

margin-right: calc(((100% - 340px) / 2));

}


.u-section-1 .u-group-1 {

margin-top: 24px;

}

.u-section-1 .u-text-2 {

margin-right: 6px;

margin-left: 0;

}

.u-section-1 .u-text-3 {

margin-top: 24px;

margin-right: calc(((100% - 340px) / 2) + 74px);

margin-left: calc(((100% - 340px) / 2) + 96px);

}

.u-section-1 .u-btn-1 {

margin-top: 391px;

margin-right: auto;

}

.u-section-1 .u-btn-2 {

margin-top: -46px;

margin-right: auto;

margin-left: calc(((100% - 340px) / 2) + 6px);

}


.u-section-1 .u-btn-3 {

margin-top: -494px;

margin-left: auto;

}

.u-section-1 .u-btn-4 {

margin-top: 12px;

margin-left: auto;

}

}.u-section-2 {

background-image: linear-gradient(0deg, rgba(0,0,0,0.3), rgba(0,0,0,0.3)),
url("/static/media/6f19c437ef861c3924cd28a85f71aaca7a8925c20a4a9fdd4465
69cf6aa3c893cb337d26d6397c7a0f852b352a3bdf7b947354c815aeb21b09ff7f_
1280.jpg");

background-position: 50% 50%;

}

.u-section-2 .u-sheet-1 {

min-height: 750px;

}

.u-section-2 .u-layout-wrap-1 {

margin-top: 60px;

margin-bottom: 59px;

}

.u-section-2 .u-layout-cell-1 {

min-height: 631px;


background-image: none;

}

.u-section-2 .u-container-layout-1 {

padding: 30px 0;

}

.u-section-2 .u-text-1 {

font-weight: 700;

font-size: 1.5rem;

margin: 0 394px 0 25px;

}

.u-section-2 .u-btn-1 {

border-style: solid;

font-size: 1.25rem;

background-image: none;

font-weight: normal;

margin: 444px auto 0 16px;

padding: 11px 22px 13px 20px;

}

.u-section-2 .u-layout-cell-2 {

min-height: 622px;

}

.u-section-2 .u-container-layout-2 {


padding: 30px;

}

.u-section-2 .u-text-2 {

font-weight: 700;

margin: -23px 91px 0 0;

}

.u-section-2 .u-text-3 {

font-size: 1.25rem;

margin: 39px 91px 0 0;

}

.u-section-2 .u-group-1 {

width: 561px;

min-height: 420px;

background-image: none;

margin: 44px -60px 0 auto;

}

.u-section-2 .u-container-layout-3 {

padding-left: 30px;

padding-right: 30px;

padding-top: 0;

}

.u-section-2 .u-text-4 {


font-size: 1.5rem;

font-weight: 700;

margin: 16px 286px 0 -7px;

}

@media (max-width: 1199px) {

.u-section-2 {

background-position: 49.33% 50%;

}

.u-section-2 .u-sheet-1 {

min-height: 771px;

}

.u-section-2 .u-layout-wrap-1 {

margin-top: 75px;

}

.u-section-2 .u-layout-cell-1 {

min-height: 654px;

}

.u-section-2 .u-text-1 {

width: auto;

margin-right: 299px;

margin-left: 20px;

}


.u-section-2 .u-btn-1 {

margin-top: 442px;

margin-left: 20px;

}

.u-section-2 .u-layout-cell-2 {

min-height: 513px;

}

.u-section-2 .u-text-2 {

margin-right: 0;

margin-left: 25px;

}

.u-section-2 .u-text-3 {

margin-top: 49px;

margin-right: 0;

}

.u-section-2 .u-group-1 {

width: 451px;

margin-top: 20px;

margin-left: 0;

margin-right: 0;

}


.u-section-2 .u-container-layout-3 {

padding-top: 30px;

padding-bottom: 30px;

}

.u-section-2 .u-text-4 {

margin-top: 21px;

margin-right: 21px;

}

}

@media (max-width: 991px) {

.u-section-2 .u-sheet-1 {

min-height: 507px;

}

.u-section-2 .u-layout-wrap-1 {

position: relative;

}

.u-section-2 .u-layout-cell-1 {

min-height: 657px;

}

.u-section-2 .u-text-1 {

margin-top: 13px;

margin-right: 196px;


margin-left: 13px;

}

.u-section-2 .u-btn-1 {

margin-top: 436px;

margin-left: 13px;

}

.u-section-2 .u-layout-cell-2 {

min-height: 657px;

}

.u-section-2 .u-text-3 {

margin-top: 20px;

margin-left: 25px;

}

.u-section-2 .u-group-1 {

width: 351px;

margin-top: 13px;

margin-right: -53px;

margin-left: auto;

}

.u-section-2 .u-text-4 {

margin-right: 151px;

}


}

@media (max-width: 767px) {

.u-section-2 .u-sheet-1 {

min-height: 1273px;

}

.u-section-2 .u-layout-wrap-1 {

margin-top: 135px;

margin-bottom: 0;

}

.u-section-2 .u-layout-cell-1 {

min-height: 100px;

}

.u-section-2 .u-layout-cell-2 {

min-height: 586px;

}

.u-section-2 .u-container-layout-2 {

padding-left: 0;

padding-right: 0;

}

.u-section-2 .u-text-2 {

width: auto;


margin-top: -703px;

margin-right: 35px;

margin-left: 10px;

}

.u-section-2 .u-text-3 {

width: auto;

margin-top: 0;

margin-right: 35px;

margin-left: 10px;

}

.u-section-2 .u-group-1 {

margin-top: 638px;

margin-right: initial;

margin-left: initial;

width: auto;

}

.u-section-2 .u-container-layout-3 {

padding-left: 10px;

padding-right: 10px;

}

.u-section-2 .u-text-4 {

width: auto;

margin-top: 19px;


margin-right: 133px;

margin-left: 11px;

}

}

@media (max-width: 575px) {

.u-section-2 .u-sheet-1 {

min-height: 1290px;

}

.u-section-2 .u-layout-wrap-1 {

width: 340px;

margin: 128px -9px 60px auto;

}

.u-section-2 .u-layout-cell-1 {

min-height: 624px;

}

.u-section-2 .u-text-1 {

margin-top: 0;

margin-right: 0;

margin-left: 9px;

}

.u-section-2 .u-btn-1 {

margin-left: 25px;


}

.u-section-2 .u-layout-cell-2 {

min-height: 178px;

}

.u-section-2 .u-text-2 {

margin-top: -765px;

margin-right: 25px;

margin-left: 0;

}

.u-section-2 .u-text-3 {

margin-top: 13px;

margin-right: 8px;

margin-left: -17px;

}

.u-section-2 .u-group-1 {

min-height: 495px;

margin-top: 671px;

margin-bottom: -372px;

width: auto;

margin-right: initial;

margin-left: initial;

}


.u-section-2 .u-text-4 {

margin-top: -22px;

margin-right: 119px;

margin-left: 0;

}

}.u-section-3 {

background-image: linear-gradient(0deg, rgba(0,0,0,0.3), rgba(0,0,0,0.3)),
url("/static/media/6f19c437ef861c3924cd28a85f71aaca7a8925c20a4a9fdd4465
69cf6aa3c893cb337d26d6397c7a0f852b352a3bdf7b947354c815aeb21b09ff7f_
1280.jpg");

background-position: 50% 50%;

}

.u-section-3 .u-sheet-1 {

min-height: 767px;

}

.u-section-3 .u-group-1 {

width: 1080px;

min-height: 656px;

margin: 42px -15px 0 auto;

}

.u-section-3 .u-container-layout-1 {

padding: 30px;

}

.u-section-3 .u-text-1 {


margin: 75px 84px 0 572px;

}

.u-section-3 .u-layout-wrap-1 {

width: 553px;

margin: -595px auto 60px 17px;

}

.u-section-3 .u-layout-cell-1 {

min-height: 569px;

background-image: none;

}

.u-section-3 .u-container-layout-2 {

padding: 30px;

}

.u-section-3 .u-text-2 {

font-size: 1.875rem;

font-weight: 600;

margin: 0 72px 0 35px;

}

.u-section-3 .u-text-3 {

margin: 313px 118px 0 -11px;

}


.u-section-3 .u-btn-1 {

border-style: none;

font-weight: 700;

font-size: 1.25rem;

background-image: none;

margin: 17px auto 0 -11px;

padding: 8px 33px;

}

@media (max-width: 1199px) {

.u-section-3 .u-sheet-1 {

min-height: 766px;

}

.u-section-3 .u-group-1 {

width: 863px;

min-height: 646px;

margin-top: 47px;

margin-right: 0;

}

.u-section-3 .u-text-1 {

width: auto;

margin-top: 71px;

margin-right: 17px;

margin-left: 422px;

}


.u-section-3 .u-layout-wrap-1 {

width: 470px;

margin-top: -620px;

margin-left: 0;

}

.u-section-3 .u-btn-1 {

margin-left: 0;

}

}

@media (max-width: 991px) {

.u-section-3 .u-sheet-1 {

min-height: 745px;

}

.u-section-3 .u-group-1 {

width: 672px;

min-height: 651px;

margin-top: 60px;

margin-right: -25px;

}

.u-section-3 .u-text-1 {

margin-top: 120px;

margin-right: -83px;


margin-left: 331px;

}

.u-section-3 .u-layout-wrap-1 {

width: 409px;

margin-top: -625px;

margin-bottom: 102px;

margin-left: -27px;

}

.u-section-3 .u-layout-cell-1 {

min-height: 617px;

}

.u-section-3 .u-text-2 {

width: auto;

margin-left: 14px;

margin-right: 14px;

}

.u-section-3 .u-text-3 {

margin-right: 145px;

}

}

@media (max-width: 767px) {

.u-section-3 .u-sheet-1 {


min-height: 1305px;

}

.u-section-3 .u-group-1 {

margin-top: 40px;

margin-right: initial;

margin-left: initial;

width: auto;

}

.u-section-3 .u-container-layout-1 {

padding-left: 10px;

padding-right: 10px;

}

.u-section-3 .u-text-1 {

margin-top: 22px;

margin-right: 130px;

margin-left: 96px;

}

.u-section-3 .u-layout-wrap-1 {

margin-top: -1226px;

margin-left: auto;

margin-bottom: 156px;

}


.u-section-3 .u-layout-cell-1 {

min-height: 569px;

}

.u-section-3 .u-container-layout-2 {

padding-left: 10px;

padding-right: 10px;

}

.u-section-3 .u-text-2 {

margin-right: 28px;

margin-left: 0;

}

.u-section-3 .u-text-3 {

width: auto;

margin-right: 134px;

margin-left: 0;

}

}

@media (max-width: 575px) {

.u-section-3 .u-sheet-1 {

min-height: 1317px;

}

.u-section-3 .u-group-1 {


margin-top: 636px;

width: auto;

margin-right: initial;

margin-left: initial;

}

.u-section-3 .u-text-1 {

margin-right: 26px;

margin-left: 0;

}

.u-section-3 .u-layout-wrap-1 {

margin-bottom: 60px;

margin-right: initial;

margin-left: initial;

width: auto;

}

.u-section-3 .u-layout-cell-1 {

min-height: 617px;

}

.u-section-3 .u-container-layout-2 {

padding-top: 0;

}

.u-section-3 .u-text-2 {


width: 231px;

margin-top: 41px;

margin-left: auto;

margin-right: auto;

}

.u-section-3 .u-text-3 {

margin-top: 272px;

margin-right: 51px;

margin-left: 14px;

}

}


### CHAPTER 7

### OBSERVATIONS AND RESULTS


#### 7. OBSERVATIONS AND RESULTS

###### Home Page :

###### Text Filter:


###### Image Filter:

###### Admin Panel:


###### Database:


###### Insert and Save an Element :

##### Search an Element:


# CHAPTER 8

# FUTURE SCOPE


##### 8. FUTURE SCOPE:

Following the conclusions drawn in this article, there are a few clear next steps with regard to
moving beyond listbased profanity detection systems, and tailoring systems for specific
communities.

First, since list-based profanity detection systems don’t suffice, future work involves building
profanity detection systems from a machine learning point of view that take into account the
context in which profane language is used. Learning the context, in addition to the actual
profane words, has a greater potential for robustness, enabling the system to stand up to
misspellings, disguised or partially censored words and evolving profane language. Similarly
relevance feedback can be used to adapt and improve the model over time.

Secondly, since we established that profanity use and tolerance is very specific to a
community, it is very clear that these systems will have to be developed or trained by each
community. Future work involves building toolkits that allow this sort of tailoring. The use of
Amazon Mechanical Turk and other low cost crowdsourcing mechanisms will prove crucial
in labeling profanity in data sets from each community in order to train these machine
learning systems.

Finally, we believe our results are most valuable as part of a larger investigation into the
social nature of profanity and negative content within specific domains and user
communities. In future studies we intend to extend our explorations of the social meanings of
profanity and its context-specific use through qualitative interviews and survey studies.
Furthermore, we expect that cross-site studies may be particularly revealing about the uses of
profanity and possible context-specific approaches for detecting it. In future work we hope to
compare and contrast multiple data sets that share a topical domain (e.g. politics) but are
drawn from several different sites.


# CHAPTER 9

# CONCLUSION


##### 9.CONCLUSION:

We had an aim to create a profanity filter API that will restrict the use of
profane words in texts or images for the user inputs. That will ultimately help us
to curb cyberbullying activities.

We used Python to create the backend of the project. And HTML, CSS,
Javascript for the front end.

With this project, we created an API to filter out profane, obscene and other
unwanted content. Hence, we achieved our aim successfully.


# CHAPTER 10

# REFERENCES


##### 10.REFERENCES:

➢ Profane Words List: https://www.cs.cmu.edu/~biglou/resources/
➢ Vision API Documentation: https://cloud.google.com/vision/docs

➢ Vision API Tutorials:
https://www.youtube.com/watch?v=xKvffLRSyPk&list=PL3JVwFmb_B
nSLFyVThMfEavAEZYHBpWEd

➢ Django Documentation: https://docs.djangoproject.com/en/3.2/


