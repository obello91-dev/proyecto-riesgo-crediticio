
import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib

# Cargar los datos de entrenamiento
X_train = pd.read_csv('/Users/usuario/Desktop/agente/X_train.csv')
y_train = pd.read_csv('/Users/usuario/Desktop/agente/y_train.csv').values.ravel() # .values.ravel() para convertirlo a un array 1D

# Crear y entrenar el modelo de Regresión Logística
# Usamos class_weight='balanced' para dar más importancia a la clase minoritaria (malos clientes)
model = LogisticRegression(random_state=42, class_weight='balanced', max_iter=1000)
model.fit(X_train, y_train)

# Guardar el modelo entrenado
joblib.dump(model, '/Users/usuario/Desktop/agente/logistic_regression_model.joblib')

print("Modelo de Regresión Logística entrenado y guardado como logistic_regression_model.joblib")
