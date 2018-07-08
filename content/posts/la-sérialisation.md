Title: La sérialisation
Category: Le développement web pour les nuls
Tags: développement, Falcon, Python, web
Summary:
Lang: fr
Status: draft

___


Maintenant que j'ai réalisé que
[les premiers pas avec SQLAlchemy ne se passaient pas aussi mal que je l'aurais pensé][sqlalchemy-intro],
vient le moment de faire interagir la base de
données avec Falcon. Par exemple, renvoyer la liste des utilisateurs quand on
fait un GET sur l'adresse `/api/users/`.

Aussi croyais-je bêtement pouvoir écrire un truc du genre :

    :::python
    from .models import User

    class Resource(object):
        def on_get(self, req, resp):
            users = req.db.query(User).all()
            resp.body = json.dumps(users, ensure_ascii=False)

Mais *bizarrement* ce n'est pas aussi simple :

    :::python
    Traceback (most recent call last):
      File "/home/theenglishway/Documents/falcon/.venv/lib/python3.5/site-packages/gunicorn/workers/sync.py", line 135, in handle
        self.handle_request(listener, req, client, addr)
      File "/home/theenglishway/Documents/falcon/.venv/lib/python3.5/site-packages/gunicorn/workers/sync.py", line 176, in handle_request
        respiter = self.wsgi(environ, resp.start_response)
      File "/home/theenglishway/Documents/falcon/.venv/lib/python3.5/site-packages/falcon/api.py", line 244, in __call__
        responder(req, resp, **params)
      File "/home/theenglishway/Documents/falcon/myapp/users.py", line 10, in on_get
        resp.body = json.dumps(req.session.query(User).all(), ensure_ascii=False)
      File "/usr/lib/python3.5/json/__init__.py", line 237, in dumps
        **kw).encode(obj)
      File "/usr/lib/python3.5/json/encoder.py", line 198, in encode
        chunks = self.iterencode(o, _one_shot=True)
      File "/usr/lib/python3.5/json/encoder.py", line 256, in iterencode
        return _iterencode(o, 0)
      File "/usr/lib/python3.5/json/encoder.py", line 179, in default
        raise TypeError(repr(o) + " is not JSON serializable")
    TypeError: <User(name='way', fullname='theenglishway')> is not JSON serializable

Quelques problèmes se conjuguent dans ma tentative naïve qui était vouée à
l'échec : une petite incompréhension de la réponse attendue par Falcon, et la
sérialisation des objets renvoyées par la base de données.

## L'objet `Response` de Falcon

Comme déjà dit dans un précédent article, Falcon n'est pas là pour nous mâcher
le travail ... pour autant il peut quand même faire quelques petites choses pour
nous si l'on utilise les bons champs de l'objet `Response` (l'objet `Request`
dispose des mêmes champs).

Pour le corps de la réponse, on doit faire le choix d'utiliser un des champs
suivants : `media`, `body`, `data`, ou `stream`.

### `stream`

Comme son nom l'indique, un *stream* binaire avec une méthode `read()`
permettant de le décoder. Utile pour les fichiers binaires de taille importante,
j'imagine.

### `data`

Une représentation binaire de la réponse. Pour les fichiers binaires de taille
moindre, style image ?

### `body`

Une représentation de la réponse sous forme de *string* ; Falcon nous fait alors
la bonté de l'encoder comme il faut derrière nous.

### `media`

Un objet de n'importe quel type, *du moment qu'il est sérialisable*, et qu'on
a enregistré sa méthode de sérialisation auprès de Falcon, qui de base ne
propose que la sérialisation JSON.

C'est donc très configurable mais de base un poil limité, et là aussi il y a
du boulot à faire à la main. Mais [la documentation][falcon-media] est très
bien fichue, et il suffit d'ajouter une classe avec des méthodes `serialize`
/ `deserialize` pour gérer n'importe quel type de contenu. C'est aussi là que
l'on pourra le valider.





2. Dans tous les cas, les objets renvoyés par SQLAlchemy ne sont pas sérialisables en JSON

Le premier problème n'est en plus un si l'on utilise l'attribut `media` plutôt que `body`.

[sqlalchemy-intro]: {filename}sqlalchemy-intro.md
[falcon-media]: https://falcon.readthedocs.io/en/stable/api/media.html#media
