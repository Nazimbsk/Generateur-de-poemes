## Membres du projet
* Ahmed Tahar Amar
* Nazim Bouskra

 
 # Generateur-de-Poemes
Bienvenue dans le projet Generateur-de-Poemes. Ce projet a été créé pour explorer la génération automatisée de poèmes en utilisant différentes technologies et bibliothèques.

# Bibliothèques Utilisées
Ce projet utilise deux principales bibliothèques :

PIL (Python Imaging Library) : Utilisée pour le traitement des images. Elle permet la création, la modification et la manipulation d'images en Python.

NLTK (Natural Language Toolkit) : Utilisée pour le traitement de texte. Cette bibliothèque offre des outils pour le traitement du langage naturel et est largement utilisée pour l'analyse et la manipulation de textes.

# Fichiers Utilisés
Deux fichiers sont au cœur de ce projet :

Metaphores.txt : Un fichier contenant des métaphores sous forme de poèmes. Ces métaphores ont été générées à l'aide de ChatGPT, puis extraites et traitées pour être utilisées dans le projet.

Poeme.txt : Un fichier contenant un poème généré également à l'aide de ChatGPT. Les poèmes générés sont extraits à partir de corpus de textes, puis traités pour créer des compositions poétiques.

# Génération de Poèmes et d'Images
Le processus de génération de poèmes et d'images comprend les étapes suivantes :

Extraction de Corpus : Des corpus de textes sont extraits pour fournir une base à la génération de poèmes.

Traitement de Texte : Les textes extraits sont traités à l'aide de NLTK pour améliorer la qualité et la cohérence des poèmes générés.

Génération de Poèmes : ChatGPT est utilisé pour générer des poèmes en s'inspirant des corpus de texte traités. Le code intègre également une métaphore avec une probabilité de 30%, ajoutant ainsi une touche poétique et variée aux compositions générées.

Génération d'Images : Les poèmes générés sont associés à des images. Pour créer des compositions poétiques visuelles, le programme choisit aléatoirement une image parmi celles disponibles dans le dossier 'images'.

# Instructions d'Utilisation
Pour utiliser ce projet, assurez-vous d'avoir installé les dépendances nécessaires mentionnées dans le fichier `requirements.txt`. Ensuite, exécutez le script principal pour générer des poèmes et des images.

python3 nltk_poeme.py

N'oubliez pas d'explorer l'image générée dans le répertoire pour découvrir le poème ainsi que l'image créée par le générateur.


