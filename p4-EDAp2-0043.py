import pandas as pd
import matplotlib.pyplot as plt

# Sebastian Farfan NC = 0043 (11/11/26)
# 1. Crear diccionario con datos de películas
peliculas_catalogo = {
    'id_pelicula': [101, 102, 103, 104, 105, 106],
    'titulo': ['Inception', 'The Matrix', 'Interstellar', 'Parasite', 'Avengers', 'Joker'],
    'director': ['C. Nolan', 'L. Wachowski', 'C. Nolan', 'B. Joon-ho', 'J. Whedon', 'T. Phillips'],
    'ano_estreno': [2010, 1999, 2014, 2019, 2012, 2019],
    'genero': ['Ciencia ficcion', 'Ciencia ficcion', 'Ciencia ficcion', 'Drama', 'Accion', 'Drama'],
    'duracion_minutos': [148, 136, 169, 132, 143, 122],
    'calificacion_imdb': [8.8, 8.7, 8.6, 8.5, 8.0, 8.4],
    'recaudacion_millones': [836, 463, 701, 263, 1518, 1074],
    'idioma_original': ['Ingles', 'Ingles', 'Ingles', 'Coreano', 'Ingles', 'Ingles'],
    'disponible_streaming': [True, True, True, True, True, True]
}

print("Análisis Exploratorio de Datos ")
print("Exploratory Data Analysis (EDA por sus siglas en inglés) por Arath Valenzuela (NC:0148)")
print("--------+ 📝  Crear el diccionario con 10 listas y 6 elementos +--------")

# 2. Convertir diccionario en DataFrame
df = pd.DataFrame(peliculas_catalogo)
print("\n--- TABLA ORIGINAL DE PELÍCULAS ---")
print(df)

# 3. Exportar los datos a CSV
print("--------+ 💾 Convertir el DataFrame en archivo CSV +--------")
df.to_csv(
    'peliculas_catalogo_0043.csv',
    index=False,
    encoding='utf-8-sig'
)
print("\n✅ Archivo CSV creado correctamente")
print("--------+ 📂 Leer los datos desde el archivo CSV +--------")

# 4. Leer el archivo CSV
df = pd.read_csv('peliculas_catalogo_0043.csv')
print("peliculas_catalogo_0043.csv")
print("\n--- DATOS LEÍDOS DESDE CSV ---")
print(df)

# 5. Primeros y últimos registros
print("\n1. --------+ PRIMEROS REGISTROS (Head): +--------")
print(df.head(3))  # Muestra los primeros 3
print("\n2. --------+ ÚLTIMOS REGISTROS (Tail): +--------")
print(df.tail(2))  # Muestra los últimos 2

# 6. Dimensiones y estructura
print("\n6. --------+ Dimensiones y estructura +--------")
print(df)
print("\n3. DIMENSIONES (Filas, Columnas):", df.shape)
print("\n4. NOMBRES DE COLUMNAS:\n", df.columns)
print("\n5. TIPOS DE DATOS:\n", df.dtypes)
print("\n6. INFORMACIÓN GENERAL:")
df.info()

# 7. Estadísticas y limpieza
print("\n--------+ 7. ESTADÍSTICAS DESCRIPTIVAS: +--------")
print(df.describe())
print("\n--------+ 8. VALORES FALTANTES (Nulls): +--------")
print(df.isnull().sum())
print("\n--------+ 9. REGISTROS DUPLICADOS: +--------")
print(df.duplicated().sum())
print("\n--------+ 10. VALORES ÚNICOS POR COLUMNA: +--------")
print(df.nunique())
print("Géneros únicos:", df['genero'].unique())

# 8. Análisis específico
print(df)
print("+--------------------------------------------------------------------------+")
print("\n11. PELÍCULAS POR GÉNERO:")
print(df['genero'].value_counts())

print("\n12. PROMEDIO DE RECAUDACIÓN: $", round(df['recaudacion_millones'].mean(), 2), "millones")
print("13. RECAUDACIÓN MÁXIMA: $", df['recaudacion_millones'].max(), "millones")
print("14. RECAUDACIÓN MÍNIMA: $", df['recaudacion_millones'].min(), "millones")

# 9. Ordenamiento, filtrado y agrupación
print("9. Ordenamiento, filtrado y agrupación")

print("\n--------+ 15. PELÍCULAS ORDENADAS POR RECAUDACIÓN (Mayor a menor): +--------")
print(df.sort_values(by='recaudacion_millones', ascending=False))

print("\n--------+ 16. PELÍCULAS CON RECAUDACIÓN MAYOR A $800 MILLONES: +--------")
filtro = df[df['recaudacion_millones'] > 800]
print(filtro)

print("\n--------+ 17. RESUMEN POR GÉNERO: +--------")
resumen = df.groupby('genero').agg(
    peliculas=('id_pelicula', 'count'),
    recaudacion_promedio=('recaudacion_millones', 'mean'),
    recaudacion_maxima=('recaudacion_millones', 'max')
)
print(resumen)

# 18. Gráfica de barras: Películas por género
print("--------+ 18. Gráfica de barras: Películas por género +--------")
conteo = df['genero'].value_counts()
plt.figure(figsize=(8, 5))
plt.bar(conteo.index, conteo.values, color='skyblue')
plt.title('Películas por género (Sebastian 0043)')
plt.xlabel('Género')
plt.ylabel('Cantidad de películas')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 19. Gráfica de barras: Recaudación por película
print("--------+ 19. Gráfica de barras: Recaudación por película +--------")
plt.figure(figsize=(8, 5))
plt.bar(df['titulo'], df['recaudacion_millones'], color='lightgreen')
plt.title('Recaudación en taquilla por película (Sebastian 0043)')
plt.xlabel('Película')
plt.ylabel('Recaudación (Millones USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 20. Histograma: Distribución de duración en minutos
plt.figure(figsize=(8, 5))
plt.hist(df['duracion_minutos'], bins=5, color='orange', edgecolor='black')
plt.title('Distribución de duración de películas (EDA Sebastian 0043)')
plt.xlabel('Duración (minutos)')
plt.ylabel('Frecuencia')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 21. Gráfica de dispersión: Calificación IMDb vs Recaudación
plt.figure(figsize=(8, 5))
plt.scatter(df['calificacion_imdb'], df['recaudacion_millones'], color='red', s=100)
plt.title('Relación entre calificación IMDb y recaudación por Sebastian 0043')
plt.xlabel('Calificación IMDb')
plt.ylabel('Recaudación (Millones USD)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 22. Diagrama de caja: Distribución de recaudación
plt.figure(figsize=(7, 5))
plt.boxplot(df['recaudacion_millones'], patch_artist=True, boxprops=dict(facecolor='lightblue'))
plt.title('Distribución de recaudación (Boxplot) (Sebastian Farfan)')
plt.ylabel('Recaudación (Millones USD)')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

# 23. Matriz de correlación
# Excluimos la columna booleana 'disponible_streaming' porque todos sus valores son True (desviación 0) y generaría NaN
columnas_numericas = df.select_dtypes(include=['int64', 'float64'])
correlacion = columnas_numericas.corr()
print("\n--- MATRIZ DE CORRELACIÓN ---")
print(correlacion)

plt.figure(figsize=(9, 6))
plt.imshow(correlacion, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar()
plt.xticks(range(len(correlacion.columns)), correlacion.columns, rotation=45)
plt.yticks(range(len(correlacion.columns)), correlacion.columns)
plt.title('Matriz de correlación de variables numéricas (Sebastian 0043)')
plt.tight_layout()
plt.show()