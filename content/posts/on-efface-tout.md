Title: On efface tout et on recommence
Category: 3615 ma vie mon oeuvre
Tags: 3615, facile !, logiciel, programmation
Date: 2018/08/01 18:00
Modified: 2018/08/01 18:00
Summary: De mon code faisons table rase
Image: /images/house_of_cards.jpg
Lang: fr
Status: published

___

![Allez hop][house-of-cards]

Comme je le disais dans [mon premier article][blog-first], me voilà donc lancé
depuis plusieurs mois dans un grand projet de plateforme web. Et pour la 4e (?)
fois, je jette presque tout le code que j'ai écrit pour repartir de
zéro ; principe qui peut paraître saugrenu à ceux qui ne connaissent pas le
domaine, et même auprès de certains de mes anciens camarades codeurs ! C'est
par ailleurs une pratique qui ne semble manifestement pas très populaire
auprès de la plupart
des responsables - je ne l'avais vu appliquée en entreprise qu'une ou deux
fois en 8 ans d'expérience, malgré le temps souvent considérable perdu par tous
ceux qui continuaient à travailler sur le code qu'on leur imposait.

## Euh ... faire du code, ça consiste en quoi en fait ?

Avant de rentrer plus dans le pourquoi du comment, il peut être utile pour les
néophytes qui auraient atterri sur cette page (à qui je recommande déjà mon
[précédent article sur le sujet][software-what]) en quoi consiste grosso modo (et
en théorie) le "cycle de production" d'un logiciel / code informatique ... qu'on va
se contenter de définir comme étant la traduction d'un besoin ou d'une fonctionnalité
qu'on exprime généralement "en français" dans un langage (dit
**_langage de programmation_**) qui est à la fois - plus ou moins -
manipulable par un humain ET automatiquement traduisible en quelque chose
qu'une machine pourra comprendre.

Par exemple, le besoin
"_Calcule-moi le pourcentage d'augmentation de telle valeur x par rapport à telle valeur y_" pourra se traduire ainsi :

```
def pourcentage_augmentation(avant, apres):
    return 100.0 * (apres - avant) / avant
```

... ou encore, dans un autre langage :

```
float pourcentage_augmentation(int avant, int apres) {
    return 100.0f * (apres - avant) / avant;
}
```

Le travail du programmeur s'arrête normalement à l'écriture de ce genre de code
là ; c'est évidemment un exemple
très simple, pas très représentatif de la réalité, mais ce n'est tout de même
pas aussi obscur que l'on se le répresente, et presque lisible pour peu que l'on
parle anglais (et que le code soit bien écrit).

On utilise ensuite différents outils qui traduisent cela en langage machine,
ce qui donne ça :

```
31 c0 c3 66 2e 0f 1f 84
00 00 00 00 00 0f 1f 00
f3 c3 66 2e 0f 1f 84 00
00 00 00 00 0f 1f 40 00
29 fe 66 0f ef c0 66 0f
ef c9 f3 0f 2a c6 f3 0f
59 05 8e 00 00 00 f3 0f
2a cf f3 0f 5e c1 c3 90
```

Pardon, ça c'est la version complètement imbitable pour un humain ...
En version "_vaguement compréhensible pour ceux qui aiment vraiment ça_", ça
ressemble plutôt à ça :

```
pourcentage_augmentation:
        sub             esi, edi
        pxor            xmm0, xmm0
        pxor            xmm1, xmm1
        cvtsi2ss        xmm0, esi
        mulss           xmm0, DWORD PTR .LC0[rip]
        cvtsi2ss        xmm1, edi
        divss           xmm0, xmm1
        ret
.LC0:
        .long           1120403456
```

Limpide, non ?

## Et en pratique, ça se passe comment ?

Enormément de littérature et de travaux a été consacré à l'ingéniérie
logicielle, soit la question : "comment
passer du besoin au code (sans passer par la case "Départ", le plus vite et le
plus efficacement possible)" ... sans qu'ils ne soient nécessairement beaucoup
utilisés en pratique, malheureusement, alors que [certains ouvrages][knuth] qui font
[encore référence][mythical] datent de plus de 40 ans.

On peut quand même discerner quelques étapes indispensables par lesquelles
tout le monde passe, consciemment ou inconsciemment :

* **définition / analyse du besoin** : est-ce qu'on a bien tout prévu, est-ce que
c'est vraiment ce que l'on veut faire, est-ce qu'on a bien compris ce que veut
faire l'éventuel client ?
* **spécification** : que faire pour que cela réponde au besoin ?
* **conception haut niveau** : comment le faire en découpant le tout en un ensemble de
petits problèmes plus faciles à résoudre ?
* **conception bas niveau** : comment fait-on chacun des petits bouts ?
* **développement** : on écrit le code correspondant

A ces phases descendant du besoin vers la réalisation correspondent des phases
remontant de la réalisation vers le besoin, qui y répondent en "miroir", et qui
sont généralement situées après, temporellement parlant :

* **test unitaire** : on vérifie que les petits bouts font bien ce qu'on veut
* **test d'intégration** : on vérifie que les petits bouts fonctionnent bien ensemble
* **test de validation** : on vérifie que l'ensemble des petits bouts fait bien ce
que l'on voulait
* **recette** : on vérifie que cela correspond bien au besoin

Je n'ai rien ici décrit d'autre que le bon vieux [cycle en V][V-cycle], que tous
les ingénieurs de France et de Navarre (et de plus loin encore) connaissent
forcément.

## Nan mais, la vraie pratique ?

Bon, ça c'était la théorie ...

En pratique ces étapes sont plus ou moins
formalisées (puisqu'on est pas seul à travailler, il peut-être utile de rédiger
des documents à l'intention de ceux qui utiliseront notre travail à une autre
étape du cycle), appliquées avec plus ou moins de rigueur, et parfois
certaines sont tout bonnement sautées, selon les contraintes, les habitudes, la
culture d'entreprise, ou les normes auxquelles il faut se conformer.
Parfois elles se suivent à la queue leu-leu ;
parfois on se permet de revenir en arrière pour se demander si le travail des
étapes précédentes n'est pas à revoir ; parfois on commence par écrire des tests
avant même de commencer le développement. Cela a tendance à devenir un sujet
en soi, dans lequel toutes les contributions ne sont pas très pertinentes.

Pour mon propre cas, l'organisation est énormément facilitée par le fait que je
suis encore seul maître à bord ; et avec le recul, je retiens surtout de la théorie quelques
principes de bon sens, qui me paraissent applicables à tout
problème important : **décomposition en sous-problèmes plus simples**,
**vérification de son travail, de l'assemblage du tout**, ... d'autant plus pertinents qu'ils permettent à terme la
répartition du travail entre plusieurs personnes, plusieurs équipes, voire
plusieurs entreprises différentes, qui n'ont pas nécessairement besoin
d'échanger en permanence pour avancer chacune de leur côté et produire un
ensemble cohérent (là encore c'est de la théorie). En tous les cas,
**"perdre" du temps en réfléchissant à la manière de s'organiser pour la suite en fait souvent gagner énormément**, au final.

Pour autant, et comme dans bien d'autres cas, il faut **trouver un équilibre** entre
rigueur du suivi de ces principes (pour ce qu'ils apportent au long terme) et
souplesse dans leur application (parce que le développement n'est pas un long
fleuve tranquille). Dans le logiciel il est bien plus facile que dans d'autres
domaines de **tatônner, explorer, teste rapidement différentes solutions**, et en
faisant cela on se retrouve souvent à reconsidérer les choix qu'on avait faits
au départ. Alors, comme si l'on bâtissait une maison ou un château de
cartes qui commence à bringuebaler parce qu'on a empilé trop d'étages, il faut
parfois savoir **reprendre une partie ou la totalité de zéro** avant que l'ensemble
ne s'effondre de soi-même (ou qu'il soit trop compliqué de continuer à monter).

Là aussi c'est une question d'équilibre, parce que nul travail ne saurait être
parfait ... Mais en ayant remis le compteur à zéro seulement 4 fois, je suis
encore raisonnable, non ?


[house-of-cards]: {filename}/images/house_of_cards.jpg
[blog-first]: {filename}blog-pour-quoi.md
[knuth]: https://www.amazon.fr/Computer-Programming-Volumes-1-4A-Boxed/dp/0321751043
[mythical]: https://www.amazon.fr/Mythical-Man-Month-Software-Engineering-Anniversary/dp/0201835959
[software-what]: {filename}le-logiciel-intro.md
[V-cycle]: https://fr.wikipedia.org/wiki/Cycle_en_V
