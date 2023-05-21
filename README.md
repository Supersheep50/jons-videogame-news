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
      4. As a first time visitor I want to try to beat the game and enter my name into the logbook.

  -   #### Returning Visitor Goals

      1. As a returning visitor I want to see new news artciles. 
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

    - Each time a user logins or logs out a message alert flashes to tell they have been successful in doing so.
    
    ![Login/Log out Alert](/static/images/login-alert.jpg)

- __News Articles__

    - At the centre of the screen is where users will find all the news articles posted to the site.
    
    ![News Artciles](/static/images/news-articles-image.jpg)

- __Contact Section__

    - At the top right of the screen is a link for users to contact the admins of the website with any questions/concerns they may have.

    ![Contact Section](/static/images/contact-image.jpg)

    __Contact Section Confirmed__

    - Once a message ahs been sent, users receive this confirmation message.

    ![Contact Section Confirmed](/static/images/contact-form-confirmed-image.jpg)

- __Register Section__

    - At the top right of the website users can register with the webiste so that they write and like comments.

    ![Register Section](/static/images/register-section.jpg)

- __Social Links__

    - Screenshot of social media links in footer
   
    ![Social Links](/static/images/social-links.jpg)

- __Post Comments__

    - Logged in Users are able to post comments on news articles.

    ![Post Comments](/static/images/post-comment-image.jpg)

 - __Edit & Delete Comments__

    - Users are able to edit and delete teir comments. 

     ![Edit & Delete Comments](/static/images/edit-delete-comments.jpg)

- __Like and Unlike Comments__

    - Users are able to like and unlike posts once they are logged in.

    ![Like and Unlike Comments](/static/images/like-posts-image.jpg)


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

The instructions to create a new account can be[found here](https://code-institute-students.github.io/deployment-docs/02-elephantsql/elephantsql-01-sign-up), provided by Code Institute. 

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

## Credits 

### Media
- [Patorjk.com](https://patorjk.com/) was used to create the heading.

- Emojis used from [Unicode.com](https://unicode.org/emoji/charts/full-emoji-list.html)

### Content 
- I used Code Institute's Love Sandwiches Walkthrough ([repo here](https://github.com/Code-Institute-Solutions/love-sandwiches-p5-sourcecode/tree/master/05-deployment/01-deployment-part-1)) for guidance with code structure, linking my program to Google Sheets using an API, and deployment steps.

- For slower printing to the terminal I used Stackoverflow. The page is [here](https://stackoverflow.com/questions/510348/how-do-i-make-a-time-delay) 

- To change the color of the text I used ANSI color. Page from Stackoverflow helping it explain it to me found [here](https://stackoverflow.com/questions/4842424/list-of-ansi-color-escape-sequences)

- For the add inventory function I used this video to help me form the basics of what I needed [here](https://www.youtube.com/watch?v=rvKxC-p6kbg)

- Code to help validate the user input [here](https://initialcommit.com/blog/python-isalpha-string-method) and two seperate sessions with Tutor Support.

- To create the ability to move from tomb to tomb I referenced this page [here](https://www.makeuseof.com/python-text-adventure-game-create/)

- Used Love Sandwiches walkthrough to build out collecting data for the logbook.

- To clear the screen after the user selects Try Again, I referenced this page [here](https://stackoverflow.com/questions/4810537/how-to-clear-the-screen-in-python)


## Acknowledgements 

- Big shout out to my partner Stephanie for all her help and wisdom! Thanks to tutor support for helping on a couple of issues and to my mentor AJ for the guidance.