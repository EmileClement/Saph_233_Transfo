#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Ce programme permet de simuler une inductance par FEMM
"""

__author__ = "Javier OJEDA"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Javier OJEDA"
__email__ = "javier.ojeda@ens-cachan.fr"
__status__ = "Education"

###############################################################################
##
#%%  Dimensionnement d'une inductance saturable
##
###############################################################################

import femm
import numpy as np

class Inductance:
    Last_id = 0
    """Classe définissant une inductance caractérisée par :

    - Son volume externe (volume_externe)
    - Sa hauteur réelle (hauteur)
    - Sa largeur réelle (largeur)
    - Sa longueur active (l_active)
    - Son entrefer (entrefer)
    - La largeur d'une dent fer (l_dent)
    - Son coefficient de bobinage (k_b)
    - Sa densité de courant maximale (j_max)
    - Son courant maximum (i_max)"""


    def __init__(self, induct):
        """Les elements sont dans un dictionnaire rangé par ordre :hauteur, largeur, l_active,
            entrefer, l_dent, k_b, j_max"""
        self.id = Inductance.Last_id
        Inductance.Last_id += 1
        for key, value in induct.items():
            if key == "hauteur":
                self.hauteur = value
            elif key == "largeur":
                self.largeur = value
            elif key == "l_active":
                self.l_active = value
            elif key == "entrefer":
                self.entrefer = value
            elif key == "l_dent":
                self.l_dent = value
            elif key == "k_b":
                self.k_b = value
            elif key == "j_max":
                self.j_max = value
            elif key == "i_max":
                self.i_max = value
            else:
                print("Paramètres {0} non requis".format(key))
                
    @property
    def densite_courant(self):
        """ Getter permettant d'obtenir la veleur de j_max """
        
        return self.j_max
    
    @densite_courant.setter
    def densite_courant(self, j_max):
        """ Setter permettant de modifier la veleur de j_max """
        
        self.j_max = j_max
        
    def creation_FEMM(self):
        """Méthode permettant de générer une simulation FEMM"""
        
        # Permet de lancer le logiciel FEMM.
        femm.openfemm()

        # Création d'un problème de magnétostatique ( = 0 ).
        femm.newdocument(0)

        # Définition du problème.  Magnetostatique, Unités mètres, Problème plan, 
        # Precision de 10^(-8), longueur active de 1m, angle de contraintes de 30deg
        femm.mi_probdef(0,'meters','planar',1e-8,1,30)
        
    def creation_geometrie(self):
        """Méthode permettant de générer la géométrie"""       
        
        # Dessin d'un rectangle (xmin,ymin,xmax,ymax)
        femm.mi_drawrectangle(-self.largeur/2,
                              -self.hauteur/2,
                              self.largeur/2,
                              self.hauteur/2);
                              
        # Dessin de points (x,y)
        femm.mi_addnode(self.l_dent/2, self.entrefer/2)
        femm.mi_addnode(-self.l_dent/2, self.entrefer/2)
        femm.mi_addnode(self.l_dent/2, -self.entrefer/2)
        femm.mi_addnode(-self.l_dent/2, -self.entrefer/2)
        
        femm.mi_addnode(self.l_dent/2, self.hauteur/2-self.l_dent/2)
        femm.mi_addnode(-self.l_dent/2, self.hauteur/2-self.l_dent/2)
        femm.mi_addnode(self.l_dent/2, -self.hauteur/2+self.l_dent/2)
        femm.mi_addnode(-self.l_dent/2, -self.hauteur/2+self.l_dent/2)
        
        femm.mi_addnode(self.largeur/2-self.l_dent/2,
                        self.hauteur/2-self.l_dent/2)
        femm.mi_addnode(-self.largeur/2+self.l_dent/2,
                        self.hauteur/2-self.l_dent/2)
        femm.mi_addnode(self.largeur/2-self.l_dent/2,
                        -self.hauteur/2+self.l_dent/2)
        femm.mi_addnode(-self.largeur/2+self.l_dent/2,
                        -self.hauteur/2+self.l_dent/2)
        
        # Dessin des lignes (x1,y1,x2,y2)
        femm.mi_addsegment(self.l_dent/2, self.entrefer/2,
                           -self.l_dent/2, self.entrefer/2)
        femm.mi_addsegment(self.l_dent/2, -self.entrefer/2,
                           -self.l_dent/2, -self.entrefer/2)
        
        femm.mi_addsegment(self.l_dent/2, self.entrefer/2,
                           self.l_dent/2, self.hauteur/2-self.l_dent/2)
        femm.mi_addsegment(-self.l_dent/2, self.entrefer/2,
                           -self.l_dent/2, self.hauteur/2-self.l_dent/2)
        femm.mi_addsegment(self.l_dent/2, -self.entrefer/2,
                           self.l_dent/2, -self.hauteur/2+self.l_dent/2)
        femm.mi_addsegment(-self.l_dent/2, -self.entrefer/2,
                           -self.l_dent/2, -self.hauteur/2+self.l_dent/2)
                
        femm.mi_addsegment(self.l_dent/2, self.hauteur/2-self.l_dent/2,
                           self.largeur/2-self.l_dent/2,
                           self.hauteur/2-self.l_dent/2)
        femm.mi_addsegment(-self.l_dent/2, self.hauteur/2-self.l_dent/2,
                           -self.largeur/2+self.l_dent/2,
                           self.hauteur/2-self.l_dent/2)
        femm.mi_addsegment(self.l_dent/2, -self.hauteur/2+self.l_dent/2,
                           self.largeur/2-self.l_dent/2,
                           -self.hauteur/2+self.l_dent/2)
        femm.mi_addsegment(-self.l_dent/2, -self.hauteur/2+self.l_dent/2,
                           -self.largeur/2+self.l_dent/2,
                           -self.hauteur/2+self.l_dent/2)
        
        femm.mi_addsegment(self.largeur/2-self.l_dent/2,
                           self.hauteur/2-self.l_dent/2,
                           self.largeur/2-self.l_dent/2,
                           -self.hauteur/2+self.l_dent/2)
        femm.mi_addsegment(-self.largeur/2+self.l_dent/2,
                           self.hauteur/2-self.l_dent/2,
                           -self.largeur/2+self.l_dent/2,
                           -self.hauteur/2+self.l_dent/2)
        
        femm.mi_addsegment(self.l_dent/2, self.entrefer/2,
                           self.l_dent/2, -self.entrefer/2)
        femm.mi_addsegment(-self.l_dent/2, self.entrefer/2,
                           -self.l_dent/2, -self.entrefer/2)      
   

    def affectation_materiaux(self):
        """Méthode permettant d'attribuer la propriété des matériaux"""
        
        # Affectation de l'air (x,y)
        femm.mi_addmaterial('Air', 1, 1, 0, 0,
                            0, 0, 0, 0, 0, 0, 0)
        femm.mi_addblocklabel(0, 0)
        femm.mi_selectlabel(0, 0)
        femm.mi_setblockprop('Air', 0, 1, '<None>', 0, 0, 0)
        femm.mi_clearselected()
        
        # Affectation du Cuivre (bobine positive) (Attention J en A/mm²)
        femm.mi_addmaterial('Cuivre+', 1, 1, 0, self.k_b*self.j_max*1.0e-6,
                            0, 0, 0, 0, 0, 0, 0)
        femm.mi_addblocklabel(self.largeur/4, 0)
        femm.mi_selectlabel(self.largeur/4, 0)
        femm.mi_setblockprop('Cuivre+', 0, 1, 'incricuit', 0, 0, 0)
        femm.mi_clearselected()
        
        # Affectation du Cuivre (bobine négative)
        femm.mi_addmaterial('Cuivre-', 1, 1, 0, -self.k_b*self.j_max*1.0e-6,
                            0, 0, 0, 0, 0, 0, 0)
        femm.mi_addblocklabel(-self.largeur/4, 0)
        femm.mi_selectlabel(-self.largeur/4, 0)
        femm.mi_setblockprop('Cuivre-', 0 ,1 ,'incircuit', 0, 0, 0)
        femm.mi_clearselected()
        
        
        # Matériau non linéaire
        
        # Création d'un matériau linéaire
        femm.mi_addmaterial('Iron', 2100, 2100, 0, 0, 0, 0, 0, 0, 0, 0, 0)

        # Les points de la courbe BH
        bdata = [ 0., 0.2, 0.4, 0.7, 1, 1.2,
                 1.3, 1.4, 1.5, 1.55, 1.6, 1.65,
                 1.7, 1.8, 1.91, 2, 2.1, 3.2454]  
        
        hdata = [ 0., 31.9, 44.9, 67.3, 106., 164.,
                 235., 435., 1109., 1813., 2802., 4054.,
                 5592., 9711., 16044., 31319., 88491., 1000000.]
        
        # Affectation des points de la courbe
        for n in range(0,len(bdata)):
            femm.mi_addbhpoint('Iron', bdata[n], hdata[n])
            
        # Affectation du matériau
        femm.mi_addblocklabel(self.largeur/2-self.l_dent/4, 0)
        femm.mi_selectlabel(self.largeur/2-self.l_dent/4, 0)
        femm.mi_setblockprop('Iron', 0, 1, '<None>', 0, 0, 0)
        femm.mi_clearselected()
        
        
    def conditions_limites(self):
        """Méthode permettant d'attribuer les conditions aux limites"""
        
        femm.mi_addboundprop('lim',0,0,0,0,0,0,0,0,0)
        femm.mi_selectsegment(0, self.hauteur/2)
        femm.mi_selectsegment(0, -self.hauteur/2)
        femm.mi_selectsegment(self.largeur/2, 0)
        femm.mi_selectsegment(-self.largeur/2, 0)      
        femm.mi_setsegmentprop('lim', 0, 1, 0, 0)
        femm.mi_clearselected();
        
        
    def sauvegarde_simulation(self):
        """Sauvegarde de la simulation (à faire avant de simuler)"""
        
        femm.mi_saveas('temp/transfo_{:0>5}.fem'.format(self.id))
        
    def maillage(self):
        """Maillage de la géométrie"""

        femm.mi_createmesh()
        
    def simulation(self):
        """Simulation du système"""
        
        femm.mi_analyze()
        femm.mi_loadsolution()
     
    def calcul_energie(self):
        """Calcul de l'energie dans l'entrefer et le fer"""
        
        femm.mo_selectblock(0, 0) # On selectionne l'entrefer
        femm.mo_selectblock(0, self.hauteur/2 - self.l_dent/4) # On selectionne le fer
        energie = femm.mo_blockintegral(2)*self.l_active
        femm.mo_clearblock()
        return energie
        
    def calcul_volume_externe(self):
        """Calcul du volume de l'inductance"""
        
        return self.l_active*self.hauteur*self.largeur
    
    def calcul_volume_fer(self):
        """Calcul du volume de fer de l'inductance"""
        
        v_fer = (self.calcul_volume_externe()-
                 self.calcul_volume_cuivre()-
                 self.entrefer*self.l_dent*self.l_active)
        
        return v_fer
    
    def calcul_volume_cuivre(self):
        """Calcul du volume de cuivre de l'inductance"""
        
        v_cuivre = 2*(self.hauteur/2-
                      self.l_dent)*(self.largeur/2-
                                 self.l_dent)*self.l_active
        
        return v_cuivre
    
    def calcul_masse_fer(self):
        """Calcul de la masse de fer de l'inductance"""
        
        RHO_FER = 7874
        
        m_fer = RHO_FER*self.calcul_volume_fer()
        
        return m_fer
    
    def calcul_masse_cuivre(self):
        """Calcul de la masse de cuivre de l'inductance"""
        
        RHO_CUIVRE = 8960
        
        m_cuivre = RHO_CUIVRE*self.calcul_volume_cuivre()
        
        return m_cuivre
    
    def calcul_pertes_joule(self):
        """Calcul des pertes cuivre de l'inductance"""
        
        SIGMA_CUIVRE = 59.6e6
        
        pertes_joule = (1/SIGMA_CUIVRE*
                        self.k_b*
                        self.calcul_volume_cuivre()*
                        self.j_max**2)
        
        return pertes_joule
    
    def calcul_pertes_fer(self):
        """Calcul des pertes fer de l'inductance"""
        
        FREQUENCE = 50
        
        # Coefficients des pertes fer : 
        # Pertes volumique = ALPHA*B**1.5*FREQUENCE**1.5+
        #                    BETA*B**2*FREQUENCE+
        #                    GAMMA*B**2*FREQUENCE**2
        ALPHA = 1.1119e-4
        BETA = 1.688e-4
        GAMMA = 4.361e-4
        
        # Mesure du Bx, By au milieu de la dent centrale
        b_x, b_y = femm.mo_getb(0, self.hauteur/4)
        
        b_moy = np.sqrt(b_x**2 + b_y**2)
        
        pertes_fer_masse = (ALPHA*b_moy**1.5*FREQUENCE**1.5+
                             BETA*b_moy**2*FREQUENCE+
                             GAMMA*b_moy**2*FREQUENCE**2)
        
        pertes_fer = pertes_fer_masse*self.calcul_masse_fer()

        return pertes_fer
    
    def fit_zoom(self):
        """Méthode permettant de générer la géométrie""" 

        # Zoom pour avoir une meilleur vue
        femm.mi_zoomnatural()
        
    def fermeture_simulation(self):
        """Fermeture de FEMM"""
        
        femm.closefemm()
        


###############################################################################
#%% Corps du programme
###############################################################################


# Définition des paramètres de l'inductance
induct = {"hauteur":0.1, "largeur":0.1,
            "l_active":0.06, "entrefer":0.006, "l_dent":0.026,
            "k_b":0.4, "j_max":5.0e6, "i_max":20}


A=Inductance(induct)
A.creation_FEMM()
A.creation_geometrie()
A.fit_zoom()
A.affectation_materiaux()
A.conditions_limites()
A.sauvegarde_simulation()
A.maillage()
A.simulation()

print("L'energie de l'inductance est de {0:.3f} J".format(A.calcul_energie()))
print("Le volume externe de l'inductance est de {0:.6f} m^3".format(A.calcul_volume_externe()))
print("Le volume de fer de l'inductance est de {0:.6f} m^3".format(A.calcul_volume_fer()))
print("Le volume de cuivre de l'inductance est de {0:.6f} m^3".format(A.calcul_volume_cuivre()))
print("La masse de fer de l'inductance est de {0:.3f} kg".format(A.calcul_masse_fer()))
print("La masse de cuivre de l'inductance est de {0:.3f} kg".format(A.calcul_masse_cuivre()))
print("Les pertes Joule sont de {0:.1f} W".format(A.calcul_pertes_joule()))
print("Les pertes fer sont de {0:.1f} W".format(A.calcul_pertes_fer()))

# Fermeture de FEMM (à commenter si garder la fenêtre ouverte)
# A.fermeture_simulation()