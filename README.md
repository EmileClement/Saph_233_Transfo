# Saph 233 Inductance
Le but de ce projet est de dimentionner une inducatance. Elle doit etre la plus petite possible tout en stockant une energie de 4J. Elle ne doit pas non plus surchauffer lorsque le courant électrique la traverse.

## Methode de modélisation du transformateur
On utilise une classe inductance, crée par J.OJEDA, pour representer une inductance. Cette classe permet d'intéragir avec FEMM pour obtenir les performances.
![system overview](http://www.plantuml.com/plantuml/proxy?cache=no&src=https://raw.github.com/EmileClement/Saph_233_Transfo/master/assets/Diagramme_classe.iuml)
## Fonction du coût
La fonction doit prendre en compte le volume de l'inductance, les pertes et l'energie stocké.

## Minimisation du coût
'''plantuml
@startuml
Inductance : - volume_externe
Inductance : - hauteur
Inductance : - larger
Inductance : - l_active
Inductance : - entrefer
Inductance : - l_dent
Inductance : - k_b
Inductance : - j_max
Inductance : - i_max

Inductance : - calcul_energie()
Inductance : - calcul_pertes_fer()
@enduml
'''
### scypi

### Platypus

### Notre algorithme évolutif
