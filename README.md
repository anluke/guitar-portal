![GuitarPortal](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/title.png?raw=true)

# WELCOME TO GUITAR PORTAL  


[View the live project here.](https://guitar-portal.herokuapp.com/)


This project was built for Code Institute's Portfolio 4 Assessment.

This project is a fictitious portal for famous guitar players and their signature guitars.
It's a great read but everyone's welcome to post their own stories about the guitars they own.  


![Mockup](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/mockup/mockup.png?raw=true)


* [Introduction](#introduction)

* [UX](#ux) 
    - User Stories
        -  First Time Visitor Goals
        -  Site Administrator Goals  
* [Layout](#layout)

    - Design
        - Colour scheme
        - Images
    - Wireframes
        - Ideas
        - Links to Wireframes
* [Features](#features)
    - Responsivity
        - Interactive elements
    - Sections / Pages
    - Features to add in future

* [Sections](#sections)

* [Technologies Used](#technologies-used) 
    - Languages Used
    - Frameworks, Libraries and Programs Used  

* [Testing](#testing)
    - Validation Testing
    - Manual Testing
    - Unresolved Bugs 

* [Deployment](#deployment)

* [Credits](#credits)


# Introduction

Guitar Portal is a fan-based page. The name is just 'portal' but it is a blog. The intro already tells you that this is a site that will cover guitar instruments.  
It enables the user to view the posts but not comment until they are registered. It also does not allow users to create posts or delete them.
And it also does not allow users to delete or update posts they did not create.


# UX

-   ### User stories 

    -   #### Site User

        1. As a Site User I'd like to register for an account and log in afterwards.
        2. As a Site User I'd like to view the list of created posts.
        3. As a Site User I'd like to Open a post and view it's contents.
        4. As a Site User I'd like to sign up for newsletter be that registered or guest without registering.
        5. As a Site User I'd like to view Latest Posts made by all site users.
        6. As a Site User I'd like to view comments and Views on Blog posts.
        7. As a Site User I'd like to view my log in status at Navbar.
        

    -   #### Site Administrator Goals
        1. As a Site Administrator I would like to be able to create, view, edit and delete bookings.    
        
    -   #### Guitar Portal User Stories

        As you can see below, all of the user stories are completed and they have all been tested as they were being implemented and through testing phase.
<!-- 
        ![Navbar-Logged](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/navbar-logged.png?raw=true) -->


# Layout
-   ### Design
    -   #### Colour Scheme
        -   The main colours in the website theme for header, background, footer and text labels are white, light gray, blue and black.
    -   #### Imagery
        -   As for Imagery I chose to go with the vivid pictures capturing the moment or just a good angle with the guitar, adding more meaning to the blog post. Photos chosen were 'Portrait' formats.

*   ### Wireframes
    -   #### Ideas
        -   I had an idea of building a blog or expanding on the blog created by Matt during 'I Think Therefore I Blog' lesson. However, I didn't feel like it was something I'd like to do, expand on already finished project. So I went with a Django project advised to me by my Mentor. I followed an idea from the Boostrapious template but adjusted it to my liking. The Template looks great and it comes with pleny of configuration that may not be necessary. However I was reluctant to start playing around with other files as I did not want to break the functionality of the site.

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


-  #### Interactive elements
    * Nav links for Home, Menu, Blog, About, My bookings, Signup, Login and Logout link.
    * Form input fields on signup, logout, update and delete posts.
    * Buttons - including form buttons (signup, login, logout, table booking, edit and delete posts buttons and page navigation buttons (when there is too many blog posts)

-   ### Features to add in future   
    -   #### I would like to add a notification pop up that shows up on screen when user logs in/logs out.
    -   #### I would like to add a possibility of deleting comments but only if you are an owner.
    -   #### I would like to add more options to the Sign In form and have Registration only be active once the user has verified their account through email address.
<br>

# Sections

## Navigation
![Navbar](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/navbar.png?raw=true)

Above is a Navbar that's constisting of Logo at, **LOGIN** & **SIGNUP** in the middle and **Home, Blog, About, Create** on the right hand side.

This is how **navbar** looks like when user is signed in:

![Navbar-Logged](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/navbar-logged.png?raw=true)

And also below is the display of site navbar when reduced with 'hamburger' menu. Navbar is fully responsive.

![Hamb-Nav-Open](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/hamb-nav-open.png?raw=true)


## Hero

![Hero](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/hero.png?raw=true)

## Home

<details><summary>Home Page Full (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/home-page-large.png?raw=true">
</details>  

- Site home page has a guitar for the hero image. A small button to scroll down a bit and a introduction.  
- Just below the hero and intro section there is a small banner with 'famous' quote. And below that we have our Latest Blogs. This is where they will appear as they're created.


## Banner

![Banner](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/side-banner.png?raw=true)  
A banner with the famous quote from Mr. Jimmy Page. It separates the Latest blog section and our Hero section.


## Latest Blogs:

![Latest Blog](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/latest%20blogs.png?raw=true)  

Latest Blog section that covers our latest created blogs. As they are created the list moves from left to right and updates accordingly.


## Newsletter section:

![Newsletter](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/newsletter.png?raw=true)

Here we can see our Newsletter section. User can input their email address and they should receive an introductionary email from our Site.

<details><summary>Email Received Proof (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/email-received.png?raw=true">
</details>  


## Footer

![Footer](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/footer.png?raw=true)  

Site footer is at the bottom of the page, featuring Company Name, Email & Social Media section.



## Blog

<details><summary>Blog Post Section (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/blog.png?raw=true">
</details>

Blog is the site where you can see all the blog posts, and make use of the Navigation bar to switch between slides if there's more then 3-4 blogs posted.

It has a category section that displays all the current 'Active' categories that the users selected and also latest posts on the top.

It also features the number of views by users that are logged in along with the number of comments aside.

<details><summary>Blog Post As Author/Owner (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/blog-post-author.png?raw=true">
</details>  

<details><summary>Blog Post As Non Owner (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/blog-post-nonauthor.png?raw=true">
</details>  

This shows that admin created the first post and can delete that one but he can't delete or update Jonathan's post.

An Admin account is just used a normal user and if it would be necessary to delete that post it can be done through Admin portal. Deletion from the portal is something we can expand this project down the line.


## Sign up Section

![Sign Up](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/signup.png?raw=true)

We have our three input forms for signing in. User needs to follow the guide provided under the input forms in order to successfully create an account. After he creates an account it automatically logs him in.


## Log in Section

![Log In](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/login.png?raw=true)

Similar to our Sign up form. It only has two input forms. Password and Username.


## About


And below is our About page. It only holds text and it's purpose is to educate user on the purpose of the site along with some information for the future projects, etc.

<details><summary>About Section (Click to View)</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/about.png?raw=true">
</details>


## Admin Section

And of course we have our Admin section. We need to access this section by going into 'SITE URL' and then just add **/admin/** at the end.

![Admin Logged](https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/LINKS/admin-logged.png?raw=true)



<br>


# Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://en.wikipedia.org/wiki/Python_(programming_language))
-   [JavaScript](https://en.wikipedia.org/wiki/JavaScript)

### Frameworks, Libraries, Programs & Packages Used
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
1. [Email JS:](https://www.emailjs.com/)
    - Send an email to the user or visiting guest when using 'Newsletter' submit form on our home page.
1. [Git:](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
1. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
1. [Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/)
    - To style the forms inside our Django app. Installed as a Django package.
1. [Tinymce4 Lite:](https://karansthr.gitlab.io/fosstack/how-to-set-up-tinymce-in-django-app/index.html)
    - WYSIWYG HTML Text Editor for 'Content' input form in our 'Create' tab.
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

Testing was constistent throughout the deployment especially with Python.

The W3C Markup Validator and W3C CSS Validator Services were used to validate every pagefor HTML and CSS of the project. The issue is that this project is using a template and if loaded directly via link from Heroku or via GitPod link it will throw many errors as can be seen below:

-   [W3C URI Validator](https://validator.w3.org/#validate_by_uri)    
    - <details><summary>HTML TEST</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/HTML-TEST-IMG/html.png?raw=true">
    </details>  

    HTML Summary tested without any Errors. There is a warning for my gallery. It is asking for heading elements but that whole section is filled with my pictures so I decided to leave it like that as it is not affecting functionality of my site and the TEST passed.  
<br>
    
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
    - <details><summary>CSS TEST</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/CSS-TEST-IMG/css.png?raw=true">
    </details>  
    CSS Summary tested without any errors. CSS did give warnings and when I looked into it they are just webkit tools. They are related to Google Fonts and vendor extension prefixes which will not affect the CSS performance. A lot of them have also been imported through Bootstrapious.

```
    -webkit-transition    |    -webkit-text-fill-color     |    -webkit-box-shadow     |    -webkit-text-decoration-skip-ink
```  

- [PEP8 Python Validation](http://pep8online.com/)  

    The only warnings Python gave was 'line-too-long' which I tried to fix in 'settings.py' file and other files and it did not look right and in some cases was breaking the page. I have decided to leave them in as they are not major issues:
    #### Accounts
    - <details><summary>urls.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Accounts/urls.png?raw=true">
    </details>  

    - <details><summary>views.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Accounts/views.png?raw=true">
    </details>  

    #### Guitarportal
    - <details><summary>settings.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Guitarportal/settings.png?raw=true">
    </details>  

    - <details><summary>urls.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Guitarportal/urls.png?raw=true">
    </details> 

    #### Marketing
    - <details><summary>admin.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Marketing/admin.png?raw=true">
    </details>  

    - <details><summary>models.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Marketing/models.png?raw=true">
    </details>  

    #### Posts
    - <details><summary>admin.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/admin.png?raw=true">
    </details>  

    - <details><summary>forms.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/forms.png?raw=true">
    </details>  

    - <details><summary>models.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/models.png?raw=true">
    </details>  

    - <details><summary>views.png</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Python/Posts/views.png?raw=true">
    </details>  
    <br>
- ### Lighthouse  
  
  Lighthouse was used to test Performance, Best Practices, Accessibility and SEO on Desktop. Snippet bellow:

    - <details><summary>Lighthouse Desktop Test</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/lighthouse/lighthouse_desktop.png?raw=true">
    </details>  

    - <details><summary>Lighthouse Mobile Test</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/lighthouse/lighthouse_mobile.png?raw=true">
    </details>  

    Due to outdated jQuery version and other files that came with 'Bootstrapious' there are slight discrepancies, but it's functional and the test passed.

<br>

-   [JSHINT JavaScript Validator](https://jigsaw.w3.org/css-validator/#validate_by_input)

    As I didn't write much JS, I can only post emailJS that I added to submit a newsletter request. Snippet below:
    The guide was followed by Code Institite's lesson on Email JS.

    - <details><summary>JSHINT</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/JavaScript/jshint%20test.png?raw=true">
    </details>  


- ### Manual Testing

    * The Signup, Login and Logout all working correctly.

    * All the internal links are working and bring the user to the right page on the website.

    * All the external links are working and bring the user to the right social media page by 
    opening a new browser tab.
    
    * The Categories Page shows the genres and guitar brands. It picks up new categories from created posts.

    * The newsletter submit form takes the email and sends the newsletter welcome email to the user. The don't have to be logged in to use that service.

    * The pagination system is working. It adds another page after 3 posts or so.

    * The comment form has no issues and it submits a new comment once the form is completed by a
        registered user. 

    * CRUD is working. User is able to create, read, update and and delete their own posts. Superuser is able to delete posts in the backend 'admin' area regardless of the level.

    * When switching between accounts, the 'views' icon is incrementing as it should be.

    * When comment is posted it also incremenets an icon on the latest page section and the actual blog post.

<br>

- ### Unresolved Bugs


    - <details><summary>Chrome Console</summary>
        <img src="https://github.com/anluke/guitar-portal/blob/main/README-IMAGES/TESTING-IMG/Console%20test/console.png?raw=true">
    </details>  

    Tested this feature few days ago just after successfully uploading to Heroku. I was told by one of the Tutors that it is most likely and issue between Heroku and Cloudinary Everything else seems to work so this is only error which does not seem to be affecting my site's functionality.


## Deployment

The site was deployed via Heroku.
1.  Log in to Heroku or create an account if required.
2.  Then, click the button labelled New from the dashboard in the top right corner and from the drop-down menu select Create New App.  You must enter a unique app name
3.  Next, select your region.
4.  Click on the Create App button.
5.  In your app go to Resources tab and add a Heroku Postgres database.
6.  The next page you will see is the project’s **Deploy Tab**. Click on the Settings Tab and scroll down to **Config Vars** and enter:
    *   **CLOUDINARY_URL** = your cloudinary key
    *   **DATABASE_URL** = the url of your heroku postgres database
    *   **SECRET_KEY** = a secret key for your app.
    *   **PORT = 8000**
    *   **DISABLE_COLLECTSTATIC = 1** during development and remove when deploying to production

7.  Scroll to the top of the page and now choose the Deploy tab.
8.  Select Github as the deployment method.
9.  Confirm you want to connect to GitHub.
10. Search for the repository name and click the connect button.
11. Scroll to the bottom of the deploy page and select preferred deployment type:
12. Click either Enable Automatic Deploys for automatic deployment when you push updates to Github.
13. Select the correct branch for deployment from the drop-down menu and click **Deploy Branch** for manual deployment.

NB: Ensure in Django settings, **DEBUG is False**, create a **Procfile** and save database and cloudinary urls and secret key to **env.py.**

## Credits

*   Bootstrapious template downloaded from [Bootstrapios.com](https://bootstrapious.com/)
*   MS4 Project Preparation & Planning from [Code Institute's YouTube Channel](https://www.youtube.com/watch?v=qAseQckru9o)
*   Got a lot of help in understanding Models, Views from [TheNetNinja YouTube Channel](https://www.youtube.com/watch?v=n-FTlQ7Djqc&list=PL4cUxeGkcC9ib4HsrXEYpQnTOTZE1x0uc)
*   [Just Django](https://www.youtube.com/c/JustDjango)helped me out greatly with understanding my Models and also template tags. I based my layout on his template but removed some things I did not need and accomodated for my purpose.
*   HERO image from: [PRS Guitars](https://prsguitars.com/)
*   Banner cover image with Quote [Wallpapercave](https://wallpapercave.com/wp/KARQiCN.jpg)
*   Gallery Image 1: James Hetfield [faceoffrockshow](https://www.faceoffrockshow.com/post/james-hetfield)
*   Gallery Image 2: Mark Tremonti [musicradar.com](https://www.musicradar.com/news/mark-tremonti-my-top-5-tips-for-playing-live)
*   Gallery Image 2: Dan Donegan [nme.com](https://www.nme.com/wp-content/uploads/2022/07/Disturbed-Dan-Donegan-696x442.jpg)
*   Gallery Image 3: Adam Dutkiewicz [loudwire.com](https://loudwire.com/killswitch-engage-adam-d-pandemic-depression-worst-year-my-life/)
*   Blog Story 1 video [Mark Tremonti](https://www.youtube.com/watch?v=xG6NctwsOxs)
*   Blog Story 2: video [James Hetfield](https://www.youtube.com/watch?v=1Eq9RVKT9XQ)
*   Blog Story 3: video [Dimebag Darrell](https://www.youtube.com/watch?v=p40B6-p5u8w&feature=emb_title)


## Special Thanks:

- To all the Tutors, especially Scott and Ger. They helped me out when I was badly stuck.
- Also want to thank my Mentor for his support and guidance and the material he sent that helped me get the better idea for this project.


## Plans for implementation

- Project was hard. I wanted to do so much more but I couldn't risk it as I was quite late to start with already.  
There is definitely room for improvement but I wanted to get at least a working MVP with CRUD implementation that looks nice and can be implemented down the line.
- I have learned a lot during this PP4.