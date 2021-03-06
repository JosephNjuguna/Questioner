# Questioner
 `language : Python`

**Badges**
---
[![Build Status](https://travis-ci.org/JosephNjuguna/Questioner.svg?branch=develop)](https://travis-ci.org/JosephNjuguna/Questioner)
[![Coverage Status](https://coveralls.io/repos/github/JosephNjuguna/Questioner/badge.svg)](https://coveralls.io/github/JosephNjuguna/Questioner)
[![Maintainability](https://api.codeclimate.com/v1/badges/014f3891087e4424bc08/maintainability)](https://codeclimate.com/github/JosephNjuguna/Questioner/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/014f3891087e4424bc08/test_coverage)](https://codeclimate.com/github/JosephNjuguna/Questioner/test_coverage)
## Getting started
---
This is a Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize
questions to be answered. Other users can vote on asked questions and they bubble to the top
or bottom of the log.

Visit the Questioner UI templates on :

https://josephnjuguna.github.io/Questioner/UI/templates/ 

Get the Questioner API on : 

https://questioner123.herokuapp.com/

## Prerequisites
what you need for the app to run ??

#### `postman`
#### `terminal of your choice`

**Installing**

1. open your terminal
2. copy the link below and clone this repo on your machine
```
git clone https://github.com/JosephNjuguna/Questioner.git
```
3. after cloning the repo open your change directory into this repo folder  by running following command :

```
cd Questioner
```

4. Setting up Virtualenv
   
   ```bash
    virtualenv venv

   ```

   Activation

   ```bash
    source venv/bin/activate
   ```

5. Installing dependencies

    ```bash
      pip install -r requirements.txt
    ```

**Running the App**

1. then run the following command on the terminal to start the app 

```
python run.py
```
5. Open Postman app  and  navigate into following api endpoints:

| FEATURES                          | API ENDPOINT                                           |
| --------------------------------- | ------------------------------------------------------ |
| user sign up                      | [POST] /api/v1/auth/signup                             |
| user log in                       | [POST] /api/v1/auth/login                              |
| user view upcoming meetups        | [GET] /api/meetups/upcoming                            |
| user view specific meetup details | [GET]   /api/v1/meetups/<meetup:id>/                   |
| user post question                | [POST] /api/v1/question                                |
| user RSVP for a meetup            | [POST] /api/v1/meetups/<meetup:id>/rsvps               |
| user get a specific question      | [GET] /api/v1/meetup/<meetup:id>/questions/<meetup:id> |
| admin post a question             | [POST] /api/v1/meetups                                 |
| user upvote question              | [PATCH]/questions/<question:id>/upvote                 |
| user downvote question            | [PATCH]/questions/<question:id>/downvote               |



**Running Test**
---
open the project with terminal/cmd and
at the root of the folder run 

`python -m pytest`

you will get to run atleast 12 test for the app

## What test are run during the test?

#### AUTHENTICATION
  1. USER LOG IN 
  1. USER SIGN UP

 #### MEETUP

1. USER RSVP FOR A MEETUP
2. USER GET SPECIFIC RECORDS OF A MEETUP
3. USER GET ALL UP COMING MEETUPS
4. USER GET RECORD OF SPECIFIC QUESTION IN A MEET UP
 
#### QUESTION
 1. USER CAN POST QUESTION
 2. USER CAN UPVOTE QUESTION 
 3. USER CAN DOWNVOTE QUESTION


### BUILT WITH:
>Flask - Python MicroFramework

>Python 3.6



## API VERSION
```
v1
```
### Authors 

JosephNjuguna
