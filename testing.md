## AUTOMATED TESTING

### Validator Testing - HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. 

* After failing the Project, I went back and fixed all of the errors that popped up on the HTML Checker. Like I mentioned to my tutor, the HTML checks failed when using the URLs, but worked fine when using Direct Input, which I originally did. No where in the course material does it say I had to use the URLs.

* [Home Page](/static/images/home-validator.png4) - No errors or warnings.
* [About Page](/static/images/about-validator.jpg) - No errors.
* [Contact Page](/static/images/contact-validator.jpg) - No errors.
* [Register Page](/static/images/register-validator.jpg) - No errors.
* [Login Page](/static/images/login-validator.jpg) - No errors.
* [News Articles](/static/images/news-articles-image.jpg) - 28 errors. Due to the fact that the news article posts are written in the back end using an editor, they throw up errors on the validator as it is reading the text as html. I was not ables to figure out a way around this and it was not mentioned in the course material for the Django Blog.
- [HTML Errors](/static/images/tutor-support-summernote-fail.png) - Further to this point, I spoke with both my Tutor and Student support. I was informed to leave it the way it is with regards to the summernote errors on the HTML checker.
-[HTML Width Error](/static/images/html-errors-issue-tutor-support.png) - There is one HTML error remaining which I spent hours troubleshooting with Tutor support. We could not find a fix and believe it has something to do with running an earlier version of bootstrap. My tutor advised to keep the in-style styling and to mention the error here. 



### Validator Testing - CSS
No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/):
- [CSS validator results](/static/images/css-testing-image.jpg)


### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [script.js](/static/images/jshint-validator.png)


### Python Validator

- Code Institutes Python Linter was used to validate any written Python Code.

* - Went back after Project failing and fixed all Pep8 errors except for one. There is an error in my settings.py related to cloudinary, with the line being 1 character too long. After speaking with tutor support I was told to leave it as any changes seemed to cause the app to not open.

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

The site was tested manually by going through all CRUD screens and forms, and ensuring error validation and functionality. The HTML, Python and Javascript code was all manually tested as shown below.


| Test Case | Pass? | Screenshot |
|-----------|-------|------------|
|Register- Username Required|Yes|![Successful error message](/static/images/register-username-error.png)|
|Register- Password Required|Yes|![Successful error message](/static/images/register-password-error.png)|
|Register- Password Confirmation|Yes|![Successful error message](/static/images/register-password-confirmation-error.png)|
|Login- Username Required |Yes|![Successful error message](/static/images/login-username-error.png)|
|Login- Password Required |Yes|![Successful error message](/static/images/login-password-required-error.png)|
|Login Successful|Yes|![Successful error message](/static/images/login-successful-alert.png)|
|Logout Successful|Yes|![Successful error message](/static/images/logout-successful-alert.png)|
|Contact Email Required|Yes|![Successful error message](/static/images/contact-email-required-error.png)|
|Contact Subject Required|Yes|![Successful error message](/static/images/Contact-subject-required.png)|
|Contact Message Required|Yes|![Successful error message](/static/images/Contact-message-required-error.png)|
|Comment Message Required|Yes|![Successful error message](/static/images/comment-message-required-error.png)|
|Comment Message Successful|Yes|![Successful error message](/static/images/comment-message-successful-alert.png)|
|Comment Posted|Yes|![Successful error message](/static/images/comment-posted.png)|
|Comment Edit|Yes|![Successful error message](/static/images/comment-edit-page.png)|
|Comment Edit Message Required|Yes|![Successful error message](/static/images/comment-edit-message-required-error.png)|
|Comment Edit Message Successful|Yes|![Successful error message](/static/images/comment-edit-successful-alert.png)|
|Comment Edit Posted|Yes|![Successful error message](/static/images/comment-edited-posted.png)|
|Comment Delete Page|Yes|![Successful error message](/static/images/comment-delete-page.png)|
|Comment Delete Successful|Yes|![Successful error message](/static/images/comment-delete-successful.png)|
|Like Button|Yes|![Successful error message](/static/images/like-button.png)|
|Like Successful|Yes|![Successful error message](/static/images/like-button-successful.png)|
|Admin Username Required |Yes|![Successful error message](/static/images/admin-username-required-error.png)|
|Admin Password Required |Yes|![Successful error message](/static/images/admin-password-required-error.png)|
|Admin Staff Account Required |Yes|![Successful error message](/static/images/admin-staff-account-required-error.png)|




























The site was tested on the following devices: MacBook Air, MacBook Pro, iPhone, iPad, Google Pixel and ASUS laptop. The site was tested in Chrome and Safari.