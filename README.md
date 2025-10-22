# Hackaton_Data

# __Introduction__

En partenariat avec le DataLab de l'Elysée, nous nous sommes attelés à cette tâche.

# __Les données__

Grâces aux sources fournies par le DataLab, Nous avons pu explorer plusieurs dataset Open source et publique, résumant les différens actes et les différentes conséquences des précédéntes campagne de vaccination contre la grippe.

Nous avons décidé de fusionner plusieurs de ces Datasets en un seul, permettant de mettre en corrélation la plupart de ces données à l'échelle départementale, régionale mais aussi nationale.

Les Datasets que nous avons pris comme base montrent des données telles que la couverture vaccinnale par région, par tranche d'âge mais aussi le taux de passage aux urgences.

Ces données ont été compilé dans une "Master DataSet".

# Notre réalisation

Nous avons décidé de réaliser un modèle prédictif se basant que sur des modèles pré éxistant tels que  **XGBoost** et **Prophet**.

L'objectifs de ces prédictions est de déterminer quelles sont les saisons et les régions les plus à risques et généralement les plus touchées pendant les périodes de grippe. Permettant ainsi de mieux répartir les doses de vaccin et de réduire la pression sur les infrastructures hospitalière.

# Rendu

Pour le côté simple, nous avons créé plusieurs notebook Jupyter  permettant d'éxécuter les différentes fonction et d'entrainer les modèles avec nos données.
Nous avons également ajouté un dashboard

# Exécuter le projet

Pour lancer les notebooks: 

``cd projet``

Afin de se placer dans le dossier contenant les différents notebooks, puis :

`` python run_all.py``
