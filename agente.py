import os
import time
from google import genai
from google.genai.errors import ServerError, ClientError

# Inicializamos el cliente
client = genai.Client()

# Leer el prompt
with open("PROMPT.md", "r") as f:
    input_prompt = f.read()

contexto = (
    "Eres un programador expert en Python. Modifica el archivo 'ruleta.py' "
    "según las instrucciones del usuario. Devuelve ÚNICAMENTE el código Python empaquetado "
    "dentro de un bloque de código markdown de python. No añadas explicaciones de texto."
)

# Bucle de reintentos inteligente (hasta 3 intentos si el servidor está saturado)
max_intentos = 3
for intento in range(max_intentos):
    try:
        print(f"Invocando a Gemini (Intento {intento + 1}/{max_intentos})...")
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=f"{contexto}\n\nInstrucciones del usuario:\n{input_prompt}",
        )
        # Si la llamada tiene éxito, rompemos el bucle
        break
    except (ServerError, ClientError) as e:
        if intento < max_intentos - 1:
            print(f"Servidor saturado (Error {e.code}). Reintentando en 5 segundos...")
            time.sleep(5)
        else:
            print("Se agotaron los reintentos debido a la alta demanda del servidor.")
            raise e

# Extraer el código del bloque markdown y guardarlo en ruleta.py
texto_respuesta = response.text
if "```python" in texto_respuesta:
    codigo = texto_respuesta.split("```python")[1].split("```")[0].strip()
    with open("ruleta.py", "w") as f:
        f.write(codigo)
    print("¡'ruleta.py' ha sido actualizado por Gemini con éxito!")
else:
    print("Error: Gemini no devolvió el formato de código esperado.")
