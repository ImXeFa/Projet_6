#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

#Demande de l'hote a configurer
ch_hote=str(input("\nQuel hôte voulez vous configurer ? \nTapper all pour tous les configurer\n"))
#Demande du mots de passe de l'administrateur pour l'hote en question
mdp= str(input("Quel est votre mots de passe ?\n"))
#test pous savoir si l'hote peut se ocnnecter ou non
response = os.system(f"ping -c 3 {ch_hote}")

#Si le ping fonctonne: on lance le procesus Ansible et si il ne fonctionne pas on l'arrête
if response == 0:
  os.system(f'ansible-playbook /etc/ansible/playbook.yml -e ansible_become_pass={mdp} -e chote={ch_hote}')
else:
  print("\nerreur lors de la communication entre machine")
