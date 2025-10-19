
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# --- Cargar Artefactos del Modelo ---
try:
    model = joblib.load('/Users/usuario/Desktop/agente/logistic_regression_model.joblib')
    scaler = joblib.load('/Users/usuario/Desktop/agente/scaler.joblib')
    ohe = joblib.load('/Users/usuario/Desktop/agente/ohe.joblib')
    X_train_cols = pd.read_csv('/Users/usuario/Desktop/agente/X_train.csv', nrows=0).columns.tolist()
except FileNotFoundError:
    st.error("Error: No se encontraron los archivos del modelo. Asegúrate de que los archivos 'logistic_regression_model.joblib', 'scaler.joblib', 'ohe.joblib' y 'X_train.csv' se encuentren en el directorio '/Users/usuario/Desktop/agente/'.")
    st.stop()


# --- Configuración de la Página ---
st.set_page_config(page_title="Evaluador de Riesgo Crediticio", layout="wide")


# --- Título y Descripción ---
st.title("Herramienta de Evaluación de Riesgo Crediticio")
st.markdown("""
Esta aplicación utiliza un modelo de Regresión Logística para predecir si un solicitante de crédito es un buen o mal pagador.
A continuación, puedes ingresar los datos de un nuevo solicitante para obtener una predicción.
""")


# --- Interfaz de Usuario para Ingreso de Datos ---
st.sidebar.header("Ingrese los Datos del Solicitante")

# Usar un formulario para agrupar los inputs y el botón
with st.sidebar.form("applicant_form"):
    # --- Recolección de datos del usuario ---
    # Basado en german.doc, creamos los controles
    checking_account_status = st.selectbox('Estado de la cuenta corriente', ['A11', 'A12', 'A13', 'A14'], help="A11: < 0 DM, A12: 0-200 DM, A13: >= 200 DM, A14: Sin cuenta")
    duration_months = st.number_input('Duración del crédito (meses)', min_value=1, max_value=100, value=24)
    credit_history = st.selectbox('Historial de crédito', ['A30', 'A31', 'A32', 'A33', 'A34'], help="A30: Sin créditos, A31: Créditos pagados, A32: Créditos actuales pagados, A33: Retrasos previos, A34: Cuenta crítica")
    purpose = st.selectbox('Propósito del crédito', ['A40', 'A41', 'A42', 'A43', 'A44', 'A45', 'A46', 'A48', 'A49', 'A410'], help="A40: Auto nuevo, A41: Auto usado, A42: Muebles, A43: TV/Radio, etc.")
    credit_amount = st.number_input('Monto del crédito (DM)', min_value=100, max_value=20000, value=5000)
    savings_account = st.selectbox('Cuenta de ahorros', ['A61', 'A62', 'A63', 'A64', 'A65'], help="A61: < 100 DM, A62: 100-500 DM, A63: 500-1000 DM, A64: >= 1000 DM, A65: Sin ahorros")
    present_employment_since = st.selectbox('Tiempo de empleo actual', ['A71', 'A72', 'A73', 'A74', 'A75'], help="A71: Desempleado, A72: < 1 año, A73: 1-4 años, A74: 4-7 años, A75: >= 7 años")
    installment_rate = st.slider('Tasa de cuotas (% de ingreso disponible)', 1, 4, 2)
    personal_status_sex = st.selectbox('Estado personal y sexo', ['A91', 'A92', 'A93', 'A94'], help="A91: Hombre soltero, A92: Mujer no soltera, A93: Hombre soltero, A94: Hombre casado/viudo")
    other_debtors = st.selectbox('Otros deudores/garantes', ['A101', 'A102', 'A103'], help="A101: Ninguno, A102: Co-solicitante, A103: Garante")
    present_residence_since = st.slider('Tiempo en residencia actual (años)', 1, 4, 1)
    property = st.selectbox('Propiedad más importante', ['A121', 'A122', 'A123', 'A124'], help="A121: Bienes raíces, A122: Seguro de vida/ahorro, A123: Auto u otro, A124: Sin propiedad")
    age = st.number_input('Edad (años)', min_value=18, max_value=80, value=35)
    other_installment_plans = st.selectbox('Otros planes de cuotas', ['A141', 'A142', 'A143'], help="A141: Banco, A142: Tiendas, A143: Ninguno")
    housing = st.selectbox('Vivienda', ['A151', 'A152', 'A153'], help="A151: Alquilada, A152: Propia, A153: Gratis")
    num_existing_credits = st.slider('Número de créditos existentes en este banco', 1, 5, 1)
    job = st.selectbox('Tipo de empleo', ['A171', 'A172', 'A173', 'A174'], help="A171: No calificado/No residente, A172: No calificado/Residente, A173: Calificado, A174: Gerencia/Autoempleado")
    num_dependents = st.slider('Número de dependientes', 1, 4, 1)
    telephone = st.selectbox('Teléfono', ['A191', 'A192'], help="A191: No, A192: Sí")
    foreign_worker = st.selectbox('Trabajador extranjero', ['A201', 'A202'], help="A201: Sí, A202: No")

    # Botón de predicción
    submit_button = st.form_submit_button(label='Evaluar Solicitud')


# --- Lógica de Predicción ---
if submit_button:
    # Crear un DataFrame con los datos del usuario
    input_data = {
        'checking_account_status': [checking_account_status],
        'duration_months': [duration_months],
        'credit_history': [credit_history],
        'purpose': [purpose],
        'credit_amount': [credit_amount],
        'savings_account': [savings_account],
        'present_employment_since': [present_employment_since],
        'installment_rate': [installment_rate],
        'personal_status_sex': [personal_status_sex],
        'other_debtors': [other_debtors],
        'present_residence_since': [present_residence_since],
        'property': [property],
        'age': [age],
        'other_installment_plans': [other_installment_plans],
        'housing': [housing],
        'num_existing_credits': [num_existing_credits],
        'job': [job],
        'num_dependents': [num_dependents],
        'telephone': [telephone],
        'foreign_worker': [foreign_worker]
    }
    input_df = pd.DataFrame(input_data)

    st.write("### Datos Ingresados por el Usuario:")
    st.dataframe(input_df)

    # --- Preprocesamiento de los Datos ---
    # Separar columnas numéricas y categóricas
    numeric_features = input_df.select_dtypes(include=np.number).columns.tolist()
    categorical_features = input_df.select_dtypes(include='object').columns.tolist()

    # Aplicar StandardScaler a las variables numéricas
    input_df_num_scaled = scaler.transform(input_df[numeric_features])
    input_df_num = pd.DataFrame(input_df_num_scaled, columns=numeric_features)

    # Aplicar OneHotEncoder a las variables categóricas
    input_df_cat_encoded = ohe.transform(input_df[categorical_features])
    input_df_cat = pd.DataFrame(input_df_cat_encoded, columns=ohe.get_feature_names_out(categorical_features))

    # Combinar features procesados
    processed_input_df = pd.concat([input_df_num, input_df_cat], axis=1)
    
    # Reordenar columnas para que coincidan con el set de entrenamiento
    processed_input_df = processed_input_df.reindex(columns=X_train_cols, fill_value=0)

    # --- Realizar Predicción ---
    prediction = model.predict(processed_input_df)
    prediction_proba = model.predict_proba(processed_input_df)

    # --- Mostrar Resultado ---
    st.write("---")
    st.header("Resultado de la Evaluación")
    
    if prediction[0] == 1:
        st.success("🎉 **Crédito Aprobado** (Buen Pagador)")
        st.write(f"Probabilidad de ser un buen pagador: **{prediction_proba[0][1]:.2f}**")
    else:
        st.error("🚨 **Crédito Rechazado** (Mal Pagador)")
        st.write(f"Probabilidad de ser un mal pagador: **{prediction_proba[0][0]:.2f}**")

# --- Sección de Evaluación del Modelo ---
st.write("---")
st.header("Rendimiento del Modelo de Clasificación")
st.markdown("""
Estos son los resultados obtenidos por el modelo sobre un conjunto de datos de prueba que no vio durante el entrenamiento.
Nos dan una idea de qué tan confiable es la predicción.
""")

try:
    X_test = pd.read_csv('/Users/usuario/Desktop/agente/X_test.csv')
    y_test = pd.read_csv('/Users/usuario/Desktop/agente/y_test.csv').values.ravel()
    y_pred = model.predict(X_test)

    from sklearn.metrics import classification_report, confusion_matrix
    import matplotlib.pyplot as plt
    import seaborn as sns

    # Reporte de Clasificación
    st.subheader("Reporte de Clasificación")
    report = classification_report(y_test, y_pred, target_names=["Mal Pagador (0)", "Buen Pagador (1)"], output_dict=True)
    st.table(pd.DataFrame(report).transpose())

    # Matriz de Confusión
    st.subheader("Matriz de Confusión")
    cm = confusion_matrix(y_test, y_pred)
    fig, ax = plt.subplots()
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax, 
                xticklabels=["Mal Pagador", "Buen Pagador"], 
                yticklabels=["Mal Pagador", "Buen Pagador"])
    ax.set_xlabel("Predicción del Modelo")
    ax.set_ylabel("Valor Real")
    st.pyplot(fig)

except FileNotFoundError:
    st.warning("No se encontraron los archivos de prueba ('X_test.csv', 'y_test.csv') para mostrar la evaluación del modelo.")
except Exception as e:
    st.error(f"Ocurrió un error al mostrar la evaluación del modelo: {e}")

