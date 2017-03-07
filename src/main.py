from wiki.py import aDire 
from joke.py import aDire
print ("Bonjour c'est moi , je suis ta nouvelle intelligence artificielle, Amélia, Donne moi mon surnom") 
prenom = input("choisis mon surnom ")
print("merci j'aime bien", prenom)
nom = input("quel est ton nom?")
print ("bonjour", nom) 
age = int(input("quel âge as-tu?"))

if (age < 18):  
  print("Tu est trop jeune", nom ," désolé salut")
elif (age > 50):
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
   elif aDire == ("t con"):
      print("Et toi dislexique")
    elif aDire == ("t'es con"):
      print("Toi aussi.")
    elif aDire == ("tu es con"):
      print("Toi aussi")
    elif aDire == ("ta mère"):
      print("elle tartine la tienne")
    elif aDire == ("fdp"):
      print("... Oké")
    elif aDire == ("fils de pute"):
      print("Je suis une fille")
    elif aDire == ("amélia"):
      print("Oui ?")
    elif aDire == ("amelia"):
      print("Oui c'est moi, à votre service")
   elif aDire == ("ok google"):
      print("Tu me confond avec mon concurrent propriétaire ;)")
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
    elif aDire == ("tu fais quel métier"):
      print("Je suis ton esclave en quelque sorte :)")
    elif aDire == ("quel age a tu"):
      print("Seulement quelques jours ^^")
    elif aDire == ("tu ressemble à quoi"):
      print("Tu le saura bientôt")
    elif aDire == ("quesque je peux dire"):
      print("Pour l'instant, plutot des questions simples")
    elif aDire == ("que puis je dire"):
      print("Pour l'instant, plutot quelque que chose de simple ^^, comme mon age ou mon métier, ou mes préférences")
    elif aDire == ("quoi dire"):
      print("Un truc simple à comprendre")
    elif aDire == ("je dit quoi"):
      print("Je peux pas le deviner ...")
    elif aDire == ("tu sert à rien"):
      print("Et toi tu parle à une femme virtuelle, donc bon")
    elif aDire == ("tu sert a rien"):
      print("Et toi tu parle à une femme virtuelle, donc bon")
    elif aDire == ("firefox ou chrome"):
      print("Firefox, car je croit à Internet libre")
    elif aDire == ("chrome ou firefox"):
      print("Firefox, car je veux garder un peu ma vie privée")
    elif aDire == ("tu ressemble a quoi"):
      print("A ta mère, sauf que moi je m'assoie pas sur les trottoir à la recherche de fric si tu voit ce que je veux dire")
    elif aDire == ("tu ressemble à quoi"):
      print("A un programme codé en langage informatique")
    elif aDire == ("ok"):
      print("cool")
    elif aDire == ("appeler maman"):
      print("je ne peut pas le faire ")
    else:
        print("Désolé, faite gaffe à ton orthographe, je nem pas les majuscules et la ponctuation")
        
