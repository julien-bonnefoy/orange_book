# OBJECTIFS ET CONTRAINTES

## OBJECTIF 1

<p style='font-size: 24px; display: block; line-height: 30px; background-color: #9400ff; background-image: linear-gradient(to right, #9400ff, #fff);color: #fff;'><b>DASHBOARD</b></p>

Les **fournisseurs de formations** doivent pouvoir suivre l'état de leurs Learning Objects (quantité, type, actifs ou non, etc... et ainsi **monitorer** leur offre pour l'adapter le cas échéant


````{margin}
```{admonition} Coming up soon
:class: seealso
Dashboarding & Monitorig avec Plotly Dash, Flask & SQLAlchemy
```
````

```{note}
L'analyse de l'usage (la 'consommation') des Learning Objects devra aussi faire l'objet d'une analyse approfondie.   
``` 

## OBJECTIF 2

<p style='font-size: 24px; display: block; line-height: 30px; background-color: #9400ff; background-image: linear-gradient(to right, #9400ff, #fff);color: #fff;'><b>OPTIMISATION DE MOTEUR DE RECHERCHE</b></p>

Celui-ci est l'objectif primaire à moyzen terme. Parmi les objectifd secondaires qui en découlent nous avons:

**PISTE 1**: 
- Evaluer la **PERTINENCE** des **TITRES** (de Learning Objects)

Les fournisseurs de formations aimeraient avoir une mesure de la pertinence des Titres de Learning Objects en fonction du contenu de leur description. 
Le moteur de recherhce est actuellemnt indexé sur les Titres. Si ces Titres ne sont pas adéquats, le moteur perd en performance  
<br>

    Coming up soon: Keywords (features) Extraction avec TF-IDF

<br>

**PISTE 2**: 
- Relier **LEARNING OBJECTS** avec le/les **JOBS/SKILLS** potentiellement concernés
    
D'un côté nous avons les Learning Objects avec leurs Titres, Descripions, Types, Matières...
De l'autre nous avons des JOBS qui sont définis de manière très précise par un ensemble de SKILLS, elles-mêmes divisées en 4 niveaaux d'expertise. Et à aujourd'hui aucun lien n'est fait entre les 2 ni même ne fait l'objet d'un "champ obligatoire" lors de l'enregistrmeent d'un  objet..  
Il y a pourtant les colonnes  'Mots clés' ou 'Compétences pour la formation' qui font partie de l'extraction du 'Catalogue' mais qui ne sont pas exploitées.

Les fournisseurs de fotrmations aimeraient obtenir une IA capable de 'auto-tagger' tous les Learning Objects en fonction  

- des SKILLS qu'ils permettent de développer et/ou 
- des JOBS qui sont concernés

<br>

    Coming up soon:  Machine Learning & Deep Learning for Text Classification

<br>



## CONTRAINTES

<p style='font-size: 24px; display: block; line-height: 24px; background-color: #9400ff; background-image: linear-gradient(to right, #9400ff, #fff);color: #fff;'>RANDOM<br><b/b></p>

> - Orange Learng est 'on top of' Corner Stone On Demand, leader du marché des LMS. Les requêtes se fonest via une interface graphique simpliste (pas acces au code) et renvoient du csv ou xlsx. 

> - Les modifcations ne me sont évidemment pas accessibles  

> - N'ayant pas de serveur disponible en DRHG (ni d'ordinateur de Dev...), j'ai du utiliser mon matériel personnel tout au long du développeemnt de ce projet et donc y implémenter un serveur HTTP Apache pour le Web et un serveur MySQL pour la gestion des bases de données crées à partir des csv/xlsx  

> - Certaines requêtes communes, comme celle du  "Catalogue" des objets sont assez surprenantes (Cf. plus tard)  l'utilisation qui sont parfois faites avec certaines colonnes sont tantôt du doublon à usage prticulier tantôt des grands vides. Pourquoi les intégrer dabs ce type de requêtes  ?  

> - Pour enrtainer les modèles de Machine Learning à classer du texte par exemple, il faut un jeu d'entrainement dit 'lablélisé' servant de base d'apprentissage et de référence pour corriger l'apprentissage en cours. Il n'y aucune feature 'corresponding SKILL' ou 'corresponding JOBS' pour servir de 'cible'. Il faudra soit lableliser à la main ... soit touver une autre solution (Non supervisé? Semi supervisé?

> - Mon tuteur n'etait pas,  à mon grnad regret, ni développeur, ni 'connaisseur' d'Intelligences Artificielles

> - La gestion d'Orange Learning est divisée entre plusieurs directions ce ui cause parfois des conflits et entraine arfois du gaspillage de temps et d'énerie

> - Ce qui fait penser aux aspects politiques inévitables dans des strctures ausssi grande mais l) aussi, temps, energie, gaspillage

