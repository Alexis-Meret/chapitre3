# -*- coding: utf-8 -*-
"""
Created on Fri Jul  3 07:25:36 2020

@author: User
"""


import numpy as np
from PIL import Image
import matplotlib.pyplot  as plt

"""question 1"""
im=Image.open("output_00205.jpg")
tab=np.array(im,dtype="uint8")
print(tab[195,429])#--->[ 81 132   0]
print(tab[200,429])#--->[ 93 127   0]
print(tab[205,429])#--->[103 122   0]
print(tab[195,435])#--->[ 89 141   0]
print(tab[195,425])#--->[ 81 132   0]
print(tab[200,200])#--->[174 176 171]
def f(tab):
    tab_new=np.array(tab, dtype=float)#conversion pour éviter d'envetuels overflow
    h,k,l=np.shape(tab_new)
    tab_zero=np.zeros((h,k,l))
    test=tab_new[:,:,2] < 5#génération du tableau test
    tab_new[test,:]=tab_zero[test,:]
    tab_new=np.array(tab_new,dtype="uint8")#reconversion
    nouvelle_image = Image.fromarray(tab_new)
    nouvelle_image.save("photo.jpg")
    nouvelle_image.show()

"""question2"""
def barycentre (tab):
    tab_new=np.array(tab, dtype=float)
    n,p,q=np.shape(tab_new)
    tab_colonnes,tab_lignes=np.meshgrid(np.arange(0,p,1),np.arange(0,n,1))#X = colonnes et Y =lignes
    test=tab_new[:,:,2] < 5
    y=np.around(np.mean(tab_lignes[test]))#valeur moyenne des lignes "vertes"
    x=np.around(np.mean(tab_colonnes[test]))#valeur myenne des colonnes "vertes"
    return [x,y]


def extraction():
    X=[]
    Y=[]
    T=[]
    for  i in range(1,242):
        file = ("output_{:05d}.jpg".format(i))#d pour injecter un entier decimal en base dix
        im=Image.open(file)
        X.append(barycentre(im)[0])
        Y.append(barycentre(im)[1])
        T.append((i-1)/25)
    plt.plot(T,X,label="X(t) : dépalcement horizontal")
    plt.grid()
    plt.xlabel("temps(s)")
    plt.ylabel("position horizotale en pixel")
    plt.legend()
    plt.show()
    return X,Y,T
extraction()



