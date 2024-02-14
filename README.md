# YT Relay API
This is a Simple Project Aimed at Simplifying the Process of Making a Custom YouTube Music Client.

The Approach here is to use the ytmusicapi library for Python to create and host a simple API that can be used in Various kinds of Frontends ranging from Native/Progressive Applications to Web Application.

## How to Use it?
### 1. Setting up Pipenv
Well, I recently started using pipenv and I love it, so I used pipenv here and you should too!
Install pipenv for you Platform. Visit [Pipenv Docs](https://pipenv.pypa.io/en/latest/) and follow the steps there.
As far as I know its only 
```bash
pip install --user pipenv
```
### 2. Installing Dependencies
Dependencies are listed in the `Pipfile` and `Pipfile.lock` files so installing them is really easy!!
```bash
pipenv install
```
### 3. Run the Damn Thing
#### Either One Line
Reccomended if you know it will work no matter what
```bash
pipenv run gunicorn --reload wsgi:app
```
#### or 2 Lines
Reccomended if you wanna debug and dont want to suffix `pipenv run` everytime
```bash
pipenv shell
```
```bash
gunicorn --reload wsgi:app
```