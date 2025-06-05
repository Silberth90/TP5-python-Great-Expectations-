
import great_expectations.dataset as ge_dataset
import ExtraccionDatos as ed


data_loaded = ed.data

# Convertir el dataframe en un odjeto great expectations
df_ge = ge_dataset.PandasDataset(data_loaded)

#definir expectativas

df_ge.expect_column_values_to_not_be_null('transaction_id')
df_ge.expect_column_values_to_not_be_null('sales_amount')
df_ge.expect_column_values_to_not_be_null('transaction_date')
df_ge.expect_column_values_to_be_unique('transaction_id')
df_ge.expect_column_values_to_be_of_type('sales_amount', 'float')
df_ge.expect_column_values_to_match_strftime_format('transaction_date', '%Y-%m-%d')

#ejecutar pruebas y generar reporte
validation_result = df_ge.validate()
print("\nresultados de las validaciones: ")
print(validation_result)

# exportar reporte de validaciones a html
# df_ge.save_expectation_suite(discard_failed_expectations=False)
#generar reporte de resultados
validation_report = df_ge.validate()
print("\nGeneracion de reporte completada.")