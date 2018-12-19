# -*- coding: utf-8 -*-

from Tkinter import *
from ttk import *

prgprincipal = Tk() #version du programme : alpha build 0.0.2

version = 2

prgprincipal.geometry ("300x700+450+500")
prgprincipal.title ("Amélia alpha build")

def aboutwindow():
    about = Tk()
    about.geometry ("300x90+350+400")
    about.title ("A propos d'Amélia")

    
    label = Label(about, text="Amélia est un logiciel libre. Codé en Python 2.7")
    label.pack()
    
    label = Label(about, text="par Mael Le Boulicaut et Evan Diberder")           
    label.pack()

    label = Label(about, text="Version Alpha 0.0.2, License GPL V3")           
    label.pack()

    
    canvas = Canvas(aboutwindow,width=60, height=25)
    canvas.create_image(1000, 1000, anchor=NW, image=visageAmelia)
    canvas.pack()

def Enter_pressed(event):
    input_get = input_field.get()
    if input_get == ("salut"):
        label = Label(prgprincipal, text="hello")
    elif input_get == ("ca va"):
        label = Label(prgprincipal, text="Bien sur et vous ?")
    elif input_get == ("comment ca va"):
        label = Label(prgprincipal, text=" Ca va bien et vous ?"
    elif input_get == ("Je suis nul"):
        label = Label(prgprincipal, text="Bien sur "
    elif input_get == ("Tu m aime"):
        label = Label(prgprincipal, text="Bah non quelle question !"
    elif input_get == ("connard"):
        label = Label(prgprincipal, text="La PS4 dans crane à ta mère"
    elif input_get == ("je comprends rien au math"):
        label = Label(prgprincipal, text="NANI"
    elif input_get == ("quand est né steve jobs"):
        label = Label(prgprincipal, text="le 24 février 1955, a San Fransisco, Californie, Etat Unis")
    elif input_get == ("steve jobs"):
        label = Label(prgprincipal, text="Steve Jobs est, avec Steve Wozniak, le cofondateur d’Apple. Ils sont tous deux considérés comme les pionniers de la micro-informatique pour avoir introduit l’ordinateur dans les foyers (bien avant l’avènement de l’IBM PC), puis pris conscience du potentiel du couple interface graphique / souris à la suite d’une visite avec une équipe de leur société au PARC de Xerox. Cette idée mènera à la commercialisation par la société Apple Computer du Macintosh, le premier ordinateur grand public profitant de ces innovations.Il est en 2009 la 43e fortune américaine.")
    elif input_get == ("guernica"):
        label = Label(prgprincipal, text="Guernica est un tableau de Pablo Picasso. Cette oeuvre d'art a été créée en réponse au bombardement de Guernica par l'aviation allemande et italienne, à la demande des forces espagnoles nationalistes, le 26 avril 1937, durant la guerre civile espagnole.")
    elif input_get == ("résumé de eldorado"):
        label = Label(prgprincipal, text="Le travail du commandant Salvatore Piracci consiste a intercepter les immigrants qui arrivent par bateau en Sicile. Ils sont clandestins et attendent tout de leur nouvelle vie. Un jour, une femme arrivée deux années plus tôt sur l'île le retrouve. Elle lui raconte dans quelles conditions elle a voyagé et comment elle a perdu son bébé qui était avec elle sur le bateau. Plus tard, un homme qui se trouvait dans un bateau de clandestins qu'il vient d' intercepter lui demande son aide. Le commandant refuse.")
    elif input_get == ("bretagne"):
        label = Label(prgprincipal, text="C'est un petit pays ayant été envahi par un pays capitaliste la France")
    elif input_get == ("résumé de pierre et jean"):
        label = Label(prgprincipal, text="Les Roland , anciens bijoutiers parisiens se sont retirés au Havre, où ils vivent des jours heureux. Ils ont deux fils : l'aîné, Pierre, près de la trentaine, brun, maigre et nerveux, tourmenté par de grands projets et sujet à des découragements imprévus , vient d'obtenir son de terminer ses études de médecine.Les Roland , anciens bijoutiers parisiens se sont retirés au Havre, où ils vivent des jours heureux , ils ont deux fils : l aîné, Pierre, près de la trentaine, brun, maigre et nerveux, tourmenté par de grands projets et sujet à des découragements imprévus , vient d obtenir son de terminer ses études de médecine.")
    elif input_get == ("résumé de un monde sauvage"):
        label = Label(prgprincipal, text="Felitsa accompagne régulièrement sa mère, garde forestier, dans ses inspections. Nous sommes au bout du bout de la taiga russe, la nature est sauvage et la vie difficile pour tous, humains comme animaux. Des traces de tigre sont repérées, c'est un animal très convoité par les braconniers. Felitsa et sa mère arriveront-elles à sauver cette tigresse et ses petits ?")
    elif input_get == ("tom cruise"):
        label = Label(prgprincipal, text="un acteur et producteur américain, né le 3 juillet 1962 à Syracuse dans l'État de New York.Après avoir interprété des seconds rôles, notamment dans Taps et Outsiders, il obtient son premier rôle important dans la comédie dramatique Risky Business en 1983, mais c'est après avoir interprété Pete « Maverick » Mitchell dans Top Gun (1986) qu'il devient une star internationale. Depuis, il a joué dans de nombreux films à succès, tels que Rain Man, Né un 4 juillet, Entretien avec un vampire et les cinq épisodes de la saga Mission impossible.")
    elif input_get == ("brad pitt"):
        label = Label(prgprincipal, text="William Bradley Pitt, dit Brad Pitt, est un acteur et producteur de cinéma américain né le 18 décembre 1963 à Shawnee (Oklahoma).Repéré dans une publicité pour Levi's, Brad Pitt sort de l'anonymat grâce à un petit rôle dans le film Thelma et Louise de Ridley Scott. En très peu de temps, il devient une véritable star et sa collaboration avec le réalisateur David Fincher donne naissance aux films cultes Seven, Fight Club et L'Étrange Histoire de Benjamin Button")
    elif input_get == ("johnny depp"):
        label = Label(prgprincipal, text="Johnny Depp est un acteur, réalisateur, guitariste, scénariste et producteur de cinéma américain, né le 9 juin 1963 à Owensboro, Kentucky. Il est devenu célèbre dans les années 1980 grâce à son rôle dans la série télévisée 21 Jump Street. Il a ensuite voulu se détacher de son image de jeune premier en se consacrant principalement à l'interprétation de personnages originaux et excentriques tels qu'Edward dans Edward aux mains d'argent, Raoul Duke (alter ego de l'écrivain Hunter S. Thompson) dans Las Vegas Parano, Ichabod Crane dans Sleepy Hollow, Jack Sparrow dans la saga Pirates des Caraïbes, le Chapelier fou dans Alice au pays des merveilles et Barnabas Collins dans Dark Shadows")
    elif input_get == ("torvald"):
        label = Label(prgprincipal, text="Tu respectes cette personne et met un T en majuscule")
    elif input_get == ("Torvald"):
        label = Label(prgprincipal, text="Linus Benedict Torvalds, né le 28 décembre 1969 à Helsinki en Finlande, est un informaticien américano-finlandais. Il est connu pour avoir créé en 1991 le noyau Linux dont il continue de diriger le développement.")
    elif input_get == ("joconde"):
        label = Label(prgprincipal, text="La Joconde, ou Portrait de Mona Lisa1, est un tableau de l'artiste italien Léonard de Vinci, réalisé entre 1503 et 1506, qui représente un portrait mi-corps, probablement celui de la florentine Lisa Gherardini, épouse de Francesco del Giocondo. Acquise par François Ier, cette peinture à l'huile sur panneau de bois de peuplier de 77 × 53 cm est exposée au musée du Louvre à Paris. La Joconde est l'un des rares tableaux attribués de façon certaine à Léonard de Vinci.")
    elif input_get == ("le radeau de la meduse"):
        label = Label(prgprincipal, text="Le Radeau de La Méduse est une peinture à l'huile sur toile, réalisée entre 1818 et 1819 par le peintre et lithographe romantique français Théodore Géricault (1791-1824). Son titre initial, donné par Géricault lors de sa première présentation, est Scène d'un naufrage. Ce tableau, de très grande dimension (491 cm de hauteur et 716 cm de largeur), représente un épisode tragique de l'histoire de la marine française : le naufrage de la frégate Méduse, qui s'échoue sur un banc de sable au large des côtes de l'actuelle Mauritanie, le 2 juillet 1816.")
    elif input_get == ("la cene"):
        label = Label(prgprincipal, text="La Cène (en italien : L'Ultima Cena, soit « le Dernier Repas ») de Léonard de Vinci est une peinture murale à la détrempe (tempera) de 460 × 880 cm, réalisée de 1494 à 1498 pour le réfectoire du couvent dominicain de Santa Maria delle Grazie à Milan, qui était considérée jusqu'au milieu du XIXe siècle comme son chef-d'œuvre.")
    elif input_get == ("le cri"):
        label = Label(prgprincipal, text="Le Cri (en norvégien : Skrik) est une œuvre expressionniste de l'artiste norvégien Edvard Munch dont il existe cinq versions (trois peintures, un pastel et une lithographie) réalisées entre 1893 et 1917. Symbolisant l'homme moderne emporté par une crise d'angoisse existentielle, elle est considérée comme l'œuvre la plus importante de l'artiste. Le paysage en arrière-plan est le fjord d'Oslo, vu d'Ekeberg. L'une des cinq versions a été vendue par Sotheby's à New York pour un montant de 119,9 millions de dollars. Elle détient ainsi, le 2 mai 2012, le record de vente d'une peinture aux enchères.")
    elif input_get == ("l'etranger"):
        label = Label(prgprincipal, text="L’Étranger est le premier roman d’Albert Camus, paru en 1942. Il prend place dans la tétralogie que Camus nommera « cycle de l’absurde » qui décrit les fondements de la philosophie camusienne : l’absurde. Cette tétralogie comprend également l’essai intitulé Le Mythe de Sisyphe ainsi que les pièces de théâtre Caligula et Le Malentendu. Le roman a été traduit en quarante langues et une adaptation cinématographique en a été réalisée par Luchino Visconti en 1967.")
    elif input_get == ("la villa savoye"):
        label = Label(prgprincipal, text="La villa Savoye est une villa construite de 1928 à 1931 par l'architecte Le Corbusier, sur la commune française de Poissy, dans les Yvelines.")
    elif input_get == ("la cité radieuse"):
        label = Label(prgprincipal, text="L'unité d'habitation de Marseille connue sous le nom de Cité radieuse, « Le Corbusier » ou plus familièrement « La Maison du fada » , est une résidence édifiée entre 1947 et 1952 par l'architecte Le Corbusier (280 boulevard Michelet, 8e arrondissement de Marseille). Bâtie sous forme de barre sur pilotis (en forme de piètements évasés à l'aspect brutaliste) elle tente de concrétiser une nouvelle forme de cité, un « village vertical » appelé « Unité d'habitation ».")
    elif input_get == ("breizh brezel"):
        label = Label(prgprincipal, text="Le conflit entre le duché de Bretagne et le royaume de France se décline en une succession d'épisodes militaires et diplomatiques entre 1465 et 1491, date du mariage entre Anne de Bretagne et Charles VIII de France. Il aboutira par la suite à la fin de l'indépendance de la Bretagne.Ce conflit fait suite à la guerre de Succession de Bretagne, lors de laquelle deux partis, un pro-anglais et un pro-français, s'étaient affrontés entre 1341 et 1364.")
    elif input_get == ("trump"):
        label = Label(prgprincipal, text="désolé , mais ce nom n'existe plus ou a été exterminer!")
    elif input_get == ("donald"):
        label = Label(prgprincipal, text="Donald Fauntleroy Duck, ou simplement Donald Duck, est un personnage de fiction développé, entre autres, par l'animateur Dick Lundy")
    elif input_get == ("porte contenaire"):
        label = Label(prgprincipal, text="Un porte-conteneurs est un navire destiné au transport de conteneurs à l'exclusion de tout autre type de marchandises. Apparu dans les années 1970, le porte-conteneurs est maintenant le principal mode de transport maritime de fret dans les ports de commerce. Il fait partie intégrante du commerce mondial. Leur taille sans cesse croissante crée de nombreux problèmes architecturaux et portuaires.")
    elif input_get == ("tom hanks"):
        label = Label(prgprincipal, text="Thomas Jeffrey Hanks dit Tom Hanks, né le 9 juillet 1956 à Concord (Californie), est un acteur, réalisateur et producteur de cinéma américain.Il est devenu célèbre avec le film Splash, avant de connaître la consécration avec Philadelphia et Forrest Gump, qui lui valurent chacun l'Oscar du meilleur acteur. La quasi-totalité de ses films suivants furent des grands succès, comme Apollo 13, Il faut sauver le soldat Ryan et La Ligne verte. Il est souvent comparé à James Stewart, et son talent reconnu lui a permis de devenir l'un des acteurs fétiches des réalisateurs Steven Spielberg, Robert Zemeckis et Ron Howard.")
    elif input_get == ("jean racine"):
        label = Label(prgprincipal, text="Jean Racine (La Ferté-Milon, 22 décembre 1639 - Paris, 21 avril 1699) est un dramaturge et poète français, considéré comme l'un des plus grands auteurs de tragédies de la période classique en France.")
    elif input_get == ("leonardo dicaprio"):
        label = Label(prgprincipal, text="Leonardo DiCaprio, né le 11 novembre 1974 à Los Angeles, est un acteur, scénariste et producteur de cinéma américain.")
    elif input_get == ("charlie chaplin"):
        label = Label(prgprincipal, text="Charles Spencer Chaplin, dit Charlie Chaplin (né le 16 avril 1889 à Londres - 25 décembre 1977 à Corsier-sur-Vevey), est un acteur, réalisateur, scénariste, producteur et compositeur britannique qui devint une idole du cinéma muet grâce à son personnage de Charlot. Durant une carrière qui ne dura pas moins de 65 ans, il joua dans plus de 80 films, et sa vie publique et privée a fait l'objet d'adulation comme de controverses.")
    elif input_get == ("morgan freeman"):
        label = Label(prgprincipal, text="Morgan Freeman, né le 1er juin 1937 à Memphis (Tennessee), est un acteur américain.Ayant commencé sa carrière théâtrale et cinématographique en 1964, il fut habitué aux seconds rôles pendant plus de vingt ans. Il acquiert une large reconnaissance internationale après avoir été nommé aux Oscars pour La Rue en 1987, Miss Daisy et son chauffeur en 1989, Les Évadés en 1994 et Invictus en 2009 ; il a par ailleurs reçu l'Oscar du meilleur acteur dans un second rôle pour Million Dollar Baby en 2004.")
    elif input_get == ("marlo brando"):
        label = Label(prgprincipal, text="Marlon Brando, Jr., né le 3 avril 1924 à Omaha et décédé le 1er juillet 2004 à Los Angeles, est un acteur et réalisateur qui est considéré comme l'un des acteurs américains les plus grands et les plus influents du XXe siècle. L'American Film Institute l'a classé ""quatrième acteur de légende du cinéma américain"".")
    elif input_get == ("angelina jolie"):
        label = Label(prgprincipal, text="Angelina Jolie, née Angelina Jolie Voight le 4 juin 1975 à Los Angeles, est une actrice, réalisatrice, scénariste, productrice, mannequin, philanthrope, écrivaine et ambassadrice de bonne volonté américano-cambodgienne. Elle a reçu trois Golden Globes, deux Screen Actors Guild Awards et un Oscar du cinéma. Selon le magazine Forbes Angelina Jolie est l'actrice la mieux payée d'Hollywood entre juin 2012 et juin 2013.")
    elif input_get == ("louis de funes"):
        label = Label(prgprincipal, text="Louis de Funès de Galarza, dit Louis de Funès, est un acteur français né le 31 juillet 1914 à Courbevoie et mort le 27 janvier 1983 à Nantes")
    elif input_get == ("will smith"):
        label = Label(prgprincipal, text="Will Smith, de son nom complet Willard Christopher Smith, Jr., est un acteur, producteur et chanteur de hip-hop américain, né le 25 septembre 1968 à Philadelphie")
    elif input_get == ("gerard jugnot"):
        label = Label(prgprincipal, text="Gérard Jugnot est un acteur, réalisateur, scénariste et producteur français né le 4 mai 1951 à Paris.")
    elif input_get == ("alain delon"):
        label = Label(prgprincipal, text="Alain Delon, né le 8 novembre 1935 à Sceaux (Hauts-de-Seine), est un acteur et homme d'affaires français ; il a également la nationalité suisse depuis 1999")
    elif input_get == ("john travolta"):
        label = Label(prgprincipal, text="John Travolta est un acteur, chanteur, danseur et producteur de cinéma américain né le 18 février 1954 à Englewood (New Jersey).")
    elif input_get == ("gerard"):
        label = Label(prgprincipal, text="Julio Gerardo Hernández dit Gérard Hernandez, né le 20 janvier 1933 à Valladolid, est un acteur français d'origine espagnole naturalisé en 1975")
    elif input_get == ("guillaume pley"):
        label = Label(prgprincipal, text="Guillaume Pley est un animateur de radio et un présentateur de télévision française, né le 26 juillet 1985 à Sainte-Adresse en Seine-Maritime.")
    elif input_get == ("lesage"):
        label = Label(prgprincipal, text="Alain-René Lesage ou Le Sage, né à Sarzeau le 8 mai 1668 et mort à Boulogne-sur-Mer le 17 novembre 1747, est un romancier et auteur dramatique français surtout connu comme étant l'auteur du roman picaresque Histoire de Gil Blas de Santillane.")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    elif input_get == (""):
        label = Label(prgprincipal, text="")
    else:
        label = Label(prgprincipal, text="Je n'ai pas compris")
    input_user.set('')
    label.pack()
    return "break"

menubar = Menu(prgprincipal)

menu1 = Menu(menubar, tearoff=0)
menu1.add_command(label="Proposer un tuto pour un logiciel")
menu1.add_separator()
menu1.add_command(label="Quitter", command=prgprincipal.quit)
menubar.add_cascade(label="Amélia", menu=menu1)

menu2 = Menu(menubar, tearoff=0)
menu2.add_command(label="Preferences")
menu2.add_command(label="Copier")
menu2.add_command(label="Coller")
menubar.add_cascade(label="Options", menu=menu2)

menu3 = Menu(menubar, tearoff=0)
menu3.add_command(label="A propos de Amelia", command=aboutwindow)
menubar.add_cascade(label="Aide", menu=menu3)

visageAmelia = PhotoImage(file="amelia.png")

prgprincipal.config(menu=menubar)

canvas = Canvas(prgprincipal,width=180, height=300)
canvas.create_image(0, 0, anchor=NW, image=visageAmelia)
canvas.pack()

input_user = StringVar()
input_field = Entry(prgprincipal, text=input_user)
input_field.pack(side=BOTTOM, fill=X)

input_field.bind("<Return>", Enter_pressed)

prgprincipal.style = Style()
#Voici les différents styles : 'clam', 'alt', 'default', 'classic'
prgprincipal.style.theme_use("alt")

prgprincipal.mainloop()


