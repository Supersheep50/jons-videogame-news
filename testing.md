## AUTOMATED TESTING

### Validator Testing - HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. I have checked the HTML via address input and also by inspecting the page source and running this through the validator.

* [Home Page](/static/images/home-validator.png4) - No errors or warnings.
* [About Page](/static/images/about-validator.jpg) - No errors.
* [Contact Page](/static/images/contact-validator.jpg) - No errors.
* [Register Page](/static/images/register-validator.jpg) - No errors.
* [Login Page](/static/images/login-validator.jpg) - No errors.
* [News Articles](/static/images/news-articles-image.jpg) - 28 errors. Due to the fact that the news article posts are written in the back end using an editor, they throw up errors on the validator as it is reading the text as html. I was not ables to figure out a way around this and it was not mentioned in the course material for the Django Blog.


### Validator Testing - CSS
No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/):
- [CSS validator results](/static/images/css-testing-image.jpg)


### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [script.js](/static/images/jshint-validator.png)


### Python Validator

- Code Institutes Python Linter was used to validate any written Python Code.

* [contact/forms.py](/static/images/contact-forms-validator.jpg) - No errors or warnings.
* [contact/models.py](/static/images/contact-models-validator.jpg) - No errors or warnings.
* [contact/urls.py](/static/images/contact-form-urls.jpg) - No errors or warnings.
* [contact/views.py](/static/images/contact-form-views.jpg) - No errors or warnings.
* [jvn/urls.py](/static/images/jvn-urls-validation.jpg) - No errors or warnings.
* [news/admin.py](/static/images/news-admin-validation.jpg) - No errors or warnings.
* [news/forms.py](/static/images/news-forms-validation.jpg) - No errors or warnings.
* [news/models.py](/static/images/news-models-validation.jpg) - No errors or warnings.


### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website. 

### Desktop Results

* [Home Page](/static/images/homepage-lighthouse.png)
* [About Page](/static/images/aboutpage-lighthouse.png)
* [Contact Page](/static/images/contactpage-lighthouse.png)
* [Login Page](/static/images/loginpage-lighthouse.png)


### Mobile Results

* [Home Page](/static/images/homepage-mobile-lighthouse.png)
* [About Page](/static/images/aboutpage-mobile-lighthouse.png)
* [Contact Page](/static/images/contactpage-mobilie-lighthouse.png)
* [Login Page](/static/images/loginpage-mobile-lighthouse.png)


## MANUAL TESTING

### Testing User Stories

### Manual Testing

The site was tested manually by going through all CRUD screens and forms, and ensuring error validation and functionality. 


| Test Case | Pass? | Screenshot |
|-----------|-------|------------|
|Name & age input options: enter a space|Yes|![Successful error message](/documents/testing/name-input-error-1.png)|
|Name & age input options: enter a letter|Yes|![Successful error message](/documents/testing/name-input-error-2.png)|
|Name & age input options: enter a special character|Yes|![Successful error message](/documents/testing/name-input-error-3.png)|
|Main menu options: enter a number not between 1-3|Yes|![Successful error message](/documents/testing/main-menu-input-error.png)|
|Main menu options: enter a space |Yes|![Successful error message](/documents/testing/main-menu-input-error.2.png)|
|Main menu options: enter a special character |Yes|![Successful error message](/documents/testing/main-menu-input-error.3.png)|
|Yes or No questions: enter a special character |Yes|![Successful error message](/documents/testing/yes-no-error.png)|
|Yes or No questions: enter a number |Yes|![Successful error message](/documents/testing/yes-no-error.2.png)|
|Yes or No questions: enter a space |Yes|![Successful error message](/documents/testing/yes-no-error.3.png)|
|Crossroad direction questions: enter a number |Yes|![Successful error message](/documents/testing/crossroads-error.png)|

The site was tested on the following devices: MacBook Air, MacBook Pro, iPhone, iPad, Google Pixel and ASUS laptop. The site was tested in Chrome and Safari.