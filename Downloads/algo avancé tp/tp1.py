import numpy as np
import matplotlib.pyplot as plt


# Génération de points de données aléatoires
np.random.seed(0)
n = 99
x = np.linspace(0, 10, n)
y = 1* x + np.random.normal(0, 2, n)#fonction y = 3x+b,b est random par numpy

# Calcul de la régression linéaire
a, b = np.polyfit(x, y, 1)
z = a * x + b

# Calcul de la différence en norme 1
inter1 = np.max(np.abs(z - y))

# Calcul de la différence en norme infi
interf = np.min(inter1)

# Tracé des points de données et des lignes de régression
plt.scatter(x, y, label='Données originales')#scatter les points
plt.plot(x, z, color='red', label='interpolation linéaire en norme 1')
#plt.plot(x,inter1,color='blue')
plt.plot([x[0], x[-1]], [z[0] - interf, z[-1] - interf], color='green', label='interpolation linéaire en norme infini')

# Ajout d'une légende et d'un titre
plt.legend()
plt.title('interpolation en normes 1 et infini')

# Affichage du résultat
plt.show()


"""

On va le manipuler comme l'interopolation en norme 1 en commencant par
introduire les variables z0, ..., z{n-1} telles que
    z_i >= ax_i + b - y_i
    z_i >= -(ax_i + b - y_i)
pour i=0, ..., n-1 et on cherche le
    max( Σz_i )
En suite on pose 
    t_i = max_i(z_i), i=0, ..., n-1
    t_i >= z_i, pour chaque i ==> 
    { t_i >= ax_i + b - y_i && t_i >= -(ax_i + b - y_i) }.
Donc,
    max(Σz_i) <= Σ(max(z_i)) <= Σ(t_i)
==> min(max(Σ(z_i))) <= min(Σ(t_i))
Alors notre probleme prend la forme d'optimisation lineaire suivante
    min(Σ(t_i))
    t_i >= ax_i + b - y_i       i=0, ..., n-1
    t_i >= -(ax_i + b - y_i)    i=0, ..., n-1

"""