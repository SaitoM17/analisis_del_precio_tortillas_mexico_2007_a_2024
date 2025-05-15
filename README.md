# 📊 Anáisis del Precio de las tortillas en México 2007 - 2024
# [Título del Análisis]

Este proyecto realiza un análisis [exploratorio / predictivo / descriptivo] de [tema del proyecto]. El conjunto de datos incluye información sobre [breve descripción del contenido del dataset].

---

## 📚 Tabla de Contenidos

- [🎯 Propósito](#-propósito)
- [📦 Conjunto de Datos](#-conjunto-de-datos)
- [🧪 Pasos del Proyecto](#-pasos-del-proyecto)
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

## 🧪 Pasos del Proyecto

1. **Carga y exploración inicial de los datos**:
   - Exploración básica con `.head()`, `.info()`, `.describe()`, etc.

2. **Limpieza y preprocesamiento**:
   - Manejo de valores nulos, duplicados, formatos y conversiones de fechas.

3. **Análisis exploratorio de datos (EDA)**:
   - [Ej. Distribución, correlaciones, agrupaciones, etc.]

4. **Visualización de datos**:
   - Uso de gráficos de barras, líneas, cajas, dispersión y mapas de calor.

5. **Modelado o reportes (opcional)**:
   - [Si aplica: modelos de ML, clustering, predicciones, etc.]

6. **Conclusiones y recomendaciones**:
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