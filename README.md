![Battleship Banner](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/title.png?raw=true)

# WELCOME TO GUITAR PORTAL  


[View the live project here.](https://guitar-portal.herokuapp.com/)


This project was built for Code Institute's Portfolio 4 Assessment.

This project is a fictitious portal for famous guitar players and their signature guitars.  


![Mockup](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/mockup/mockup.png?raw=true)


* [Introduction](#introduction)

* [UX](#ux) 
    - User Stories
        -  First Time Visitor Goals
        -  Site Administrator Goals  
* [Layout](#layout)

    - Design
        - Colour scheme
        - Typography
        - Images
    - Wireframes
        - Discrepancy with Original Ideas
        - Links to Wireframes
* [Features](#features)
    - Responsivity
    - Interactive Elements
    - Features to add in future

* [Technologies Used](#technologies-used) 
    - Languages Used
    - Frameworks, Libraries and Programs Used  

* [Testing](#testing)
    - Testing User Stories from User Experience (UX) Section
    - Further Testing
    - Unresolved Bugs 

* [Deployment](#deployment)

* [Credits](#credits)


# Introduction

Guitar Portal is a fan based page. The name is just 'portal' but it is actually a blog. The intro already tells you that this is a site that will cover guitar instruments.  
It enables user to view the posts but not comment until they are registered. It also does not allow users to create posts or delete them.
And it also does not allow users to delete or update posts they did not create.


# UX

-   ### User stories 

    -   #### Site User

        1. As a Site User I'd like to register for an account and login afterward.
        2. As a Site User I'd like to View the list of created posts.
        3. As a Site User I'd like to Open a post and view it's contents.
        4. As a Site User I'd like to sign up for newsletter be that registered or guest without registering.
        5. As a Site User I'd like to View Latest Posts made by all site users.
        6. As a Site User I'd like to View Comments and Views on Blog posts.
        7. As a Site User I'd like to View my Login status at Navbar.
        

    -   #### Site Administrator Goals
        1. As a Site Administrator I would like to be able to create, view, edit and delete bookings.    
        

# Layout
-   ### Design
    -   #### Colour Scheme
        -   The main colours in the website theme for header, background, footer and text labels are white, light gray, blue and black.
    -   #### Imagery
        -   Imagery was chosen to go with the vivid pictures capturing the moment or just a good angle with the guitar, adding more meaning to the blog post. Photos chosen were 'Portrait' formats.

*   ### Wireframes
    -   #### Discrepancy with original ideas
        -   I had an idea of building a blog or expanding on the blog created by Matt during 'I Think Therefore I Blog' lesson. However I didn't feel like it was something I'd like to do, expand on already finished project. So I went with a Django project advised to me by my Mentor. I followed an idea from the Boostrapious template but adjusted it to my liking. Template looks great and it comes with pleny of configuration that may not be necessary. However I was reluctant to start playing around with other files as I did not want to break the functionality of the site.
    -   #### Links to Wireframes


        <details><summary>Desktop Wireframes</summary>

        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/desktop_home.png?raw=true">
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/blog_desktop.png?raw=true">
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/about_desktop.png?raw=true">
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/desktop_signup.png?raw=true">
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/desktop_login.png?raw=true">
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/create_desktop.png?raw=true">
        </details>
        <details><summary>Tablet Wireframes</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/tablet_home.png?raw=true">
        </details>
        <details><summary>Phone Wireframes</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/wireframes/phone_layout.png?raw=true">
        </details>


# Features

-   ### Responsivity

The application is responsive on all device sizes, thanks to the [Bootstrapious](https://bootstrapious.com/) (bootstrap4)
 theme. In mobile view there is a collapsible menu icon. All images, text labels, forms get appropriately resized.


-   ### Interactive elements
    -   #### Nav links for Home, Menu, Blog, About, My bookings, Signup, Login and Logout link.
    -   #### Form input fields on signup, logout, update and delete posts.
    -   #### Buttons - including form buttons (signup, login, logout, table booking, edit and delete posts buttons and page navigation buttons (when there is too many blog posts)

-   ### Features to add in future   
    -   #### I would like to add a dropdown list for registered users to acess their account-related activites like view bookings, login and logout.


# Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))

### Frameworks, Libraries & Programs Used
1. [Django:](https://www.djangoproject.com/)
    - The Python-based Django framework was used to set up the structure, functionalities,  data model and database of the website.
1. [Bootstrapious Template:](https://bootstrapious.com/)
    - Derived from Bootstrap 4. Bootstrap was used to assist with the responsiveness and styling of the website.
1. [Google Fonts:](https://fonts.google.com/)
    -    Used for Roboto Font.
1. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
1. [jQuery:](https://jquery.com/)
    - Originally used by my template. I am putting it on the list as it can be found within my files but I have not personally used it for this project.
1. [Javascript:](https://en.wikipedia.org/wiki/JavaScript)  
    - Used for loading Bootstrapious CSS Templates and to create Email JS and connect it to our 'Newsletter' button.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Balsamiq:](https://balsamiq.com/)
    - Balsamiq was used to create the wireframes during the design process.
1. [Lucidchart:](https://www.lucidchart.com/) was used to create the data model of the project .
    <details><summary>Data Model</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/data-model/data-model.png?raw=true">
    </details>   
1. [PostgreSQL:](https://www.postgresql.org/)
    - Used PostgreSQL as per instructions of CI lessons in PP4.
1. [Cloudinary:](https://cloudinary.com/)
    - I used cloudinary for cloud-based storage and partly for linking of my website images.
1. [Heroku:](https://www.heroku.com/)
    -  Heroku is used for the deployment and ultimate cloud-based storage of my application.


# Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every pagefor HTML and CSS of the project. The issue is that this project is using a template and if loaded directly via link from Heroku or via GitPod link it will throw many errors as can be seen below:

-   [W3C URI Validator](https://validator.w3.org/#validate_by_uri)    
    <details><summary>HTML Summary - Direct Link</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/HTML-TEST-IMG/html.png?raw=true">
    </details>  

    But if you use the HTML files directly from the project without Python template tags there are no Major problems. The issue here is with the template as it has too many files that are intertwined and removing them broke my code so many times that I had no other choice but to leave it. I don't like submitting a test like this but I have spent hours on this. I tried testing some stuff with Tutor help and they told me that it could also be Django's issue with the template..
    <details><summary>HTML Summary - Direct Link</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/HTML-TEST-IMG/html.png?raw=true">
    </details>  

-   [W3C URI Validator](https://validator.w3.org/#validate_by_uri)
    - See the [URI Validator Results](https://github.com/renatalantos/booking-system/tree/main/restaurant/documents/screenshots/html%20validation)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - See the [CSS Validator Results](https://github.com/renatalantos/booking-system/blob/main/restaurant/documents/screenshots/css%20validation/Jigsaw%20CSS%20Validator.JPG)
-   [Gitpod Pylint](https://pylint.org/)
    - See the [Gitpod Pylint Results](https://github.com/renatalantos/booking-system/tree/main/restaurant/documents/screenshots/pylint%20validation)    
