import pandas as pd
import ExtraccionDatos as ed

data = ed.data
#Elminimar duplicados basados en customer_id y transaction_date

data_cleaned = data.drop_duplicates(subset = ['customer_id','transaction_date'])

#convertir el campo  de 'sales_amount' a float,manejando errores

data_cleaned['sales_amount'] = pd.to_numeric(data_cleaned['sales_amount'],errors = 'coerce')

#convertir el campo de 'transaction_data' al formato YYYY-MM-DD

data_cleaned['transaction_date'] = pd.to_datetime(data_cleaned['transaction_date'],errors ='coerce',format ='%y-%m-%d')

print("\Datos despues de la transformacion:")
print(data_cleaned)

# cargar los datos limpios en un DataFrame centralizado
data_loaded = data_cleaned

print("\nDatos cargados con exito")
print(data_loaded)