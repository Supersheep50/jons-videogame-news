![Responsive](/static/images/responsive-image.jpg)


# Jons-Videogame-News

- Jons Videogame News is a news website that reports on all the latest and greatest videogame news. The website gives readers the ability to keep up to date on videogame news and read news articles that the writers have written. 

- Readers have the ability to write, edit and delete comments on news stories. They can also like comments from other users.

[View the deployed version here!](https://jvn.herokuapp.com/)

## Wireframes

- I created a wireframe to map out the basic style and functionality of the website. 

![Website](/static/images/wireframes-image.png)

## User Stories

  -   #### First Time Visitor Goals

      1. As a first time user I want to understand what is JVN.
      2. As a first time visitor I want to understand how to navigate JVN. 
      3. As a first time user I want to understand how to read news articles, like comments, read, edit and delete comments.

  -   #### Returning Visitor Goals

      1. As a returning visitor I want to see new news articles. 
      2. As a returning visitor I want to see what new comments are there. 
      3. As a returning visitor I want to see if people have liked or reacted to my comments.

  -   #### Frequent User Goals
      1. As a frequent user I want to build relationships on the website through the ability to comment.
      2. As a frequent user I want to be able to check the website daily for new news articles and comments.


## Agile Planning

### Github Projects

- I used Github Projects to map out my weeks for the project. Adding items as I went and moving them to the completed section once finished. 

![Github Projects](/static/images/github-projects.jpg)


## Features

### Existing Features

- __Logo and Nav Header__

    - At the top left of the screen there is a custom made logo for the news wesbite. Clicking the logo brings you to the homepage. The logo scales with different devices.

   ![Logo and Nav Header](/static/images/logo-navbar.png)

- __Register & Login__

    - At the top right of the screen users have the ability to register with the website and then login or logout upon visiting the website. 
    
    ![User creation](/static/images/register-login-image.jpg)

- __Login/Log out Alert__

    - Each time a user logins or logs out a message alert flashes to tell them they have been successful in doing so.
    
    ![Login/Log out Alert](/static/images/login-alert.jpg)

- __News Articles__

    - At the centre of the screen is where users will find all the news articles posted to the site.
    
    ![News Artciles](/static/images/news-articles-image.jpg)

- __Contact Section__

    - At the top right of the screen is a link for users to contact the admins of the website with any questions/concerns they may have.

    ![Contact Section](/static/images/contact-image.jpg)

    __Contact Section Confirmed__

    - Once a message has been sent, users receive this confirmation message.

    ![Contact Section Confirmed](/static/images/contact-form-confirmed-image.jpg)

- __Register Section__

    - At the top right of the website users can register with the website so that they write and like comments.

    ![Register Section](/static/images/register-section.jpg)

- __Social Links__

    - Screenshot of social media links in footer
   
    ![Social Links](/static/images/social-links.jpg)

- __Post Comments__

    - Logged in Users are able to post comments on news articles.

    ![Post Comments](/static/images/post-comment-image.jpg)

 - __Edit & Delete Comments__

    - Users are able to edit and delete their comments. 

     ![Edit & Delete Comments](/static/images/edit-delete-comments.jpg)

- __Like and Unlike Comments__

    - Users are able to like and unlike posts once they are logged in.

    ![Like and Unlike Comments](/static/images/like-posts-image.jpg)


- __Admin for posting News Articles__

    - Ability to post comments through the backend admin by the superuser.

    ![Backend Admin](/static/images/admin-post-articles.png)


- __Admin for editing and writing News Articles__

    - Ability to write/edit comments through the backend admin by the superuser.

    ![Backend Admin Write/Edit posts](/static/images/admin-post-edit-articles.png)


- __Admin for approving comments__

    - Ability to approve comments through the backend admin by the superuser.

    ![Backend Admin Write/Edit posts](/static/images/approve-comments.png)

## Testing 

- Please see the [Testing file](testing.md) for manual & validator testing.

## Deployment

### Local Deployment
​
*Gitpod* IDE was used to write the code for this project.

To make a local copy of this repository, you can clone the project by typing the follow into your IDE terminal:
- `git clone https://supersheep5-jonsvideoga-7balifezslz.ws-eu96b.gitpod.io`

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://supersheep5-jonsvideoga-7balifezslz.ws-eu96b.gitpod.io)
​
### ElephantSQL Deployment

To host my database, I used ElephantSQL. 

The instructions to create a new account can be [found here](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up), provided by Code Institute. 

Once you have created an account:
- Log in to ElephantSQL to access your dashboard.
- Click *Create New Instance*.
- Give your plan a name (usually the name of the project, in this case *ME1 Planet Tracker*).
- Select the Tiny Turtle (Free) plan.
- Leave the Tags field blank.
- Click *Select Region* and choose a data center near you.
- Click *Review*, then, if everything looks correct, *Create Instance*.
- Go back to your dashboard and click on the name of the project. 
- Copy the database URL for your project, and use it in two places:
  - In your `env.py` file, create a new key called `DATABASE_URL` and give it the value of the ElephantSQL database URL, as follows: ` os.environ.setdefault("DATABASE_URL", "my_copied_database_url")`.
    - Before deploying the project, create a file called `env.py` (if it hasn't been created already), and complete the following steps:
      - In `settings.py`: At the top of the file, add the following import:
      ```python
      import os

      if os.path.isfile("env.py"):
          import env
      ```
      - Replace the pasted-in database url with the following code:
      ```python
      os.environ.get("DATABASE_URL")
      ```
  - Paste the database URL into the config vars section of your project on Heroku - instructions are in the *Heroku Deployment* section below. 

After the above steps are completed, install dj-database-url to your project, by typing the following command in the terminal and pressing enter:
- `os.environ.setdefault("DATABASE_URL", "my_copied_database_url")`
- Then update `requirements.txt` by typing `pip3 freeze --local > requirements.txt`.

### Heroku Deployment
​
This project uses [Heroku](https://www.heroku.com), a platform as a service (PaaS) that enables developers to build, run, and operate applications entirely in the cloud.
​
Deployment steps are as follows, after account setup:
​
- Select *New* in the top-right corner of your Heroku Dashboard, and select *Create new app* from the dropdown menu.
- Enter a name for your app. The app name must be unique, so you need to adjust the name until you find a name that hasn't been used.
- From the dropdown, choose the region closest to you (EU or USA), and finally, select *Create App*.
- From the new app *Settings*, click *Reveal Config Vars*, and set the value of KEY to `PORT`, and the value to `8000` then select *add*.
- Now, add a seecond Config Var for the `creds.json`file, which contains the API Key from Google Sheets. Set the value of KEY to `CREDS` and paste the entire contents of `creds.json` in the VALUE box. Select *add*.
- Further down, to support dependencies, select *Add buildpack*.
- The order of the buildpacks is important. Select `Python` first, then *Save changes*. Click *Add buildpack* again, and select `Node.js`, then *Save changes*. If they are not in this order, you can drag them to rearrange them

Heroku needs two additional files in order to deploy properly.
- requirements.txt
- Procfile

You can install this project's requirements (where applicable) using: `pip3 install -r requirements.txt`. If you have your own packages that have been installed, then the requirements file needs to be updated using: `pip3 freeze --local > requirements.txt`

The Procfile can be created with the following command: `echo web: node index.js > Procfile`

For Heroku deployment, follow these steps to connect your GitHub repository to the newly created app:
​
- At the top of the screen on Heroku, select *Deploy*.
- Next to *Deployment method* select *GitHub*, then scroll down and click *Connect to GitHub* to confirm you want to connect.
- In the *repo-name* field, search for the name of the GitHub repository to deploy, and click *Search*.
- Click *Connect* to link the GitHub repository with Heroku. 
- Scroll down to the *Manual deploy* section, and click *Deploy Branch*.
- If you like, click *Enable Automatic Deploys* in the *Automatic deploys* section to have Heroku rebuild your app every time you push a new change to GitHub.

The frontend terminal should now be connected and deployed to Heroku.

## Credits and Bugs

### Media
- [Looka.com](https://looka.com/) was used to create the logo. 

- [realgear.net](https://realgear.net) for the Home page background photo.

- [raregallery.net](https://realgear.net) for the About page background photo.

- [wallpaperFlare](https://wallpaperflare.com) for the Contact page background photo.

- [supermariobrosmovie.com](https://www.thesupermariobros.movie/character-gallery/) for the Mario News Article photo.

- [imdb.com](https://www.imdb.com) for the God of War News Article photo.

- [ign.com](https://sea.ign.com/google-stadia/197408/news/former-stadia-boss-phil-harrison-quietly-leaves-google-following-service-closure) for the Stadia News Article photo.

- [comicbook.com](https://comicbook.com/gaming/news/the-witcher-3-wild-hunt-incredible-mod-first-person/) for the Witcher News Article photo.

### Content 

- [Code Institute's Gitpod Full Template](https://github.com/Code-Institute-Org/gitpod-full-template) was used as the starting workspace template for this project.

- [Code Institute's README Template](https://github.com/Code-Institute-Solutions/readme-template) was used to structure this README.

- [Balsamiq](https://balsamiq.com/) to create wireframes during the design phase.

- [gamespot.com](https://www.gamespot.com/reviews/the-super-mario-bros-movie-review-actually-awesome/1900-6418051/#:~:text=The%20Super%20Mario%20Bros..,Super%20Show%20theme%2D%2Dstruggling.) was used for the Super Mario bros article content.

- [gamespot.com](https://www.gamespot.com/articles/god-of-war-ragnaroks-new-game-plus-mode-is-available-now-offers-increased-level-cap/1100-6512992/) was used for the God of War article content.

- [ign.com](https://www.ign.com/articles/former-stadia-boss-phil-harrison-quietly-leaves-google-following-service-closure) was used for the Stadia article content.

- [vulkk.com](https://vulkk.com/2022/12/12/the-witcher-3-next-gen-update-everything-you-should-know/) was used for the Witcher article content.

### Code

- [Code Pen](https://codepen.io/) Lots and lots of time spent in Code Pen testing and trying diffetent bits of code before adding to Gitpod.

- Basic structure for posting news articles was used from the Code Institute modules I Think Therefore I Blog and Hello Django. As well as setting up the admin backend.

- Both modules and source code also used for adding commenting and editing commenting functionality. As well as the ability to like comments.

- [MDN Web Docs](https://developer.mozilla.org/en-US/) for general debugging. 

- [StackoverFlow](https://stackoverflow.com/questions/62610222/adding-comment-class-view) used ideas and suugesstions from StackOverflow to add comment functionality.

- [StackoverFlow](https://stackoverflow.com/questions/49926871/django-edit-comment) also used some code from Stackoverflow to add ability to edit comments.

- Code from Nav Bar used from previous project A History of the Playstation. 

- [Geeks for Geeks](https://www.geeksforgeeks.org/deleteview-class-based-views-django/) code for deleting comments assisted by this site. A Student Support Tutor helpfully sent this on.

- [Twilio](https://www.twilio.com/blog/build-contact-form-python-django-twilio-sendgrid) code for adding a contact form app partially used from this site. I also must credit Alan in Tutor support as we spent hours together fixing a bug here.

- Advice, help, debugging and guidance for my whole project from my mentor AJ and my partner Steph.

- Alert functions for logging in and logging out used from Code Institutes course material and source code.

- Javascript Alert and timeout function taken from previous project The Hey! Look! Listen! Quiz and some assistance from Tutor Support.

- Some deployment instructions are from Code Institute's 'Deployment' section, in the 'Hello Django' module of the course.

- Slack used to ask questions from fellow students and alumnis. This was particular helpful when trying to get my Heroku Deployment working properly.


## Bugs 

- Initially website would not load correctly on Heroku. Issue with Cloudinary was discovered and needed to delete all static files being hosted on the website.
- Contact form originally was sending emails but not diverting users to the correct page afterwards to show that the message was sent. Tutor support helped me here in discovering what ended up being a fairly simple typo. 
- Not exactly a bug but had one instance of not pushing code when I thought I had, Lost all code and work that was around building a delete comment functionality. Only discovered at Readme phase but was thankfully able to recall some of it and also had some of it shared in a comment on Slack. Lesson learned. 


## Bug fixes after Project Failing

- This project was failed due to not having proper Defensive Design. It was possible to edit or delete other comments via the comment URLs. This has now been fixed. 

- [Defensive Design](/static/images/defensive-design.png)



## Acknowledgements 

- Big shout out to my partner Stephanie for all her help and wisdom! Thanks to tutor support for helping on a couple of issues and to my mentor AJ for the guidance.