from typing import Tuple, List, Dict

datos_recibidos: List[Tuple[float|int]] = recibir()

tipos_de_datos: List[str] = [f'cat{i}' for i in range(1,7)]
n_sensores: int = 5

columnas: List[str] = [f'{tipo}_{i}' for i in range(n_sensores) for tipo in tipos_de_datos]

with open('data.csv', 'x') as file:
    file.write(','.join(columnas) + '\n')

def guardar_csv(datos_recibidos: List[Tuple[float|int]]) -> None:
    nueva_lista: List[float|int] = []
    for data in datos_recibidos:
        nueva_lista.extend(list(data))
    with open('data.csv', 'a') as file:
        file.write(','.join(nueva_lista) + '\n')

if __name__ == '__main__':
    while True:
        main()



