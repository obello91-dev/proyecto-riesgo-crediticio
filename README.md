[README.md](https://github.com/user-attachments/files/22992465/README.md)

# Proyecto de Análisis y Visualización de Riesgo Crediticio

Este proyecto analiza el conjunto de datos "German Credit Data" para construir un modelo de clasificación que predice el riesgo crediticio de un solicitante. Además, incluye una aplicación web interactiva para probar el modelo y un archivo de datos procesado para su visualización en herramientas de Business Intelligence.

---

## Estructura del Proyecto

```
/
├── data/                     # Contiene el dataset original (german.data).
├── solemne_2/
│   ├── scrips y data/        # Scripts de Python, la app Streamlit y datos procesados.
│   ├── datos_para_visualizacion.csv  # Datos limpios para Power BI/Tableau.
│   └── Analisis-de-Riesgo-Crediticio (1).pptx # Presentación final del proyecto.
└── README.md                 # Este archivo.
```

---

## Instrucciones de Ejecución de la Aplicación Web

Para ejecutar la aplicación interactiva de Streamlit, por favor sigue estos pasos.

### 1. Prerrequisitos

- Python 3.7 o superior.
- `pip` (manejador de paquetes de Python).

### 2. Configuración del Entorno

**a. Clona o descarga este repositorio y navega a la carpeta de los scripts:**

```bash
cd ruta/al/proyecto/solemne_2/scrips y data/
```

**b. Crea un entorno virtual:**

Esto crea un ambiente aislado para instalar las dependencias del proyecto sin afectar el sistema.

```bash
python3 -m venv venv
```

**c. Activa el entorno virtual:**

- En macOS / Linux:
  ```bash
  source venv/bin/activate
  ```
- En Windows:
  ```bash
  .\venv\Scripts\activate
  ```

**d. Instala las dependencias:**

El archivo `requirements.txt` contiene todas las librerías necesarias.

```bash
pip install -r requirements.txt
```

### 3. Ejecutar la Aplicación Streamlit

Una vez que las dependencias estén instaladas, ejecuta el siguiente comando para iniciar la aplicación:

```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador web.

---

## Scripts Adicionales (Opcional)

Los siguientes scripts se utilizaron para preparar los datos y entrenar el modelo. No es necesario ejecutarlos para correr la aplicación, ya que los archivos resultantes (`.csv`, `.joblib`) están incluidos.

- `prepare_data.py`: Carga los datos crudos, los procesa y los guarda en formato CSV. También guarda los objetos de preprocesamiento (scaler y one-hot encoder).
- `train_model.py`: Carga los datos de entrenamiento procesados y entrena el modelo de Regresión Logística, guardándolo como `logistic_regression_model.joblib`.
