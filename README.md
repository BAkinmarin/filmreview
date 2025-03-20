# My Film Review Blog

My Film Review is a blog bringing you fresh and original views of different genres of films. This web application allows users to register an account, login, and comment on reviews.

This blog was created using Django and has full CRUD functionality with an intuitive User Interface to make interactions with posts and other users simple and fun!

<!--![Am I Responsive Screenshot]()-->

- [Live Site](https://my-film-blog-pp4-d9dc642517af.herokuapp.com/)
- [GitHub Repository](https://github.com/BAkinmarin/filmreview)

## Table of Contents

1. [UX](#ux)
2. [Features](#features)
3. [Future Features](#future-features)
4. [Responsiveness](#responsiveness)
5. [Technologies](#technologies)
6. [Testing](#testing)
7. [Bugs](#bugs)
8. [Deployment](#deployment)
9. [Credits](#credits)
10. [Acknowledgements](#acknowledgements)


## UX

This website was created using the Five Planes of Website Design:

- [Strategy](#strategy)
### User

 <!--As a user, I want to be presented with a paginated list of posts, so that I can select which post I want to view in more detail.-->

 <!--As a user, I want to read film reviews so I know what to expect before committing to watching a film.

 As a user, I want to search film reviews by genre so I do not have to scroll through unneccessary content.

 As a user, I want to interact with both film reviews from the author and comments from other visitors.

 As a user, I want to know what films are yet to be released and their release date.

 As a user, I want to modify or delete comments previously left on posts.-->

 ### Super User

 <!--As a super user, I want to be able to add posts on a user-friendly inteface.

 As a super user, I want to be able to monitor comments with full CRUD functionality.-->

- [Scope](scope)
- [Structure](structure)
- [Skeleton](skeleton)
- [Surface](surface)

[Back to Top](#ux)

## Features

[Back to Top](#ux)

## Responsiveness

[Back to Top](#ux)

## Technologies

<table>
  <tr>
    <td valign="top">
      <table>
        <tr>
          <td><strong>Backend</strong></td>
          <td style="text-align:right;">Django 5.1.1 <code>Django==5.1.1</code></td>
        </tr>
        <tr>
          <td><strong>API</strong></td>
          <td style="text-align:right;">TBD <code>TBD</code></td>
        </tr>
        <tr>
          <td><strong>Database</strong></td>
          <td style="text-align:right;">PostgreSQL <code>psycopg2==2.9.10</code></td>
        </tr>
        <tr>
          <td><strong>Authentication</strong></td>
          <td style="text-align:right;">TBD <code>TBD</code></td>
        </tr>
        <tr>
          <td><strong>Frontend</strong></td>
          <td style="text-align:right;">JavaScript, JSON, HTML5, CSS3</td>
        </tr>
        <tr>
          <td><strong>Styling</strong></td>
          <td style="text-align:right;">TBD <code>TBD</code></td>
        </tr>
        <tr>
          <td><strong>Media Storage</strong></td>
          <td style="text-align:right;">TBD <code>TBD</code></td>
        </tr>
        <tr>
          <td><strong>Static Files</strong></td>
          <td style="text-align:right;">Whitenoise <code>whitenoise==6.9.0</code></td>
        </tr>
        <tr>
          <td><strong>Server</strong></td>
          <td style="text-align:right;">Gunicorn <code>gunicorn==23.0.0</code></td>
        </tr>
        <tr>
          <td><strong>Image Handling</strong></td>
          <td style="text-align:right;">TBD <code>TBD</code></td>
        </tr>
      </table>
    </td>
    <td valign="top" style="padding-left: 20px;">
      <h3>Other Dependencies</h3>
      <ul style="list-style-type: none; padding-left: 0;">
        <li><code>asgiref==3.8.1</code></li>
        <li><code>packaging==24.2</code></li>
        <li><code>setuptools==76.0.0</code></li>
        <li><code>sqlparse==0.5.3</code></li>
        <li><code>typing_extensions==4.12.2</code></li>
        <li><code>tzdata==2025.1</code></li>
        <li><code>django-summernote==0.8.20.0</code></li>
      </ul>
    </td>
  </tr>
</table>

[Back to Top](#ux)

### Tools

<!--- [Github](https://github.com/): Used to host source code and version control.
- [VSCode](https://code.visualstudio.com/): Used as Integrated Development Environment (IDE).
- [Font Awesome](https://fontawesome.com/): Source of all the icons used in this project.
- [Favicon io](https://favicon.io/favicon-converter/): Used to generate the favicon.
- [TBD](): Used to create the wireframes.
- [TBD](): Used to compress each image used in the project for optimal load times.
- [AssignmentGPT AI](https://assignmentgpt.ai/): Used to create the Entity Relationship Diagram (ERD).
- [TBD](): Used for animations on 404 page.-->

<!--### Packages
- [Django](https://www.djangoproject.com/) was used as the framework for the blog.
- [Allauth](https://django-allauth.readthedocs.io/) for the login authentication.
- [Crispy Forms](https://django-crispy-forms.readthedocs.io/) for help styling the forms.
- [Cloudinary](https://cloudinary.com/) for hosting the images.
- [Gunicorn](https://gunicorn.org/) for handling the HTTP requests in production.
- [Psycopg2](https://www.psycopg.org/) for aiding communication between Django and PostgresSQL
- [Formtools](https://django-formtools.readthedocs.io/) for additional form utilities.-->

[Back to Top](#ux)

## Testing

[Back to Top](#ux)

## Bugs

### Fixed Bugs

<details>
    <summary>Development Phase</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Bug</th>
                    <th>Solution</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>Application Error in Heroku [H10]</td>
                    <td>Resolved by amending the project name in the Procfile</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Virtual Environment Pushed to GitHub</td>
                    <td>Resolved using git rm command in terminal</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Summernote 404 Error</td>
                    <td>Resolved by setting DEBUG to True</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

<details>
    <summary>Deployment Phase</summary>
    <div style="display: flex; justify-content: center;">
        <div style="overflow-x: auto; width: 80%;">
            <table style="margin: 0 auto; border-collapse: collapse; width: 100%;">
                <tr>
                    <th>Bug</th>
                    <th>Solution</th>
                    <th>Pass/Fail</th>
                </tr>
                <tr>
                    <td>Error Loading Django Template</td>
                    <td>Resolved by moving index.html to correct directory and updating template_name</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Error Loading Static CSS</td>
                    <td>Resolved by setting DEBUG to True</td>
                    <td>Pass</td>
                </tr>
                <tr>
                    <td>Django Admin Images Not Loading To Heroku</td>
                    <td>Resolved by setting DEBUG to True</td>
                    <td>Pass</td>
                </tr>
            </table>
        </div>
    </div>
</details>

[Back to Top](#ux)

## Deployment

[Back to Top](#ux)

## Credits

### [Content](#content)
- [Spence's README](https://github.com/5pence/djangohelp/blob/main/readme.MD) was useful for setting up Django on my Windows machine.

- [Dimitris' README](https://github.com/Dimitris112/rum-away-testp4/blob/main/README.md) inspired the use of toggle view for tables.

- [Dan's README](https://github.com/DanMorriss/nialls-barbershop/blob/main/README.md) inspired some of the descriptions used in my write up.

- [StoriesOnBoard Blog](https://storiesonboard.com/blog/user-story-examples) inspired some of the language used in my User Stories write up.

- [Maria Pavlenko's Blog](https://www.altexsoft.com/blog/user-stories/) inspired some of the language used in my User Stories write u and template.

### [Media](#media)

### [Code](#code)
- [Code Institute's Codestar Blog Walkthrough]() inspired the idea for this project and informed all steps in respect to setting and wiring up the database, coding with Django and Python, Bootstrap, setting up environment variables and serving static files.

- [Ragas Imger's Stack Overflow Contribution](https://stackoverflow.com/questions/76558562/how-do-i-upload-a-picture-to-my-blog-using-the-django-administration) inspired the method used to render images directly through Django Administration.

[Back to Top](#ux)

## Acknowledgements

[Back to Top](#ux)