# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:54:49 2021

@author: 35mer
"""


kullanici_bilgileri={"mert":"mert"}

girdi=0
def Giris_ekrani():
  global girdi
  girdi=int(input("Merhaba Kullanıcı Arayüzüne Hoş Geldiniz\n->Kayıtlı Kullanıcı Girişi için 1'e Basın\n->Kayıt Olmak için 2'ye Basın\nSistemden Çıkmak için 0'a Basın\n"))
  
def Secim_tanimlama(tercih):
  if tercih == 1:
    Kullanici_giris()
  elif tercih == 2:
    Kullanici_kayit()
    
  elif tercih == 0:
    print("Çıkış gerçekleştirildi")
    
def Kullanici_giris():
  kullanici_ismi=input("Kulanıcı adınızı giriniz\n")
  if kullanici_ismi in kullanici_bilgileri.keys():
    kullanici_sifresi=input("Şifrenizi giriniz\n")
    if kullanici_sifresi == kullanici_bilgileri[kullanici_ismi]:
        print("Hosgeldin {} Oturum Açma Başarılı".format(kullanici_ismi))
    else:
        print("Girdiğiniz şifre yanlıştır.Tekrar deneyin\n")
        Kullanici_giris()
       
  else:
    print("Böyle bir kullanici yer almamaktadir.Giriş ekranına yönlendiriliyorsunuz.")
    Giris_ekrani()
    Secim_tanimlama(girdi)

def Kullanici_kayit():
   kullanici_adi=input("Kullanıcı adınızı girin\n")
   if kullanici_adi in kullanici_bilgileri.values():
       print("Bu kullanıcı adı kullanılmaktadır.\n")
       secim=int(input("Yeniden denemek için 1'i giriş ekranına dönmek için 0'a basın\n"))
       if secim == 1:
           Kullanici_kayit()
       elif secim == 0:
           Giris_ekrani()
           Secim_tanimlama(girdi)
   else:
       kullanici_sifre=input("Kullanıcı sifresi girin\n")
       kullanici_bilgileri[kullanici_adi]=kullanici_sifre
       print("Kayıt gerçekleştirildi.Giris ekranına yönlendiriliyorsunuz")
       Giris_ekrani()
       Secim_tanimlama(girdi)
Giris_ekrani()
Secim_tanimlama(girdi)