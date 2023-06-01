# -*- coding: utf-8 -*-
"""
Created on Tue May 16 16:01:39 2023

@author: paul
"""
 
import numpy as np
class Morpion():
    
    def __init__(self,joueur1,joueur2):
        self.joueur1=joueur1
        self.joueur2=joueur2
        self.Structure=[None,None,None,None,None,None,None,None,None]
        self.actionpossible=self.Actions()
        self.Tour=""
        self.Vainqueur=None
        
    
    def SetTour(self,value):
        self.Tour=value
    
    def GetValeurPlateau(self,x):
        return self.Structure[x]

    def SetValeurPlateau(self,x,val):
        self.Structure[x]=val
        
        
        
    def Actions(self):
        """Crée et renvoie une liste des actions possibles)"""
        liste=[]
        for i in range(9):
                if self.Structure[i]==None :
                    liste.append(i)
        
        #print("Les actions possibles sont : ",liste)
        return liste
        
    def Result(self,x,char):
        """Applique l'action dans l'état self avec le charactère char"""
        self.SetValeurPlateau(x,char)
        
    def Terminal_Test(self):
        """True si c'est l'état final  False sinon"""
        
        if(self.Utility()=="Non finit"):
            return False
        else:
            return True
        
        
    def Utility(self):
        """Renvoie le vainqueur si il y a un vainqueur sinon égalité"""
        #Les lignes
        if(self.Structure[0]==self.Structure[1]==self.Structure[2] and self.Structure[0]!=None):
            return self.Structure[0]
        elif(self.Structure[3]==self.Structure[4]==self.Structure[5] and self.Structure[3]!=None):
            return self.Structure[3]
        elif(self.Structure[6]==self.Structure[7]==self.Structure[8] and self.Structure[7]!=None):
            return self.Structure[6]
        #Les colonnes
        elif(self.Structure[0]==self.Structure[3]==self.Structure[6] and self.Structure[0]!=None):
            return self.Structure[0]
        elif(self.Structure[1]==self.Structure[4]==self.Structure[7] and self.Structure[1]!=None):
            return self.Structure[1]
        elif(self.Structure[2]==self.Structure[5]==self.Structure[8] and self.Structure[2]!=None):
            return self.Structure[2]
        #Les diagonales
        elif(self.Structure[0]==self.Structure[4]==self.Structure[8] and self.Structure[0]!=None):
            return self.Structure[0]
        elif(self.Structure[2]==self.Structure[4]==self.Structure[6] and self.Structure[2]!=None):
            return self.Structure[2]
        elif (len(self.Actions())==0):
            return "Egalité"
        else :
            return "Non finit"
        
    def EvaluationMorpion(self):
        """
        Fonction qui permet d'évaluer le score d'un sous morpion
        Il prend en compte tout les éléments et affecte des scores en fonction de positions
        On a choisit que le milieu était le meilleur coup, puis les coins puis les côtés
        Il y a ensuite des points supplémentaires si l'IA a des paires créées et des points négatifs si le joueur adverse
        a des paires crées'

        """
        #On associe des points en fonction du nombre de pion présent sur la case
        #Il faut savoir que l'on associe un poids plus important sur le milieu et les coins que les côtés
        liste_pair=[]
        case=[2,1,2,1,1,1,2,1,2] #
        score=0
        for i in range(9):
            if self.Structure[i]=='O':
                score=score+case[i]
            elif self.Structure[i]=='X':
                score=score-case[i]
         #On vérifie si il y a des paires crées
        for i in range(0,9,3):
          #Les lignes
            if(self.Structure[i]==self.Structure[i+1] and self.Structure[i+2]==None) or (self.Structure[i+2]==self.Structure[i+1] and self.Structure[i]==None): #Vérifie les lignes
                liste_pair.append(self.Structure[i+1])
            elif(self.Structure[i]==self.Structure[i+2]and self.Structure[i+1]==None):
                liste_pair.append(self.Structure[i])
          #Les colonnes      
        for i in range(0,3):
            if(self.Structure[i]==self.Structure[i+3] and self.Structure[i+6]==None)or (self.Structure[i]==None and self.Structure[i+3]==self.Structure[i+6]):#Vérifie les colonnes
                liste_pair.append(self.Structure[i+3])
            elif(self.Structure[i]==self.Structure[i+6] and self.Structure[i+3]==None):
                liste_pair.append(self.Structure[i])
                
        #Diagonales
        if(self.Structure[0]==self.Structure[4] and self.Structure[8]==None) or (self.Structure[0]==None and self.Structure[4]==self.Structure[8]):
            liste_pair.append(self.Structure[4])
        elif(self.Structure[0]==self.Structure[8] and self.Structure[4]==None):
            liste_pair.append(self.Structure[8])
            
        
        if(self.Structure[4]==self.Structure[2] and self.Structure[6]==None)or(self.Structure[4]==self.Structure[6] and self.Structure[2]==None):
            liste_pair.append(self.Structure[4])
        elif(self.Structure[2]==self.Structure[6] and self.Structure[4]==None):
            liste_pair.append(self.Structure[2])

        for element in liste_pair:
            if element=='O':
                score=score+5
            elif element=='X':
                score=score-5
                
        return score
        
                
    
   
        
        
class Ultimate(Morpion):
    def __init__(self,joueur1,joueur2):
        """
        Initialisation de l'ultimate tic tac toe'
        """
     #   Morpion.__init__(self,joueur1,joueur2)
        m1=Morpion(joueur1,joueur2)
        m2=Morpion(joueur1,joueur2)
        m3=Morpion(joueur1,joueur2)
        m4=Morpion(joueur1,joueur2)
        m5=Morpion(joueur1,joueur2)
        m6=Morpion(joueur1,joueur2)
        m7=Morpion(joueur1,joueur2)
        m8=Morpion(joueur1,joueur2)
        m9=Morpion(joueur1,joueur2)
        self.tour=""
        self.tableau=[m1,m2,m3,m4,m5,m6,m7,m8,m9]
        self.gagnantmorpion=[None,None,None,None,None,None,None,None,None] #quand un joueur gagne un morpion , on aimerai le stocker ici en tant que X ou O
        
        
    def __str__(self):
        return f"C'est au tour de {self.tour}"
    #Ici si le gagnant est par exemple X il faudrait afficher un grand X ... A voir si possible (ou mettre que des x dans cette case pour montrer qu'il la gagner)
    def AfficherTableau(self):
        """
        Permet d'afficher proprement le jeu'
        """
        
        print("  1   2   3    4   5   6    7   8   9 \n ______________________________________")
        for i in range(0,9,3 ):
            for j in range(0,9,3):
              #  print("|   |   |   |   |   |   |   |   |   |")
                for k in range(i,i+3):
                   if self.tableau[k].Structure[j]==None:
                        print("| _ ",end="")
                   else:
                        print("|",self.tableau[k].Structure[j],"",end="")
                    
                   if self.tableau[k].Structure[j+1]==None:
                         print("| _ ",end="")
                   else:
                         print("|",self.tableau[k].Structure[j+1],"",end="")
                   if self.tableau[k].Structure[j+2]==None:
                        print("| _ ",end="")
                   else:
                        print("|",self.tableau[k].Structure[j+2],"",end="")
                    
                   print("|",end="")
                print("")
            #if(i!=6):
            print("|===|===|===||===|===|===||===|===|===|")
            #else:
             #   print("|_____________________________________|")
                
            
    def Terminal_Test2(self):
        """
        Vérifie si l'état actuel est finit ou pas 
        True si final False sinon
        """
        if self.Utility2()=="X" or self.Utility2()=="O":
            return True
        elif self.Utility2()=="Egalité":
            return True
        else:
            return False
            
    
    def ActionsPossibles(self):
        """
        Retourne une liste de liste contenant les coups qui sont libres dans l'ultimate tic tac toe'
        
      """
        liste=[]
        for i in range(9):
            if self.tableau[i].Terminal_Test()==False:
                liste.append(self.tableau[i].Actions())
            else:
                liste.append([])
        return liste
     
    def Utility2(self):
        """
        Fonction qui permet de regarder si le jeu est finit
        Cette fonction prend en compte gagnantmorpion qui n'est actualisé qu'après un tour
        """
        i=0
        for element in self.ActionsPossibles():
            i=i+len(element)
            #On vérifie les lignes
        if(self.gagnantmorpion[0]==self.gagnantmorpion[1]==self.gagnantmorpion[2] and self.gagnantmorpion[0]!=None):
            return self.gagnantmorpion[0]
        elif(self.gagnantmorpion[3]==self.gagnantmorpion[4]==self.gagnantmorpion[5] and self.gagnantmorpion[3]!=None):
            return self.gagnantmorpion[3]
        elif(self.gagnantmorpion[6]==self.gagnantmorpion[7]==self.gagnantmorpion[8] and self.gagnantmorpion[7]!=None):
            return self.gagnantmorpion[6]
        #On vérifie les colonnes
        elif(self.gagnantmorpion[0]==self.gagnantmorpion[3]==self.gagnantmorpion[6] and self.gagnantmorpion[0]!=None):
            return self.gagnantmorpion[0]
        elif(self.gagnantmorpion[1]==self.gagnantmorpion[4]==self.gagnantmorpion[7] and self.gagnantmorpion[1]!=None):
            return self.gagnantmorpion[1]
        elif(self.gagnantmorpion[2]==self.gagnantmorpion[5]==self.gagnantmorpion[8] and self.gagnantmorpion[2]!=None):
            return self.gagnantmorpion[2]
        #On vérifie les diagonales
        elif(self.gagnantmorpion[0]==self.gagnantmorpion[4]==self.gagnantmorpion[8] and self.gagnantmorpion[0]!=None):
            return self.gagnantmorpion[0]
        elif(self.gagnantmorpion[2]==self.gagnantmorpion[4]==self.gagnantmorpion[6] and self.gagnantmorpion[2]!=None):
            return self.gagnantmorpion[2]
        elif i==0:
            return "Egalité"
        else :
            return "Non fini"
        
        
    def Utility3(self) :
        """Une autre fonction qui regarde si le jeu est fini, elle est appelée dans le minimax et qui regarde à chaque fois dans chaque morpion si le morpion est final et si des lignes, colonnes ou diagonales sont finies
        """
        i=0
        for element in self.ActionsPossibles():
            i=i+len(element)
            #On vérifie les lignes
        if(self.tableau[0].Utility()==self.tableau[1].Utility()==self.tableau[2].Utility() and self.tableau[1].Utility()!='Non finit'):
            return self.tableau[1].Utility()
        elif(self.tableau[3].Utility()==self.tableau[4].Utility()==self.tableau[5].Utility() and self.tableau[3].Utility()!='Non finit'):
            return self.tableau[3].Utility()
        elif(self.tableau[6].Utility()==self.tableau[7].Utility()==self.tableau[8].Utility() and self.tableau[7].Utility()!='Non finit'):
           return self.tableau[7].Utility()
       #On vérifie les colonnes
        elif(self.tableau[0].Utility()==self.tableau[3].Utility()==self.tableau[6].Utility() and self.tableau[0].Utility()!='Non finit'):
            return self.tableau[0].Utility()
        elif(self.tableau[1].Utility()==self.tableau[4].Utility()==self.tableau[7].Utility() and self.tableau[1].Utility()!='Non finit'):
            return self.tableau[1].Utility()
        elif(self.tableau[2].Utility()==self.tableau[5].Utility()==self.tableau[8].Utility() and self.tableau[1].Utility()!='Non finit'):
            return self.tableau[2].Utility()
        #On vérifie les diagonales
        elif(self.tableau[0].Utility()==self.tableau[4].Utility()==self.tableau[8].Utility() and self.tableau[0].Utility()!='Non finit'):
            return self.tableau[0].Utility()
        elif(self.tableau[2].Utility()==self.tableau[4].Utility()==self.tableau[6].Utility() and self.tableau[2].Utility()!='Non finit'):
            return self.tableau[2].Utility()
        elif i==0:
            return "Egalité"
        else :
            return "Non fini"
        
    def Result2(self,i,j,char):
        """
        Permet de placer le char dans le morpion i dans la case j
        """
        self.tableau[i].Result(j,char)
      
        
    def TestMorpionGagnant(self):
        """
        Regarde si les morpions sont gagnants, cela permet d'actualiser le tableau gagnantmorpion utilisé dans utility2
        """
        for i in range(9):
            if self.tableau[i].Utility()=="O":
                self.gagnantmorpion[i]="O"
            elif self.tableau[i].Utility()=="X":
                self.gagnantmorpion[i]="X"
                
                
    def Position_ElligibleCase(self,x1):
       """
       Vérifie que la position de la case est éligible
       """
       x2=input(f"Veuillez choisir dans quelle case du morpion numéro {x1} voulez-vous jouer (1 à 9) ? \n ")
       while(x2.isdigit()==False):
           x2=input(f"Veuillez choisir dans quelle case du morpion numéro {x1} voulez-vous jouer (1 à 9) ? \n ")
       x2=int(x2)
       while(x2<1 or x2>9 or self.tableau[x1-1].Structure[x2-1]!=None):
           print("Posiition non valide")
           x2=input(f"Veuillez choisir dans quelle case du morpion numéro {x1} voulez-vous jouer (1 à 9) ? \n ")
           while(x2.isdigit()==False):
               x2=input(f"Veuillez choisir dans quelle case du morpion numéro {x1} voulez-vous jouer (1 à 9) ? \n ")
           x2=int(x2)
       return x2
   
   
    def Position_Elligible_Morpion(self):
       """
       Vérifie que la position du morpion est éligbile

       """
       x=input("Veuillez choisir dans quel morpion voulez-vous jouer ? (1 à 9) \n")
       while(x.isdigit()==False):
           x=input("Veuillez choisir dans quel morpion voulez-vous jouer ? (1 à 9) \n")
       x=int(x)
       while(x<1 or x>9 or self.gagnantmorpion[x-1]!=None or len(self.tableau[x-1].Actions())==0):
           print("Position non valide ")
           x=input("Veuillez choisir dans quel morpion voulez-vous jouer ? (1 à 9) \n")
           while(x.isdigit()==False):
               x=input("Veuillez choisir dans quel morpion voulez-vous jouer ? (1 à 9) \n")
           x=int(x)
       return x
    
    
    def minimax2(self,profondeur,Est_Max,MorpionForce,alpha,beta):
        """
        Fonction minimax qui renvoie la meilleure évaluation possible, on peut choisir la profondeur

        """
        p=self.Utility3()
        if(p=='X'):
            return -1000000
        if p=='O':
            return 1000000
        if p=='Egalité':
            return 0
        if profondeur==0:  #Si on a atteint la profondeur max, on calcule le score grâce à notre heuristique
            return self.Evaluation(MorpionForce,Est_Max)

        if(MorpionForce!=None and self.tableau[MorpionForce].Terminal_Test()):
            MorpionForce=None
        #Vérifier si le morpion MorpionForce est fini ou pas 
        if Est_Max:   #C'est l'IA qui joue donc O 
            max_eval=-np.inf
            if MorpionForce!=None:
                for element in self.tableau[MorpionForce].Actions(): #On récupere toutes les actions possibles dans ce morpion
                    self.Result2(MorpionForce,element,"O")
                    score=self.minimax2(profondeur-1,False,element,alpha,beta)
                    self.Result2(MorpionForce,element,None)
                    max_eval=max(max_eval,score)
                    alpha=max(alpha,score)
                    if beta<=alpha:
                        break
                return max_eval
            else:
                for i in range(9):
                    for element in self.ActionsPossibles()[i]:
                        self.Result2(i,element,"O")
                        score=self.minimax2(profondeur-1,False,element,alpha,beta)
                        self.Result2(i,element,None)
                        max_eval=max(max_eval,score)
                        alpha=max(alpha,score)
                        if beta<=alpha:
                           break
                return max_eval
        else:   #Cas du minimum donc c'est le joueur qui joue ; X
             max_eval=np.inf
             if MorpionForce!=None:
                 for element in self.tableau[MorpionForce].Actions(): #On récupère toutes les actions possibles dans ce morpion
                     self.Result2(MorpionForce,element,"X")
                     score=self.minimax2(profondeur-1,True,element,alpha,beta)
                     self.Result2(MorpionForce,element,None)
                     max_eval=min(score,max_eval)
                     beta=min(beta,score)
                     if beta<=alpha:
                         break
                 return max_eval
             else:
                 for i in range(9):
                     for element in self.ActionsPossibles()[i]:
                         self.Result2(i,element,"X")
                         score=self.minimax2(profondeur-1,True,element,alpha,beta)
                         self.Result2(i,element,None)
                         max_eval=min(score,max_eval)
                         beta=min(beta,score)
                         if beta<=alpha:
                            break
                 return max_eval
                        
                
            
            
            
    
    def cout_ordi_ultimate(self,MorpionForce,profondeur): 
        """
        Permet de trouver le meilleur coup possible en appellant minimax
        """
        max_eval=-np.inf
        bestplay=""
        if(MorpionForce!=None and self.tableau[MorpionForce].Terminal_Test()):
            MorpionForce=None
        if MorpionForce!=None:
            for element in self.tableau[MorpionForce].Actions(): #On récupère toutes les actions possibles dans ce morpion
                self.Result2(MorpionForce,element,"O")
                score=self.minimax2(profondeur,False,element,-np.inf,np.inf)
                self.Result2(MorpionForce,element,None)
                if score>max_eval:
                    max_eval=score
                    bestplay=(MorpionForce,element)
        else:
            for i in range(9):
                for element in self.ActionsPossibles()[i]:
                    self.Result2(i,element,"O")
                    score=self.minimax2(profondeur-1,False,element,-np.inf,np.inf)
                    self.Result2(i,element,None)
                    
                    if score>max_eval:
                        max_eval=score
                        bestplay=(i,element)
        self.Result2(bestplay[0], bestplay[1],"O")
        return bestplay
    
    def Evaluation(self,MorpionForce,Est_Max): #On va se placer du point de vue de l'IA qui est "O"
        """
         Fonction très importante, c'est la fonction qui va calculer notre heurisitique.On va associer des points en fonction des morpions gagnés,
         De même que dans le sous morpion, on associe de poids différents au sous morpion, en associant le plus de point au morpion du milieu
         On vérifie aussi si des paires sont créees
        """
    
        score=0
        grille=[2,1,2,1,3,1,2,1,2]     
        resultat=[]
        liste_pair=[]
        compteur=-1
        for element in self.tableau:
            compteur=compteur+1
            if element.Terminal_Test(): #si un petit morpion est gagné : on associe la valeur 100 si il est gagné par le joueur, -100 pour l'IA
                b=element.Utility()
                resultat.append(b)
            else:
                resultat.append(None)
                score=score+element.EvaluationMorpion()*grille[compteur]#Si le morpion n'est pas fini, on calcule son score
                
        for i in range(9):
       #     print('Test')
            if resultat[i]=="O": #si un petit morpion est gagné : on associe la valeur 100 si il est gagné par nous, -100 pour l'IA
                score=score+100*grille[i]
            elif resultat[i]=="X":
                score=score-100*grille[i]
    #Ici on vérifie si les on a commencé à créer des doublons de gros morpion ce qui renvoie plus de points
        for i in range(0,9,3):
            if(resultat[i]==resultat[i+1] and resultat[i+2]==None) or (resultat[i+2]==resultat[i+1] and resultat[i]==None): #Vérifie les lignes
                liste_pair.append(resultat[i+1])
            elif(resultat[i]==resultat[i+2]and resultat[i+1]==None):
                liste_pair.append(resultat[i])
                
        for i in range(0,3):
            if(resultat[i]==resultat[i+3] and resultat[i+6]==None)or (resultat[i]==None and resultat[i+3]==resultat[i+6]):#Vérifie les colonnes
                liste_pair.append(resultat[i+3])
            elif(resultat[i]==resultat[i+6] and resultat[i+3]==None):
                liste_pair.append(resultat[i])
                
        
        if(resultat[0]==resultat[4] and resultat[8]==None) or (resultat[0]==None and resultat[4]==resultat[8]):
            liste_pair.append(resultat[4])
        elif(resultat[0]==resultat[8] and resultat[4]==None):
            liste_pair.append(resultat[8])
            
        
        if(resultat[4]==resultat[2] and resultat[6]==None)or(resultat[4]==resultat[6] and resultat[2]==None):
            liste_pair.append(resultat[4])
        elif(resultat[2]==resultat[6] and resultat[4]==None):
            liste_pair.append(resultat[2])
        for element in liste_pair:
            if element=='O':
                score=score+1500
            elif element=='X':
                score=score-1500
                
        return score
        
    
def JeuUltimateVsIA():
    """
    Fonction qui permet le jeu contre une intelligence artificielle
    """
    print("Bonjour voici le jeu du Morpion ")
    print("Ici le jeu se joue contre une IA) ")
    nom1=input("Donnez votre nom\n")
    nom2='IA'
    ultimate=Ultimate(nom1,nom2)
    valeur=int(input(f"Qui va commencer ? {nom1} (1) ou {nom2} (2)\n"))
    if valeur==1:
        ultimate.tour=nom1
    else:
        ultimate.tour=nom2
    print(ultimate)
    ultimate.AfficherTableau()
    previous=None
    print(ultimate.Utility2())
    print(ultimate.Terminal_Test2())
    profondeur=4
    nbtour=0
    while(ultimate.Terminal_Test2()==False):
        if(ultimate.tour==nom1):
            print(f"C'est au tour de {nom1} et vous êtes les X")
            if(previous==None):
                previous=ultimate.Position_Elligible_Morpion()
            choix2=ultimate.Position_ElligibleCase(previous)
            ultimate.Result2(previous-1,choix2-1,"X")
            previous=choix2-1
            ultimate.TestMorpionGagnant()
            ultimate.tour=nom2
            nbtour+=1
            if ultimate.gagnantmorpion[previous]!=None or len(ultimate.tableau[previous].Actions())==0:
                previous=None
            ultimate.AfficherTableau()
                     
        else:
            
            
            print(f"C'est à l'IA de jouer...")
           
            coup=ultimate.cout_ordi_ultimate(previous,profondeur)
            coup_reel=(coup[0]+1,coup[1]+1)
            previous=coup[1]+1
            ultimate.AfficherTableau()
            print("L'IA a joué en ",coup_reel)
            ultimate.TestMorpionGagnant()
            if ultimate.gagnantmorpion[previous-1]!=None or len(ultimate.tableau[previous-1].Actions())==0:
                previous=None
            ultimate.tour=nom1
            nbtour+=1
         
    print("La partie est fini : ")
    ultimate.AfficherTableau()
    resultat=ultimate.Utility2()
    if resultat=="X":
        print(f"Féliciations {nom1}, vous avez gagné !")
    elif(resultat=="O"):
        print(f"Dommage.... vous avez perdu, notre IA a gagné ! !")
    else:
        print("Egalité")
            
JeuUltimateVsIA()    
    
        
            

                    
                    
  
        
