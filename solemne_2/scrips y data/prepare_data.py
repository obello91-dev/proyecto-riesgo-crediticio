
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
import joblib

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

# Separar features (X) y target (y)
X = df.drop('credit_risk', axis=1)
y = df['credit_risk']

# Identificar columnas numéricas y categóricas
numeric_features = X.select_dtypes(include=['int64', 'float64']).columns
categorical_features = X.select_dtypes(include=['object']).columns

# Dividir los datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

# Procesar variables categóricas
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
X_train_cat_encoded = ohe.fit_transform(X_train[categorical_features])
X_test_cat_encoded = ohe.transform(X_test[categorical_features])

# Crear DataFrames con las columnas codificadas
X_train_cat = pd.DataFrame(X_train_cat_encoded, index=X_train.index, columns=ohe.get_feature_names_out(categorical_features))
X_test_cat = pd.DataFrame(X_test_cat_encoded, index=X_test.index, columns=ohe.get_feature_names_out(categorical_features))

# Procesar variables numéricas
scaler = StandardScaler()
X_train_num_scaled = scaler.fit_transform(X_train[numeric_features])
X_test_num_scaled = scaler.transform(X_test[numeric_features])

# Crear DataFrames con las columnas escaladas
X_train_num = pd.DataFrame(X_train_num_scaled, index=X_train.index, columns=numeric_features)
X_test_num = pd.DataFrame(X_test_num_scaled, index=X_test.index, columns=numeric_features)

# Combinar features procesados
X_train_processed = pd.concat([X_train_num, X_train_cat], axis=1)
X_test_processed = pd.concat([X_test_num, X_test_cat], axis=1)

# Guardar los datos procesados
X_train_processed.to_csv('/Users/usuario/Desktop/agente/X_train.csv', index=False)
X_test_processed.to_csv('/Users/usuario/Desktop/agente/X_test.csv', index=False)
y_train.to_csv('/Users/usuario/Desktop/agente/y_train.csv', index=False)
y_test.to_csv('/Users/usuario/Desktop/agente/y_test.csv', index=False)

# Guardar el OneHotEncoder y el StandardScaler
joblib.dump(ohe, '/Users/usuario/Desktop/agente/ohe.joblib')
joblib.dump(scaler, '/Users/usuario/Desktop/agente/scaler.joblib')

print("Datos preparados, transformadores guardados y CSVs generados exitosamente.")
print("Dimensiones de X_train_processed:", X_train_processed.shape)
print("Dimensiones de X_test_processed:", X_test_processed.shape)
