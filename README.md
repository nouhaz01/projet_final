Le projet vise à simuler un projet d'entreprise réel où plusieurs développeurs travaillent sur le même projet. 

Nous avons commencé par créer un Repository GitHub contenant un README et un .gitignore.
Ensuite, nous avont fait le clonage du repository, cela crée une copie locale du repository sur la machine de chacun de nous.

Un modèle de clustering Kmeans a été développé, chacun de nous a utilisé un méthode de réduction de dimension  (dev 1 : ACP, dev 2: UMAP, dev3 :TSNE), l'objectif est de de comparer ces trois méthodes.

Un modèle supplémentaire 'agg_clustering()' (BONUS) a été développé également.

Chaque developpeur a crée une branche intitulée method_kmeans ( eg : ACP_kmeans, UMAP_kmeans..)
Nous avons inclu dans une partie du code (BONUS), une boucle pour changer les données dans chaque itération, aussi, nous avons crée une partie du code qui permet la visualisation (BONUS).

Chaque développeur a travaillé individuellement et d'une manière indépendante sur un fichier template_method_kmeans.pynb portant sur son approche qu'il a développée. Ensuite, restant dans la branche du développeur, celui-ci a adapté son fichier main.py et l'a fusionné avec la branche main.

Nous avons optimisé le code pour éviter de les télécharger à chaque instantiation d'un nouveau conteneur (BONUS).

Des conflits ont été constatées, nous les avons ensuite résolus.
Nous avons crée un fichier requirements.txt qui contient toutes les dependencies.

Par la suite, dev1 a crée un dockerfile afin de créer l'image Docker.
Dans d'attente de la création de l'image, time's out.

Le travail asynchrone a permis à chaque développeur de contribuer de manière indépendante, et la fusion des branches a été réalisée de manière coordonnée. Le résultat est un projet bien structuré, avec une documentation complète et une automatisation de déploiement en production.

