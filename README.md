# Saph 233 Inductance
Le but de ce projet est de dimentionner une inducatance. Elle doit etre la plus petite possible tout en stockant une energie de 4J. Elle ne doit pas non plus surchauffer lorsque le courant électrique la traverse.

## Methode de modélisation du transformateur
On utilise une classe inductance, crée par J.OJEDA, pour representer une inductance. Cette classe permet d'intéragir avec FEMM pour obtenir les performances.
![system overview](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/EmileClement/Saph_233_Transfo/master/assets/Diagramme_classe.iuml)

## scypi
On va utilisé Scypi, une librairie commune de python, pour tenter de trouver une première réponse
### Fonction du coût
La fonction doit prendre en compte le volume de l'inductance, les pertes et l'energie stocké. Elle permet de representer la qualité d'une jeu de carractéristique.
On va utilisé la fonction J = (E - 4)^2 + V^2 
### Minimisation du coût
On 
## Platypus

## Notre algorithme évolutif
