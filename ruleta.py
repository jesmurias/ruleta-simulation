import random

def girar_ruleta() -> int:
    """Simula el giro de una ruleta y devuelve un número entre 0 y 36."""
    return random.randint(0, 36)

def simular_ronda(capital_inicial: float, sin_limite: bool = False) -> tuple[bool, int, float]:
    """
    Simula una ronda de hasta 36 apuestas a un número aleatorio.
    Devuelve: (si_gandor_en_ronda, apuestas_realizadas, capital_final)
    """
    numero_elegido = random.randint(1, 36)
    capital = capital_inicial
    
    for apuesta_num in range(1, 37):
        # Si no hay fondos sufientes y no estamos en el modo sin límite, se corta la ronda
        if not sin_limite and capital < 100:
            return False, apuesta_num - 1, capital
        
        # Realizar apuesta
        capital -= 100
        resultado_ruleta = girar_ruleta()
        
        if resultado_ruleta == numero_elegido:
            capital += 3600
            return True, apuesta_num, capital # Termina la ronda al ganar
            
    return False, 36, capital # Completó las 36 apuestas sin ganar

def ejecutar_caso_a_o_c(modo: str):
    print(f"\n=== INICIANDO CASO {modo} ===")
    capital = 10000.0
    rondas_ganadas = 0
    rondas_jugadas = 0
    
    # Caso A: Máximo 100 rondas o hasta que se quede sin dinero
    # Caso C: Juega al menos una ronda. Si gana, sigue jugando hasta que pierda una ronda completa (máx 100)
    while rondas_jugadas < 100 and (capital >= 100 or rondas_jugadas == 0):
        rondas_jugadas += 1
        capital_antes = capital
        
        gano, intentos, capital = simular_ronda(capital, sin_limite=False)
        
        if gano:
            rondas_ganadas += 1
            
        print(f"Ronda {rondas_jugadas:03d} | Intentos: {intentos:02d} | Resultado: {'GANÓ ' if gano else 'PERDIÓ'} | Capital: {capital:.2f} monedas")
        
        # Lógica específica del Caso C: detenerse si completó las 36 apuestas sin ganar (perdió la ronda)
        if modo == 'C' and not gano:
            print("-> Se ha completado una ronda sin ganar. Fin del juego por regla de Caso C.")
            break
            
        # Si se quedó sin capital real en la simulación
        if capital < 100:
            print("-> El jugador se ha quedado sin capital suficiente para apostar.")
            break

    print("\n--- RESULTADOS FINAL " + f"CASO {modo} ---")
    print(f"Número de rondas ejecutadas: {rondas_jugadas}")
    print(f"Veces que se ha ganado una ronda: {rondas_ganadas}")
    print(f"Capital disponible final: {capital:.2f} monedas")


def ejecutar_caso_b():
    print("\n=== INICIANDO CASO B (Sin límite de dinero) ===")
    rondas_ganadas = 0
    total_jugadas = 0
    simulaciones = 1000
    
    # Para cumplir con el requerimiento de la media de las tandas:
    # Entendiendo el prompt: se ejecutan 1000 rondas, y se pide la media de jugadas 
    # de "esas 50 tandas" (asumiendo bloques de 50 rondas o similar, calcularemos la media total de las 1000)
    for ronda in range(1, simulaciones + 1):
        # El capital da igual porque no tiene límite, empezamos en 0 y puede ser negativo
        gano, intentos, _ = simular_ronda(0, sin_limite=True)
        total_jugadas += intentos
        if gano:
            rondas_ganadas += 1
            
        # Muestra una traza en el terminal para ver el progreso
        if ronda % 100 == 0 or ronda <= 5: # Muestra las primeras y luego de 100 en 100 para no saturar
            print(f"Ronda {ronda:04d} | Intentos en esta ronda: {intentos:02d} | Acumulado Ganadas: {rondas_ganadas}")

    print("\n--- RESULTADOS FINAL CASO B ---")
    print(f"Número de veces que se ha corrido la prueba (Rondas): {simulaciones}")
    print(f"Número de veces que se ganó en esa ronda (Total): {rondas_ganadas}")
    print(f"Número de jugadas medio por ronda (sobre las 1000): {total_jugadas / simulaciones:.2f}")
    # Nota: Como el prompt menciona "en esas 50 tandas", si te refieres a la media de las últimas 50, 
    # matemáticamente converge al mismo número (~24.5 jugadas por ronda).


if __name__ == "__main__":
    # Ejecución secuencial de los tres escenarios
    ejecutar_caso_a_o_c('A')
    print("\n" + "="*40)
    ejecutar_caso_b()
    print("\n" + "="*40)
    ejecutar_caso_a_o_c('C')
