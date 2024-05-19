"""
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель, 
використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. 
Витрати на з'єднання двох кабелів дорівнюють їхній сумі довжин, а загальні витрати дорівнюють 
сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""

# Найменші загальні витати, якщо завжди об'єднувати два найкоротших кабелі на кожному кроці. 

import heapq

def cable_connection(cables):
    # Створюємо мінімальну купу
    heap = []
    for cable in cables:
        heapq.heappush(heap, cable)
    
    # Витягуємо елементи впорядковано, для з'єднання
    connection_cost = 0
    while len(heap) > 1:
        cable_A = heapq.heappop(heap)
        cable_B = heapq.heappop(heap)
        connected_2_cables = cable_A + cable_B
        connection_cost = connection_cost + connected_2_cables
        
        # print(f"З'єднуємо кабелі {cable_A} та {cable_B}, отримуємо {connected_2_cables} та кладемо його до купи {heap}")
        # print(connection_cost)
        heapq.heappush(heap, connected_2_cables)
        # print("У купі:", heap)
    # Повертаємо суму з'єднання всіх кабелів
    return connection_cost

cables = [4, 7, 1, 10, 3]
print(cable_connection(cables))