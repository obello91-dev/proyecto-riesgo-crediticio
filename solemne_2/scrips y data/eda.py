
import pandas as pd
import io

# Nombres de las columnas
column_names = [
    'checking_account_status', 'duration_months', 'credit_history', 'purpose',
    'credit_amount', 'savings_account', 'present_employment_since',
    'installment_rate', 'personal_status_sex', 'other_debtors',
    'present_residence_since', 'property', 'age', 'other_installment_plans',
    'housing', 'num_existing_credits', 'job', 'num_dependents', 'telephone',
    'foreign_worker', 'credit_risk'
]

# Cargar datos
df = pd.read_csv('/Users/usuario/Desktop/agente/data/german.data', sep=' ', header=None, names=column_names)

# Mapear variable objetivo
df['credit_risk'] = df['credit_risk'].map({1: 1, 2: 0})

# Imprimir análisis
print("### Primeras 5 filas de los datos:")
print(df.head())
print("\n### Información general del DataFrame:")
df.info()
print("\n### Resumen estadístico de las variables numéricas:")
print(df.describe())
print("\n### Distribución de la variable objetivo (credit_risk):")
print(df['credit_risk'].value_counts())

