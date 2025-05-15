# 📊 Precio de las tortillas en México
# Análisis del Precio de las Tortillas en México 2007 - 2024

Este proyecto realiza un análisis [exploratorio / predictivo / descriptivo] de [tema del proyecto]. El conjunto de datos incluye información sobre [breve descripción del contenido del dataset].

---

## 📚 Tabla de Contenidos

- [🎯 Propósito](#-propósito)
- [📦 Conjunto de Datos](#-conjunto-de-datos)
- [🧪 Desarrollo del Proyecto](#-desarrollo-del-proyecto)
- [🛠️ Tecnologías](#-tecnologías)
- [⚙️ Instalación](#-instalación)
- [🚀 Uso](#-uso)
- [📈 Conclusiones y Recomendaciones](#-conclusiones-y-recomendaciones)
- [👤 Autor](#-autor)
- [📝 Licencia](#-licencia)

---

## 🎯 Propósito

Analizar la evolución del precio de las tortillas en México desde 2007 hasta 2024, identificando patrones temporales, diferencias regionales y factores que podrían haber influido en su comportamiento.

---

## 📦 Conjunto de Datos

El conjunto de datos utilizado contiene las siguientes columnas:
tortilla_price.csv:
- `State`: Estado de México donde se ubica la ciudad, los 32 estados de México están incluidos en el conjunto de datos.
- `City`: Principales ciudades de México donde se realizan escuentas de precios.
- `Year`: Año correspondiente a la observación.
- `Month`: Mes correspondiente a la observación.
- `Day`: Día correspondiente a la observación.
- `Store type`: Tipo de teinda de los precios encuentados (puede ser una tienda familiar o una gran tienda minorista).
- `Price per kilogram`: Estimación de precios para el tipo de tienda, día y ciudad encuestada.

Fuente: https://www.kaggle.com/datasets/richave/tortilla-prices-in-mexico.

---

## 🧪 Desarrollo del Proyecto

### **Carga y exploración inicial de los datos**
El proyecto comenzó con la obtención del conjunto de datos sobre los precios de la tortilla de maíz en México desde el año 2007 hasta el 2024, publicado en kaggle por 
*Rick Chavelas*. Se realizó una exploración preliminar para entender la estructura del dataset, la cantidad de registros, las variables disponibles, y la granularidad temporal y geográfica. Esta fase incluyó el uso de funciones como `.head()`, `.info()` y `.describe()` para detectar inconsistencias básicas y comprender las dimensiones generales del problema.

El problema identificando fue la falta de datos en la columna Price per kilogram
```python 
# Identificar valores nulos
print('Identificar Valores Nulos por Columnas')
valores_nulos = df_tortilla_price.isnull().sum()
print(valores_nulos)
```
```
Identificar Valores Nulos por Columnas
State                    0
City                     0
Year                     0
Month                    0
Day                      0
Store type               0
Price per kilogram    6390
dtype: int64
```
***Archivo: 1_EDA.ipynb***

### **Limpieza y preprocesamiento**
En la limpieza de los datos el un único problema crítico es: la presencia de valores nulos en la columna Price per kilogram. Debido a su relevancia central para el análisis, se decidió eliminar esos registros para mantener la integridad estadística del estudio. Otras columnas como las fechas y entidades se dejaron intactas en esta fase, ya que no presentaban problemas estructurales, y serían transformadas más adelante cuando fuera necesario.

Código para verificar la cantidad de filas y columnas
```python
# Verificar la cantidad de filas y columnas 
num_fias, num_columnas = df_tortilla_prices.shape
print(f'Número de filas: {num_fias}\nNúmero de columnas: {num_columnas}')
```
Salida:
```bash
Número de filas: 289146
Número de columnas: 7
```

Código para eliminar las filas con valores nulos:
```python
# Eliminar las filas con los valores nulos
df_tortilla_prices_sin_nulos = df_tortilla_prices.dropna()

# Verificar la cantidad de filas y columnas
num_filas_sin_nulos, num_columnas_sin_nulos = df_tortilla_prices_sin_nulos.shape
print(f'Número de filas: {num_filas_sin_nulos}\nNúmero de columnas: {num_columnas_sin_nulos}')
```
Salida:
```bash
Número de filas: 282756
Número de columnas: 7
```

Para finalizar la limpieza y preprocesamiento de los datos se guardaron los datos sin valores nulos en un nuevo archivo csv.
```python
df_tortilla_prices_sin_nulos.to_csv('../data/processed/tortilla_prices_sin_nulos.csv', index=False)
```
***Archivo: 2_limpieza_datos.ipynb***

### **Análisis exploratorio de datos (EDA)**
Con los datos limpios, se procedió a realizar un análisis exploratorio profundo para entender la distribución y evolución de los precios a lo largo del tiempo. Entre los principales hallazgos:

Se observó una tendencia general al alza en los precios promedio anuales de la tortilla.

![tendencia_general_evolución_precio_promedio_anual_tortilla_mexico_2007_a_2024](reports/figures/tendencia_general_evolución_precio_promedio_anual_tortilla_mexico_2007_a_2024.png)

Algunas entidades federativas destacan la presencia de precios sistemáticamente más altos y mínimos que otras, destacando diferencias regionales en 2007 y 2024.

Código:
```python
min_state_2007 = promedio_state_2007.idxmin()
min_precio_state_2007 = promedio_state_2007[min_state_2007]

max_state_2007 = promedio_state_2007.idxmax()
max_precio_state_2007 = promedio_state_2007[max_state_2007]


print('Esatdo del 2007 con precios Mínimos')
print(f'{"Estado":<11} Precio \n{min_state_2007:<11} ${min_precio_state_2007:.2f}')

print('\nEsatdo del 2007 con precios Máximos')
print(f'{"Estado":<11} Precio \n{max_state_2007:<11} ${max_precio_state_2007:.2f}')
```
Salida:
```bash
Estados del 2007 con precios Mínimos
Estado      Precio 
Oaxaca      $6.81

Estados del 2007 con precios Máximos
Estado      Precio 
Sonora      $8.56
```
Código:
```python
min_state_2024 = promedio_state_2024.idxmin()
min_precio_state_2024 = promedio_state_2024[min_state_2024]

max_state_2024 = promedio_state_2024.idxmax()
max_precio_state_2024 = promedio_state_2024[max_state_2024]

print('\nEsatdo del 2024 con precios Mínimos')
print(f'{"Estado":<11} Precio \n{min_state_2024:<11} ${min_precio_state_2024:.2f}')

print('\nEsatdo del 2007 con precios Máximos')
print(f'{"Estado":<11} Precio \n{max_state_2024:<11} ${max_precio_state_2024:.2f}')
```
Salida:
```bash
Estados del 2024 con precios Mínimos
Estado      Precio 
Tlaxcala    $15.35

Estados del 2007 con precios Máximos
Estado      Precio 
Sonora      $21.89
```

La dispersión de precios también ha crecido con el tiempo, lo que indica un mercado cada vez más heterogéneo en cuanto a costos.

Se usaron funciones como .groupby(), .mean() y .std() para obtener promedios y desviaciones estándar por año y por estado, y así facilitar el análisis comparativo.

4. **Análisis exploratorio de datos (EDA)**:
   - [Ej. Distribución, correlaciones, agrupaciones, etc.]

5. **Visualización de datos**:
   - Uso de gráficos de barras, líneas, cajas, dispersión y mapas de calor.

6. **Modelado o reportes (opcional)**:
   - [Si aplica: modelos de ML, clustering, predicciones, etc.]

7. **Conclusiones y recomendaciones**:
   - Síntesis de hallazgos clave y propuestas de acción.

---

## 🛠️ Tecnologías

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## ⚙️ Instalación

### 1. Clonar este repositorio:
```bash
git clone https://github.com/tu_usuario/nombre_del_proyecto.git
```
### 2. Uso de un Entorno Virtual para Aislar Dependencias

Para evitar conflictos con versiones de librerías, se recomienda usar entornos virtuales.

####  Crear y Activar un Entorno Virtual

##### Crear el entorno virtual:
```
python -m venv venv
```
##### Activar el entorno:
* #### En Windows:

    ```
    venv\Scripts\activate
    ```

* #### En Mac/Linux::

    ```
    source venv/bin/activate
    ```
#### 3. Instalar dependencias dentro del entorno:
* #### Opición 1:
    ```
    pip install -r requirements.txt
    ```

* #### Opción 2 (De forma manual):
    ```
    pip install numpy pandas matplotlib seaborn scikit-learn
    ```
---

## 📈 Conclusiones y Recomendaciones

- [Insight 1]
- [Insight 2]
- [Recomendación práctica o estratégica basada en los datos]

---

## 👤 Autor

**Said Mariano Sánchez** – *smariano170@gmail.com*  
Este proyecto forma parte de mi portafolio como analista de datos Jr.

---

## 📝 Licencia

Este proyecto está licenciado bajo la **Licencia MIT**. Puedes usarlo, modificarlo y distribuirlo libremente, siempre que menciones al autor original.

---