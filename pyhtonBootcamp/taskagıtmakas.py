import random
def tas_kagit_makas_EBRU_SAĞMAK():
 print("TAŞ KAĞIT MAKAS OYUNUNA HOŞGELDİN\nKURALLAR:\n1.Taş Makası yener\n2.Makas Kağıdı yer\n3.Kağıt Taşı yener\n4.Her iki oyuncu da aynı seçimi yaparsa,durum berabere olur\n5.İlk iki galibiyeti alan oyunu kazanır.\n")

  

   
 tur_sayac=0
 bil_kazandı=0
 sec_kazandı=0
 print("TAŞ KAĞIT MAKAS OYUNUNA HOŞGELDİN")
 isim=input("litfen isminizi girer misiniz?\nİSİM: ")
 while tur_sayac<3:
   secsayi=0
   bilgisayarsayi=0
   sayac=0
    
   while sayac<3:
      bilgisayar=input("TAŞ,KAĞIT,MAKAS BUNLARDAN BİRİNİ SEÇİNİZ LÜTFEN\nSEÇİMİNİZ: ").lower()

      liste=["taş","kağıt","makas"]
      sec=random.choice(liste).lower()

      print("BİLGİSAYARIN SEÇİMİ:",sec)

 

      if bilgisayar==sec:
       print("SEÇİMLER EŞİT")
       continue
      elif bilgisayar=="taş" and sec=="kağıt":
       bilgisayarsayi+=1
       print("bilgisayar: ",bilgisayarsayi)
       print(isim,":",secsayi)
      elif bilgisayar=="taş" and sec=="makas":
       secsayi+=1
       print("bilgisayar: ",bilgisayarsayi)
       print(isim,":",secsayi)
      elif bilgisayar=="kağıt" and sec=="taş":
       secsayi+=1
       print("bilgisayar: ",bilgisayarsayi)
       print(isim,":",secsayi)
      elif bilgisayar=="kağıt" and sec=="makas":
       bilgisayarsayi+=1
       print("bilgisayar: ",bilgisayarsayi)
       print(isim,":",secsayi)
      elif bilgisayar=="makas" and sec=="taş":
       bilgisayarsayi+=1
       print("bilgisayar: ",bilgisayarsayi)
       print(isim,":",secsayi)
      elif bilgisayar=="makas" and sec=="kağıt":
       secsayi+=1
       print("bilgisayar: ",bilgisayarsayi)
       print(isim,":",secsayi)  
      else:
        print("geçersiz opsiyon girdiniz")
        print("lütfen yeniden bir seçenek giriniz")
        continue
      sayac+=1
   if secsayi>bilgisayarsayi:
        sec_kazandı+=1
        print(f"{tur_sayac + 1}.TURUN KAZANANI:\n{isim}={secsayi}\nBilgisayar={bilgisayarsayi}")
   elif secsayi<bilgisayarsayi:
        bil_kazandı+=1
        print(f"{tur_sayac + 1}.TURUN KAZANANI:\nBilgisayar={bilgisayarsayi}\n{isim}={secsayi}")  
   tur_sayac+=1
 if sec_kazandı>bil_kazandı:
   print(f"TEBRİKLER OYUNU {isim} KAZANDI.")
 elif bil_kazandı>sec_kazandı:
   print("OYUNU BİLGİSAYAR KAZANDI.")
 else: 
   print("MAÇ BERABERE BİTTİ")  
   
   
   

   

      


   
tas_kagit_makas_EBRU_SAĞMAK()



oyundevametsinmi=input("oyuna devam etmek ister misiniz?\n EVET/HAYIR\nCEVAP:")
liste1=["evet","hayır"]
oyundevametsinmi1=random.choice(liste1)
print("BİLGİSAYARIN CEVABI:",oyundevametsinmi1)
while True:
 if oyundevametsinmi=="evet" and oyundevametsinmi1=="hayır":
   print(f"sizin cevabınız:{oyundevametsinmi},bilgisayarın cevabı:{oyundevametsinmi1}")
   print("oyuna devam edilmiyor")
   break
 elif oyundevametsinmi=="hayır" and oyundevametsinmi1=="evet":
   print(f"sizin cevabınız:{oyundevametsinmi},bilgisayarın cevabı:{oyundevametsinmi1}")
   print("oyuna devam edilmiyor")
   break
 elif oyundevametsinmi=="hayır" and oyundevametsinmi1=="hayır":
   print(f"sizin cevabınız:{oyundevametsinmi},bilgisayarın cevabı:{oyundevametsinmi1}")
   print("oyuna devam edilmiyor")
   break
 if oyundevametsinmi=="evet" and oyundevametsinmi1=="evet":
   print(f"sizin cevabınız:{oyundevametsinmi},bilgisayarın cevabı:{oyundevametsinmi1}")
   print("oyuna devam ediliyor")
   tas_kagit_makas_EBRU_SAĞMAK()
   oyundevametsinmi=input("oyuna devam etmek ister misiniz?\n EVET/HAYIR\nCEVAP:").lower()
   oyundevametsinmi1=random.choice(liste1)


   
 else:
   print("geçersiz cevap girdiniz")
   continue
 oyundevametsinmi=input("oyuna devam etmek ister misiniz?\n EVET/HAYIR\nCEVAP:").lower()
 oyundevametsinmi1=random.choice(liste1)
  


   




   


    
    

