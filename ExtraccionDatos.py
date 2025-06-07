import pandas as pd


#simulacion de extraccion de datos desde un archivo csv t json

csv_data = {
    "transaction_id": [1, 2, 3, 4, 5],
    "customer_id:": [1001, 1002, 1003, 1002, 1001],
    "sales_amount": [250.50,'300.00', 150, 300.00, 250.50],
    "transaction_date": ['2023/01/05', '2023/02/15', '2023-03-20', '15-03-2023', '2023-01-05']
}

json_data = {
    "transaction_id": [6,7],
    "customer_id": [1004,1005],
    "sales_amount": [500,'invalid'],
    "transaction_date": ['2023-04-10','2023-05-20']
}

#creamdo datafremes desde las fuestes

df_csv = pd.DataFrame(csv_data)
df_json = pd.DataFrame(json_data)

#uniendo los dos dataframes simulados

data = pd.concat([df_csv, df_json],ignore_index=True)

print("datos extraidos con exito")
print(data)

#Elminimar duplicados basados en customer_id y transaction_date

data_cleaned = data.drop_duplicates(subset = ['customer_id','transaction_date'])

#convertir el campo de 'sales_amount' a float,manejando errores

data_cleaned['sales_amount'] = pd.to_numeric(data_cleaned['sales_amount'],errors = 'coerce')

#convertir el campo de 'transaction_date' al YYYY-MM-DD

data_cleaned['transaction_date'] = pd.to_datetime(data_cleaned['transaction_date'],errors = 'coerce', format ='%Y-%m-%d')

print("\nDatos despues de la transformacion: ")
print(data_cleaned)

#cargar los datos limpios en un dataframe centralizado

data_loaded = data_cleaned
print("\nDatos cargados (Centralizados):")
print(data_loaded)
