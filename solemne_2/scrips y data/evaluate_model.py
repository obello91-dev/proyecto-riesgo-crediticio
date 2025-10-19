
import pandas as pd
import joblib
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# Cargar el modelo entrenado
model = joblib.load('/Users/usuario/Desktop/agente/logistic_regression_model.joblib')

# Cargar los datos de prueba
X_test = pd.read_csv('/Users/usuario/Desktop/agente/X_test.csv')
y_test = pd.read_csv('/Users/usuario/Desktop/agente/y_test.csv').values.ravel()

# Realizar predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

# Evaluar el modelo
print("### Métricas de Evaluación del Modelo de Regresión Logística ###")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision (Good Credit - 1): {precision_score(y_test, y_pred, pos_label=1):.4f}")
print(f"Recall (Good Credit - 1): {recall_score(y_test, y_pred, pos_label=1):.4f}")
print(f"F1-Score (Good Credit - 1): {f1_score(y_test, y_pred, pos_label=1):.4f}")
print(f"Precision (Bad Credit - 0): {precision_score(y_test, y_pred, pos_label=0):.4f}")
print(f"Recall (Bad Credit - 0): {recall_score(y_test, y_pred, pos_label=0):.4f}")
print(f"F1-Score (Bad Credit - 0): {f1_score(y_test, y_pred, pos_label=0):.4f}")

print("\n### Matriz de Confusión ###")
print(confusion_matrix(y_test, y_pred))

print("\n### Reporte de Clasificación ###")
print(classification_report(y_test, y_pred))
