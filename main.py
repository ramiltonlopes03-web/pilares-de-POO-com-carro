from classes import CarroSportivo, CarroInteligente, CarroCorrida

def test_drive(carro):
    print(f"\nTestando {carro.__class__.__name__}:")
    carro.acelera()
    carro.exibir_velocidade()

if __name__ == "__main__":
    # Instantiate and test CarroInteligente
    carro_inteligente = CarroInteligente(10)
    carro_inteligente.estaciona()
    test_drive(carro_inteligente)  # polymorphic call

    # Instantiate and test CarroSportivo
    carro_sportivo = CarroSportivo(50)
    carro_sportivo.turbo()
    test_drive(carro_sportivo)  # polymorphic call

    # Instantiate and test CarroCorrida
    carro_corrida = CarroCorrida(100)
    test_drive(carro_corrida)  # polymorphic call