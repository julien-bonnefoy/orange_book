# Cas pratique E3: "Techniques de classification de texte: Revue de littérature et tendances actuelles"

## APPRENANT: Julien Bonnefoy 

Bien qu'il existe une littérature volumineuse indiquant les capacités de différents types de techniques de 
classification de texte, la diffusion de ces techniques dans des domaines avancés comme l'intelligence artificielle (IA)
 / l'apprentissage automatique (ML) est rarement signalée.   
 
 En outre, l'examen des approches de classification de texte d'un point de vue algo-rithmique profitera à la fois 
 à l'industrie et au milieu universitaire. La quantité de données d'entreprise augmente constamment et le besoin 
 croissant d'automatisation des applications complexes à forte intensité de données pousse l'industrie à rechercher 
 de meilleures approches pour la découverte des connaissances.   Ces connaissances mèneront à des investissements 
 judicieux et augmenteront la productivité d'une organisation. 
 
 Par conséquent, le développement de modèles de traitement de texte basés sur l'IA est la nécessité de 
 l'heure.
  
 En dehors de cela, la variété des données disponibles, le traitement informatique moins cher et le stockage 
 de données abordable nécessitent l'automatisation des modèles de données qui peuvent analyser des données complexes 
 pour fournir des résultats rapides.   
 
 Pour cette raison, cette étude analyse les techniques de classification de texte  par rapport à l'IA / ML.  
  
 Le reste de l'article est organisé comme suit.  
  
 La section revue de la littérature décrit  les tendances actuelles en matière de recherche dans diverses
 techniques de classification de texte.   
 
 La section  méthodologie décrit la nature de l'étude entreprise pour cet article.   
 
 La section sur les techniques de classification  de texte décrit en détail diverses approches.  
  
 La section des résultats explique divers résultats observés à partir des articles examinés. 
 
 La section des discussions explique les lacunes de la recherche et la section des conclusions  met en évidence 
 certaines des tendances actuelles et des options de recherche futures dans les techniques de classification de texte.  
 
# REVIEW
 
Cet article est une revue de la littérature de diverses études liées aux approches de classification de texte; par conséquent,
cette section élucide certaines des directions de recherche observées à cet égard. Mod de sujet statistique
eling est appliqué pour la classification de documents multi-étiquettes, où chaque document est attribué à un ou
plus de classes. Il est devenu un sujet intéressant au cours de la dernière décennie car il a bien fonctionné pour les ensembles de données avec
nombre croissant d'instances pour une entité (Rubin, Chambers, Smyth et Steyvers, 2012).  

Lorsque le nombre de documents augmentait, la complexité de calcul augmentait également (Stas, Juhar,
Et Hladek, 2014). Le ML est souvent considéré comme une émanation des statistiques en ce qui concerne l'exploration de données. Il
utilise des modèles avancés pour prendre des décisions basées sur sa propre connaissance (Du, 2017; Ranjan & Pra-
triste, 2017). Cependant, une approche purement statistique et purement ML est considérée comme moins compétente.
une approche hybride est généralement préférée (Srivastava, 2015).  

Méthode de pondération des attributs auto-adaptative basée sur le système immunitaire artificiel (AIS) pour la classe Naive Bayes
sification utilise la théorie de l'immunité dans les systèmes immunitaires artificiels pour rechercher la valeur optimale de poids d'attribut
ues (Wu et al., 2015). La régression logistique est un classificateur linéaire efficace basé sur les probabilités. Le problème
lem de surajustement (le modèle de données mémorise l'ensemble de données au lieu de la procédure d'apprentissage.) pourrait être
résolu en utilisant une régression logistique pénalisée dans un algorithme d'apprentissage actif (Wang & Park, 2017).  

Une technique de sélection d'instance appropriée pourrait terminer la moitié de la procédure de découverte des connaissances. UNE
nouveau sélecteur d'instance basé sur Support Vector Machine (SVM) appelé, prend en charge
la sélection de position est suggérée pour supprimer les données bruyantes (Tsai et Chang, 2013). Certains chercheurs ont analysé
le rôle des arbres de décision dans les données multi-valeurs et multi-étiquetées. Ce type de données rend difficile la
choisissez un ensemble particulier d'attributs. Il est également difficile de calculer des scores de similarité à valeurs multiples et
données multi-étiquetées (Yi, Lu et Liu, 2011).  

Les algorithmes d'arbre de décision calculent les scores de similarité de manière complète et précise. Ça a été
prouvé efficace pour les scénarios où la synchronisation entre les éléments est moindre. Pour surmonter le problème
lem de l'ordre des classes dans l'apprentissage des règles, l'algorithme d'apprentissage des règles parallèles basé sur la complexité est
suggéré (Asadi & Shahrabi, 2016). Dans un contexte différent, la classification multi-classes est essayée par com Dans un autre contexte,
 la classification multi-classes est essayée en combinant l'estimation de la densité du noyau avec k-NN (Tang & Xu, 2016). Il améliore le principe de pondération
de k-NN, augmentant ainsi la précision de la classification. Il a également été prouvé efficace pour problèmes de classification complexes.

Le rôle des RNA dans les données de grande dimension et volumineuses est significatif. Classificateurs neuronaux tels que flou
Les cartes associatives de résonance adaptative sont évolutives pour de grands volumes de données (Benites & Sapozhnikova,
2017). L'apprentissage non supervisé offre de nombreuses opportunités de recherche dans la gestion du flux de travail et
planification des tâches, en particulier dans le domaine du big data (Zhoua, Pana, Wanga, Athanasios, & Vasilakos,
2017).

# MÉTHODOLOGIE  

Pour cette étude, un total de 91 articles de recherche ont été téléchargés à partir de bases de données, telles que 
IEEE, Science Direct, Springer, ACM, Google Scholar, Academia et d'autres blogs techniques publiés entre le
2010 et 2017.  

Le problème de la gestion d'une information abondante a commencé à la fin des années 20, augmentant le besoin de 
procédures de traitement des données. 
Diverses techniques de classification de texte ont été initialement identifiées via Wikipedia et d'autres encyclopes.
dias et corroboré avec le contenu de divers articles de recherche. Les principales approches étaient en outre
ils sont organisés sous forme d'arborescence après avoir analysé les similitudes et les différences entre ces différents
approches avec leurs algorithmes respectifs.  

Les différents termes de recherche utilisés étaient, texte + classification, texte + classification + algorithmes et tous les
sous-titres indiqués dans la figure 1 en ce qui concerne la classification du texte et AI / ML. Chaque article était com
complètement lu et divers problèmes de recherche liés aux techniques de classification de texte dans le domaine du ML
ont été identifiés. Ensuite, les domaines de recherche ont été regroupés en fonction de leur domaine plus large, comme les statistiques
techniques techniques, algorithmes d'apprentissage supervisé, non supervisé et semi-supervisé,
gression, Naïve Bayes, SVM, arbre de décision, K-Means, etc.
conforme aux procédures d'apprentissage (supervisé, semi-supervisé et non supervisé). Parmi les 91
articles de recherche, seulement 74 articles traitant uniquement des techniques de classification de texte dans le ML
contexte ont été utilisés dans cette étude.


TECHNIQUES DE CLASSIFICATION DE TEXTE
Les algorithmes de classification forment la croûte des techniques de text mining (Allahyari et al., 2017).
En règle générale, une technique de classification peut être divisée en ap-
proaches. Les techniques statistiques satisfont purement manuellement les hypothèses proclamées, d'où la nécessité
pour les algorithmes, c'est peu, mais les techniques de ML ont été spécialement inventées pour l'automatisation (Allahyari et al.,
2017). Dans la figure 1, les algorithmes sont globalement divisés en supervisé, non supervisé et semi-
catégories supervisées selon les critères d'apprentissage suivis.
Parmi les algorithmes de classification supervisée, il existe deux catégories, à savoir, paramétrique et
non paramétrique, basée sur la suprématie des paramètres dans les données. Régression logistique et naïve
Les bayes sont les algorithmes de classification paramétrique les plus utilisés (Tsangaratos & Ilia, 2016). Souper-
Port Vector Machine (SVM), Decision Tree, Rule Induction, K-nn and Neural Networks sont leurs
homologues non paramétriques (Aliwy & Ameer, 2017). Fuzzy c-means, k-means clustering et Hierar-
le clustering chical sont des approches d'apprentissage non supervisé et co-formation, auto-formation, transductif
SVM et les méthodes basées sur des graphes forment les composants des méthodes d'apprentissage semi-supervisé (Reit-
maier, Calma et Sick, 2016).
Vous trouverez ci-dessous quelques-unes des techniques de classification de texte et leurs orientations de recherche.

# A PPROCHE S TATISTIQUE  

Les techniques statistiques sont des processus purement mathématiques, et elles servent de fondement mathématique
pour tous les autres classificateurs de texte. Il fonctionne comme un programme informatique, exécutant les instructions données
sans aucune capacité propre (Srivastava, 2015). Pour obtenir une bonne classification, la quantité de
la formation à traiter par l'application doit être concise et elle est obtenue en réduisant la di-
dimensionnalité (nombre de variables à prendre en compte, par exemple dans un ensemble de données de recensement, «âge», «gen-
der »,« localité », etc., sont des variables) dans les données (Vieira, Borrajo, & Iglesias, 2016). Les données dans les e-mails sont
complexe et multidimensionnel. Techniques d'extraction de caractéristiques statistiques, telles que la composition principale
Analyse nente (PCAII), analyse discriminante biaisée (BDA) et marge moyenne du quartier
La maximisation (ANMM) s'est avérée être de meilleures techniques de réduction de dimensionnalité (Gomez,
Boiy et Moens, 2012). Ils sont classés par pertinence mais ne conviennent pas aux données non linéaires.
Ils s'avèrent également inefficaces pour les grands ensembles de données. À l'avenir, ces méthodes pourront également être utilisées
pour la classification de texte binaire, pour déterminer si un e-mail particulier est du spam ou non. Fortement corre-
les fonctionnalités liées jouent un rôle essentiel dans la classification de texte binaire. En un autre mot, semblable à la détection des anomalies
processus de classification, sur le modèle des arbres de classification non paramétriques, un classificateur filtre les auteurs inconnus »
documents texte. Il est basé sur la combinaison des tests de Kruskal – Wallis et de Brunner – Dette – Munk
(Cerchiello et Giudici, 2012). Il reconnaît les mots les plus typiques utilisés par un auteur connu et iden-
tifie les nouveaux auteurs. Il peut être appliqué pour les applications de détection de fraude.  

# MACHINE LEARNING  

L'augmentation du volume, de la vitesse et de la variété des données a nécessité l'automatisation des techniques de traitement de texte
y compris la classification de texte. Dans certaines situations, définir un ensemble de règles logiques à l'aide des connaissances
techniques d'ingénierie et sur la base d'avis d'experts pour classer les documents permet d'automatiser la
tâche de classification. La classification des textes peut être divisée en trois catégories: la classification des textes supervisés
classification, classification de texte non supervisée et classification de texte semi-supervisée basée sur l'apprentissage
principe suivi par le modèle de données (Korde & Mahender, 2012).
Dans la terminologie de l'apprentissage automatique, le problème de classification relève de l'apprentissage supervisé
principe, où le système est formé et testé sur les connaissances sur les classes avant le
processus de classification. L'apprentissage non supervisé se produit lorsque les données étiquetées ne sont pas accessibles. Le processus
est compliqué et présente des problèmes de performances. Il convient aux mégadonnées. L'apprentissage semi-supervisé est le suivant
faible lorsque les données sont partiellement étiquetées et partiellement non étiquetées (Dwivedi et Arya, 2010).
Cependant, il est difficile d'établir une relation concrète entre les données étiquetées et non étiquetées. le
l'efficacité est mesurée à l'aide de mesures, telles que la précision, la précision et le rappel. Lorsque le jeu de données est volumineux,
les erreurs de classification ont tendance à être moindres. On sait également que la sélection d'algorithmes appropriés
pour un ensemble de données particulier joue un rôle majeur dans la classification de texte.

## Enseignement supervisé

L'apprentissage supervisé est le plus coûteux et le plus difficile des trois. La principale raison derrière
cette notion est qu'elle nécessite une intervention humaine en attribuant des étiquettes à des classes qui ne sont pas
sible dans de grands ensembles de données. Bien que le flux de travail imite les techniques suivies dans les processus d'IA, il est
long. Il est également appelé apprentissage inductif en ML (Y. Liu, Ni, Sun et Chen, 2011). Supervisé
l'apprentissage devient coûteux lorsque différentes distributions de données, différentes sorties et différentes fonctionnalités
les espaces se produisent comme dans les corpus de textes hétérogènes. L'une des méthodes supervisées les plus utilisées est
estimation du maximum de vraisemblance (Park, 2018) .Ici; le processus d'apprentissage pourrait être simplifié par des
hypothèses. Ces types d'hypothèses sur les données introduisent deux approches telles que la
et non paramétrique.

### Modèles paramétriques
Le modèle qui pourrait résumer les données en fonction des paramètres sous-jacents est appelé un modèle paramétrique
(Brownlee, 2016). La régression logistique et les algorithmes de Naïve Bayes sont des classificateurs paramétriques. Soutien
les machines vectorielles, k-plus proche voisin, l'induction de règles, les arbres de décision et les réseaux de neurones ne sont pas
classificateurs paramétriques.

#### Classificateur Naive Bayes  
__
Ce sont des classificateurs probabilistes couramment utilisés en ML. Cependant, les classificateurs bayésiens sont des statistiques
tical et possèdent également une capacité d'apprentissage. Le modèle multinomial est utilisé par Naïve Bayes pour les grands ensembles de données.
Les performances pourraient être améliorées en recherchant les dépendances parmi les attributs. C'est principalement
utilisé dans les applications de prétraitement de données en raison de la facilité de calcul. Raisonnement bayésien et proba-
l'inférence de bilité est utilisée pour prédire la classe cible. Les attributs jouent un rôle important dans la classification
fication. Par conséquent, l'attribution de valeurs de poids différentes aux attributs peut potentiellement améliorer la
formance (Sucar, 2015).
La pondération profonde des fonctionnalités estime les probabilités conditionnelles en calculant en profondeur la pondération des fonctionnalités
fréquences parmi les données d'entraînement (Jiang, Li, Wang et Zhang, 2016). Cela résout le problème des conditions
hypothèse d'indépendance nationale, qui est une amélioration majeure du classifieur bayésien naïf et
calcule avec précision la probabilité conditionnelle (L. Zhang, Jiang, Li et Kong, 2016). Bien que ces fea-
Les techniques de pondération de la ture présentent des défauts tels qu'une amélioration inadéquate des performances,
simplicité compromise et temps d'exécution accru des modèles, il agit pour réduire le calcul
coût du modèle de données. En outre, l'approche Naïve Bayes pourrait représenter des dépendances d'attributs arbitraires.  

Bien que l'apprentissage d'un réseau bayésien optimal à partir de données textuelles de grande dimension augmente le temps
complexité. Ainsi, un classificateur Naive Bayes multi-nominal étendu de structure est appliqué pour améliorer la
attribuer l'hypothèse d'indépendance en faisant la moyenne de toutes les estimations multinomiales pondérées à une dépendance
mators est suggéré (Jiang, Wang, Li et Zhang, 2016).
La performance de Naïve Bayes dépend de l'exactitude de la probabilité conditionnelle estimée
termes. Il est difficile d'estimer précisément ces termes lorsque les données d'entraînement sont rares. Par conséquent, certains
des méthodes méta-heuristiques comme les algorithmes génétiques (GA), le recuit simulé (SA) et les différences
L'évolution entiale (DE) est suivie pour estimer les termes de probabilité conditionnelle. Dans certains cas, l'annonce
Les avantages du NB sont remis en cause par une forte hypothèse d'indépendance conditionnelle entre les attributs
qui a son mot à dire dans la performance de classement (Diab & El Hindi, 2016). Pour améliorer cela, divers
techniques de méta-apprentissage telles que l'extension de structure, la sélection d'attributs, la transformation de fréquence,
la pondération des attributs, la pondération des instances et l'apprentissage local sont utilisés. Ainsi, les classificateurs bayésiens naïfs
sont simples et aussi puissants en termes de degré de certitude, l'optimisation est moins compliquée et
permet une mise à jour dynamique (Arar & Ayan, 2017) .Ces possibilités en font une option plus simple pour
gérer les problèmes de traitement du langage naturel (Merinopoulou, Ramagopalan, Malcolm, & Cox,
2017).
Régression logistique
Régression logistique dans l'apprentissage supervisé, en sélectionnant les meilleures matières à étiqueter pour
classification, est une opportunité de réduire les coûts temporels. L'apprentissage actif est utilisé pour trouver le meilleur
sujets à étiqueter dans les modèles ML, qui est un domaine de recherche en pleine croissance dans le text mining. Il a prouvé
minimiser l'erreur de généralisation des modèles. Adaptation automatique des paramètres de régularisation et application d'un
Un apprentissage actif basé sur une régression logique pénalisée à des problèmes multi-classes est suggéré
recherche (Maalouf & Siddiqi, 2014). Les méthodes du noyau transforment les données en un espace dimensionnel supérieur
contraste avec les classificateurs linéaires qui sont implémentés directement sur les données dans leur espace d'origine. Le déséquilibre
Les données sur les événements rares anciens ont été un problème persistant dans le domaine ML. Une nouvelle régression logistique basée
sur des poids d'événements rares, le noyau est recommandé pour le même. Il est également plus facile à mettre en œuvre même si
il existe un important déséquilibre des données et de nombreux événements rares (Yen, Lee, Ying et Wu, 2011)
Les classificateurs linéaires conviennent aux ensembles de données volumineux et de grande dimension. Un lissage à base de N grammes est
timator utilisant la régression logistique pour la catégorisation de texte chinois sans jeton de mot chinois
a été suggérée (Yen et al., 2011). Il utilise la régression logistique pour lisser la probabilité de n-
grammes. Il a été prouvé qu'il surpasse le lissage traditionnel, car le premier a le
capacité à traiter des termes inconnus et évite également de surévaluer la probabilité conditionnelle qui est
à l'origine zéro. À l'avenir, ces types d'ouvrages pourraient être étendus pour évaluer les relations entre
des phrases plutôt que des mots (Aseervatham, Antoniadis, Gaussier, Burlet, & Denneulin, 2011)
La catégorisation automatique du texte est le processus d'affectation d'un ou plusieurs documents textuels à
catégories définies en fonction de son contenu. Cependant, il rencontre un problème lorsque le nombre de fea-
tures dépasse le nombre d'observations. En outre, les techniques de ML ont tendance à fonctionner faiblement en raison de ces
problèmes de surajustement; auquel cas, le modèle mémorise l'ensemble d'apprentissage au lieu d'acquérir
leurs connaissances (Aseervatham et al., 2011). Pour éviter cela, la complexité du modèle a
à contrôler pendant le processus de formation en utilisant des techniques de sélection de modèles. La régression logistique est
mieux adapté à ces types de problèmes que les SVM (An, Tang et Xie, 2017).
La régression logistique Ridge est une solution populaire au problème de catégorisation de texte, mais son rôle dans
les documents à l'échelle sont encore discutables (Pereira, Basto & Silva, 2016) .Pour éliminer cette difficulté,
la solution est combinée avec la régression des crêtes. La sparsification supprime les caractéristiques moins importantes.
en résolvant le problème classique des régresseurs de crête (Pereira et al., 2016).  

Modèles non paramétriques
Le modèle qui ne pouvait pas résumer les données en fonction des paramètres sous-jacents est appelé un modèle non paramétrique
modèle. Supporte les machines vectorielles, k-plus proche voisin, l'induction de règles, les arbres de décision et le réseau neuronal
les travaux sont pour la plupart des classificateurs non paramétriques.
Machine de vecteur de soutien
L'algorithme SVM (Support Vector Machine) est l'un des algorithmes d'apprentissage automatique supervisé
utilisé pour divers problèmes de classification (Demidova, Klyueva, Sokolova, Stepanov, &
Tyart, 2017). Il a ses applications dans l'analyse du risque de crédit, le diagnostic médical, la catégorisation de texte et
extraction d'informations. Les SVM conviennent particulièrement aux données de grande dimension. Il y en a tellement
raisons étayant cette affirmation. Plus précisément, la complexité des classificateurs dépend du nombre
de vecteurs de support au lieu de dimensions de données, ils produisent le même hyper plan pour des trains répétés
et ils ont de meilleures capacités de généralisation (Altınel, Ganiz et Diri, 2015). Les SVM par-
forme avec la même précision même lorsque les données sont rares.
Une variante des noyaux standard, connus sous le nom de noyaux personnalisés, augmente les performances de l'algo-
rithms car il inclut les détails d'arrière-plan pour la catégorisation de texte. Un tel noyau personnalisé est
Classe Signification Noyau utilisé pour lisser les termes des documents en utilisant des valeurs de signification basées sur les classes
des termes (Goudjil, Koudil, Bedda et Ghoggali, 2016). Cela s'avère être un lisse sémantique prometteur-
noyau pour les SVM. Le même noyau pourrait être testé pour capturer des informations sémantiques implicites
tout en calculant la similitude entre les documents à l'avenir. En outre, une méthode d'apprentissage active est suggérée
pour la catégorisation de texte basée sur SVM afin de réduire l'effort d'étiquetage en sélectionnant intelligemment
échantillons à étiqueter (Goudjil et al., 2016)
Une autre direction intéressante est proposée en utilisant le clustering semi-supervisé pour la classification de texte
(W. Zhang, Tang et Yoshida, 2015). Il aide à déterminer la catégorie de texte à partir de plusieurs compositions
nents. Dans ce scénario, les données non étiquetées sont également utilisées pour améliorer les performances du système,
puisqu'ils prennent en charge une estimation efficace des paramètres. Bien qu'il soit démontré qu'il surpasse le traditionnel
SVM, il est toujours en retard dans la gestion des données déséquilibrées. Il faut vérifier que les données sont soigneusement pré-
traitées pour augmenter les performances des classificateurs. Pour obtenir de meilleures données pour une analyse efficace
Une SVM basée sur la sélection d'instances est suggérée (Ramesh & Sathiaseelan, 2015). Il a montré de remarquables
précision avec analyse multi-ensembles de données. Une machine vectorielle de support de classe est une excellente détection d'anomalie.
technique pour améliorer la précision des problèmes de classification de texte (Tbarki, Said, Ksantini, &
Lachiri, 2017).
Arbres de décision
Les arbres de décision sont des modèles très compréhensibles par rapport aux réseaux neuronaux. Ces travaux dans un
séquence, pour tester une décision par rapport à une valeur de seuil particulière parmi les valeurs disponibles. Essai
se produit selon certaines règles logiques similaires au concept de poids des réseaux de neurones. C4.5
et CART sont des techniques d'arbre de décision largement utilisées (Kotsiantis, 2013). La phase de croissance des arbres parti-
L'ensemble de formation et la phase d'élagage généralise les données sur celui-ci. Fuzzy ID3 est un autre
variante qui intègre le flou des attributs dans les règles de décision. Les arbres basés sur un ensemble font
utilisation de techniques de suralimentation et d'ensachage pour combiner plus d'un classificateur qui emploie différents
règles de décision pour différents ensembles de données (Savas & Nasibov, 2017). Ces ensembles ont montré des
performances comparées aux arbres de décision normaux, cependant, le coût de calcul augmente à mesure que chaque
La requête d'entrée est transmise à chaque classificateur de composant (Nguyen, Nguyen, H., Wu et Li, 2015).
Les arbres de décision ont toujours été un problème avec les données de grande dimension. Pour résoudre ce problème, regroupez
des arbres sont suggérés (Sun, Ye, Deng et Huang, 2011). Le streaming de données est un autre défi dans les données
arène de traitement. L'espace pour accueillir ces données et la vitesse nécessaire pour les gérer sont
deux problèmes persistants dans les données à haute vitesse. Les arbres de décision incrémentiels sont les mieux adaptés aux flux de données car ils
ont la capacité de se stabiliser en fonction des données accumulées. Il utilise plusieurs attributs pour l'entraînement  

les fonctions. Un algorithme d'apprentissage d'arbre de décision min-max flou évolutif est recommandé dans cette direc-
tion pour les futurs chercheurs. Il se divise de manière non linéaire pour produire des arbres peu profonds qui augmentent la précision (Mir-
zamomen et Kangavari, 2017).
La performance des arbres est directement proportionnelle à l'efficacité de la construction. L'optimisation
La question des arbres décisionnels est un autre domaine à explorer largement. Dans un travail récemment publié, génétique
l'algorithme est combiné avec une fonction d'objectif multi-tâches qui construit des arbres efficaces avec les meilleurs paramètres
ters (Karabadji, Seridi, Bousetouane, Dhifli et Aridhi, 2017). C'est une technologie d'optimisation méta-heuristique
nique. Cela augmente non seulement la précision des prévisions, mais simplifie également l'approche. Décider
quand arrêter la phase d'élagage et construire un meilleur vecteur de représentation d'encodage pour les cas,
où le nombre d'attributs est élevé sont deux axes de recherche vitaux pour les futurs chercheurs
l'approche de classification de texte basée sur des arbres est concernée.
Cependant, les arbres de décision fonctionnent bien pour les données avec peu d'attributs très pertinents, le calcul
la complexité augmente avec la complexité accrue des relations. Malgré toutes les capacités de
ces arbres mentionnés ci-dessus, l'utilisateur final ordinaire peut encore avoir du mal à comprendre le contexte
détails qui ont conduit à une décision particulière dans un problème de classification.
Induction de règle
La classification du texte libre avec une description d'étiquette minimale est un problème majeur dans la catégorisation de texte. UNE
un cadre basé sur des règles de modèles syntaxiques lexicaux est choisi comme fonction de classification qui réduit
erreurs de classification courantes. Dans cette approche, les performances sont mesurées à l'aide d'une métrique appelée
analyse de sensibilité. Il optimise le nombre de règles qui prennent en charge une catégorisation efficace. Les règles
dépendent des entrées de lexique qui décrivent plus en détail le domaine des documents considérés
Par conséquent, la catégorisation est plus efficace (Zamil et Can, 2011).
RIPPER est une autre technique d'induction de règle célèbre. L'ordre d'apprentissage des règles encadrées est l'homme-
datory pour une classification efficace, car un ordre aléatoire de règles entraînera des erreurs. L'ordre des règles est optimal
misé en utilisant l'algorithme de colonie de fourmis sur la liste de décision. La liste de décision se présente principalement sous la forme de «si,
then et else if ’structure. Recuit simulé, algorithme génétique et optimisation de l'essaim de particules
sont d'autres techniques d'optimisation de l'ordre des règles largement suivies. Certains des principaux écueils de cette technologie
nique sont la nature des règles qui dépendent des règles précédemment générées et l'apprentissage des règles se produit
séquentiellement, retardant davantage le processus d'apprentissage pour une nouvelle classe. Sélection du meilleur schéma de routage
pour ordonner les règles est une autre bonne direction de recherche (Asadi et Shahrabi, 2017).
Voisin le plus proche K
K-Nearest Neighbor (k-NN) fonctionne sur le principe des échantillons d'apprentissage les plus proches, ces points de données
qui sont proches les uns des autres appartiennent à une classe particulière, communément appelée apprentissage par instance
(Nidhi et Gupta, 2011). Bien qu'il soit robuste pour les données bruyantes, il est compliqué de décider de la valeur de k.
La complexité du calcul augmente encore avec l'augmentation de la dimensionnalité. Pour réduire le coût de
calcul de la valeur k, k-NN basé sur un arbre est utilisé. Cela réduit la portée de la recherche grâce à une meilleure technologie de traversée.
niques (Maillo, Ramfrez, Triguero et Herrera, 2016). Certaines techniques distribuées comme MapReduce sont
également intégré à k-NN pour réduire les contraintes de mémoire dans les données à grande échelle. Une étincelle open source
package est spécialement conçu pour gérer des ensembles de données distribués pour la classification k-NN.
Spark prend en charge les opérations en mémoire, l'intégration cloud ainsi que les algorithmes de streaming (Maillo et al.,
2016). À l'avenir, imputation des valeurs manquantes, approches à vues multiples pour plusieurs entités, instance
Les techniques de sélection peuvent être essayées avec k-NN à base d'étincelles en utilisant une approche d'apprentissage semi-supervisé.
Les k-NN sont également des algorithmes d'apprentissage axés sur la spécificité, dans lesquels aucun modèle de données n'est dérivé explicitement
et les décisions de classification sont formulées localement. En ajustant le biais d'induction des k-NNs, la classe
Le problème de déséquilibre des ensembles de données peut être résolu grâce à une modélisation de classe rare, qui est une
avantage des k-NN, en particulier lorsqu'il s'agit d'une tâche de classification (X. Zhang, Li, Kotagiri, Wu, Tari, &
Cheriet, 2017).  

Certaines des autres stratégies d'apprentissage existantes pour ce problème sont le rééchantillonnage, l'apprentissage sensible aux coûts.
et apprendre des approches spécifiques aux algorithmes. L'extension de ces travaux pourrait être réalisée pour
plusieurs situations de classe rares et classer les instances en fonction de la probabilité postérieure de chaque classe. k-NNs
sont également les plus populaires pour classer les instances en fonction du contexte des points de données par majorité
vote (X. Liu, Wang, Yin, Edwards et Xu, 2017). Cette méthode convient parfaitement aux petits ensembles de données.
Réseaux de neurones artificiels
Les réseaux de neurones artificiels (RNA) fonctionnent de la même manière que le cerveau humain pour prendre une décision.
L'intelligence Swarm et l'algorithme d'évolution sont utilisés pour généraliser un modèle de réseau neuronal. Ça marche
sur la vertu de l'apprentissage et de l'évolution avec une intervention humaine minimale ou nulle. Pour classifier les données
un modèle de réseau neuronal basé sur un algorithme de co-évolution compétitif est suggéré. Base radiale
La fonction est le composant ANN car il utilise des algorithmes d'apprentissage plus rapides. Il dispose d'un réseau compact
architecture qui augmente la précision de la classification. De plus, les algorithmes évolutifs ont tendance à
bien performer dans des environnements dynamiques en apprenant les règles à la volée et en adaptant fortement le terme «flou»
caractéristiques (Hiew, Tan et Lim, 2016).
Les réseaux de neurones sont également populaires parmi les cas où une approche de classification hiérarchique multi-étiquettes
est requis. Ce type de classification est complexe car chaque échantillon peut appartenir à plus d'une classe
et les prédictions d'un niveau sont alimentées comme entrées au niveau suivant pour prendre une décision finale (Cerri, Barros, &
Carvalho, 2014). Également dans une configuration similaire, la régression linéaire pourrait être utilisée pour la sélection de caractéristiques dans un
classificateur boosté par l'ensemble (Nie, Jin, Fei et Ma, 2015). Le réseau neuronal constitue la base de l'en-
semble à l’aide de souches composites.
Les ANN ont une bonne valeur d'application, un potentiel de développement et il n'est pas non plus nécessaire de former
les classificateurs binaires individuels pour les problèmes multi-classes donc ils forment de meilleurs classificateurs de base en
une approche d'ensemble. De plus, le sur-ajustement est pris en charge par Adaboost et la précision est maintenue
à travers les ANN (Nie et al., 2015).
Apprentissage non supervisé
L'apprentissage non supervisé est un type d'algorithme ML où les inférences sont tirées des données par clus-
en classant les données dans différents groupes sans réponses étiquetées (résultats attendus). En d'autres termes, non
les données de formation sont fournies au système. Cela semble complexe au départ, mais lorsque plus de données sont introduites dans
le modèle, l'algorithme se raffine à l'efficacité. Analyse en composantes principales, regroupement et auto-
les cartes d'organisation sont fréquemment utilisées dans l'apprentissage non supervisé. Dans de nombreux scénarios, le clustering est le
même que l'apprentissage non supervisé. Plusieurs fois, les connaissances spécialisées nécessaires pour étiqueter les échantillons sont soit
inexistante ou inadéquate. Dans ce cas, des cartes auto-organisées et un coefficient de corrélation sont utilisés pour
regrouper les documents et l'utiliser pour étiqueter les documents en vue d'une classification plus poussée (Shafiabady et al.,
2016). Il élimine également la malédiction de la dimensionnalité et de l'intervention d'experts. Ce genre d'hybride
Le modèle est plus adapté aux données à volume élevé.
L'analyse statistique des clusters peut être utilisée pour l'extraction de caractéristiques dans des données de grande dimension, telles qu'elles sont
itérative pour faciliter les mises à jour périodiques, compte tenu du volume de données. Les techniques de clustering réduisent également
le temps et la complexité des coûts des procédures de prétraitement compliquées (H.Liu, Cheng, & Wang,
2017). La classification des types de requêtes est une autre direction intéressante, compte tenu des catégories de
rechercher des requêtes et les étiqueter comme étant de navigation, d'information, etc. (B. Liu, 2011).
La classification transactionnelle des requêtes est considérée comme un problème d'approche d'apprentissage non supervisé (Y. Liu, Ni,
Sun et Chen, 2011). La transaction est ce qu'un utilisateur exécute après qu'un moteur de recherche a renvoyé la date demandée.
ta. Ces requêtes pourraient être converties en modèles pour obtenir des connaissances sur le besoin d'informations
derrière les requêtes. Les clics de formulaire aident à généraliser les requêtes en fonction des informations contenues dans
les formulaires. À l'avenir, les formulaires Web peuvent également être utilisés pour optimiser les performances des moteurs de recherche en
classer les résultats de la recherche.  

La plupart des derniers outils ML prennent en charge les algorithmes parallélisables et le réglage automatique
options. Cependant, échanger des données confidentielles dans une plate-forme de Big Data reste un défi. Localisation des données
la propriété joue un rôle majeur dans de telles situations. Un domaine de prudence est de ne dépendre que de la
Les algorithmes ML, car ils peuvent conduire à des relations fausses, il est donc toujours suggéré qu'un minimum
une intervention humaine est nécessaire (Yan, Zhang, Ma et Yang, 2017). L'efficacité des itérations est également primordiale
mal pour la capacité de calcul efficace de ces algorithmes.
Dans le regroupement de documents, le nombre de points de données, leur dimensionnalité et le nombre de clusters
augmentent avec le temps, de sorte que les algorithmes devraient avoir suffisamment d'espace pour se développer dans de tels cas. Filtration
des données non fiables provenant de sources de données sont une option intéressante pour les futurs chercheurs dans de tels cas
(Yan et al., 2017). Certains des célèbres algorithmes d'apprentissage non supervisé sont, la détection d'anomalies,
Apprentissage Hebbian, algorithme de maximisation des attentes, analyse en composantes principales, indépendant
analyse des composants, factorisation matricielle non négative, décomposition en valeurs singulières et aussi celles
mentionné dans la figure 1 (Ahmad, Lavin, Purdy et Agha, 2017).
Apprentissage semi-supervisé (SSL)
L'apprentissage semi-supervisé est une combinaison de techniques d'apprentissage supervisé et non supervisé. Ce
type d'apprentissage utilise une petite quantité de données étiquetées et une grande quantité de données non étiquetées pour la formation
ing. Les étiquettes sont attribuées en combinant des instances étiquetées et non étiquetées, car les données non étiquetées atténuent
l'effet de données étiquetées insuffisantes sur la précision du classificateur. Certaines des techniques SSL incluent, l'auto-
formation ou auto-apprentissage ou bootstrap, co-formation, SVM transductives, modèles génératifs et
méthodes basées sur des graphes (Altınel & Ganiz, 2016).
Les modèles d'espace vectoriel sont principalement utilisés dans les problèmes de traitement du langage pour traiter le langage naturel
la sémantique qui suppose que les mots dans des contextes similaires ont des significations similaires. Les valeurs de signification sont calculées
selon le principe de Helmholtz. Ce modèle est non itératif mais efficace pour augmenter
l'efficacité du classificateur. Le système peut être combiné avec des noyaux sémantiques qui lissent la documentation
vecteurs de termes utilisant des relations sémantiques terme à terme. Découvrir d'autres approches pour extraire le
des informations issues du contexte d'une classe pourraient être essayées à l'avenir (Altınel & Ganiz, 2016).
Les approches traditionnelles de classification de texte deviennent nulles lorsqu'il n'y a pas de données étiquetées pour un
classe de l'ensemble de données, par exemple, les données étiquetées ne sont disponibles que pour les échantillons positifs et non pour
échantillons négatifs. Un algorithme semi-supervisé basé sur l'apprentissage approximatif de tolérance et d'ensemble est
recommandé pour la même chose (Shi, Ma, Xi, Duan et Zhao, 2011). La classe indisponible est extraite
approximativement à partir de l'ensemble de données et défini comme échantillon étiqueté. Le classifieur d'ensemble de manière itérative
construit la marge entre les classes positives et négatives pour se rapprocher davantage des données négatives, car
les données négatives sont mélangées aux données positives. Par conséquent, sans avoir besoin d'échantillons de formation, classi-
La fication est obtenue grâce à une approche hybride. Il élimine le coût de l'étiquetage manuel des données, en particulier
dans le Big Data.
L'application d'algorithmes semi-supervisés est très utile dans les exigences de filtrage d'informations
(Santos et Canuto, 2014). Le rôle des algorithmes semi-supervisés dans la classification hiérarchique multi-étiquettes
le cation est un domaine où il y a encore un besoin d'exploration. Auto-formation avec semi-
un classificateur supervisé est recommandé pour la classification hiérarchique multi-étiquettes. Il a également prouvé un
meilleure façon d'obtenir l'attribution automatique des étiquettes.
RÉSULTATS
Sur la base de l'étude réalisée pour cet article, il a été constaté que la classification de texte la plus largement utilisée
les techniques de formation suivent une approche d'apprentissage semi-supervisé (Deshmukh & Tripathy, 2017; Pavlinek &
Podgorelec, 2017; W. Zhang, Tang et Yoshida, 2015). Depuis, il a le potentiel d'améliorer la classification
l’efficacité, par les avantages combinés des techniques d’apprentissage supervisé et non supervisé. Il
convient également pour résoudre le problème d'étiquetage tout en traitant un plus grand nombre d'instances de
une entité. On constate qu'une méthode d'apprentissage actif est suivie pour réduire les coûts temporels impliqués parsélectionner uniquement l'instance la plus appropriée pour classer un échantillon (apprentissage itératif supervisé) (Reitmaier
et al., 2016).
L'algorithme génétique aide à obtenir un ordre optimal des règles dans la liste de décision. On constate qu'il élimine
nate les conflits entre les règles générées et améliore la précision du modèle.
«Bien commencé est à moitié fait», s’applique littéralement à la classification de texte comme lemmatisation et issue idéales
l'étape de prétraitement conduit à une classification précise. Cela implique que les performances du classifieur
dépend de la nature des données analysées.
Les entrepôts de données jouent un rôle important dans tout type d'analyse. L'ingestion des données est la phase cruciale de
maintenir de grands ensembles de données et y accéder pour la découverte des connaissances. Il prend deux formes telles que
traitement par lots et ingestion en continu (Mirzamomen & Kangavari, 2017). Il pourrait également être mis à l'échelle
utiliser les technologies cloud avec peu d'efforts. Amazon Redshift, Google BigQuery et Snowflake
sont des entrepôts de données populaires avec des possibilités de support cloud.
Cette étude a révélé que l'extraction de sens profond, le traitement sémantique, l'efficacité de l'algorithme, l'hétér-
données ogènes, automatisation des audits, évolutivité des données, violation de données et prise de décision en temps réel
des domaines qui nécessitent une recherche et un développement plus poussés, en ce qui concerne la procédure de classification de texte
durs.
Certaines des conclusions cruciales concernant les algorithmes de classification de texte sont les points saillants de cette étude. Il
on voit que, le temps de classification pris par k-NN est croissant et il est difficile d'estimer k optimal
valeur (Maillo et al., 2016). Bien que les arbres de décision réduisent la complexité, une erreur rendra l'ensemble
sous-arbre va mal (Karabadji et al., 2017). Le réglage des paramètres est un problème majeur dans les SVM (Altinel et al.,
2015). Les algorithmes de vote comme les techniques d'amplification sont connus pour leur grande précision; cependant, ils exigent
calculs compliqués et plus de mémoire (Hiew et al., 2016). Ces déclarations impliquent qu'il y a
pas d'algorithme ultime pour un problème de classification de texte particulier par rapport à l'automatisation.
Les différents algorithmes discutés dans cette étude sont résumés en fonction de leurs atouts et
faiblesses du tableau 1 Ce tableau aidera le lecteur à comprendre le potentiel de chaque algorithme
et aider à sélectionner le meilleur modèle pour chaque objectif.  

DISCUSSIONS
En général, les techniques de classification de texte constituent la base de tout processus de découverte de connaissances. Comme ils
fournir une structure formelle aux données brutes. Certains des problèmes majeurs des méthodes de classification de texte sont
traitement pour supprimer les balises, mots vides, extraction de caractéristiques pour supprimer les termes non informatifs, stockage,
accès, estimation des paramètres, déséquilibre des données, surajustement, etc. (Pereira et al., 2016).
Sur la base de la littérature disponible, il est connu que différents types de classificateurs existent. Par conséquent, Identi-
trouver le classificateur optimal, améliorer les performances des grands ensembles de données et gérer de grandes taxonomies dans
les données hétérogènes sont d'autres problèmes rencontrés lors de la construction d'un modèle de données (Rasane & Patil,
2016).
Extraire un sens ou des concepts profonds à partir de documents est difficile dans les procédures d'exploration de données. le
les techniques sémantiques sont confrontées à plus de problèmes dans les scénarios de traitement du langage naturel, en particulier pour les
tion. Ceci est principalement dû au problème de l'ambiguïté dans les langues naturelles. Les problèmes comme Polysemy
(un mot-plusieurs significations) et la synonymie (plusieurs mots-significations similaires) sont deux
problèmes dans le text mining (Brindha et al., 2016).
La présence de composants hétérogènes dans les documents texte tels que, e-mails, textes multilingues, abréviations
viations, argots, codes SMS défient encore plus les outils de text mining existants, car chacun nécessite un
algorithme à trier (projets de doctorat, 2016; Sucar, 2015).
Atténuer la violation de données dans les installations de stockage de données est une autre exigence importante de l'analyse de texte.
Bien que ce soit une question de sécurité des données, le besoin d’applications d’analyse de texte pour assurer la sécurité
les opérations sont en hausse (Yan et al., 2017).
CONTRIBUTIONS
Cet article expose les forces, les limites et les tendances actuelles de la recherche en classification de texte dans une annonce.
champ évolué comme l'IA. La connaissance de la classification de texte est cruciale pour les data scientists, car ces
les techniques sont au cœur de toute analyse de données. Ce travail répertorie presque toutes les variantes de classificateurs disponibles
par rapport aux données textuelles. Les résultats de cette étude pourraient être appliqués pour concevoir non seulement personnaliser
modèles de données. Il aide également l'industrie à comprendre l'efficacité opérationnelle des techniques minières.
La connaissance des avantages / inconvénients d'une technique particulière permet d'optimiser les données
modèles pour divers besoins de l'industrie. Il contribue en outre à réduire le coût des projets,
et soutient une prise de décision efficace.
R ECOMMANDATIONS POUR LES RECHERCHEURS ET LES P RACTITIONNEURS
Analyse de cadres pour les articles de presse, détection de tromperie dans les données des médias sociaux concernant les rumeurs,
la science narrative où les données expriment une histoire, les applications de la santé pour diagnostiquer les maladies,
l’analyse de l’analyse des problèmes de santé sont quelques-uns des domaines qui nécessitent le développement de nouvelles applications par des praticiens
Exploration de texte basée sur l'IA. D'autre part, développer des algorithmes plus simples en termes de codage et
mise en œuvre, meilleure efficacité opérationnelle, approches améliorées pour la distillation des connaissances,
affinage du texte lingual, intégration de la connaissance du domaine, détection de la subjectivité, point de vue contrastif
résumé sont quelques domaines qui pourraient être explorés par les chercheurs à cet égard (Reamy, 2012).
IMPACT SUR LA S OCIÉTÉ
La classification de texte constitue la base de l'analyse des données et agit comme le moteur de la découverte des connaissances.
ery. Il prend en charge la prise de décision de pointe, par exemple, prédire un événement avant qu'il ne soit réellement
se produit, classant une transaction comme «frauduleuse», etc. En outre, la valeur des décisions éclairées est plus
que celle des suppositions calculées. Les résultats de cette étude pourraient être utilisés pour développer de telles applications.
dédiées à l’aide à la décision. Ces applications aideront en outre à optimiser
ressources et maximiser les avantages pour l'humanité.  

L IMITATIONS
Cette étude n'a donné de l'importance qu'aux techniques basées sur l'apprentissage supervisé plutôt que non supervisé
et les approches semi-supervisées. De plus, cette étude n’a pas pu spécifier un classificateur particulier comme le meilleur
pour un besoin analytique particulier. À l'avenir, des études pourraient être entreprises pour un apprentissage semi-supervisé
des approches et de meilleures méthodes d'optimisation des paramètres pourraient être explorées.
CONCLUSION
Sur la base de cette revue de la littérature, diverses techniques de classification de texte ont été identifiées avec leur
les forces, les possibilités et les faiblesses de l'extraction des connaissances à partir des données. À ce stade, il est essentiel de
réaliser les problèmes présents dans les techniques de classification de texte, de sorte que le jugement de divers classificateurs
être plus facile.
Cependant, sur la base de la littérature, la classification de texte semi-supervisée gagne en importance dans le texte
l'exploitation minière en raison de son efficacité de classification. Cela réduit les coûts temporels. Certains des autres problèmes cruciaux
sont, amélioration des performances, gestion de grandes taxonomies, sélection de fonctionnalités, zones de document et données
déséquilibre.
Il est également intéressant de déduire qu'il n'est toujours pas pratique de prescrire un classificateur particulier pour un partici-
problème majeur. Néanmoins, le nombre «d’essais et d’erreurs» pour sélectionner le meilleur classificateur pourrait être min.
imized sur la base des informations fournies dans cette étude. Algorithmes plus simples mais puissants pour les paramètres
L'optimisation et le traitement des données en continu sont d'autres domaines à explorer par les chercheurs dans le futur.
ture.  

REFERENCES
Ahmad, S., Lavin, A., Purdy, S., & Agha, Z. (2017). Unsupervised real-time anomaly detection for streaming
data. Neurocomputing, 262(1), 134-147.https://doi.org/10.1016/j.neucom.2017.04.070
Aliwy, A. H., & Ameer, E. (2017). Comparative study of five text classification algorithms with their improve-
ments. International Journal of Applied Engineering Research, 12, 4309-4319.
Allahyari, M., Pouriyeh, S. A., Assefi, M., Safaei, S., Trippe, E. D., Gutierrez, J. B., &Kochut, K. J. (2017). A
brief survey of text mining: classification, clustering and extraction techniques. CoRR, abs/1707.02919.
Altınel, B., & Ganiz, M. C. (2016). A new hybrid semi-supervised algorithm for text classification with class-
based semantics. Knowledge-Based Systems, 108, 50–64.https://doi.org/10.1016/j.knosys.2016.06.021
Altınel, B., Ganiz, M. C., &Diri, B. (2015). A corpus-based semantic kernel for text classification by using
meaning values of terms. Engineering Applications of Artificial Intelligence, 43, 54–66.
https://doi.org/10.1016/j.engappai.2015.03.015
An, Y., Tang, X., & Xie, B. (2017). Sentiment analysis for short Chinese text based on character-level methods.
Proceedings of the 9th international conference on knowledge and smart technology (KST). IEEE. Chonburi. Thailand.
https://doi.org/10.1109/KST.2017.7886093
Arar, O. F., & Ayan, K. (2017). A feature dependent Naive Bayes approach and its application to the software
defect prediction problem. Applied Soft Computing, 59, 197-209. https://doi.org/10.1016/j.asoc.2017.05.043
Asadi, S., &Shahrabi, J. (2016). ACORI: A novel ACO algorithm for rule induction. Knowledge-Based Systems, 97,
174-187. https://doi.org/10.1016/j.knosys.2016.01.005
Asadi, S., & Shahrabi, J. (2017). Complexity-based parallel rule induction for multiclass classification. Information
Sciences, 380, 53–73. https://doi.org/10.1016/j.ins.2016.10.047
Aseervatham, S., Antoniadis, A., Gaussier, E., Burlet, M., &Denneulin, Y. (2011). A sparse version of the ridge
logistic regression for large-scale text categorization. Pattern Recognition Letters, 32, 101–106.
https://doi.org/10.1016/j.patrec.2010.09.023
Benites, F., & Sapozhnikova, E. (2017). Improving scalability of ART neural networks. Neurocomputing, 230,
219–229. https://doi.org/10.1016/j.neucom.2016.12.022
Brindha, S., Sukumaran, S., & Prabha, K. (2016). A survey on classification techniques for text mining. Proceed-
ings of the 3rd International Conference on Advanced Computing and Communication Systems. IEEE. Coimbatore, In-
dia. https://doi.org/10.1109/ICACCS.2016.7586371
Brownlee, J. (2016). Parametric and non-parametric machine learning algorithms. Retrieved on March 14 from
http://machinelearningmastery.com/parametric-and-nonparametric-machine-learning-algorithms
Cerchiello, P., & Giudici, P. (2012). Non parametric statistical models for on-line text classification. Advanced
Data Analysis and Classification, 6, 277–288. https://doi.org/10.1007/s11634-012-0122-2
Cerri, R., Barros, R. C., & Carvalho, A. (2014). Hierarchical multi-label classification using local neural net-
works. Journal of Computer and System Sciences, 80, 39–56. https://doi.org/10.1016/j.jcss.2013.03.007
Demidova, L., Klyueva, I., Sokolova, Y., Stepanov, N., &Tyart, N. (2017). Intellectual approaches to improve-
ment of the classification decisions quality on the base of the SVM classifier. Procedia Computer Science, 103,
222-230. https://doi.org/10.1016/j.procs.2017.01.070
Deshmukh, J. S., & Tripathy, A. K. (2017). Text classification using semi-supervised approach for multi domain.
Proceedings of the International Conference on Nascent Technologies in Engineering (ICNTE).IEEE. Navi Mumbai,
India. https://www.doi.org/10.1109/ICNTE.2017.7947982
Diab, M., & El Hindi, K. (2017).Using differential evolution for fine tuning Naive Bayesian classifiers and its
application for text classification. Applied Soft Computing, 54, 183-199.
https://doi.org/10.1016/j.asoc.2016.12.043
Du, J. (2017). Automatic text classification algorithm based on gauss improved convolutional neural network.
Journal of Computational Science, 21, 195-200. https://doi.org/10.1016/j.jocs.2017.06.010
Dwivedi, S. K., & Arya, C. (2010). Automatic text classification in information retrieval: A survey. Proceedings of
the Second International Conference on Information and Communication Technology for Competitive Strategies. ACM.
Udaipur, India. https://doi.org/10.1145/2905055.2905191
Gomez, J. C., Boiy, E., & Moens, M. F. (2012). Highly discriminative statistical features for email classification.
Knowledge Information Systems, 31, 23–53.https://doi.org/10.1007/s10115-011-0403-7
Goudjil, M., Koudil, M., Bedda, M., & Ghoggali, N. (2016). A novel active learning method using SVM for text
classification. International Journal of Automation and Computing, 1-9. Springer.
https://doi.org/10.1007/s11633-015-0912-z
Hiew, B. Y., Tan, S. C., & Lim, W. S. (2016). Intra-specific competitive co-evolutionary artificial neural network
for data classification. Neurocomputing, 185, 220–230. https://doi.org/10.1016/j.neucom.2015.12.051
Jiang, L., Li, C., Wang, S., & Zhang, L. (2016). Deep feature weighting for Naive Bayes and its application to
text classification. Engineering Applications of Artificial Intelligence, 52, 26–39.
https://doi.org/10.1016/j.engappai.2016.02.002
Jiang, L., Wang, S., Li, C., & Zhang, L. (2016). Structure extended multinomial Naive Bayes. Information Sciences,
329, 346–356. https://doi.org/10.1016/j.ins.2015.09.037
Karabadji, N. I., Seridi, H., Bousetouane, F., Dhifli, W., &Aridhi, S. (2017). An evolutionary scheme for decision
tree construction. Knowledge-Based Systems, 119, 166–177. https://doi.org/10.1016/j.knosys.2016.12.011
Khan, A., Baharudin, B., Lee, L. H., & Khan, K. (2010). A review of machine learning algorithms for text-
documents classification. Journal of Advances in Information Technology, 1, 4-20.
Korde, V., & Mahender, N. C. (2012). Text classification and classifiers: a survey. International Journal of Artificial
Intelligence & Applications, 3(2), 85-99. https://doi.org/10.5121/ijaia.2012.3208
Kotsiantis, S. B. (2013). Decision trees: A recent overview. Artificial Intelligence Review, 39, 261–283.
https://doi.org/10.1007/s10462-011-9272-4
Liu, B. (2011).Supervised learning. In B. Liu, Web data mining: Exploring hyperlinks, contents, and usage data (pp. 63-
132). Springer. https://doi.org/10.1007/978-3-642-19460-3_3
Liu, H., Cheng, J., & Wang, F. (2017). Sequential subspace clustering via temporal smoothness for sequential
data segmentation. IEEE Transactions on Image Processing, 27(2), 866-878.
https://doi.org/10.1109/TIP.2017.2767785
Liu, X., Wang, J., Yin, M., Edwards, B., & Xu, P. (2017). Supervised learning of sparse context reconstruction
coefficients for data representation and classification. Neural Computing & Applications, 28, 135–143.
https://doi.org/10.1007/s00521-015-2042-5
Liu, Y., Ni, X., Sun, J., & Chen, Z. (2011). Unsupervised transactional query classification based on webpage
form understanding. Proceedings of the 20th ACM International Conference on Information and Knowledge Manage-
ment. Glasgow, Scotland, UK. https://doi.org/10.1145/2063576.2063590
Maalouf, M., & Siddiqi, M. (2014). Weighted logistic regression for large-scale imbalanced and rare events data.
Knowledge-Based Systems, 59, 142–148. https://doi.org/10.1016/j.knosys.2014.01.012
Maillo, J., Ramfrez, S., Triguero, I., & Herrera, F. (2016). kNN-IS: An iterative spark-based design of the k-
nearest neighbors classifier for big data. Knowledge-Based Systems, 117, 3-15.
https://doi.org/10.1016/j.knosys.2016.06.012
Merinopoulou, E., Ramagopalan, S., Malcolm, B., & Cox, A. (2017). RM3 - Methods for extracting treatment
patterns for renal cell carcinoma (RCC) from social media (SM) forums using natural language processing
(NLP) and machine learning (ML). Value in Health, 20(9), A402. https://doi.org/10.1016/j.jval.2017.08.021
Mirzamomen, Z.,& Kangavari, M.R. (2017). Evolving fuzzy min–max neural network based decision trees for
data stream classification. Neural Processing Letters, 45(1), 341–363. https://doi.org/10.1007/s11063-016-
9528-8
Nguyen, T. T., Nguyen, H., Wu, Y., & Li, M. J. (2015). Classifying gene data with regularized ensemble trees.
Proceedings of the International Conference on Machine Learning and Cybernetics (ICMLC). IEEE. Guangzhou. Chi.
https://doi.org/10.1109/ICMLC.2015.7340911
Nidhi & Gupta, V. (2011). Recent trends in text classification techniques. International Journal of Computer Applica-
tions, 35(6), 45-51.
Nie, Q., Jin, L., Fei, S., & Ma, J. (2015). Neural network for multi-class classification by boosting composite
stumps. Neurocomputing, 149, 949–956. https://doi.org/10.1016/j.neucom.2014.07.039
Park, J. (2018). Simultaneous estimation based on empirical likelihood and general maximum likelihood estima-
tion. Computational Statistics & Data Analysis, 117, 19-31. https://doi.org/10.1016/j.csda.2017.08.003
Pavlinek, M., & Podgorelec, V. (2017). Text classification method based on self-training and LDA topic models.
Expert System with Applications, 80, 83-93. https://doi.org/10.1016/j.eswa.2017.03.020
Pereira, J. M., Basto, M., & Silva, A. F. (2016). The logistic lasso and ridge regression in predicting corporate
failure. Procedia Economics and Finance, 39, 634-641. https://doi.org/10.1016/S2212-5671(16)30310-0
PhD projects. (2016). PhD research topic in text mining. Retrieved on October 3 from http://phdprojects.org/phd-
research-topic-text-mining
Ramesh, B., & Sathiaseelan, J. G. R. (2015). An advanced multi class instance selection based support vector
machine for text classification. Procedia Computer Science, 57, 1124-1130.
https://doi.org/10.1016/j.procs.2015.07.400
Ranjan, N. M., & Prasad, R. S. (2017).Automatic text classification using BPLion-neural network and semantic word pro-
cessing. https://doi.org/10.1080/13682199.2017.1376781
Rasane, S., &Patil, D. V. (2016).Handling various issues in text classification: a review. International Journal on
Emerging Trends in Technology, 3, 4076-4082.
Reamy, T. (2012). Future directions in text analytics. Retrieved on September 27 from
http://www.textanalyticsworld.com/pdf/Future_directions.pdf
Reitmaier, T., Calma, A., & Sick, B. (2016). Semi-supervised active learning for support vector machines: A
novel approach that exploits structure information in data. Cornell University Library, arXiv :1610.03995
[stat.ML]. 1-35.
Rubin, T. N., Chambers, A., Smyth, P., & Steyvers, M. (2012). Statistical topic models for multi-label document
classification. Machine Learning, 88, 157–208. https://doi.org/10.1007/s10994-011-5272-5
Santos, A., & Canuto, A. (2014). Applying semi-supervised learning in hierarchical multi-label classification.
Expert Systems with Applications, 41, 6075–6085. https://doi.org/10.1016/j.eswa.2014.03.052
Savas, S. K., & Nasibov, E. (2017). Fuzzy ID3 algorithm on linguistic dataset by using WABL defuzzification
method. Proceedings of the IEEE International Conference on Fuzzy Systems (FUZZ-IEEE), Naples. Italy.
https://doi.org/10.1109/FUZZ-IEEE.2017.8015502
Shafiabady, N., Lee, L. H., Rajkumar, R., Kallimani, V. P., Akram, N. A., & Isa, D. (2016). Using unsupervised
clustering approach to train the support vector machine for text classification. Neurocomputing, 211, 4–10.
https://doi.org/10.1016/j.neucom.2015.10.137
Shi, L., Ma, X., Xi, L., Duan, Q., & Zhao, J. (2011). Rough set and ensemble learning based semi-supervised
algorithm for text classification. Expert Systems with Applications, 38, 6300–6306.
https://doi.org/10.1016/j.eswa.2010.11.069
Srivastava, T. (2015). Difference between machine learning & statistical modeling. Retrieved on September 28 from
https://www.analyticsvidhya.com/blog/2015/07/difference-machine-learning-statistical-modeling/
Stas, J., Juhar, J., & Hladek, D. (2014). Classification of heterogeneous text data for robust domain-specific lan-
guage modeling. EURASIP Journal on Audio, Speech, and Music Processing, 14, 1-12.
Sucar, L.E. (2015). Bayesian classifiers. In L. E. Sucar, Probabilistic graphical models (pp. 41-62). Springer.
https://doi.org/10.1007/978-1-4471-6699-3_4
Sun, Z., Ye, Y., Deng, W., & Huang, Z. (2011). A cluster tree method for text categorization. Procedia Engineering,
15, 3785-3790. https://doi.org/10.1016/j.proeng.2011.08.709
Tang, X., & Xu, A. (2016). Multi-class classification using kernel density estimation on K-nearest neighbours.
Electronics Letters, 52(8), 600–602. https://doi.org/10.1049/el.2015.4437
Tbarki, K., Said, S. B., Ksantini, R., &Lachiri, Z. (2017). One-class SVM for landmine detection and discrimina-
tion. Proceedings of the International Conference on Control Automation and Diagnosis (ICCAD). IEEE. Hammam-
et. Tunisia. https://doi.org/10.1109/CADIAG.2017.8075676
Tsai, C. F., & Chang, C. W. (2013). SVOIS: Support vector oriented instance selection for text classification.
Information Systems, 38, 1070–1083. https://doi.org/10.1016/j.is.2013.05.001
Tsangaratos, P., & Ilia, I. (2016). Comparison of a logistic regression and Naïve Bayes classifier in landslide
susceptibility assessments: The influence of models complexity and training dataset size. Catena, 145, 164–
179. https://doi.org/10.1016/j.catena.2016.06.004
Vasa, K. (2016). Text classification through statistical and machine learning methods: A survey. International
Journal of Engineering Development and Research, 4, 655-658.
Vieira, A .S., Borrajo, L., & Iglesias, E. L. (2016). Improving the text classification using clustering and a novel
HMM to reduce the dimensionality. Computer Methods and Programs in Biomedicine, 136, 119-130.
https://doi.org/10.1016/j.cmpb.2016.08.018
Wang, J., & Park, E. (2017). Active learning for penalized logistic regression via sequential experimental design.
Neurocomputing, 222, 183–190. https://doi.org/10.1016/j.neucom.2016.10.013
Wu, J., Pan, S., Zhu, X., Cai, Z., Zhang, P., & Zhang, C. (2015). Self-adaptive attribute weighting for Naive
Bayes classification. Expert Systems with Applications, 42, 1487–1502.
https://doi.org/10.1016/j.eswa.2014.09.019
Yan, W., Zhang, B., Ma, S., & Yang, Z. (2017). A novel regularized concept factorization for document cluster-
ing. Knowledge-Based Systems, 135(1), 147-158. https://doi.org/10.1016/j.knosys.2017.08.010
Yen, S., Lee, Y., Ying, J., & Wu, Y. (2011). A logistic regression-based smoothing method for Chinese text cate-
gorization. Expert Systems with Applications, 38, 11581–11590. https://doi.org/10.1016/j.eswa.2011.03.036
Yi, W., Lu, M., & Liu, Z. (2011). Multi-valued attribute and multi-labeled data decision tree algorithm. Interna-
tional Journal of Machine Learning and Cybernetics, 2(2), 67-74. https://doi.org/10.1007/s13042-011-0015-2
Zamil, M., & Can, A. B. (2011). ROLEX-SP: Rules of lexical syntactic patterns for free text categorization.
Knowledge-Based Systems, 24, 58–65. https://doi.org/10.1016/j.knosys.2010.07.005
Zhang, L., Jiang, L., Li, C., & Kong, G. (2016). Two feature weighting approaches for Naive Bayes text classifi-
ers. Knowledge-Based Systems, 100, 137–144. https://doi.org/10.1016/j.knosys.2016.02.017
Zhang, W., Tang, X., & Yoshida, T. (2015). TESC: An approach to text classification using semi-supervised
clustering. Knowledge-Based Systems, 75, 152–160. https://doi.org/10.1016/j.knosys.2014.11.028
Zhang, X., Li, Y., Kotagiri, R., Wu, L., Tari, Z., & Cheriet, M. (2017). KRNN: K rare-class nearest neighbour
classification. Pattern Recognition, 62, 33–44. https://doi.org/10.1016/j.patcog.2016.08.023
Zhoua, L., Pana, S., Wanga, J., Athanasios, V., & Vasilakos. (2017). Machine learning on big data: opportunities
and challenge. Neurocomputing, 237, 350–361. https://doi.org/10.1016/j.neucom.2017.01.026
