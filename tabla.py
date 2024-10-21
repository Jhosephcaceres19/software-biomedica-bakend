import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

# Configuración del acceso a la API
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

# Reemplaza 'ruta_a_tus_credenciales.json' con el nombre de tu archivo JSON
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/jhoseph/Desktop/biomedica-backend/anacoraguaapikey.json', scope)
client = gspread.authorize(creds)

# Abrir la hoja por URL
spreadsheet = client.open_by_url("https://docs.google.com/spreadsheets/d/1Vw8yaUB-DNTrobFJPeFtF1syyjM8yGwjP0D7atewh74/edit#gid=0")
sheet = spreadsheet.sheet1  # Selecciona la primera hoja

# Obtener los datos como lista de listas
data = sheet.get_all_values()

# Convertir los datos a un DataFrame de pandas
df = pd.DataFrame(data[1:], columns=data[0])  # La primera fila como encabezados

# Convertir columnas numéricas a tipo float (ignora errores por celdas vacías o no numéricas)
df = df.apply(pd.to_numeric, errors='coerce')

# Calcular la suma de cada columna
suma_columnas = df.sum(numeric_only=True)

# Mostrar los resultados
print("Suma por cada columna:")
print(suma_columnas)
