Title: SQLAlchemy, c'est pas sorcier !
Category: Le développement web pour les nuls
Tags: développement, SQLAlchemy, Python, web
Summary:
Image: /images/sqlalchemy_logo.png
Lang: fr
Status: draft

___

![Logo SQLAlchemy][sqlalchemy-logo]

Après plusieurs mois à me reposer sur l'ORM de Django, voici venu le temps de me
frotter à quelquechose d'un peu plus conséquent : la Rolls de l'ORM Python,
SQLAlchemy.

# Initialisation

Voilà quelquechose dont je m'étais fait une montagne en survolant la
documentation, et qui n'est pourtant pas si complexe que cela quand on
décompose bien les étapes. Je m'inspire très largement et sans aucune honte de
[cet excellent article expliquant SQLAlchemy aux habitués de Django][sqlalchemy-django]
et du [tutoriel disponible sur le site officiel][sqlalchemy-tutorial].

SQLAlchemy est un peu le couteau suisse de l'ORM, mais beaucoup de sa puissance
est cachée et ne sera invoquée directement que pendant l'initialisation. La
première étape consiste donc en l'établissement de la connexion avec la base
de données :

    :::python
    from sqlalchemy import create_engine

    engine = create_engine('sqlite:///./db.sqlite3', echo=True)

Dès ce moment, toute l'abstraction par rapport au type de base de données
manipulée est faite, et l'on a plus à s'en préoccuper. Visiblement on peut
décider d'interagir directement avec cet objet *Engine* dans les cas très
pointus, mais quand on utilise l'ORM, on peut s'en passer.

La deuxième étape consiste à décrire à SQLAlchemy les tables que nous allons
manipuler et les classes Python qui leur seront associées (et qui nous
permettront d'interagir avec la BDD sans écrire une ligne de SQL). Dans les
versions modernes de SQLAlchemy, cela se fait en une seule fois, en utilisant
une *declarative base class* fournie par la librairie et qui servira à déclarer
tous les modèles de l'application.

    :::python
    from sqlalchemy.ext.declarative import declarative_base

    Base = declarative_base()

Une fois que l'on dispose de cette base, on fait dériver tous nos modèles de
cette classe, et la magie de SQLAlchemy opère en arrière plan. Le principe se
rapproche beaucoup de celui utilisé dans l'ORM de Django, mais il y aura de base
plus de choses à expliciter (le nom de la table, la clef primaire, etc.)

    :::python
    from sqlalchemy import Column, Integer, String

    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)

Toutes les informations apportées de cette manière sont agrégées dans la *Base*
dont le champ "metadata" peut désormais être utilisé pour connecter tous les
morceaux (la connexion à la base de données, et la déclaration du schéma).

    :::python
    Base.metadata.create_all(engine)

Cette expression va à la fois créer la base de données (si elle n'existe pas
encore), les tables (si elles n'existent pas encore), et permettre d'utiliser
l'ORM. Le fait d'hériter de Base permettait déjà de créer des instances des
classes déclarées :

    :::ipython3
    In [1]: user = User(name="way", fullname="theenglishway")
    Out [1]: <User(name='way', fullname='theenglishway')>

... mais en tant que telles, elles ne peuvent être directement envoyées dans la
base de données (là où l'ORM de Django aurait déjà permis de faire
`user.save()`). Il faudra pour cela en passer par un dernier type d'objet
qui est au coeur de SQLAlchemy, la *session* ; elle représente véritablement
la connexion à la base de données, et toute transaction devra se faire au
travers d'une session. Ces sessions seront crées à partir d'une *factory* là
aussi fournie par la librarie, à laquelle on passe entre autres comme arguments
l'*engine* déclaré au tout début.

    :::python
    from sqlalchemy.orm import sessionmaker

    Session = sessionmaker(bind=engine)

Cette classe doit être gardée précieusement dans un coin de son code, car l'on
y fera appel dès lors que l'on voudra ouvrir une connexion, ce qui se fera
simplement via `session = Session()`.

Tout est maintenant en place pour pouvoir échanger avec la base de données, y
créer des entrées, effectuer des requêtes, etc. Il y a certes un peu plus à
écrire que pour le même résultat dans Django, mais ça reste finalement assez
simple une fois bien compris l'apport de chaque élément.

Voici à quoi ressemble le fichier complet :

    :::python
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from sqlalchemy import Column, Integer, String

    Base = declarative_base()


    # Ceci pourrait être déplacé dans un fichier à part type 'models.py' ou
    # n'importe quoi d'autre convenant à l'arborescence qu'on souhaite adopter
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

# Utilisation basique

Maintenant que l'on a une belle base de données avec une table vide, il ne reste
plus qu'à l'utiliser. Contrairement à Django qui faisait beaucoup pour nous dans
notre dos (pour le meilleur et pour le pire), SQLAlchemy nous laisse un peu plus
nous débrouiller.

La notion primordiale est celle de **_session_**. De nombreux articles et talks
expliquent en détails en quoi ce système est supérieur à celui utilisé par des
ORM plus basiques (comme celui de Django).

De ce que j'en comprends, au prix d'une utilisation peut-être un poil plus
complexe, il permet :

* de limiter le nombre de requêtes vraiment relayées à la base de données
* de complètement annuler une transaction en cours, au besoin
* d'assurer la cohérence au sein d'une transaction donnée, avant même la
moindre requëte

Un exemple vaut mille mots :

    :::ipython3
    # On crée une première session
    In [1]: session = Session()

    # ... dans laquelle on ajoute un utilisateur
    In [2]: session.add(User(name="way", fullname="theenglishway"))

    # Une query fait bien apparaître ce nouvel utilisateur
    In [3]: session.query(User).all()
    Out[3]: [<User(name='way', fullname='theenglishway')>]

    # On ouvre une autre session
    In [4]: session2 = Session()

    # L'ajout n'y est pas encore visible
    In [5]: session2.query(User).all()
    Out[5]: []

    # Mais dès que l'on commit l'autre session ...
    In [6]: session.commit()

    # L'utilisateur y apparaît
    In [7]: session2.query(User).all()
    Out[7]: [<User(name='way', fullname='theenglishway')>]

# Le cas des frameworks web

Petite subtilité importante à noter à propos des sessions utilisées dans le
cadre d'un framework web qui traite les requêtes en utilisant un thread donné :
il faut alors utiliser des [**_scoped sessions_**][sqlalchemy-sessions].


[sqlalchemy-django]: http://lucumr.pocoo.org/2011/7/19/sqlachemy-and-you/
[sqlalchemy-tutorial]: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html
[sqlalchemy-logo]: /images/sqlalchemy_logo.png
[sqlalchemy-sessions]: http://docs.sqlalchemy.org/en/latest/orm/contextual.html#using-thread-local-scope-with-web-applications
