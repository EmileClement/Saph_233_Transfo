from simulation_femm_inductance import Inductance
import numpy as np
import scipy.optimize

distance_min = 0.01
def encapsulation_inductance(X):
    """
    

    Parameters
    ----------
    X : list de
        X = (hauteur, largeur, l_active, entrefer, l_dent)

    Returns
    -------
    None.

    """
    print(X)
    
    parametre = {}
    parametre["k_b"] = 0.4
    parametre["j_max"] = 5*10**6
    
    parametre["hauteur"] = X[0]
    parametre["largeur"] = X[1]
    parametre["l_active"] = X[2]
    parametre["entrefer"] = X[3]
    parametre["l_dent"] = X[4]
    
    inductance = Inductance(parametre)
    
    inductance.creation_FEMM()
    inductance.creation_geometrie()
    inductance.fit_zoom()
    inductance.affectation_materiaux()
    inductance.conditions_limites()
    inductance.sauvegarde_simulation()
    inductance.maillage()
    inductance.simulation()
    
    cout = 0
    cout += (inductance.calcul_energie() - 4)**2
    cout += 1000 * inductance.calcul_volume_externe()**2
    print(cout)
    return cout

X_0 = (0.1, 0.1, 0.01, 0.01, 0.01)

constraint_x = scipy.optimize.LinearConstraint([0, 1, 0, 0, -2 ], 
                                               distance_min, np.inf, True)
constraint_y = scipy.optimize.LinearConstraint([1, 0, 0, 1, -1 ], 
                                               distance_min, np.inf, True)

opti = scipy.optimize.minimize(encapsulation_inductance, X_0, 
                        constraints = (constraint_x, constraint_y), 
                        bounds = 5*[(distance_min, 1)])

print(opti)
