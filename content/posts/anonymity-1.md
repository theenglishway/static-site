Slug: anonymity-1
Title: Pour en finir avec l'anonymat sur Internet (1)
Category: Mon avis sur tout (et surtout mon avis)
Tags: société, politique, opinion, internet
Date: 2019/01/29 21:15
Summary: Parce que c'est vraiment plus possible !
Image: /images/anonymous.png
Lang: fr
Status: published

---

![J'ai réussi à éviter le masque de Guy Fawkes comme illustration!][anonymous]

Dans l'**ensemble des critiques** que formulent à son encontre les gens qui ne 
connaissent pas 
grand chose à Internet, il en est une qui rencontre un succès certain auprès
des commentateurs de tout poil, surtout quand elle est assortie de 
formules magiques comme "réseaux sociaux" ou "fake news" : c'est celle de
**l'anonymat**, souvent présenté comme intolérable, permettant à des 
foules d'Internautes déchainés d'exprimer toute leur haine et leur violence 
en toute impunité (voir [cette belle compilation][compilation_reactions] à 
laquelle je rajoute cet article insultant au sens 
propre, "_[Lettre aux haineux dissimulés][le_vaillant]_"). 

Tremblez, citoyens ! Il est urgent de légiférer ! Il faut lutter contre le 
cyber-harcèlement ! Et tous ces jeunes qui vont rejoindre Daesh ! Tu n'as rien 
à te reprocher de toute façon ! Pourquoi tu voudrais te cacher, **hein** ?

Entendant ce type de propos revenir assez souvent dans des débats pourtant 
souvent d'un bon niveau, et voulant expliquer à mes proches les raisons qui me poussait 
moi-même à m'exprimer sous pseudo, j'avais entamé cet article bien avant qu'il ne 
**devienne à la mode d'y aller de son avis**. J'ai donc raté une occasion 
de me transformer en **hipster précurseur et visionnaire**, mais je vais quand même y aller de mon 
commentaire. N'hésitez d'ailleurs surtout pas à **réagir et commenter** (de manière
anonyme ou non, c'est votre choix), je vais peut-être dire beaucoup de bêtises.

L'effervescence de mise autour du sujet fait en grande part suite à 
la [sortie récente 
d'Emmanuel Macron][macron] lors d'un des "débats" de ces dernières semaines : 

> _Je crois qu’on doit aller vers une levée progressive de toute forme 
d’anonymat et je crois qu’on doit aller vers des processus où l’on sait 
distinguer le vrai du faux et où l’on doit savoir d’où les gens parlent et 
pourquoi ils disent des choses, ça participe de cette transparence._

**L'angle est un peu nouveau** de celui employé habituellement : il estime cette 
**transparence essentielle à une bonne "_hygiène démocratique_"**. 
Cela ne manque pas de piquant si l'on rappelle que la 
grandiloquente "_[loi pour la confiance dans la vie politique][loi_transparence]_" 
votée en tout 
début de son mandat a assez largement oublié **le sujet du lobbying auprès des 
parlementaires** ; que les amendements proposés par certains députés se 
[retrouvent entre les mains de groupes de pression][batho] avant même 
leur discussion ; que les députés ont le droit de rencontrer des lobbyistes ou 
de **recevoir des cadeaux** de leur part sans obligation de déclaration (voir 
les propositions de l'association [Anticor][anticor] sur le sujet) ; 
que des [amendements copiés-collés à la virgule près][amendements_copies_colles] 
sont proposés par des dizaines de députés (du groupe LREM, notamment), sans qu'on 
ne sache d'où leur vient cette étrange inspiration. L'hygiène démocratique 
commande sûrement plus impérieusement de permettre à tous de connaître 
la provenance des 
textes de loi qui régissent en bonne partie nos vies que de savoir **qui se cache 
derrière le compte Twitter "parodique" [Le Journal de l’Elysée ᵖᵃʳᵒᵈᶦᵉ][journal_elysee]**.    

On m'opposera que l'on peut bien agir sur deux fronts à la fois, ce que je 
concède bien volontiers.
Mais alors qu'une action en faveur de la transparence dans les agissements des
élus et le fonctionnement des assemblées nous rapprocherait du vertueux
exemple scandinave, la levée de l'anonymat sur Internet est une 
demande qui invite plutôt à la **comparaison avec les régimes les plus 
autoritaires** de la planète.

Il doit être palpable que **je ne suis _pas vraiment_ en faveur de cette idée**, 
mais il ne suffit pas de le dire. Aussi je vous propose de tenter un panorama du sujet, 
qui je l'espère permettra à tous ceux qui veulent se faire un avis sur le sujet 
de le faire en toute connaissance de cause. Je lance donc une série d'articles 
qui abordera plusieurs facettes du sujet ; car **avant de parler du _problème_ de 
l'_anonymat_ sur _Internet_ et de _quoi faire_**, encore faut-il peut-être 
démêler certaines confusions qui semblent persister, ce que j'espère pouvoir 
faire au cours d'une suite d'articles (à la base prévu pour être unique, mais 
il y a vraiment trop à dire). Ils balaieront les thèmes suivants, pas 
forcément dans cet ordre : 

* C'est quoi l'anonymat ?
* C'est quoi Internet ?
* Y a-t-il vraiment un problème ?
* Quelle est la situation actuelle ?
* Quelles sont les perspectives à venir dans la matière ?

Je n'hésiterai pas à verser dans **des aspects techniques**, car cela me semble absolument 
essentiel pour se faire un avis ; mais je le ferai de la manière la plus 
didactique possible, car là comme ailleurs, les principes fondamentaux ne sont 
**pas du tout aussi complexes** que ce que certains laissent parfois entendre. À la 
fin de cette série, vous aurez vu passer des termes qui vous paraîtront pour le
moment abscons, comme _protocole TCP/IP_, _DPI_, _TOR_, _dark web_ ... mais 
vous aurez aussi compris, je l'espère, qu'on ne peut pas vraiment parler de 
ce sujet sans avoir au moins une fois vus.

Alors allons-y (quel art de la transition, n'est-ce pas ?), 
**demandons-nous déjà ce qu'est l'anonymat**. On peut simplement 
partir de la [définition][atilf] du dictionnaire de l'Académie Française : 

> **ANONYMAT**, subst. masc.  
> **I**.− État d'une personne, d'une chose dont on ignore le nom, l'identité.   
> _Sous l'anonymat, sous le voile de l'anonymat, garder l'anonymat_. 

En rebondissant sur cette définition, on peut se poser quelques questions 
qui amèneront plusieurs distinctions utiles : que recouvre ce "on" ? Vous, moi,
mon voisin, l'État, Mark Zuckerberg ? Quelle est la raison de cette ignorance ?
Une volonté, une impossibilité physique, technique, juridique, ...? 

Puisque nous sommes sur mon blog, **commençons par parler de moi** : 
si vous faites partie des trois lecteurs qui 
êtes arrivés par hasard sur cette page sans ma recommandation préalable, 
vous ne connaissez pas mon identité. On peut déja noter que **si vous êtes arrivés 
jusqu'ici**, c'est que le fait de ne pas la connaître ne semble pas vous empêcher
de lire ma prose, ni de l'apprécier (permettez-moi de le penser !). Après 
tout, ne pas vous donner plus d'information que cela sur ma véritable identité
est un bon moyen de faire en sorte que vous jugiez mon propos **uniquement sur 
son fond et sa forme**, et non sur sa provenance ; une hygiène de pensée qu'il 
est souvent bon d'avoir, même si là, de fait, je vous force la main. 

Si je reste donc un inconnu pour vous, cela ne vous empêche pas pour autant 
de pouvoir vous faire une petite opinion de moi, de ce que je suis, de ce qui 
m'importe, de mon parcours ... Il suffit pour cela de **lire ce que je publie 
ici**, ou sur d'autres coins assez visibles du web où je publie sous le même 
pseudonyme (et profitez-en pour me partager, me retweeter, me liker, c'est mon
but ultime dans la vie !). Cela vous donnera une **vision certes partielle et biaisée**
(car 
je décide librement de ce que je veux bien diffuser), mais pas forcément très 
éloignée de ce que je suis réellement. À force de me lire, peut-être même 
éprouverez-vous une certaine sympathie à mon égard, l'envie de correspondre avec 
moi sur tel ou tel sujet, pourquoi pas de me rencontrer ; c'est **un des charmes 
propres à Internet** que de permettre ce type de relation entre deux humains, 
et en tant que relativement vieux routard des 
espaces de discussion, il me serait difficile de faire un décompte du 
**nombre de rencontres, amicales ou amoureuses**, que j'ai vu se faire par ce 
biais (sans même parler des 
sites de rencontres dont c'est le but et le principe).

Ainsi donc, l'anonymat, ou plus exactement, le pseudonymat dont il est question 
ici (qui déconnecte totalement l'État Civil de l'identité sous laquelle on se 
présente) **n'empêche absolument pas la création de relations humaines bien réelles 
entre individus**. Par ailleurs, l'écriture, l'expression d'idées, ou la 
conception artistique sous pseudonyme ne sont **pas exactement des 
nouveautés de l'ère numérique**. Les exemples étant innombrables, je me 
contenterai d'en citer deux contemporains : l'artiste [**Banksy**][banksy] dont les 
œuvres affolent les critiques et le marché de l'art, et 
[**Satoshi Nakamoto**][nakamoto]. Vous ne le connaissez pas ? Il a pourtant fait 
le bonheur (ou le malheur) de spéculateurs du monde entier, puisqu'il s'agit ni 
plus ni moins du **créateur du [bitcoin][bitcoin]** et du principe technique 
sous-jacent de la blockchain. Personne ne sait pourtant de qui il s'agit, ni 
même si c'est une seule et même personne. 

Dans le cas d'Internet comme dans celui de ces exemples de la "vraie vie", 
le simple fait de vouloir l'anonymat n'est pour autant **pas une 
garantie absolue** ; il suscite souvent tant de curiosité que nombreux sont ceux qui 
se donnent pour but de **percer le secret**, et comme dans une enquête digne des romans 
de détectives, rassemblent les indices pour retrouver l'identité réelle
de celui qui souhaitait se cacher. Pour les deux personnes citées ci-dessus,
cela se traduit par l'existence, pour chacun d'entre eux, d'**hypothèses plus ou 
moins fantaisistes sur leur origine**. Et sur Internet, cela se fait en masse, 
**assez rarement avec de bonnes intentions**, sous le nom de "_[doxxing][doxxing]_",
une pratique qui consiste à trouver puis réveler des éléments privés concernant 
une personne qui s'exprime sur Internet : pour quelqu'un qui s'exprime en 
son identité propre, cela pourra être son adresse, son numéro de téléphone, ...
Pour quelqu'un qui s'exprime sous pseudonyme, la première étape de ce jeu pervers
consistera bien entendu à **déterminer sa véritable identité**. 

Jusqu'ici il n'a été sujet que de **la relation qui existe entre vous, lecteur, 
et moi, auteur de cet article** ; si elle se caractérise a priori par l'anonymat,
vous conviendrez que ses contours et ce qu'il recouvre précisément sont déjà 
beaucoup plus flous. Et rappelez-vous que c'est un anonyme qui vous parle, 
alors que la tendance 
depuis l'avènement des réseaux sociaux est plutôt à une **utilisation de plus en 
plus accrue de sa véritable identité**, chose qui était auparavant extrêmement 
rare sur Internet, voire impensable pour la plupart des "puristes". Au premier 
rang des "responsables" de cette tendance, on citera évidemment Facebook, qui 
a ses débuts n'était qu'**un site paraissant bien inoffensif**, permettant 
justement de rester en contact 
avec des personnes que l'on connaissait déjà dans la "vraie vie" ; nous n'avions 
alors vu aucune raison d'y dissimuler notre véritable identité, et avons 
certainement été **bien naïfs et peu prudents** d'aller y déverser volontairement 
des quantités astronomiques de données qui étaient indubitablement privées.

Mais il y a en plus de vous et moi **une myriade d'acteurs** que la plupart des 
critiques de l'anonymat 
sur Internet semblent (délibérement ?) ignorer : ceux qui rendent techniquement 
possible la publication de mes pertinents écrits, ceux qui vous permettent de 
me lire, et le législateur. Pour voir plus clair dans tout cela, je vous 
propose d'attendre **le prochain article**, qui abordera les points techniques 
nécessaires.

[compilation_reactions]: https://twitter.com/Romain_Pigenel/status/1089948307206651906
[le_vaillant]: https://www.liberation.fr/chroniques/2019/01/28/pour-qu-internet-tombe-le-masque_1705956
[macron]: https://twitter.com/BFMTV/status/1086361987871899651
[journal_elysee]: https://twitter.com/JournalElysee/
[loi_transparence]: http://www.vie-publique.fr/actualite/panorama/texte-discussion/projet-loi-organique-projet-loi-ordinaire-retablissant-confiance-action-publique.html
[amendements_copies_colles]: http://www.leparisien.fr/politique/comment-les-lobbys-s-immiscent-dans-la-fabrique-de-la-loi-29-08-2018-7868979.php
[batho]: http://www.lcp.fr/la-politique-en-video/divulgation-un-lobby-dun-amendement-interdisant-le-glyphosate-batho-denonce
[anticor]: https://www.anticor.org/2019/01/18/grand-debat-national-anticor-rappelle-ses-propositions/
[atilf]: http://www.cnrtl.fr/definition/anonymat
[banksy]: https://fr.wikipedia.org/wiki/Banksy
[nakamoto]: https://fr.wikipedia.org/wiki/Satoshi_Nakamoto
[bitcoin]: https://sciencetonnante.wordpress.com/2016/06/24/le-bitcoin-et-la-blockchain/
[doxxing]: https://fr.wikipedia.org/wiki/Doxxing
[anonymous]: {filename}/images/anonymous.png
