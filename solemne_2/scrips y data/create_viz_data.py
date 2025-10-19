
import pandas as pd

# Definir los nombres de las columnas
column_names = [
    'checking_account_status', 'duration_months', 'credit_history', 'purpose',
    'credit_amount', 'savings_account', 'present_employment_since',
    'installment_rate', 'personal_status_sex', 'other_debtors',
    'present_residence_since', 'property', 'age', 'other_installment_plans',
    'housing', 'num_existing_credits', 'job', 'num_dependents', 'telephone',
    'foreign_worker', 'credit_risk'
]

# Cargar el dataset original
df = pd.read_csv('/Users/usuario/Desktop/agente/data/german.data', sep=' ', header=None, names=column_names)

# Diccionarios para mapear los códigos a valores legibles
status_map = {'A11': '< 0 DM', 'A12': '0 - 200 DM', 'A13': '>= 200 DM', 'A14': 'Sin cuenta'}
history_map = {'A30': 'Sin créditos / Todos pagados', 'A31': 'Todos los créditos en este banco pagados', 'A32': 'Créditos existentes pagados hasta ahora', 'A33': 'Retraso en pagos en el pasado', 'A34': 'Cuenta crítica / Otros créditos'}
purpose_map = {'A40': 'Auto (nuevo)', 'A41': 'Auto (usado)', 'A42': 'Muebles/Equipo', 'A43': 'Radio/TV', 'A44': 'Electrodomésticos', 'A45': 'Reparaciones', 'A46': 'Educación', 'A47': 'Vacaciones', 'A48': 'Recapacitación', 'A49': 'Negocios', 'A410': 'Otros'}
savings_map = {'A61': '< 100 DM', 'A62': '100 - 500 DM', 'A63': '500 - 1000 DM', 'A64': '>= 1000 DM', 'A65': 'Desconocido / Sin ahorros'}
employment_map = {'A71': 'Desempleado', 'A72': '< 1 año', 'A73': '1 - 4 años', 'A74': '4 - 7 años', 'A75': '>= 7 años'}
personal_status_map = {'A91': 'Hombre: divorciado/separado', 'A92': 'Mujer: divorciada/separada/casada', 'A93': 'Hombre: soltero', 'A94': 'Hombre: casado/viudo', 'A95': 'Mujer: soltera'}
debtors_map = {'A101': 'Ninguno', 'A102': 'Co-solicitante', 'A103': 'Garante'}
property_map = {'A121': 'Bienes raíces', 'A122': 'Seguro de vida / Ahorro para vivienda', 'A123': 'Auto u otro', 'A124': 'Desconocido / Sin propiedad'}
installment_plans_map = {'A141': 'Banco', 'A142': 'Tiendas', 'A143': 'Ninguno'}
housing_map = {'A151': 'Alquiler', 'A152': 'Propia', 'A153': 'Gratis'}
job_map = {'A171': 'No calificado - no residente', 'A172': 'No calificado - residente', 'A173': 'Empleado calificado / oficial', 'A174': 'Gerencia / Autoempleado / Altamente calificado'}
telephone_map = {'A191': 'No', 'A192': 'Sí'}
foreign_worker_map = {'A201': 'Sí', 'A202': 'No'}
risk_map = {1: 'Buen Pagador', 2: 'Mal Pagador'}

# Aplicar los mapeos
df_mapped = df.copy()
df_mapped['checking_account_status'] = df_mapped['checking_account_status'].map(status_map)
df_mapped['credit_history'] = df_mapped['credit_history'].map(history_map)
df_mapped['purpose'] = df_mapped['purpose'].map(purpose_map)
df_mapped['savings_account'] = df_mapped['savings_account'].map(savings_map)
df_mapped['present_employment_since'] = df_mapped['present_employment_since'].map(employment_map)
df_mapped['personal_status_sex'] = df_mapped['personal_status_sex'].map(personal_status_map)
df_mapped['other_debtors'] = df_mapped['other_debtors'].map(debtors_map)
df_mapped['property'] = df_mapped['property'].map(property_map)
df_mapped['other_installment_plans'] = df_mapped['other_installment_plans'].map(installment_plans_map)
df_mapped['housing'] = df_mapped['housing'].map(housing_map)
df_mapped['job'] = df_mapped['job'].map(job_map)
df_mapped['telephone'] = df_mapped['telephone'].map(telephone_map)
df_mapped['foreign_worker'] = df_mapped['foreign_worker'].map(foreign_worker_map)
df_mapped['credit_risk'] = df_mapped['credit_risk'].map(risk_map)

# Guardar el archivo CSV procesado
output_path = '/Users/usuario/Desktop/agente/solemne_2/datos_para_visualizacion.csv'
df_mapped.to_csv(output_path, index=False, encoding='utf-8-sig')

print(f"Archivo de datos para visualización guardado en: {output_path}")
