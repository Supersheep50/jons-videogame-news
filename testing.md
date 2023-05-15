## AUTOMATED TESTING

### W3C Validator

[W3C](https://validator.w3.org/) was used to validate the HTML on all pages of the website. It was also used to validate the CSS. I have checked the HTML via direct input and also by inspecting the page source and running this through the validator.

* [Index Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2F) - No errors or warnings.
* [Register Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fregister) - No errors or warnings.
* [Login Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Flogin) - No errors or warnings.
* [Profile Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fprofile%3Fusername%3Dadmin) - No errors or warnings.
* [Bookshelves Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fbookshelves) - No errors or warnings.
* [Add Bookshelf Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fadd_bookshelf) - No errors or warnings.
* [Edit Bookshelf Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fedit_bookshelf%2F23) - No errors or warnings.
* [Search Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fsearch) - No errors or warnings.
* [Add Review Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fpopulate_review%3Fgbook_id%3D7OdQvuI-eygC) - No errors or warnings.
* [Books Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fview_books) - No errors or warnings.
* [Edit Review Page](https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fedit_review%2F62e458bbbd1b8de864934262) - No errors or warnings.
* [Error Page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fbookworm2022.herokuapp.com%2Fedit_bookshelf%2Ferror) - No errors or warnings.

~~The validator has returned warnings for the use of aria-labels on all pages using the bootstrap icons. I am happy to leave these warnings as I have followed the instructions on the bootstrap site regarding the use of aria labels with icons, and the use of the aria labels is important for accessibility.~~

UPDATE Nov 2022 - aria-label warning: I have since been advised that the best way to deal with the issue of the aria-labels throwing a warning in the validator is to move the aria-label to the parent DOM element. I have now updated this for all aria-labels that were included in an `<i>` tag, and the warning no longer appears when validating.

- - -


### Validator Testing - CSS
No errors were found when passing through the official [(Jigsaw) validator](https://jigsaw.w3.org/css-validator/):
- [CSS validator results](/static/images/css-testing-image.jpg)


### JavaScript Validator

[jshint](https://jshint.com/) was used to validate the JavaScript.

* [script.js](documentation/testing/validation/jshint-script.png)

- - -

### Python Validator

~~[PEP8](http://pep8online.com/) was used to validate the python files. Due to limited time for completing this project I have been unable to completely fix all PEP8 errors in all the files, I need to do some further research into the best ways to break lines that are too long.~~

UPDATE Nov 2022: The PEP8 validator site mentioned above has since gone down. I am therefore relying on using the [pycodestyle](https://pypi.org/project/pycodestyle/) package within my IDE to ensure that my code meets PEP8 guidelines.

* [app.py](documentation/testing/validation/python-app.png) - No errors or warnings.
* [models.py](documentation/testing/validation/python-models.png) - No errors or warnings.
* [__init__.py](documentation/testing/validation/python-init.png) - No errors or warnings.
* [auth/routes.py](documentation/testing/validation/python-auth-routes.png) - Please see further information below regarding nomember error resolution. No other errors or warnings.
* [books/routes.py](documentation/testing/validation/python-book-routes.png) - Please see further information below regarding nomember error resolution, and bare exception resolution. No other errors or warnings.
* [error_handlers/routes.py](documentation/testing/validation/python-error-routes.png) - There is a [warning](documentation/testing/validation/error-route-pep8.png) regarding the argument `e` not being used. I tried removing this argument from the code, however the error pages then didn't load, they defaulted to the generic error pages. I have added back in the argument `e` to allow the error handling to work correctly and to display my own error pages to the user. I am therefore happy to leave this warning in place. Pylint also gives feedback that the argument `e` doesn't conform to snake_case naming style. Again I am happy to leave this feedback, as there is no way to snake_case name a singular letter.
* [main/routes.py](documentation/testing/validation/python-main-routes.png) - No errors or warnings.

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
|Sign-up form: username is required|Yes|![Error message if username is not filled in](static/readme/test-signup-username.png)|
|Sign-up form: password must be longer than 8 characters|Yes|![Error message if username is less than 8 characters](static/readme/test-signup-password-8.jpg)|
|Sign-up form: password must not be longer than 15 characters|Yes|![Error message if username is longer than 15 characters](static/readme/test-signup-password-15.png)|
|Sign-up form: password is required|Yes|![Error message if passworld is not filled in](static/readme/test-signup-password.jpg)|
|Login form: validation message shows when user logs in|Yes|![Validation message after login](static/readme/test-login-message.png)|
|Add planet form: name is required|Yes|![Error messsage if name is not selected from the list](static/readme/test-add-planet-name.jpg)|
|Add planet form: validation message when planet is added|Yes|![Validation message when planet is added](static/readme/test-add-planet-validation.jpg)|
|Edit planet form: validation message when planet is edited|Yes|![Validation message when planet is edited](static/readme/test-edit-planet-validation.png)|
|Delete planet form: validation message when planet is deleted|Yes|![Validation message when planet is deleted](static/readme/test-delete-planet-validation.jpg)|
|Log out form: validation message when user logs out|Yes|![Validation message when user logs out](static/readme/test-sign-out-validation.jpg)|

The site was tested on the following devices: MacBook Air, MacBook Pro, iPhone, and iPad. The site was tested in Chrome and Safari.