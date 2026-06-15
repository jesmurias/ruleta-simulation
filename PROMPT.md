# Ruleta

Name: ruleta.py

## Rol

Eres un programador experto en PYTHON.

## Target

El objetivo es demostrar con una simulación de los métodos para ganar en la ruleta no funcionan, la banca siempre gana. Para ello:
- Crearás un procedimiento que simule una ruleta y devuelva un número entre 0 y 36, ambos incluidos
- El jugador puede apostar a un número entre 1 y 36 (no puede apostar al cero)
- El método consiste en hacer una serie hasta 36 apuestas seguidas al mismo número de 100 monedas.
- Si el número al que ha apostado coindice con el que sale de la ruleta, el jugador gana, añade a su saldo 3600 monedas (36 veces la apuesta) y finaliza esa ronda aunque no haya llegado al número de 26 apuestas, con el dinero que tenga, que se suma al disponible del jugador.
- Si falla, se descuentan 100 euros del disponible del jugador.
- Si en 36 veces seguidas no ha ganado, se da la ronda por perdida y se inicia una nueva.
- En cada nueva ronda de 36 apuestas, el número elegido por ej jugador cambia respecto a la anterior de manera aleatoria. Si el azar lo dicta así, puede repetir número.

Vamos a correr de dos formas distintas:
Caso A) el jugador comienza con 10000 momedas y empieza las series de 36 apuestas hasta que se quede sin dinero o haya hecho 100 rondas. El jugador juega con las monedas restantes de al ronda anterior. 
Caso b) el jugador no tiene límite de dinero y ejecuta el proceso de 36 apuestas 1000 veces.
Caso C) Como el Caso A pero:

- Se juega al menos una ronda.
- Si se gana, se sigue jugando hasta que en una ronda se completen las 36 apuestas sin ganr
- El tope máximo sigue siendo 100 rondas

## Environtment

Va a correr en un MacBook con lo siguiente:
type python
python is an alias for /opt/homebrew/bin/python3.13
type pip
pip is an alias for /opt/homebrew/bin/pip3.13
python --version
Python 3.13.13

Output es un terminal.

## Output

La salida será:
- Mientras corre la prueba veremos el número de intentos de cada ronda y capital disponible.
Al final de la prueba:
- Número de veces que se ha corrido la prueba
- Veces que se ha ganado en la ronda
- Capital disponible
- en Case B y C la salida debe incluir:
 .  Numero de veces que se ganó en esa ronda
 .  Numero de jugadas medio en esas 50 tandas 
 .  Total monedas dispobibles
- En el Caso B no se debe incluir la salida de todas las rondas, solo el resumen.
- En el Caso C se debe incluir la salida de todas las rondas, solo el resumen.
- Todos los casos deben incluir una descripción de lo que hacen.

## Requisitos de Ejecución
- Python 3.13+
