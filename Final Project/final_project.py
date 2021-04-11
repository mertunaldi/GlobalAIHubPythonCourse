# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 18:20:50 2021

@author: 35mer
"""

questions_true_answer=[["İstanbul hangi coğrafi bölgede yer alır?","Marmara"],
                      ["İnsan dolaşım sisteminde yer alan ortalama 5 litrelik sıvı nedir?","Kan"],
                      ["En büyük rakam kaçtır","9"],
                      ["İzmirin plaka kodu nedir","35"],
                      ["Türkiye'nin başkenti neresidir","Ankara"],
                      ["Global AI verdiği Python Giriş eğitimi kaç gün sürdü","5"],
                      ["3. ay nedir?","Mart"],
                      ["Bir uçan memeli hayvan ismi?","Yarasa"],
                      ["Bir deste kaç adetten oluşmaktadır?","10"],
                      ["Bir düzine kaç adetten oluşmaktadır?","12"]]
genel_puan_durumu=int()
for i in range(0,10):
    alinan_cevap=input("{}.sorunuz\n{}\n".format(i+1,questions_true_answer[i][0]))
    if(alinan_cevap==questions_true_answer[i][1]):
        genel_puan_durumu+=10
        print("Soruyu doğru bildiniz anlık puanınız {}\n".format(genel_puan_durumu))
    else:
        print("Yanlış cevap anlık puanınız {}\n".format(genel_puan_durumu))

if(genel_puan_durumu>=50):
    print("Tebrikler sınavı başarıyla bitirdiniz.Puanınız: {} Dogru Sayısı:{}\n".format(genel_puan_durumu,int(genel_puan_durumu/10)))
else:
    print("Sınavı geçemediniz!Puanınız: {} Dogru Sayısı:{}".format(genel_puan_durumu,int(genel_puan_durumu/10)))    