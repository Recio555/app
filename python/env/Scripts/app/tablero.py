import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Cargar datos (reemplaza 'tu_archivo.csv' con tu propio archivo de datos)
data = pd.read_csv('tu_archivo.csv')

# Crear un tablero con visualizaciones básicas
plt.figure(figsize=(10, 6))

# Visualización 1: Diagrama de dispersión
plt.subplot(2, 2, 1)
sns.scatterplot(x='columna_x', y='columna_y', data=data)
plt.title('Diagrama de Dispersión')

# Visualización 2: Histograma
plt.subplot(2, 2, 2)
sns.histplot(data['columna_z'], bins=30, kde=True)
plt.title('Histograma')

# Agregar más visualizaciones según sea necesario

# Mostrar el tablero
plt.tight_layout()
plt.show()