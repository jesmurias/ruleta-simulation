import random

def simular_ruleta():
    """Simula una ruleta, devolviendo un número aleatorio entre 0 y 36 (ambos incluidos)."""
    return random.randint(0, 36)

def simular_ronda_apuesta_unica_fija(saldo_inicial_para_ronda, verbose=True):
    """
    Simula una ronda de apuestas según las reglas del juego de ruleta:
    - El jugador apuesta 100 monedas cada vez a un número aleatorio entre 1 y 36.
    - La ronda consta de un máximo de 36 apuestas.
    - Si el número apostado coincide con el de la ruleta, el jugador gana 3600 monedas (36 veces la apuesta) y la ronda termina.
    - Si falla, se descuentan 100 monedas de su saldo.
    - La ronda puede terminar antes de las 36 apuestas si el jugador gana o si se queda
      sin fondos para realizar la siguiente apuesta.
    
    Args:
        saldo_inicial_para_ronda (int): El saldo del jugador al inicio de esta ronda.
                                        Este saldo se modifica durante la ejecución de la ronda.
        verbose (bool): Si es True, imprime el detalle de cada intento dentro de la ronda.
        
    Returns:
        tuple: (gana_ronda, intentos_ronda, saldo_final_despues_ronda)
            - gana_ronda (bool): True si el jugador ganó la ronda, False en caso contrario.
            - intentos_ronda (int): Número de apuestas realizadas en la ronda.
            - saldo_final_despues_ronda (int): Saldo del jugador al finalizar la ronda.
    """
    apuesta_fija = 100
    premio_ganador = 36 * apuesta_fija  # 3600 monedas

    intentos_ronda = 0
    gana_ronda = False
    
    saldo_en_ronda = saldo_inicial_para_ronda 

    for _ in range(36): # La ronda consiste en una serie de hasta 36 apuestas
        # Verificar si el jugador tiene suficiente dinero para la próxima apuesta
        if saldo_en_ronda < apuesta_fija:
            if verbose:
                print(f"  Saldo insuficiente ({saldo_en_ronda} monedas) para realizar la siguiente apuesta de {apuesta_fija}. La ronda termina.")
            break

        intentos_ronda += 1
        
        # El jugador elige un número aleatorio entre 1 y 36 para apostar
        numero_apostado = random.randint(1, 36)
        
        # Simular el giro de la ruleta para obtener un resultado
        numero_ruleta = simular_ruleta()
        
        if verbose:
            print(f"  Intento {intentos_ronda}: Apostado {numero_apostado}, Ruleta {numero_ruleta}. Saldo previo apuesta: {saldo_en_ronda}")

        if numero_apostado == numero_ruleta:
            # ¡El jugador ha ganado!
            saldo_en_ronda += premio_ganador
            gana_ronda = True
            if verbose:
                print(f"  ¡Felicidades! Ganaste en el intento {intentos_ronda}. Ganas {premio_ganador} monedas. Saldo final del intento: {saldo_en_ronda}")
            break # La ronda finaliza inmediatamente al ganar
        else:
            # El jugador ha perdido la apuesta
            saldo_en_ronda -= apuesta_fija
            if verbose:
                print(f"  Perdiste. Pierdes {apuesta_fija} monedas. Saldo final del intento: {saldo_en_ronda}")
    
    return gana_ronda, intentos_ronda, saldo_en_ronda

# --- Simulación Caso A ---
def run_case_a():
    print("--- Simulación Caso A ---")
    print("Descripción: El jugador comienza con 10000 monedas y juega series de hasta 36 apuestas. El juego continúa hasta que se quede sin dinero o haya completado 100 rondas. El jugador juega con las monedas restantes de la ronda anterior.")

    saldo_inicial_a = 10000
    rondas_max_a = 100
    
    saldo_actual_a = saldo_inicial_a
    rondas_jugadas_a = 0
    rondas_ganadas_a = 0

    print(f"\nCapital inicial del jugador: {saldo_actual_a} monedas")

    while saldo_actual_a > 0 and rondas_jugadas_a < rondas_max_a:
        rondas_jugadas_a += 1
        print(f"\n--- Ronda {rondas_jugadas_a} (Caso A) --- Capital al inicio de la ronda: {saldo_actual_a} monedas")
        
        # Ejecutar una ronda de juego
        gana, intentos, saldo_final_ronda = simular_ronda_apuesta_unica_fija(saldo_actual_a, verbose=True)
        
        if gana:
            rondas_ganadas_a += 1
        
        saldo_actual_a = saldo_final_ronda # Actualizar el saldo global del jugador

        print(f"Resultado ronda {rondas_jugadas_a}: {'Ganada' if gana else 'Perdida'} en {intentos} intentos. Capital al final de la ronda: {saldo_actual_a} monedas")
        
        if saldo_actual_a <= 0:
            print("El jugador se ha quedado sin dinero. Fin del juego.")
            break

    print("\n--- Resumen Caso A ---")
    print(f"Descripción: El jugador comenzó con {saldo_inicial_a} monedas y jugó hasta quedarse sin dinero o completar {rondas_max_a} rondas.")
    print(f"Número total de rondas jugadas: {rondas_jugadas_a}")
    print(f"Número de rondas ganadas: {rondas_ganadas_a}")
    print(f"Capital disponible al final: {saldo_actual_a} monedas")

# --- Simulación Caso B ---
def run_case_b():
    print("\n--- Simulación Caso B ---")
    print("Descripción: El jugador no tiene límite de dinero y ejecuta el proceso de hasta 36 apuestas 1000 veces. Solo se muestra el resumen final de la simulación completa.")

    rondas_max_b = 1000
    
    saldo_total_b = 0 # Para llevar la cuenta de la ganancia/pérdida neta total de la simulación
    rondas_jugadas_b = 0
    rondas_ganadas_b = 0
    total_intentos_ronda_b = 0

    # Para el Caso B, el "saldo ilimitado" se simula pasando un valor muy alto a la función de ronda,
    # asegurando que la ronda siempre pueda completar sus 36 apuestas o ganar sin quedarse sin fondos intermedios.
    saldo_ilimitado_simulado = 1_000_000_000_000 # Un valor suficientemente grande

    for _ in range(rondas_max_b):
        rondas_jugadas_b += 1
        
        # simular_ronda_apuesta_unica_fija devolverá el saldo resultante si hubiera empezado con saldo_ilimitado_simulado.
        # Nosotros solo nos interesa el cambio neto para actualizar saldo_total_b.
        gana, intentos, saldo_final_ronda_simulada = simular_ronda_apuesta_unica_fija(saldo_ilimitado_simulado, verbose=False)
        
        if gana:
            rondas_ganadas_b += 1
        
        total_intentos_ronda_b += intentos
        
        # Calculamos la ganancia/pérdida neta de esta ronda
        net_change_ronda = saldo_final_ronda_simulada - saldo_ilimitado_simulado
        saldo_total_b += net_change_ronda

    print("\n--- Resumen Caso B ---")
    print(f"Descripción: El jugador tiene fondos ilimitados para {rondas_max_b} rondas de hasta 36 apuestas.")
    print(f"Número total de rondas jugadas: {rondas_jugadas_b}")
    print(f"Número de rondas ganadas: {rondas_ganadas_b}")
    
    media_jugadas_por_ronda = total_intentos_ronda_b / rondas_jugadas_b if rondas_jugadas_b > 0 else 0
    print(f"Número de jugadas medio por ronda: {media_jugadas_por_ronda:.2f}")
    
    print(f"Total monedas disponibles (ganancia/pérdida neta total): {saldo_total_b} monedas")

# --- Simulación Caso C ---
def run_case_c():
    print("\n--- Simulación Caso C ---")
    print("Descripción: Como el Caso A, pero se juega al menos una ronda. Si se gana, se sigue jugando. Si en una ronda se completan las 36 apuestas sin ganar (o se queda sin dinero), el juego termina. El tope máximo sigue siendo 100 rondas.")

    saldo_inicial_c = 10000
    rondas_max_c = 100
    
    saldo_actual_c = saldo_inicial_c
    rondas_jugadas_c = 0
    rondas_ganadas_c = 0
    total_intentos_ronda_c = 0
    
    seguir_jugando_por_regla_c = True # Condición específica para el Caso C

    print(f"\nCapital inicial del jugador: {saldo_actual_c} monedas")

    while seguir_jugando_por_regla_c and saldo_actual_c > 0 and rondas_jugadas_c < rondas_max_c:
        rondas_jugadas_c += 1
        print(f"\n--- Ronda {rondas_jugadas_c} (Caso C) --- Capital al inicio de la ronda: {saldo_actual_c} monedas")
        
        gana, intentos, saldo_final_ronda = simular_ronda_apuesta_unica_fija(saldo_actual_c, verbose=True)
        
        total_intentos_ronda_c += intentos

        if gana:
            rondas_ganadas_c += 1
            # Si se gana, seguir_jugando_por_regla_c permanece True para continuar a la siguiente ronda
        else:
            # Si se completa la ronda sin ganar (o se queda sin saldo), se deja de jugar según la regla del Caso C
            seguir_jugando_por_regla_c = False
            print("Ronda finalizada sin ganar en 36 intentos. El jugador decide dejar de jugar (regla específica del Caso C).")
        
        saldo_actual_c = saldo_final_ronda # Actualizar el saldo global del jugador

        print(f"Resultado ronda {rondas_jugadas_c}: {'Ganada' if gana else 'Perdida'} en {intentos} intentos. Capital al final de la ronda: {saldo_actual_c} monedas")
        
        if saldo_actual_c <= 0:
            print("El jugador se ha quedado sin dinero. Fin del juego.")
            seguir_jugando_por_regla_c = False # También se detiene si se queda sin dinero.
            break

    print("\n--- Resumen Caso C ---")
    print(f"Descripción: El jugador comenzó con {saldo_inicial_c} monedas y jugó hasta que no ganó una ronda completa de hasta 36 apuestas, se quedó sin dinero o completó {rondas_max_c} rondas.")
    print(f"Número total de rondas jugadas: {rondas_jugadas_c}")
    print(f"Número de rondas ganadas: {rondas_ganadas_c}")
    
    media_jugadas_por_ronda = total_intentos_ronda_c / rondas_jugadas_c if rondas_jugadas_c > 0 else 0
    print(f"Número de jugadas medio por ronda: {media_jugadas_por_ronda:.2f}")
    
    print(f"Total monedas disponibles (capital final): {saldo_actual_c} monedas")


# --- Ejecución de todos los casos de simulación ---
if __name__ == "__main__":
    run_case_a()
    run_case_b()
    run_case_c()