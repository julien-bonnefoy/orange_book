# PRELIMINAIRES

## BESOIN FONCTIONNEL du/des clients

### DASHBOARD

#### Panel 1: Distribution statistique

```{panels}
:header: text-center

---

{badge}`PAS DE FOURNISSEUR SELECTIONNE, badge-dark badge-pill`

^^^

<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>BAR CHART</span> Réparttion des L.O. par Fournisseur</p>
<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>KPI</span> Nombre et distribution des L.O. par types</p>
<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>SUNBURST</span> Actif - Non actif vs. Type</p>

---

{badge}`FOURNISSEUR SELECTIONNE, badge-dark badge-pill`

^^^

<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>PIE CHART</span> Réparttion par 'Types'</p>
<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>KPI</span> Nombre et distribution des L.O. par types</p>
<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>PIE CHART</span> Répartition Actif - Non actif'</p>

```

#### Panel 2: Mots les plus fréquents

Pour introduire l'extraction automatique de mots clés, 


```{panels}
:body: text-center
---
{badge}`PAS DE FOURNISSEUR SELECTIONNE, badge-dark badge-pill`
---
{badge}`FOURNISSEUR SELECTIONNE, badge-dark badge-pill`
```

<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>WORDCLOUD + BAR CHART</span> Mots les plus fréquents (en dehors des "stopwords")</p>
<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>SPECIAL FEATURE</span> permettant d'ajouter "X" mots les plus fréquents aux "stopwords" et d'en voir l'impact sur les 2 visualisations précédentes</p>

#### Panel 3: Score de "pertinence" des Tiitres

Après extraction automatique des mots clés par TF-IDF (cf. bientôt) et pour **TOUS** les Learning Objects (fr) sélectionnables un à un

```{panels}
:body: text-center
---
{badge}`PAS DE FOURNISSEUR SELECTIONNE, badge-dark badge-pill`
---
{badge}`FOURNISSEUR SELECTIONNE, badge-dark badge-pill`

```

<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>LED DISPLAY</span> Décompte des L.O. + L.O. actifs + Score Moyen de "Pertinence"</p>
<p>- <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>FACE/FACE</span> Mots du Titre face aux Mots-ckés extraits automatiquement</p>

### CLASSIFICATION AUTOMATIQUE des LEARNING OBJECTS

<p>- Catégorie: <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>MATIERE DE LA FORMATION PARENTt"</span></p>
<p>- Catégorie: <span style='color: #fff; background-color: #f16e00; text-align: center; line-height: 22px; font-size: 14px; font-weight: bolder; padding-top: 2px; opacity: 0.7;'>MATIERES DE LA FOR%ATION"</span></p><br>
(Cf. bientôt)


## CHOIX des TECHNOLOGIES

### Module base de données

<img src="../../static/img/mysql_150.jpeg" alt="mySQL icon" style="float: left; margin-right: 50px; height: 150px;" />

- **mySQL** car bases de données relationnelles il y aura:
    * LA référence
    * déjà installé sur le matériel.
    * d'interface facilement avec Python


- **mysql-server** est installé sur un serveur personnel Apache2.0

### Module Entraînement

<img src="../../static/img/sklearn_150.png" alt="SciKit Learn icon" style="float: left; margin-right: 50px; height: 150px;" />

**SciKit Learn**
- pour le Machine Learning classique<br>

<img src="../../static/img/keras_tf_150.png" alt="Keras + TensorFlow icon" style="float: left; margin-right: 50px; height: 150px;" /><br>

**TensorFlow + Keras**
- pour le Deep Learning<br>

### Module application

<img src="../../static/img/flask_python_150.png" alt="Python Flask icon" style="float: left; margin-right: 50px; height: 150px;" />

**Flask**
* simple
* modulable (login, monitoring...) et
* facilemet deployable

<img src="../../static/img/dash_150.png" alt="Dash icon" style="float: left; margin-right: 50px; width: 200px;" />

**Dash**
* complet et
* customizable

