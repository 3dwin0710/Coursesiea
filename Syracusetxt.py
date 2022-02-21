
class Syracuse:

    @staticmethod # Désigne une méthode statique , ne recoit pas d'argument de référence 
    #qui soit appelée par une instance d'une classe ou d'une classe
    # Definition source : https://www.tutorialsteacher.com/python/staticmethod-decorator
    def syracuse(number):
        if number % 2 == 0:
            return number // 2
        else:
            return 3 * number + 1
    # La partie Syracuse
    
    
    def __init__(self, count):
        self.count = count

    def __iter__(self):
        self.u = self.count
        self.continuer = True
        return self

    def __next__(self):

        if self.continuer:
            resultat = self.u
            if resultat == 1: self.continuer = False
            self.u = Syracuse.syracuse(self.u)
            return resultat
        else:
            raise StopIteration


with open("fichier.txt", "r") as f:
    number = f.read()
    # Lire le fichier texte pour ainsi extraire le contenu pour l'utilisation du class Syracuse
    for k in Syracuse(int(number)):
        print(int(k)),

f.close()


with open("out.txt","w") as fichier:
    counter = 1
    fichier.write("The resultat of this operation is :"+"\n")
    for k in Syracuse(int(number)):
        z = str(k)
        fichier.write("Operation {} : {} ".format(counter,z)+"\n")
        counter +=1
    fichier.write("Total number of this operation is {} ".format(counter-1))
fichier.close()


# Thanks pour l'inspiration sur le code de Guillaume de la classe 2
# source :
# https://books.google.fr/books?id=RsldEAAAQBAJ&pg=PA387&lpg=PA387&dq=class+python+syracuse&source=bl&ots=BGu0htX_Jh
# &sig=ACfU3U1g28nqqiU_nl4tuzhZI72c_iJ3pQ&hl=fr&sa=X&ved=2ahUKEwjnxuu4iYr2AhWEzYUKHSHECO8Q6AF6BAgwEAM#v=onepage&q&f
# =false

# Thanks au youtuber : Graven + FormationVideo
