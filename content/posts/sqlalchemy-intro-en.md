Slug: sqlalchemy-intro
Title: SQLAlchemy is no sorcery !
Category: Le développement web pour les nuls
Tags: développement, SQLAlchemy, Python, web
Summary:
Image: /images/sqlalchemy_logo.png
Lang: en
Status: draft

___

![Logo SQLAlchemy][sqlalchemy-logo]

After several months using Django's ORM, the time has come to fiddle with a more
powerful toy : Python ORM's top-level library, SQLAlchemy.

## Init

Here's a topic that seemed like a huge deal skimming through the documentation,
but that is not all that difficult once the steps are well understood. I
shamelessly take inspiration from
[that excellent article explaining SQLAlchemy to Django users][sqlalchemy-django]
and the [official tutorial][sqlalchemy-tutorial].

SQLAlchemy is kind of the Swiss army knife of ORMs, but much of its power is
hidden and will be directly summoned only during init. First step is
establishing a connection with the database :

    :::python
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///./db.sqlite3', echo=True)

From now on, abstraction from the kind of database is dealt with, and it's not
even a concern anymore. One might need direct interactions with that *Engine*
object in corner cases, but that's usually not required when using the ORM.

Second step is describing to SQLAlchemy the tables that needs to be created
and the associated Python classes (which will allow us to interact with the
database without a single line of SQL limbo). In modern versions of SQLAlchemy,
that's a single-step operation done using a une *declarative base class*
provided by the library, and that as its name implies will be used to describe
all the application models.

    :::python
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

Once that base is available, one can derive all user-defined models from it,
and SQLAlchemy's magic takes place in background. This is quite close from
Django in principle, but several declarations will need to be explicit (the
table name, primary key, ...)

    :::python
    from sqlalchemy import Column, Integer, String

    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)

All the information provided there are aggregated into the *Base* whose
"metadata" field that now be used to assemble the whole puzzle (database
connection and schema declaration).

    :::python
    Base.metadata.create_all(engine)

This simple expression will simultaneously create the database, tables (if not
created yet), and allow use of the ORM. Inheriting from Base already allowed to
create instances of user defined classes :

    :::ipython3
    In [1]: user = User(name="way", fullname="theenglishway")
    Out [1]: <User(name='way', fullname='theenglishway')>

... but those instances cannot be directly sent into the database yet (Django's
ORM would have already allowed you to call `user.save()`). You will need another
kind of object for that, which is at the heart of SQLAlchemy, the *session* ;
the session basically makes the connection to the database, and any transaction
should be done using a session. Those session will be created from a *factory*
provided by the library, to which such arguments as the *engine* we encountered
in the first step should be provided.

    :::python
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)

This class should be kept easily accessible, for we'll need it every time a
connection should be open, which is done simply by `session = Session()`.

Everything is now setup for talking with the database, creating entries, making
queries, ... The init phase is a bit more verbose than in Django but does not
seem as complex once the individual role of each element is well understood.

Here's what the whole init file looks like :

    :::python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

    Base = declarative_base()

    # This should be moved to another file like 'models.py' or anything
    # convenient in the file tree we defined
    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)

        def __repr__(self):
            return "<User(name='{}', fullname='{}')>".format(self.name, self.fullname)

    engine = create_engine('sqlite:///./sqlite3.db', echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

## Basic use

We now have a pretty database with empty tables ; we just have to use it. Unlike
Django that did lots of mysterious stuff in you back (for better and for worse),
SQLAlchemy provides us with plenty of powerful choices.

The most fundamental notion is that of the **_session_**. Tons of articles and
talks go into great lengths to explain how this concept is much more powerful
than the one provided by more basic ORMs (such as Django's).

As far as I understand, and at the cost of a slightly more complex use, it
allows :

* limiting the number of requests that are effectively sent to the database
* rolling-back an entire transaction if needed
* ensure consistency within a given transaction, well before the first request
is sent

An example is worth a thousand words :

    :::ipython3
    # A first session is created
    In [1]: session = Session()

    # ... in which a user is added
    In [2]: session.add(User(name="way", fullname="theenglishway"))

    # A query returns that user
    In [3]: session.query(User).all()
    Out[3]: [<User(name='way', fullname='theenglishway')>]

    # Another session is open
    In [4]: session2 = Session()

    # The new user is not visible yet
    In [5]: session2.query(User).all()
    Out[5]: []

    # But as soon as the first session is commit ...
    In [6]: session.commit()

    # The user appears in the second session !
    In [7]: session2.query(User).all()
    Out[7]: [<User(name='way', fullname='theenglishway')>]

## The special case of web frameworks

It is worth noting a little subtlety about sessions when they are used in the
environment of a web framework that handles request in a given thread : one
should take care to use [**_scoped sessions_**][sqlalchemy-sessions]
in that case.


[sqlalchemy-django]: http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
[sqlalchemy-tutorial]: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
[sqlalchemy-logo]: /images/sqlalchemy_logo.png
[sqlalchemy-sessions]: http://docs.sqlalchemy.org/en/latest/orm/contextual.html#using-thread-local-scope-with-web-applications
