Cahier de charge de ce projet :( Languages utilisés sont : Python , HTML , CSS , JS , et Framework : Django ) 
Le Projet est une application de gestion d'école qui doit gérer tout ce qui concerne les étudiants, les professeurs, le staff d'administration, le matériel, les salles et les emplois du temps.
Ses objectifs sont de gagnée du temps en automatisée les taches, centralisé les données, facilité la recherche et sécurisé l'accès aux données.
Dans un premier temps le bureau d'administration est la seule partie qui est concernées par ce travail. Mais au fur et à mesure du développement de l'application, elle peut être partagée avec l'ensemble du personnelles de l’école (le secrétariat, les professeurs et les étudiants).
Expression fonctionnelle du besoin :
On veut réaliser l'informatisation de la gestion des étudiants au sein d'une école qui offre une
formation professionnelle en informatique.
L'école dispose de 10 salles dont 4 sont des salles d'informatiques équipées de matérielles
informatiques Chaque salle à une capacité variant de 10 à 25 places.
Le cout de la formation est 2000 DH par mois, les étudiants ont le choix de payer soit en
espèces soit par chèque.
L'inscription se fait par le remplissage d'un formulaire qui comporte l'option et le parcours désiré ainsi que les informations de l'étudiant tel que son CNE, nom, tel, année d'obtention de bac est son adresse. Les options sont : Ingénierie des Systèmes Informatique, Ingénierie des Systèmes Réseaux et Télécommunication. Les parcours sont : bac+2 ; +3 ; +5
L'option est composée de plusieurs modules, et un module contient plusieurs cours caractérisés par un nom et une masse horaire. La moyenne générale d'un module est composée de 2 contrôle continue (25%) et un examen de fin module (50%).
Le module est validé avec une note supérieure ou égale à 10, l'étudiant au droit d'un rattrapage s'il a obtenu une note entre 5 et 9.
Un cours ne peut pas être assuré par plusieurs enseignants. Les cours sont repérés par le nom de l'enseignant. Certains enseignants assurent plusieurs types de cours (algorithme, poo,...), l'enseignant est caractérisé essentiellement par son CIN, un nom et un numéro de téléphone.
Pour affecter un cours à une salle et à un enseignant, on veut Pouvoir vérifier que l'enseignant n'a pas de cours simultanément pour un autre groupe.
En ce qui concerne la gestion des absences, le traitement manuel actuel est le suivant : une feuille de présence quotidienne, marquée du n° de semaine et du nom du jour, circule d'enseignant à enseignant en cours de journée. Lorsque l'administration est avertie d'une absence d'un étudiant avant le début des cours, elle reporte la mention "Excusé sur la ligne de l'étudiant, pour chaque cours concerné. Chaque enseignant reporte la liste et le nombre d'absences non excusées et constatées à son cours. La feuille de présence retourne à l'administration en fin de journée. Toutes les absences injustifiées font l'objet d'un courrier adressé aux parents, indiquant les jours et heures d'absence de l'étudiant. Un étudiant peut être absent à un cours sans être absent sur la journée.
Une absence à un cours unique peut être justifiée à l'avance (rendez-vous dentiste...).
Gestion des étudiants :
Ajout : Pour ajouter un étudiant, un formulaire s'ouvre pour le remplir. Ce formulaire
contient les champs suivants :
• l’option et le parcours désirés :
• Les options sont :
• Ingénierie des Systèmes d'Information.
• Ingénierie des Systèmes, Réseaux et Télécommunication
• Les parcours sont : bac+2 ; +3 ; +5
• les informations de l’étudiant :
CNE (son identifiant),
• nom.
• prénom, sexe (homme, femme),
• email
• son adresse.
• année d’obtention de bac (bac Scientifique).
Suppression : un étudiant est identifié par un CNE, alors pour le supprimer l'application demande d'entrer le CNE de l'étudiant à supprimer, et de confirmer le choix.
Modification : l'application demande le CNE pour charger les informations de l'étudiant précisé, après la modification un message s'affiche pour confirmer les modifications ou les annuler.
Gestion des classes (filières) :
Ajout : pour ajouter des filières, un formulaire s'ouvre pour le remplir. Ce formulaire
Gestion des professeurs :
Ajout : Pour ajouter un professeur, un formulaire s'ouvre pour le remplir. Ce formulaire
contient les champs suivants :
• les informations de professeur: CIN
• matière enseigne, titre professeur, CV du professeur, tel
• salaire
Suppression : un professeur est identifié par un CIN, alors pour le supprimer l'application demande d'entrer le CIN de professeur à supprimer, et de confirmer le choix.
Modification : l'application demande le CIN pour charger les informations du professeur
précisé, après la modification un message s'affiche pour confirmer les modifications ou les annuler.
