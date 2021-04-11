# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 19:55:16 2021

@author: 35mer
"""
d=dict()
grades=list()
ogrenci_sayisi=int(input("Hesaplama yapmak istediğiniz ögrenci sayısını girin\n"))
sinav_adlari=["midterm","proje","final"]
for i in range(0,ogrenci_sayisi):
    isim=input("{}. kullanıcı ismini ve soyismini girin\n".format(i+1))
    d[isim]=list()
    for j in range(0,3):       
        d[isim].append(int(input("{} notunu gir\n".format(sinav_adlari[j]))))
    
    d[isim].append(d[isim][0]*0.3+d[isim][1]*0.3+d[isim][2]*0.4)
    grades.append([d[isim][3],isim])

final_list=list()
for k in range(0,len(grades)):
     final_list.append(max(grades))
     grades.remove(max(grades))
    
for l in range(0,len(final_list)):
    print("Öğrenci Adı/     Geçme Notu\n""{}                {}".format(final_list[l][1],final_list[l][0]))