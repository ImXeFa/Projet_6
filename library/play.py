#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

#Choix de l'hôte a configurer
choix_hote=str(input("\nQuel hôte souhaiter vous configurer ? \nTapper \"all\" pour configurer tous les hôtes\n"))

#Test pour verifier si un hote est joignable, passe si l'on configurer tous les hôte
if choix_hote != "all":
  response = os.system(f"ping -c 3 {choix_hote}> /dev/null")
else:
  response = int("0")

#Test pour verifier si le ping fonctionne
if response == 0:
  print("\nConnection réussi\n")
  #Demande du mots de passe de l'administrateur pour l'hote en question
  mdp= str(input("Quel est votre mots de passe ?\n"))
  #Lancement de Ansible
  os.system(f'ansible-playbook /etc/ansible/playbook.yml -e ansible_become_pass={mdp} -e chote={choix_hote}')
else:
  #Test raté, Fin de programe
  print("\nErreur lors de la communication entre machine")
