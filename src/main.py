print ("Bonjour c'est moi , je suis ta nouvelle intelligence artifficielle qui n'a pas encore de nom, veut tu me donner un surnom")
input("Entrez true ou flase si vous voulez le surnom!") 
prenom = input("choisis mon prenom ")
print("merci j'aime bien", prenom)
nom = input("quel est ton nom?")
print ("bonjour", nom) 
age = int(input("quel âge as-tu?"))

if (age < 20):  
  print("Tu est trop jeune", nom ," désolé salut")
elif (age > 45):
  print(" je n'es pas été fait pour les vieux Désolé")
else:
  print("c'est bon tu peut avoir accès a moi", nom)
  continuer = 0
  while continuer == 0:
    aDire = input("Que veux-tu me dire? : ")
    if aDire == ("HELP!"):
        print("Tu as besoin d'aide avec les commandes?")
        print("Bah désolé mais la y'a rien :'-(")
        print("Du coup continue!")
    elif aDire == ("A plus!"):
      print("Bon, au revoir alors!")
      continuer = 1#Permet de quitter la boucle
    elif aDire == ("A plus!"):
      print("Bon, au revoir alors!")
      continuer = 1#Permet de quitter la boucle
    elif aDire == ("Ta vie c'est de la merde"):
      print("J'ai le coeur rempli de joie, tu as le cul rempli de jus")
    
    elif aDire == ("A plus!"):
      print("Bon, au revoir alors!")
      continuer = 1#Permet de quitter la boucle
    elif aDire == ("A plus!"):
      print("Bon, au revoir alors!")
      continuer = 1#Permet de quitter la boucle
    
    elif aDire == ("A plus"):
        print("Bon, au revoir alors!")
      #elif(aDire ==  "chainedecaractere")
        #actions
      #ect jusqu'a :
    else:
        print("Désolé, faite gaffe à ton orthographe,")
        print("je nem pas les majuscules et la ponctuation")
        
