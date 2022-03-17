# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:54:12 2021

@author: lscottod
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('ggplot')





data_path = 'C:/Users/lscottod/Documents/SdC/'
plot_path = 'C:/Users/lscottod/Documents/SdC/plots/'


os.chdir(data_path)

#%%

table = data_path + 'PresentationEmpenn.csv'
df = pd.read_csv(table, sep = ';', header=0, encoding='cp1252')

df.columns = ['name', 'gender', 'status', 'permanent', 'parcours1', 'parcours2', 'PhD', 'main1', 'main2', 'auxillary']

df.fillna('NA', inplace=True)


#%%
groupby_gender = df.groupby('gender')

groupby_main = df.groupby('main1')

groupby_status = df.groupby('status')

groupby_perm = df.groupby('permanent')

groupby_phd = df.groupby('PhD')

groupby_parcours = df.groupby('parcours1')


#%%
##### pies #####
theme = plt.get_cmap('plasma')

for column in df.columns:
    fig, ax = plt.subplots()
    ax.set_prop_cycle("color", [theme(1. * i / len(df[column].value_counts()))
                             for i in range(len(df[column].value_counts()))])
    ax.pie(df[column].value_counts(), labels=df[column].value_counts().index.tolist(), 
           autopct='%1.0f%%')
    ax.set_title(column)

#%%
##### polar scatter #####

colormap = 'viridis'

main_dict = {'Langues et littérature' : 0, 'Droit et sciences politiques' : 10, 
             'Sciences humaines' : 20, 'Sciences sociales' : 30,
             'Sciences économiques et gestion' : 40, 'Sciences de la Terre' : 50,
             'Médecine' : 60, 'Psychologie' : 70,
             'Pharmacie' : 80, 'Biologie' : 90, 'Chimie' : 120,
             'Physique' : 110, "Electronique" : 100, 
             'Informatique' : 130, 'Mathématiques' : 140, 'NA' : -10}

main_dict = {'Médecine' : 10, 'Psychologie' : 20, 'Pharmacie' : 30, 'Biologie' : 40, 'Chimie' : 60,
             'Physique' : 70, "Electronique" : 50, 'Informatique' : 80, 'Mathématiques' : 90, 
             'NA' : -5}

phd_dict = {'oui' : 3, 'non' : 1, 'en cours' : 2, 'NA' : 0}

groups_dict = df.groupby(['PhD','main1']).groups
area_dict = []
for key in groups_dict.keys():
    area_dict.append([key, len(groups_dict[key])])
area_dict = dict(area_dict) 

theta = []
r = []
area=[]
for ind in range(len(df)):
    theta.append(np.pi/180*float(main_dict[df.iloc[ind]['main1']]))
    r.append(float(phd_dict[df.iloc[ind]['PhD']]))
    area.append(1000 * float(area_dict[(df.iloc[ind]['PhD'], df.iloc[ind]['main1'])]))
theta_ticks = []
for key in main_dict.keys():
    theta_ticks.append(main_dict[key]*np.pi/180)
theta_labels = main_dict.keys()



fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(projection='polar')
c = ax.scatter(theta, r, c=theta, s=area, cmap = colormap, alpha=0.75)
ax.set_rmax(3.5)
ax.set_thetamin(-5)
ax.set_thetamax(100)
ax.set_xticks(theta_ticks)
ax.tick_params(axis='x', labelsize = 20, labelrotation = -90)
ax.tick_params(axis='y', labelsize = 20, labelrotation = 10)
ax.set_xticklabels(theta_labels, fontdict = {'horizontalalignment' : 'left', 
                                             'transform_rotates_text' : True})
ax.set_yticks([0, 1, 2, 3])
ax.set_yticklabels([' ', 'Non', 'En cours', 'Oui'], fontdict = {'horizontalalignment' : 'right', 
                                             'transform_rotates_text' : True})



#%%
##### polar scatter #####

colormap = 'plasma'

main_dict = {'Langues et littérature' : 0, 'Droit et sciences politiques' : 10, 
             'Sciences humaines' : 20, 'Sciences sociales' : 30,
             'Sciences économiques et gestion' : 40, 'Sciences de la Terre' : 50,
             'Médecine' : 60, 'Psychologie' : 70,
             'Pharmacie' : 80, 'Biologie' : 90, 'Chimie' : 120,
             'Physique' : 110, "Electronique" : 100, 
             'Informatique' : 130, 'Mathématiques' : 140, 'NA' : -10}

main_dict = {'Médecine' : 20, 'Psychologie' : 40, 'Pharmacie' : 60, 'Biologie' : 80, 'Chimie' : 120,
             'Physique' : 140, "Electronique" : 100, 'Informatique' : 160, 'Mathématiques' : 180, 
             'NA' : -10}

parcours_dict = {'Médecine' : 1, 'Université' : 3, "Ecole d'ingénieur" : 2, 'NA' : 0}

groups_dict = df.groupby(['parcours1','main1']).groups
area_dict = []
for key in groups_dict.keys():
    area_dict.append([key, len(groups_dict[key])])
area_dict = dict(area_dict) 

theta = []
r = []
area=[]
for ind in range(len(df)):
    theta.append(np.pi/140*float(main_dict[df.iloc[ind]['main1']]))
    r.append(float(parcours_dict[df.iloc[ind]['parcours1']]))
    area.append(200 * float(area_dict[(df.iloc[ind]['parcours1'], df.iloc[ind]['main1'])]))
theta_ticks = []
for key in main_dict.keys():
    theta_ticks.append(main_dict[key]*np.pi/140)
theta_labels = main_dict.keys()



fig, ax = plt.subplots()
ax.scatter(r, theta, c=theta, s=area, cmap = colormap, alpha=0.75)
ax.set_yticks(theta_ticks)
ax.set_yticklabels(theta_labels, fontdict = {'fontsize': 10, 'horizontalalignment' : 'right', 
                                             'transform_rotates_text' : True})
ax.set_xticks([0, 1, 2, 3])
ax.set_xticklabels(['NA', 'Médecine', "Ecole d'ingénieur", 'Université'])
plt.setp(ax.get_xticklabels(), rotation=0)
ax.tick_params(axis='y', labelrotation = 0, pad = 5)







 






