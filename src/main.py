print ("Bonjour c'est moi , je suis ta nouvelle intelligence artifficielle, Amélia, Donne moi mon surnom") 
prenom = input("choisis mon surnom ")
print("merci j'aime bien", prenom)
nom = input("quel est ton nom?")
print ("bonjour", nom) 
age = int(input("quel âge as-tu?"))

if (age < 18):  
  print("Tu est trop jeune", nom ," désolé salut")
elif (age > 45):
  print(" je n'es pas été fait pour les vieux Désolé")
else:
  print("c'est bon tu peux me posez tes questions", nom)
  continuer = 0
  while continuer == 0:
    aDire = input("Que veux-tu me dire? : ")
    if aDire == ("aide"):
        print("Tu as besoin d'aide avec les commandes?")
        print("Il ne faut pas écrire de phrases trop longues, pas de ponctuation (virgules, points etc... et pas de majuscules")
        print("Continuons !")
    elif aDire == ("c'est nul"):
      print("Bon, au revoir alors!")
      continuer = 1#Permet de quitter la boucle
    elif aDire == ("au revoir"):
      print("Bon, au revoir alors!")
      continuer = 1#Permet de quitter la boucle
    elif aDire == ("Ta vie c'est de la merde"):
      print("J'ai le coeur rempli de joie, tu as le cul rempli de jus")
    
    elif aDire == ("je t'aime"):
      print("Ah, ce n'est pas reciproque...")
     
    elif aDire == ("quel heure est il"):
      print("T'as qu'a t'acheter une montre mongolito !")
    
    
    elif aDire == ("comment tu t'appelle"):
      print("Amélia, ton assistante personnelle")
    elif aDire == ("comment t'appelle tu"):
      print("Amélia, ton assistante personnelle")
    elif aDire == ("c quoi ton nom"):
      print("Amélia, ton assistante personnelle")
    elif aDire == ("comment tu tapelle"):
      print("Amélia, ton assistante personnelle")
    elif aDire == ("comment tu tappelle"):
      print("Amélia, ton assistante personnelle")
    elif aDire == ("comment tu t appelle"):
      print("Amélia, ton assistante personnelle")
    elif aDire == ("je te deteste"):
      print("Désolé si je n'ai pas pu repondre à tes attentes...")
    elif aDire == ("tu ressemble a quoi"):
      print("Pour l'instant, à pas grand chose...")
    elif aDire == ("esce que tu es belle"):
      print("Pour l'instant, à pas grand chose...")
    elif aDire == ("esque tes belle"):
      print("Pour l'instant, à pas grand chose...")
    elif aDire == ("es ce que tu es belle"):
      print("Pour l'instant, à pas grand chose...")
    elif aDire == ("pain au chocolot ou chocolatine"):
      print("alala, la grande question...")
    elif aDire == ("pain au chocolot ou chocolatine ?"):
      print("alala, la grande question...")
    elif aDire == ("pc ou mac"):
      print("Linux")
    elif aDire == ("mac ou pc"):
      print("Linux")
    elif aDire == ("iphone ou smartphone"):
      print("je préfère les hommes, donc plutot Siri :)")
    elif aDire == ("iphone ou android"):
      print("je préfère les hommes, donc plutot Siri :)")
    elif aDire == ("ios ou android"):
      print("je préfère les hommes, donc plutot Siri :)")
    elif aDire == ("siri ou cortana"):
      print("je préfère les hommes, donc plutot Siri :)")
    elif aDire == ("siri ou google"):
      print("je préfère les hommes, donc plutot Siri :)")
    elif aDire == ("siri ou ok google"):
      print("je préfère les hommes, donc plutot Siri :)")
    elif aDire == ("siri ou google now"):
      print("je préfère les hommes, donc plutot Siri :)")
      
    else:
        print("Désolé, faite gaffe à ton orthographe,")
        print("je nem pas les majuscules et la ponctuation")
        
