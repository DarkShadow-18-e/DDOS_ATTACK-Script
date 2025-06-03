# DDOS_ATTACK-Script

Manuel d'utilisation de "DDOS_ATTACK-Script"
Introduction
"DDOS_ATTACK-Script" est une application Python dotée d'une interface graphique simple qui permet d’envoyer des paquets ICMP (ping) vers une adresse IP spécifiée. Elle se veut une alternative conviviale à l’outil en ligne de commande hping3, facilitant la configuration et l’envoi de paquets réseau.

Pré-requis
Python 3.x installé sur votre système.
La bibliothèque scapy installée (pip install scapy).
Les droits administrateur/super utilisateur pour permettre l’envoi de paquets réseau bruts.
Lancement de l'application
Ouvrir le terminal ou l’invite de commande.
Naviguer jusqu’au répertoire contenant le fichier Python de l’application.
Lancer le script avec la commande :

python nom_du_script.py
Remarque : Selon votre configuration, vous pourriez avoir besoin de lancer en mode administrateur ou avec sudo (sur Linux/Mac).

Utilisation de l'interface
L’interface se compose de :

Champ "Adresse IP" : pour saisir la cible (exemple : 192.168.1.1).
Champ "Nombre de paquets" : pour définir combien de paquets envoyer (par défaut : 1).
Bouton "Envoyer Ping" : pour lancer l’envoi.
Zone de message "Statut" : pour voir le résumé de l’action.
Étapes pour envoyer un ping
Saisir l'adresse IP cible dans le champ "Adresse IP".

Exemple : 8.8.8.8 pour Google Public DNS.
Indiquer le nombre de paquets à envoyer dans "Nombre de paquets".

Par défaut, c’est 1.

Vous pouvez augmenter ce nombre pour envoyer plusieurs ping (ex : 5).

Cliquer sur "Envoyer Ping".

Le programme enverra le nombre spécifié de paquets ICMP vers l’adresse indiquée.

La zone "Statut" affichera un message de confirmation, par exemple :


Envoi de 3 ping(s) à 8.8.8.8
Précautions et conseils
Droits administrateur : certains systèmes requièrent des droits élevés pour envoyer des paquets bruts, assurez-vous d’exécuter le script avec les privilèges nécessaires.
Légalité : utilisez cet outil uniquement sur des réseaux et avec des cibles pour lesquels vous avez l’autorisation.
Réseau : si vous ne recevez pas de réponse ou si l’envoi échoue, vérifiez votre connexion ou la configuration du pare-feu.
