## AUTOMATED TESTING

### Validator Testing - HTML

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. I have checked the HTML via address input and also by inspecting the page source and running this through the validator.

* [Home Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2F) - No errors or warnings.
* [About Page](/static/images/about-validator.jpg) - No errors.
* [Contact Page](/static/images/contact-validator.jpg) - No errors.
* [Register Page](/static/images/register-validator.jpg) - No errors.
* [Login Page](/static/images/login-validator.jpg) - No errors.
* [News Articles](/static/images/news-articles-image.jpg) - 28 errors. Due to the fact that the news article posts are written in the back end using an editor, they through up errors on the validator as it is reading the text as html. I was not ablt to figure out a way around this and it was not mentioned in the course material for the Django Blog.


### Validator Testing - CSS
No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/):
- [CSS validator results](/static/images/css-testing-image.jpg)


### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [script.js](documentation/testing/validation/jshint-script.png)

- - -

### Python Validator

- Code Institutes Python Linter was used to validate any written Python Code.

* [contact/forms.py](/static/images/contact-forms-validator.jpg) - No errors or warnings.
* [contact/models.py](/static/images/contact-models-validator.jpg) - No errors or warnings.



Nomember error resolution.

The auth and book routes.py files were both showing an error:

``` bash
Instance of 'scoped_session' has no 'add' memberpylint(no-member)
```

Upon doing some research regarding this error I came across the following [solution](https://cs50.stackexchange.com/questions/32768/instance-of-scoped-session-has-no-commit-member), which also referenced this answer on [stackoverflow](https://stackoverflow.com/questions/42789666/pylint-error-message-on-cloud-9-cs50). It seems to be an issue with the way the pylinter reads the python file. Research suggested that I add the following code to a `.pylintrc` file to let the linter know to ignore this error: `ignored-classes=SQLObject,Registrant,scoped_session`.

Bare exception resolution.

In the books/route.py file I was getting an error relating E722 no bare exceptions. I did some further research on this error and added Exeption after the except to solve this issue as mentioned in this [stackoverflow question](https://stackoverflow.com/questions/54948548/what-is-wrong-with-using-a-bare-except).

I have also been able to run all my python files through the [Code Insitute Python Linter](https://pep8ci.herokuapp.com/) which they released to students on the 15th of November. It shows no errors in any of my python files.
- - -

### Lighthouse

I used Lighthouse within the Chrome Developer Tools to test the performance, accessibility, best practices and SEO of the website. These scores are somewhat lower than what I would like them to be so this is something that I would prioritise improving in the next implementation.

### Desktop Results

* [Index Page](documentation/testing/validation/lh-index-desk.png)
* [Add Bookshelf Page](documentation/testing/validation/lh-add-bookshelf-desk.png)
* [Add Review Page](documentation/testing/validation/lh-add-review-desk.png)
* [Books Page](documentation/testing/validation/lh-books-desk.png)
* [Bookshelves Page](documentation/testing/validation/lh-bookshelves-desk.png)
* [Edit Bookshelf Page](documentation/testing/validation/lh-edit-bookshelf-desk.png)
* [Edit Review Page](documentation/testing/validation/lh-edit-review-desk.png)
* [Error Page](documentation/testing/validation/lh-error-desk.png)
* [Login Page](documentation/testing/validation/lh-login-desk.png)
* [Profile Page](documentation/testing/validation/lh-profile-desk.png)
* [Register Page](documentation/testing/validation/lh-register-desk.png)
* [Search Page](documentation/testing/validation/lh-search-desk.png)

- - -

### WAVE Testing

[WAVE](http://wave.webaim.org/) (Web Accessibility Evaluation Tool) allows developers to create content that is more accessible to users with disabilities. It does this by identifying accessibility and WGAC errors.

I have used the WAVE testing tool to try and ensure there are no accessibility issues with my site.

- - -

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

The site was tested on the following devices: MacBook Air, MacBook Pro, iPhone, and iPad. The site was tested in Chrome and Safari.