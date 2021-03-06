<h1 align="center">The Food House</h1>

[View the live project here.](http://recipe-flask-johnny.herokuapp.com/)

The recipe website where you can view recipes and add your own.
 
<h2 align="center"><img src="static/images/Food-House.png"></h2>

## User Experience (UX)

-   ### User stories

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to want to make sure that I get the information I want based on the site description.

        2. As a First Time Visitor, I want to be able to easily navigate throughout the site easily to find content I am looking for.

        3. As a First Time Visitor, I want to be able to sign up to be able to access the members area of the site.

        4. As a first time visitor, I want to be able to add my own content to the website.

        5. As a first time visitor, I want to be able to easily login and logout from the site.

        6. As a first time user, I want to be able to use the website on all devices.


    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to be able to view the list of recipes.

        2. As a Returning Visitor, I want to be able to view details of every recipe.

        3. As a Returning Visitor, I want to be able to sort them by title for easy access.

        4. As a Returning Visitor, I want to be able to search specific recipes based on a query.

        5. As a Returning Visitor, I want to have access to my posts.

        6. As a Returning Visitor, I want to be the only one who is able to edit/update or delete my own posts.

        7. As a Returning Visitor, I want to find community links.


-   ### Design
    -   #### Colour Scheme
        -   The two main colours used are green and white with a beige addition to the cards. The colour green was chosen since food is something assoiated with nature (green shades) and it blends well with the food images.
    -   #### Typography
        -   The Baskervilles font has been used for this website as it helps to read the recipes more clearly. 
    -   #### Imagery
        -   The background image has been carefully selected so as to grab the users attention to the food items.

*   ### Wireframes

    -   Home Page Wireframe - [View](static/images/Home.jpg)
    -   Login Page Wireframe - [View](static/images/Login.jpg)
    -   Registration Page Wireframe - [View](static/images/Register.jpg)
    -   My Profile Page Wireframe - [View](static/images/My-Profile.jpg)
    -   Recipe Details Page Wireframe - [View](static/images/Recipe-Details.jpg)

    -   Mobile Home Wireframes - [View](static/images/Mobile-Wireframes.jpg)

    - Information: The above wireframes were designed in the initial process. But as the project went on, changes were made to make every content look better and more attractive.

## Features

-   The website is responsive on all device sizes ranging from desktop to tablet & mobiles.

-   Interactive elements.

-   Defence coding has been utilised wherever possible. If the user has entered info which is not as per criteria, errors will be generated.

-   Database connectivity.

## Project implementation

-   The Homepage - Clicking on the website link directly points to the homepage where the user is presented with the hero-image af food items above where there is a navigation bar. On the navigation bar, the user is presented with the opportunity to login or sign up if unregistered. And below they can already view a list of recipes. They can get the recipe details when they click on the view button. In the homepage, they also have the ability to view content in a specific order or search for some recipe based on a keyword. 

-   Login Page - The link for login page is available on the navigation bar. Here the user can enter their email id and password to log in. However, if not registered, they have to option to click sign up just below the Login Button. They will then be directed to the sign up page.

-   Sign Up Page - The link for the sign up page can be accessible from either the navigation bar or on the login page. Here, the user needs to add details such as Fullname, Email id, password & confirm password. Once they sign p, they will be redirected to the login page.

-   My Profile Page - This page can only be accessed once the user has successfully logged in. It welcomes the user to the site and displays recipes added by him/her. Here, the user has the ability to edit the recipes or delete them.

-   Add Recipe Page - Once the user has logged in, they can access this page to add their own recipes to the database. They can add info like title, description, category, image-url, ingredients & method/direction.

-   Edit Recipe Page - This page is accessible from the My Profile page. When the user clicks on edit button, they are redirected to the edit page where the information from the database is alreads pre-poulated in the fields. They can easily perform their edit tasks.

-   Delete Recipe - The user can delete the recipe they do not want featured by just clicking the delete button on the profile page.


## Future implementation

-   Option to have an admin.
-   Option to add categories as a dropdown list.
-   Option to add comments and reviews.
-   Adding a rating feature.
-   Share recipe on social networks.

## Technologies Used

### Languages Used

-   [HTML5](https://en.wikipedia.org/wiki/HTML5)
-   [CSS3](https://en.wikipedia.org/wiki/Cascading_Style_Sheets)
-   [Python](https://www.python.org/)

### Frameworks, Libraries & Programs Used

1. [Material Design for Bootstrap:](https://mdbootstrap.com/)
    - Bootstrap was used to assist with the responsiveness and styling of the website.
2. [Google Fonts:](https://fonts.google.com/)
    - Google fonts were used to import the 'Titillium Web' font into the style.css file which is used on all pages throughout the project.
3. [Font Awesome:](https://fontawesome.com/)
    - Font Awesome was used on all pages throughout the website to add icons for aesthetic and UX purposes.
4. [jQuery:](https://jquery.com/)
    - jQuery came with Bootstrap to make the navbar responsive but was also used for the smooth scroll function in JavaScript.
5. [Git](https://git-scm.com/)
    - Git was used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
6. [GitHub:](https://github.com/)
    - GitHub is used to store the projects code after being pushed from Git.
7. [Figma:](https://figma.com/)
    - Figma was used to create the wireframes during the design process.
8. [Flask:](https://flask.palletsprojects.com/)
    - Flask was the web framework used to build the web application.
9. [MongoDB:](https://www.mongodb.com/)
    -MongoDB was used to store and retreive data from the database.


## Testing

The W3C Markup Validator and W3C CSS Validator Services were used to validate every page of the project to ensure there were no syntax errors in the project.

-   [W3C Markup Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](static/images/HTML-Validator.jpg)
-   [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) - [Results](static/images/CSS-validator.jpg)
-   [PEP8 Compliance](http://pep8online.com/) - [Results](static/images/Pep8-compliance.jpg)

### Testing User Stories from User Experience (UX) Section

-   #### First Time Visitor Goals

    -   #### First Time Visitor Goals

        1. As a First Time Visitor, I want to want to make sure that I get the information I want based on the site description.
            - Entering the website, the visitor is presented with the navbar that shows links to the home, login and sign up page. Below are the list of the recipies already added to the site. Also there is a search and sort section where the user can get the specific recipes based on his/her preference.

        2. As a First Time Visitor, I want to be able to easily navigate throughout the site easily to find content I am looking for.
            - The website is navigation friendly. The user can easily move from one page to another.

        3. As a First Time Visitor, I want to be able to sign up to be able to access the members area of the site.
            - By clicking 'Sign Up' on the navigation bar link, the user is directed to the sign up page where they can enter their name, email id and password to register themselves.

        4. As a first time visitor, I want to be able to add my own content to the website.
            - Once the user is registered and logged in, they can enter their own recipes in the 'Add recipe' section that shows up in the navigation bar once logged in.


        5. As a first time visitor, I want to be able to easily login and logout from the site.
            - The login and logout process is very simple. To log in, the user has to only enter their registered email id and password and click on the login button. To logout, they just need to click on the 'Logout' link on the navigation page which is visible only once logged in.

        6. As a first time user, I want to be able to use the website on all devices.
            - The website is responsive on all devices. The elements on the page adjust/resize automatically on different devices.


    -   #### Returning Visitor Goals

        1. As a Returning Visitor, I want to be able to view the list of recipes.
            - The users can easily vies the available recipes on the homepage. They can also search for recipes they like or even sort them by title.

        2. As a Returning Visitor, I want to be able to view details of every recipe.
            - On the list of recipe cards, when the user clicks on the 'View Recipe' button, they are redirected to the recipe details page where they can view the ingredients used as well as he directions/method of cooking.

        3. As a Returning Visitor, I want to be able to sort them by title for easy access.
            - In the homepage itself, the user is able to sort the recipes they want by title.

        4. As a Returning Visitor, I want to be able to search specific recipes based on a query.
            - The user can search for recipes based on title or description by entering the search keyword in the search field that is present in the homepage.

        5. As a Returning Visitor, I want to have access to my posts.
            - Every user has a dedicated profile page which shows the list of their contributions.

        6. As a Returning Visitor, I want to be the only one who is able to edit/update or delete my own posts.
            - Only the user that has logged in can edit or delete their own recipes. No other user has the access to others recipes.

        7. As a Returning Visitor, I want to find community links.
            - At the footer, there are links to the social community links.


### Further Testing

-   The Website was tested on Google Chrome, Internet Explorer, Microsoft Edge and Safari browsers.
-   The website was viewed on a variety of devices such as Desktop, Laptop & Samsung S20 Plus.
-   A large amount of testing was done to ensure that all pages were linking correctly.
-   Friends and family members were asked to review the site and documentation to point out any bugs and/or user experience issues.

### Known Bugs

-   The delete button when clicked directly deletes the record. There is no mechanism added to confirm the delete function.



## Deployment

### GitHub Pages

The project was deployed to GitHub Pages using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page), locate the "Settings" Button on the menu.
    - Alternatively Click [Here](https://raw.githubusercontent.com/) for a GIF demonstrating the process starting from Step 2.
3. Scroll down the Settings page until you locate the "GitHub Pages" Section.
4. Under "Source", click the dropdown called "None" and select "Master Branch".
5. The page will automatically refresh.
6. Scroll back down through the page to locate the now published site [link](https://github.com) in the "GitHub Pages" section.

### Forking the GitHub Repository

By forking the GitHub Repository we make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository by using the following steps...

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. At the top of the Repository (not top of page) just above the "Settings" Button on the menu, locate the "Fork" Button.
3. You should now have a copy of the original repository in your GitHub account.

### Making a Local Clone

1. Log in to GitHub and locate the [GitHub Repository](https://github.com/)
2. Under the repository name, click "Clone or download".
3. To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned directory to be made.
6. Type `git clone`, and then paste the URL you copied in Step 3.

```
$ git clone https://github.com/johnnyferns14/javascript-milestone-project-2
```

7. Press Enter. Your local clone will be created.

```
$ git clone https://github.com/johnnyferns14/javascript-milestone-project-2
> Cloning into `CI-Clone`...
> remote: Counting objects: 10, done.
> remote: Compressing objects: 100% (8/8), done.
> remove: Total 10 (delta 1), reused 10 (delta 1)
> Unpacking objects: 100% (10/10), done.
```

Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to retrieve pictures for some of the buttons and more detailed explanations of the above process.

## Credits



### Content

-   All content was written by the developer.


### Media

-  The background image was freely available from the internet, taken specifically from [PNGtree on Pinterest](https://www.pinterest.com.au/pin/456622849718914305/)

### Acknowledgements

-   My Mentor for continuous helpful feedback.

-   Tutor support at Code Institute for their support.
