# Hackaton_Data

# __Introduction__

En partenariat avec le DataBab de l'Elysée, nous nous sommes attelé à cette tâche.

# __Les données__

Grâces au sources fournis par le DataLab, Nous avons pu explorer plusieurs dataset open source et publique, résumant les différens actes et les différentes conséquences des précédénte campagne de vaccination contre la grippe.

Nous avons décidé de fusionner plusieurs de ces DataSet en un seul, permettant de mettre en corrélation la plupart de ces données a l'échelle départementale, régionale mais aussi nationale.

Les DataSet que nous avons pris comme base montrent des données telles que la couverture vaccinnale par région, par tranche d'âge mais aussi le taux de passage au urgences.

Ces données ont été compilé dans une "Master DataSet".

# Notre réalisation

Nous avons décidé de réaliser un modèle prédictif se basant que des modèles pré éxistant tels que  XGBoost et Prophet.

L'objectifs de ces prédictions est de déterminer quels sont les saisons mais aussi les régions les plus a risques et généralement les plus touché pendant les périodes de grippe. Permettant ainsi de mieux répartir les doses de vaccin et de réduire la pression sur les infrastructures hospitalière.

# Rendu

Pour le coté simple, nous avons créé plusieurs notebook Jupyter  permettant d'éxécuter les différentes fonction et d'entrainer les modèles avec nos données.
Nous avons également ajouté un dashboard

# Exécuter le projet

Pour lancer les notebooks allez dans un terminal et entrez :

``cd projet``

Afin de se placer dans le dossier contenant les différents notebooks, puis :

`` python run_all.py``

Afin d'éxécuter en une fois les 5 notebooks
