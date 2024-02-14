# YouTube Music Relay API
This is a Simple Project Aimed at Simplifying the Process of Making a Custom YouTube Music Client.

The Approach here is to use the ytmusicapi library for Python to create and host a simple API that can be used in Various kinds of Frontends ranging from Native/Progressive Applications to Web Application.

## Why this and and not the Official API or Invidious or etc?
- Increased Privacy because of Anonymity
- Better Developer Experience
- Can work well with any stack

#TODO: Add GPL License

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

## Contributing
Listen to me first! Don't force me to make a PR Filter Bot.
There can be several reasons why you might wanna consider contributing to this proect [<- Yes this is intentional and I won't fix this Spelling Mistake.]

### You want to fix a Urgent Issue with this Project
Yes, there are a lot of FOSS Proects that are great and might have some flaws, and this is how they takehelp from the community and fix those.
Follow these steps:
1. Search for the Issue you want to be fixed in this Repo
2. Check if any Issue comes up in the search, if not create one.
3. If it comes up, check the thread and try to understand what is the Actual issue and what are the patches and Etc.
4. Fork the Repo, clone it in your Station and fix the Issue in your fork and commit it. 
5. Make a PR, to push your Fix to us, we will review it and Merge it if required

### You want a Feature
Hmmm...A little better quality of Life improving fixes....Who does not want it??
Follow these steps:
1. Search for the Feature you want to be added in this Repo
2. Check if any Feature comes up in the search, if not create one.
3. If it comes up, check the thread and try to understand what is the Actual Feature request and what are the patches and Etc.
4. Fork the Repo, clone it in your Station, make a separate branch with branch name either your username or feature name and add the feature in your fork and commit it. 
5. Make a PR, to push your Feature to us, we will review it and Merge it if required.

The reason why creating a Seperate brnach is important is because, unlike issues is because we need time to check that will the feature break anything else in the code.