# Social Network

Social Network is a REST API with implemented token authentication (JWT).


Features:

● user signup

● user login

● post creation

● post like

● post unlike

● analytics about how many likes was made. Example url
/api/analitics/?date_from=2020-02-02&date_to=2020-02-15 . API should return analytics aggregated
by day.

● user activity an endpoint which will show when user was login last time and when he mades a last
request to the service.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirement libraries.

```bash
pip install -r requirements.txt
```

## Usage

```python
# Create migrations for creating tables in the database
cd social_network  # make sure you are in the main social_network folder
python manage.py makemigrations
python manage.py migrate

# Run server
python manage.py runserver
```

## REST API screenshots from DRF UI and Postman
![POST_signup.jpg](screenshots%2FPOST_signup.jpg)
![POST_token.jpg](screenshots%2FPOST_token.jpg)
![GET_posts.jpg](screenshots%2FGET_posts.jpg)
![POST_posts.jpg](screenshots%2FPOST_posts.jpg)
![GET_analytics.jpg](screenshots%2FGET_analytics.jpg)
![POST_like.jpg](screenshots%2FPOST_like.jpg)