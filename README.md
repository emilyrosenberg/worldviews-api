# Worldviews Backend

This is the Django backend for the Worldviews web app. Worldviews is a community for everyone who loves traveling the world. This structure makes it possible.<br>

The deployed backend can be found [here](https://worldviews-api1-2fa5e8a86642.herokuapp.com/). <br>

The live frontend site can be visited [here](https://worldviews-162453e10c7f.herokuapp.com/).
<hr>

<div align="left">
  <img src="assets/readme_images/entity-relationships.png" alt="Entity relationship diagram" width="">
</div>

Entity relationship diagram created with [LucidChart](https://www.lucidchart.com/pages/).

## Table of contents
- [Intro](#worldviews-backend)
- [Table of contents](#table-of-contents)
- [Apps](#apps)
- [Development](#development)
- [Testing](#testing)
- [Technologies used](#technologies-used)
- [Deployment](#deployment)
- [Credits](#credits)

## Apps
The backend was created with 9 interconnected apps.
### Main app (drf_api)
This is the main app, which includes settings, URL paths, and authorization.
### Profiles
This app is for user profiles. The user can add a username, profile picture (avatar), and a bio.
### Followers
This app is for following other users. The number of followers/follows is counted on the user's profile.
### Posts
This app is for user-generated posts. The user can create a post with an image, title, and content. The date shows automatically.
### Comments
This app is for commenting on posts. The number of comments shows on the post.
### Likes
This app is for liking posts. The number of likes shows on the post.
### Plans
This app is for user-generated plans. The user can create a plan with a title, content, and location.
### Plan Comments
This app is for commenting on plans. The number of comments shows on the plan. It is the same as the comment app for posts, but this structure ensures that each comment shows under the correct content.
### Locations
This app is for choosing a location when creating a plan.

## Development
### User Stories
Please see the [kanban board](https://github.com/users/emilyrosenberg/projects/7/views/1). 
### Bugs
Please see the [frontend readme](hhttps://github.com/emilyrosenberg/worldviews/blob/main/README.md#bugs).

## Testing
### Manual testing
CRUD functionality was tested manually across the site.

<div align="left">
  <img src="assets/readme_images/manual-testing.png" alt="Manual testing diagram" width="350">
</div>

### URLs Testing
All links were tested manually.

<div align="left">
  <img src="assets/readme_images/urls-testing.png" alt="URLs testing diagram" width="150">
</div>

_Thanks to [Jody Murray's PetFriends-API](https://github.com/JodyMurray/my-api?tab=readme-ov-file#manual-testing) for inspiration about testing documentation._

## Technologies Used
### Languages, libraries, and software
- asgiref
- black
- click
- cloudinary
- cryptography
- dj-database-url
- dj-rest-auth
- Django
- django-allauth
- django-cloudinary-storage
- django-cors-headers
- django-filter
- djangorestframework
- djangorestframework-simplejwt
- gunicorn
- oauthlib
- pathspec
- pillow
- psycopg2-binary
- PyJWT
- python3-openid
- ytz
- requests-oauthlib
- sqlparse
- urllib3

## Deployment

## Credits
This project was based on the Code Institute Django REST Framework walkthrough. Please see the frontend readme for [other credits](https://github.com/emilyrosenberg/worldviews/blob/main/README.md#credits)!
