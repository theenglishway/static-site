Title: Cure de minceur avec Falcon
Category: Je tisse ma toile
Tags: développement, Falcon, Python, web, un peu compliqué quand même
Date: 2018-08-06
Summary: Premier contact avec le framework backend Falcon
Image: /images/falcon_logo.svg
Lang: fr
Status: published

___

![Falcon logo][falcon-logo]

_Comme l'indique un de ses tags, et contrairement à ceux écrits jusqu'à maintenant,
cet article est technique et pas du tout destiné à faire de la "vulgarisation",
et ce sera certainement le cas de la plupart des prochains articles !_

Dans [une énième phase de remise à plat de l'architecture de mon projet][erasing-all],
certains nouveaux choix techniques m'ont amené à remettre en question mon
utilisation du plus connu des frameworks web Python ([Django][django]), et à
basculer sur un framework des plus minimalistes (et pas forcément parmi les
alternatives les plus connues, comme Flask ou Bottle),
du petit nom de [Falcon][falcon].

Précisons d'emblée qu'il y a quelques mois, je ne connaissais RIEN au
développement web (même la différence entre frontend et backend était un
mystère pour moi), et si partir sur Django m'a énormément aidé à démêler tout
ça à mon rythme, il me semble maintenant un peu "overkill" pour accomplir les
tâches que je souhaite désormais déléguer au backend.

Je reviendrai peut être sur tout ça dans un prochain article, mais me voilà
donc parti dans l'exploration d'un nouvel outil, et partager mes découvertes
et réflexions peut être utile.

Bref, trêve de blabla.

## Mon architecture

Après avoir enfin découvert les joies d'un "vrai" framework frontend, je me dis
qu'il pourrait être profitable désormais de sévèrement limiter le travail du
backend, que je laissais absolument tout faire jusque là : authentification, gestion de
sessions, rendu des pages, validation des données, gestion des formulaires,
génération du site d'administration, gestion
automatisée des migrations de la base de données, internationalisation,
localisation, etc. (merci Django).

Cette fois, je repars sur du très basique :

* interaction avec la base de données
* validation des données
* présentation d'une jolie API RESTful
* authentification

La liste se complétera peut-être au fur et à mesure de mon avancement, mais du
coup l'approche très minimaliste de Falcon me plaît bien, dans la mesure où
on est seul maître à bord, et qu'il me paraît raisonnable de m'y attaquer
maintenant que j'ai l'impression d'enfin vaguement comprendre ce qui se passe
dans un serveur Web.

## Installation

### Procédure

On commence par se créer un petit environnement virtuel :

    :::sh
    # theenglishway @ time in ~/Documents [9:05:01]
    $ mkdir falcon

    # theenglishway @ time in ~/Documents [9:06:30]
    $ cd falcon

    # theenglishway @ time in ~/Documents/falcon [9:06:31]
    $ python3 -m venv ./.venv

    # theenglishway @ time in ~/Documents/falcon [9:06:47]
    $ source .venv/bin/activate

Puis on peut suivre gentiment les
[instructions d'installation de la page officielle][falcon-install] et
ajouter aussi l'excellent utilitaire [HTTPie][httpie] qui est recommandé par les
développeurs de Falcon (et sera bien pratique pour communiquer avec l'API).

    :::sh
    (.venv)
    # theenglishway @ time in ~/Documents/falcon [9:22:10]
    $ pip install falcon gunicorn httpie

C'est aussi le bon moment pour créer un fichier requirements.txt

    :::sh
    (.venv)
    # theenglishway @ time in ~/Documents/falcon [9:22:10]
    $ pip freeze > ./requirements.txt

... et pour créer son repo git, le .gitignore qui va bien, etc. Personnellement
j'aime bien avoir un fichier non versionné `.envsetup` qui contient les
variables d'environnement et permet aussi d'activer le virtualenv par un simple
`source .envsetup`.

    :::sh
    source .venv/bin/activate
    # Des variables comme DEBUG=1 viendront s'ajouter ici

### Vérification

On peut déjà se rassurer avec les [exemples du site officiel][falcon-examples]
histoire de vérifier que tout marche bien.

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

Bon, ça semble aller ... Et maintenant ?

## Premiers pas

Le site officiel propose un [petit tutorial][falcon-tutorial] qui m'a semblé
plutôt bien fichu, et que je recommande.

J'en retiens plusieurs points.

**Le premier**, c'est que c'est vraiment du baremetal ! Pas besoin d'invoquer
toute la machinerie cachée d'un Django, on peut lancer l'application en ligne
de commande et debugger le tout avec ses outils préférés :

    :::sh
    (.venv)
    # theenglishway @ time in ~/Documents/falcon on git:master x [10:19:12] C:1
    $ gunicorn --reload myapp/app.py
    [2018-07-08 11:29:38 +0200] [13216] [INFO] Starting gunicorn 19.9.0
    [2018-07-08 11:29:38 +0200] [13216] [INFO] Listening at: http://127.0.0.1:8000 (13216)
    [2018-07-08 11:29:38 +0200] [13216] [INFO] Using worker: sync
    [2018-07-08 11:29:38 +0200] [13219] [INFO] Booting worker with pid: 13219

Mais on peut du coup avoir un petit environnement de développement bien pratique
(ici avec [Pycharm **Community Edition**][pycharm]) :

![Pycharm et Falcon][pycharm-falcon]

En dehors on est effectivement vraiment "à poil" ! Le moindre petit test unitaire
sur une API qui renvoie un bête tableau en JSON nécessite de
sortir des lignes comme `result = json.loads(response.content.decode())`.

Côté serveur, quelques petits trucs sont proposés de base comme
[le décodage du contenu envoyé par le client][falcon-media], mais seul le JSON
est supporté de base ; pour d'autres types, il faudra aller décoder le stream
binaire "à la main".

**Le second**, c'est que dès le tutorial, ils mettent l'accent sur l'importance
des tests, et ça me plait bien !

**Le troisième**, c'est que tout paraît assez clair et cohérent, et qu'il n'y a
que peu de concepts à maîtriser : les **_requêtes_**, les **_réponses_**,
le **_routage_** (rien de bien mystérieux pour un dev-web), les **_middlewares_**
(classiques en backend). Le concept central est celui de **_ressource_** qui
comme son nom l'indique représente
l'objet qu'on souhaite récupérer, modifier ou créer (et il a le même sens que
dans la terminologie RESTful), et auquel on associera directement une **_route_**.
S'ajoutent juste à tout cela les **_hooks_** qui à première vue seront utiles pour
factoriser du code sur une ressource particulière ou certaines requêtes
spécifiques.

Accessoirement, presque tout fonctionne via le principe du duck-typing ; une
classe de middleware par exemple n'aura pas besoin de dériver d'un objet
particulier (à la Django, et avec [tout ce que ça implique][django-cbv] comme
méthodes et classes à connaître plus ou moins par coeur),
mais simplement d'implémenter quelques méthodes particulières.

**Le quatrième et dernier**, c'est qu'il y a du boulot pour la suite ! Il va
falloir faire connaissance avec toutes les librairies Python classiques pour gérer
tout ce qui était inclus de base dans Django ... Mais c'est tout l'avantage d'un
framework aussi minimaliste, qui permet d'aller piocher dans l'écosystème Python
des solutions généralement bien plus évoluées que celles proposées dans
l'écosystème Django ... tout en étant facilement intégrables, contrairement aux
autres petits frameworks qui proposent souvent dans leur écosystème des couches
d'adaptation de ces libraries. Avec Falcon, on choisit ce qu'on veut et on
l'intègre comme on veut !

D'autres articles à suivre, donc !


[erasing-all]: {filename}on-efface-tout.md
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
