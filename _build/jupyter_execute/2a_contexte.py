# LE CONTEXTE

## Formation au Titre de Développeur en I.A.

J'ai eu la chance d'être recruté fin mars 2019 pour intégrer une formation de développeeur en Intelligence Artficirelle, dont le programme est parraibé par l'Ecole Data-I.A. de Microsoft.
 mois de froamtion dite 'intensive'
 ... ... ... 
 
Ce projet a commencé lors de mon Contrat de Professionalisation chez Orange S.A. (09-11-2019 - 22-10-2020) au sein de l'équipe **Orange Learning** qui fait partie de la D.R.H. Groupe.  
Orange Learning est le Learning Management System (une plateforme d'apprentissage' qui est commune à l'internationnal et de ce fait la gestion se situe au niveau "Groupe"

- D.R.H.G.: **D**irection des **R**essources **H**umaines **G**roupe  
    - D.F.D.C.G.: **D**irection de le **F**ormation et du **D**éveloppement des **C**ompétences **G**roupe
        - D.N.E.A.: **D**irection des **N**ouvelles **E**xpériences d'**A**pprentissage
            - <p><span style='color: #f16e00; background-color: #ddd; text-align: center; width: 50%; line-height: 30px; font-size: 24px; font-weight: bolder;'>ORANGE LEARNING</span><p>

Contrat de Professionalisation chez Orange S.A. (09-11-2019 - 22-10-2020) au sein de l'équipe **Orange Learning** (D.R.H. Groupe)

Orange Learning = Learning Management System ('Plateforme d'apprentissage' commune à l'internationnal)

- D.R.H.G.: **D**irection des **R**essources **H**umaines **G**roupe  
    - D.F.D.C.G.: **D**irection de le **F**ormation et du **D**éveloppement des **C**ompétences **G**roupe
        - D.N.E.A.: **D**irection des **N**ouvelles **E**xpériences d'**A**pprentissage
            - <p><span style='color: #f16e00; background-color: #ddd; text-align: center; width: 50%; line-height: 30px; font-size: 24px; font-weight: bolder;'>ORANGE LEARNING</span><p>

Tout au long de leurs carrières chez Orange, les collaborateurs devront par exemple 
- metre à jour leurs connaissances/compétences, ou encore 
- consolider celles qu'ils ont déjà voire même 
- en développer de nouvelles jusque là inconnues.

Accès illimité à Orange Learning. 
Le plus souvent, l'utilisation de la plateforme fait suite un ordre / une demande de la hierarchie mais il est à noter que l'accès y est possible 24/7 à l'ensemble des salariés.

## Orange en chiffres

url = 'https://fr.wikipedia.org/wiki/Orange_%28entreprise%29'

from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)
driver.implicitly_wait(30)
driver.get(url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'lxml')
driver.close()
vcard = soup.find("table", {"class": "infobox_v2"})

body = soup.find_all('tbody')

rows = body[0].find_all('tr')

import re
data = {}
for row in rows:
    tds = row.find_all('td')
    ths = row.find_all('th')
    for th, td in zip(ths, tds):
        data[re.sub('\n', '', th.text)] = re.sub('\n', '', td.text)

import pandas as pd
df = pd.DataFrame.from_dict(data, orient='index')

df.drop(['Dates clés', 'Remplace',  'Fonds propres', 'Dette', 'Activité', 'Forme juridique', 'SIREN', 'Personnages clés', 'Sociétés sœurs',
         'Directeurs', 'Siège social','Produits', 'Filiales', 'Site web', 'Capitalisation'], inplace=True)

df.loc['Actionnaires', 0] = "Cf. plus bas"

actionnaires = {
    'Actionnaires institutionnels':    '64,3  %', 
    'État français (dont Bpifrance)':  '23    %',
    'Actionnaires individuels':         '5    %',
    'Salariés':                         '4,64 %',
    'Auto-détention':                   '0,4  %'
}

from IPython.display import display, HTML
# display(HTML('<img src="static/img/orange_logo.png" alt="Logo Orange"  style="float: left margin-right: 50px; width: 200px;"/>'))

<img src="/home/julien/Www/website/website/static/img/orange_logo.png" alt="Logo Orange"  style="float: left margin-right: 50px; width: 200px;"/>'

display(HTML('<img src="../../static/img/orange_logo.png" alt="Logo Orange"  style="float: left, margin-right: 50px; width: 200px;"/>'))
display(df)

display(HTML('<img src="../../static/img/orange_logo.png" alt="Logo Orange"  style="float: left margin-right: 50px; width: 200px;"/>'))
display(HTML("<p>répartition des actionnaires:<br></p>"))
actionnaires = pd.DataFrame.from_dict(actionnaires, orient='index')
display(HTML(actionnaires.to_html()))

## Orange en Métiers et Compétences

Chez Orange ont été définis **128** métiers **JOBS** et pour chacun de ces JOBS ont été listées les compétences **SKILLS** auxquelles ils font appel (environ 10 SKILLS/JOB).  


Comme on peut l'imaginer, certaines SKILLS sont plutôt techniques et donc spécifiques à (un) certain(s) métier(s). Ce sont les **hard skills**.<br> 
D'autres sont dites transverses car communes à plusieurs métiers. Ces dernières impliquent le plus souvent des qualités 'relationelles“ et/ou "manageriales" ce qui explique pourquoi ont peut les retrouver dans la définitions de plusieurs  méters. Ce sont les **soft skills**,

A savoir également, pour chaque compétence il y a 4 niveaux d'expertise qui sont détaillés: Débutant, Intermédiaire, Confirmé et Expert. C'est d'alleurs l'évoluton entre ces paliers qui  et azu coeur des **évaluations annuelles** de chaque collaborateur et qui, au bout du compte, **impacte directement la rémunération** par la répartition des augmentations de salare.

Tout au long de leurs carrières chez Orange, les collaborateurs devront par exemple 
- metre à jour leurs connaissances/compétences, ou encore 
- consolider celles qu'ils ont déjà voire même 
- en développer de nouvelles jusque là inconnues.

Pour se faire, ils ont donc un accès illimité à Orange Learning. Le plus souvent, l'utilisation de la plateforme fait suite un ordre / une demande de la hierarchie mais il est à noter que l'accès y est possible 24/7 à l'ensemble des salariés.

**128** métiers **JOBS** 

JOB ==> liste compétences **SKILLS** auxquelles il fait appel (environ 10 SKILLS/JOB).  

 **hard skills** & **soft skills**

SKILL ==> 4 niveaux d'expertise: Débutant, Intermédiaire, Confirmé et Expert. 

L\' évolution entre ces paliers fait partie des **évaluations annuelles** de chaque collaborateur (**impacte sur la rémunération**)

## Orange en Objets de Formation (Learning Objects)

La base de donnée sur laquelle Orange Learning est construite est issue de la jonction d'une dizaine de tables données qu proviennent d'entités différentes. Par exemple les données "infos salariés" qui viennent de la DRH, les données d'"usage" qui viennent des fournisseurs (écoles/campus) etc.

Cette base de données est constituée d\' Objets de Formation (Learning Objects)

Ces Learning Objects sont développés, intégrés et maintenus soit par 

- les Directions dites 'Métiers', comme la Direction Technique du Système d'Information qui va regrouper les Techniciens d'Interventon,  les Architectes Réseaux etc. Soit par

- les Écoles et Campus de formation qui sont des structures dédiées à l'évolution professionnelle des collaborateurs. Ces éocles peuvent être très specifiques 'Métiers' comme l'Ecole des Métiers Techniques (C.Q.F.D.) ou encore l'Ecole de la Vente Grand Public pour les Conseillers Clietns.
Ou plutôt transverses comme l'Innovation School ou comme sont nom l'indique l'Ecole des Compétences Transverses

Il est possible d'en avoir le catalogue via une requête commune préenregistrée nommée:
FR_Catalogue_des_objets_de_formation dont l\' execution aboutit à la création d'un ficher .csv ou xlsx

Orange Learning DB issue de la jonction d'une dizaine de bases données provenant d'entités différentes.
Ex :
- Données "infos salariées" viennent de la DRH,
- Données d'"usage" qui des fournisseurs (écoles/campus) etc.

==> Objets de Formation (Learning Objects) : Développés, intégrés et maintenus soit par 

- **les Directions dites 'Métiers'**
    * ex : Direction Technique du Système d'Information pour les Techniciens d'Intervention, les Architectes Réseaux
    
- **les Écoles et Campus de formation** : structures dédiées à l'évolution professionnelle des collaborateurs.
    * ex spécifique 'Métiers': Ecol de la Vente Grand Public (Conseillers Clients)
    * ex transverse: Innovation School

Catalogue des Learning Objects via requête commune préenregistrée :

FR_Catalogue_des_objets_de_formation  

==> ficher .csv ou .xlsx de dimensions  66517 lignes * 48 colonnes