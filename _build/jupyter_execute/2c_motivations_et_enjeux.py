# MOTIVATIONS  ET ENJEUX


Il faut absolument développer l'utilisation d'Orange Learnong et ne pas se cantonner à une utilisation 'imposée' Orange Learning est peut-être tro perçu comme un moyen de contrôle plutôt qu'une source de connnaissance.  

Quoiqu'il en soit, la plateforme est sous utilisée 

Tout ce qui touche Orange Learning est avant tout **un enjeu finacier** au regard de l'obligation de patricipation à la formation de chaque entreprise en France.   

Selon l'estimation (ci-dessous), le "budget " FORMATION " d'Orange en France est de 22 302 500 € pour l'exercice 2019.
22 millions d'euros à invertir obligatoirement dans le développement professionnel de ses salariés. C'est colossal. La rentabilité est prioritaire et à aujourd'hui, Orange Learning est sous utilisé par les salariés

## TAUX de la CONTRIBUTION FORMATION

(extrtait)

b- Taux de la contribution

    Taux de cotisation pour la formation professionnelle continue
    
| Effectif moyen de l'entreprise | Taux de cotisation (entreprises générales) | Taux de cotisation (entreprises de travail temporaire) |
| ------------------------------ | ------------------------------------------ | ------------------------------------------------------ |
|      Jusqu'à 10 salariés       |                  0,55 %                    |                          0,55 %                        |
|    À partir de 11 salariés     |                    1 %                     |                           1,3 %                        |

<p style='font-size: 12px;'>Certaines branches professionnelles peuvent fixer des taux supérieurs.</p>

c -Lissage en cas de franchissement des seuils d'effectifs

L'application de taux spécifiques permet de lisser la hausse de la contribution en cas de franchissement du seuil de 10 salariés.  


    Taux applicable en cas de franchissement de seuils
    
| Passage à 11 salariés                               |  Année N  | Année N+1 | Année N+2 | Année n-3 | Année N-4 | Année N+5 |
| --------------------------------------------------- | ------- - | --------- | --------- | --------- | --------- | --------- |
| Taux applicable (entreprises générales)             |   0,55 %  |   0,55 %  |   0,55 %  |   0,70 %  |   0,90 %  |    1 %    |
| Taux applicable (entreprises de travail temporaire) |   0,55 %  |   0,55 %  |   0,55 %  |   1,30 %  |   1,30 %  |   1,30 %  |

<p style='font-size: 10px;'>Attention : le lissage ne s'applique pas si l'accroissement de l'effectif résulte de la reprise ou de l'absorption d'une entreprise ayant employé au moins 11 salariés au cours de l'une des 3 années précédentes. Dans ce cas, le passage au taux de 1 % s'applique dès l'année durant laquelle l'effectif de 10 salariés est atteint ou dépassé.  </p>  
  

## MASSE SALARIALE

<p style='font-size: 14px;'>Extrait du Rapport financier annuel 2019, p 297</p>  

...  
Personnel<p style='font-size: 10px;'>(en millions d’euros, sauf les effectifs)</p> 

|                                                               |  2019   |  2018   |  2017   |  2016   |  2015 |
| ------------------------------------------------------------- | ------- | ------- | ------- | ------- | ----- |
| Effectif moyen pendant l’exercice (équivalent temps plein)    |   66755 |   68871 |   72098 |   76301 | 80741 |
| Montant de la masse salariale de l’exercice                   |    4055 |    4155 |    4184 |    4222 |  4277 |
| Montant des sommes versées au titre des avantages sociaux (0) |    2294 |    2358 |    2285 |    2285 |  2268 |
 
<p style='font-size: 10px;'>(0) Scurité sociale, œuvres sociales, etc...  Inclut l’intéressement (le montant de la masse salariale utilisé pour le calcul de l’intéressement versé par la société Orange SA est de 4 055 millions d’euros pour l’exercice 2019).</p>  
```

## CALCUL

from IPython.display import display, HTML

# CALCUL
taux = 0.55
masse_salariale = 4055000000
budget_formation  = round(taux * masse_salariale / 100, 2)
display(HTML(f"<p style='font-size: 24px'>BUDGET FORMATION (exercice 2019):<br><br><b>{budget_formation}0</b> €</p>"))

