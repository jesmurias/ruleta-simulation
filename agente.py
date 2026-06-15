mport os
import google.generativeai as genai

# Configurar la API de Gemini con el secreto de GitHub
genai.configure(api_key=os.environ["GEMINI_API_KEY"])

# Leer el prompt que has escrito
with open("PROMPT.md", "r") as f:
    input_prompt = f.read()

# Darle contexto a Gemini para que solo devuelva código limpio
contexto = (
    "Eres un programador experto en Python. Modifica el archivo 'ruleta.py' "
    "según las instrucciones del usuario. Devuelve ÚNICAMENTE el código Python empaquetado "
    "dentro de un bloque de código markdown de python. No añadas explicaciones de texto."
)

model = genai.GenerativeModel("gemini-1.5-pro")
response = model.generate_content(f"{contexto}\n\nInstrucciones del usuario:\n{input_prompt}")

# Extraer el código del bloque markdown y guardarlo en ruleta.py
texto_respuesta = response.text
if "```python" in texto_respuesta:
    codigo = texto_respuesta.split("```python")[1].split("```")[0].strip()
    with open("ruleta.py", "w") as f:
        f.write(codigo)
    print("¡'ruleta.py' ha sido actualizado por Gemini con éxito!")
else:
    print("Error: Gemini no devolvió el formato de código esperado.")
