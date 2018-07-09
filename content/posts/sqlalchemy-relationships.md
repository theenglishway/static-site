Title: SQLAlchemy : papa, comment on fait les relations ?
Category: Le développement web pour les nuls
Tags: développement, SQLAlchemy, Python, web
Summary:
Image: /images/sqlalchemy_logo.png
Lang: fr
Status: draft

___

![Logo SQLAlchemy][sqlalchemy-logo]


Maintenant que l'on a
[une belle base de données toute propre et de quoi faire des modèles basiques][sqlalchemy-intro],
il va peut être falloir un peu étoffer tout ça. Parce qu'une base de données
sans relation entre les modèles, ça n'a pas grand intérêt.

Là aussi, les choses vont être un peu plus compliquées que dans Django, où
comme d'habitude Django faisait beaucoup de choses dans notre dos. Et de
nouveau, certaines choses vont devoir être explicitées.

Je vais de nouveau conseiller
[l'excellent tutorial officiel][sqlalchemy-tutorial-relationship].

## Déclaration des relations

Dans le cadre d'une relation entre deux objets, il y a deux notions
complètement différentes que Django ne m'avait pas vraiment habitué à distinguer,
et qu'il faudra donc déclarer explicitement dans SQLAlchemy : celle de
`ForeignKey` et celle de `relationship`.

La `ForeignKey` est simplement la `PrimaryKey` d'une autre table, qui permet
donc d'identifier de manière unique un objet d'un autre type avec lequel existe
une relation. L'établissement d'une `relationship`, quant à lui, se fait au
niveau de l'ORM, et va nous permettre de récupérer directement une instance de
l'objet de l'autre table avec lequel on est en relation.

En pratique, déclarer une relation entre deux objets ressemble à ça (ici, une
relation 'one-to-many' de `User` vers `Thing`)

    :::python
    class User(Base):
        __tablename__ = 'users'

        id = Column(Integer, primary_key=True)
        name = Column(String)
        fullname = Column(String)

        def __repr__(self):
            return "<User(name='{}', fullname='{}')>".format(self.name, self.fullname)

    class Thing(Base):
        __tablename__ = 'things'

        id = Column(Integer, primary_key=True)
        name = Column(String)

        # Déclaration de la ForeignKey
        user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

        # Déclaration de la relationship
        user = relationship('User', backref='things')

        def __repr__(self):
            return "<Thing(name={})>".format(self.name)

L'avantage de ce petit surplus de verbosité est qu'il permet beaucoup plus de
souplesse ; si la `ForeignKey` se déclare toujours du côté 'many' d'une relation,
la `relationship` peut se déclarer d'un côté comme de l'autre, avec les noms
que l'on souhaite ... voire ne pas se déclarer du tout si elle n'est pas utile.

SQLAlchemy permet d'ailleurs d'utiliser deux mots clés différents pour déclarer
la relation réciproque : `backref`, qui crée automatiquement le champ réciproque
sur l'objet lié (ici `things` sur `User`), et `back_populates`, qui ne le fait
pas (il faudrait en plus des déclarations ci-dessus écrire explicitement
`things = relationship('Thing', back_populates='user')` dans la classe `User`).

`relationship` prend [de nombreux arguments optionels][sqlalchemy-relationships]
qui permettent une immense souplesse d'utilisation.

## Utilisation

Alors là

    :::python
    user = User(name='theenglishway', fullname='theenglishway')
    user.things = [Thing(name='something')]
    dbm.Session.add(user)
    dbm.Session.commit()


[sqlalchemy-intro]: {filename}sqlalchemy-intro.md
[sqlalchemy-tutorial-relationship]: https://docs.sqlalchemy.org/en/latest/orm/tutorial.html#building-a-relationship
[sqlalchemy-logo]: /images/sqlalchemy_logo.png
[sqlalchemy-relationships]: https://docs.sqlalchemy.org/en/latest/orm/relationship_api.html#sqlalchemy.orm.relationship
