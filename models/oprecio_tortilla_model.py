import pandas as pd
import statsmodels.api as sm

df_tortilla_prices = pd.read_csv('C:/workspace/Data Scientist/Portafolio/analisis_del_precio_tortillas_mexico_2007_a_2024/data/processed/tortilla_prices_sin_nulos.csv')

# Agrupa los datos por año y calcula el precio promedio
precios_anuales = df_tortilla_prices.groupby('Year')['Price per kilogram'].mean().reset_index()

# Define las variables independiente y dependiente
X = precios_anuales['Year']
y = precios_anuales['Price per kilogram']

# Agrega una constante al modelo
X = sm.add_constant(X)

# Ajusta el modelo
modelo = sm.OLS(y, X).fit()

# Muestra el resumen del modelo
print(modelo.summary())
