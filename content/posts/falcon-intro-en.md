Slug: falcon-intro
Title: Going slim with Falcon
Category: Je tisse ma toile
Tags: développement, Falcon, Python, web, un peu compliqué quand même
Date: 2018-08-06
Summary: First contact with Falcon backend framework
Image: /images/falcon_logo.svg
Lang: en
Status: published

___

![Falcon logo][falcon-logo]

In one of those many "let's reconsider everything" periods I've experienced
throughout my project, some new technical choices have brought into question my
use of the most famous of Python web frameworks ([Django][django]), and brought
into consideration a much more minimalist framework, whose little name is
[Falcon][falcon].

Let's start by reminding that a few months ago I still didn't know anything in
web development (even the difference between frontend and backend was a mystery
to me), and even though starting with Django helped me a lot learning through
that at my own pace, it now seems a bit overkill for the few tasks that will
now be handled by my backend.

I might develop that point in a future article, but here's me exploring a new
tool, and sharing my thoughts and findings might be useful.

Anyhow, let's cut the talk.


## My architecture

Having finally discovered the benefits of a genuine frontend framework, I
realize how valuable it would be now to drastically restrict the role of the
backend, which was in charge of everything until now : authentication, sessions
handling, page render, data validation, form handling, admin site generation,
database migrations, internationalization, localization, ... Props to Django for
that.

This time, I'll keep to the bare minimum :

* database management
* data validation
* RESTful API management
* authentication

That list might grow up as I advance in time, but the minimalist approach of
Falcon is therefore quite appealing to me ; I'm the only captain onboard, and
it seems reasonable enough to handle all those tasks myself now that I almost
start to get a glimpse of what happens within a web server.

## Installation

### Procedure

Everything starts by creating a virtual environment :

    :::sh
    # theenglishway @ time in ~/Documents [9:05:01]
    $ mkdir falcon

    # theenglishway @ time in ~/Documents [9:06:30]
    $ cd falcon

    # theenglishway @ time in ~/Documents/falcon [9:06:31]
    $ python3 -m venv ./.venv

    # theenglishway @ time in ~/Documents/falcon [9:06:47]
    $ source .venv/bin/activate

Then [the official page installation instructions][falcon-install] will be your
best guide, and you might add the excellent [HTTPie][httpie] utility, which will
be very convenient to chat with the API (and is recommended by Falcon developers).

    :::sh
    (.venv)
    # theenglishway @ time in ~/Documents/falcon [9:22:10]
    $ pip install falcon gunicorn httpie

It's a good moment to also create a requirements.txt file

    :::sh
    (.venv)
    # theenglishway @ time in ~/Documents/falcon [9:22:10]
    $ pip freeze > ./requirements.txt

... and initialize the git repo, the .gitignore, and so on. I like having a
non-versioned `.envsetup` file with all the environment variables, and that allows
activating the virtual environment through a simple `source .envsetup`.

    :::sh
    source .venv/bin/activate
    # Variables such as DEBUG=1 will come here

### Basic check

The [official site examples][falcon-examples] are useful to check that
everything is in order.

    :::sh
    (.venv)
    # theenglishway @ time in ~/Documents/falcon on git:master x [9:58:33]
    $ http :8000/things
    HTTP/1.1 200 OK
    Connection: close
    Date: Sun, 08 Jul 2018 07:58:47 GMT
    Server: gunicorn/19.9.0
    content-length: 100
    content-type: application/json; charset=UTF-8

    Two things awe me most, the starry sky above me and the moral law within me.

        ~ Immanuel Kant

    (.venv)
    # theenglishway @ time in ~/Documents/falcon on git:master x [10:03:16]
    $ http localhost:8000/1/things authorization:custom-token
    HTTP/1.0 200 OK
    Date: Sun, 08 Jul 2018 08:03:40 GMT
    Server: WSGIServer/0.2 CPython/3.5.3
    content-length: 66
    content-type: application/json; charset=UTF-8
    powered-by: Falcon

    [
        {
            "color": "green",
            "id": "fc9aee6e-5f2c-46e7-bb5e-1535475f2220"
        }
    ]

Well that seems OK ... what now ?

## First steps

The official site has a [nice little tutorial][falcon-tutorial] that seemed
good enough to me and can be recommended.

Several points stand out.

**First** is that the baremetal aspect is no joke ! No need to invoke Django's
black sorcery, the server can be launched from command line and debugged with
your favorite tools :

    :::sh
    (.venv)
    # theenglishway @ time in ~/Documents/falcon on git:master x [10:19:12] C:1
    $ gunicorn --reload myapp/app.py
    [2018-07-08 11:29:38 +0200] [13216] [INFO] Starting gunicorn 19.9.0
    [2018-07-08 11:29:38 +0200] [13216] [INFO] Listening at: http://127.0.0.1:8000 (13216)
    [2018-07-08 11:29:38 +0200] [13216] [INFO] Using worker: sync
    [2018-07-08 11:29:38 +0200] [13219] [INFO] Booting worker with pid: 13219

That allows setting up a nice and handy development environment (for instance
using [Pycharm **Community Edition**][pycharm]) :

![Pycharm et Falcon][pycharm-falcon]

As for the rest you really feel "naked" ! The slightest unit test on an API that
returns a simple JSON array requires you to write such code as
`result = json.loads(response.content.decode())`.

Server side, some basic features are included like
[decoding content sent by the client][falcon-media], but only JSON is supported.
For any other types, you'll need to decode the binary stream using your bare
hands.

**Second** is that even the tutorial points the importance of tests, and that's
always a good point for me!

**Third** is that everything seems clear enough and consistent, and only a few
concepts are involved : **_requests_**, **_responses_**, **_routing_** (nothing
unusual for a web developer), **_middleware_** (a common sight in backend). The
central concept is that of the **_resource_** which as its name implies
designates the object one wishes to get, modify or create (just as in RESTful
terminology) ; **_routes_** will be directly connected to them. Last but not
least, **_hooks_** can be defined to factorize code related to a specific
resource or request type.

Worth noting is that almost everything is implemented through duck-typing ; for
instance, a middleware class will not need to inherit from any specific object
(unlike Django, with [everything it implies][django-cbv] in terms of methods and
classes you'll need to know like the back of your hand). It should only
implement some specific methods.

**Fourth and final point** is that there's some work ahead ! I'll need to get to
know all the main Python libraries in order to handle everything that what was
included in Django ... But that's all the benefit of such a minimalist framework
to be able to browse through the Python ecosystem and pick solutions that are
usually much more advanced than those from the Django ecosystem. And they are
still easy to integrate, in contrast to other little frameworks that often
require an adaptation layer for those libraries. With Falcon you can choose
whatever you want and integrate it whichever way you want.

Which means, many other articles are on their way !

[erasing-all]: {filename}/content/on-efface-tout.md
[falcon-logo]: {filename}/images/falcon_logo.svg
[falcon-install]: https://falcon.readthedocs.io/en/stable/user/install.html#install
[httpie]: https://github.com/jkbr/httpie
[falcon-examples]: https://falcon.readthedocs.io/en/stable/user/quickstart.html
[falcon-tutorial]: https://falcon.readthedocs.io/en/stable/user/tutorial.html
[falcon]: https://falconframework.org/
[falcon-media]: https://falcon.readthedocs.io/en/stable/api/media.html#media
[pycharm-falcon]: {filename}/images/pycharm-falcon.png
[django-cbv]: https://ccbv.co.uk/
[django]: https://www.djangoproject.com/
[pycharm]: https://www.jetbrains.com/pycharm/download/
[flask]: http://flask.pocoo.org/
[bottle]: https://bottlepy.org/docs/dev/
