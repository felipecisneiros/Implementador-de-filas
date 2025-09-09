from collections import deque
import heapq

def exemplo_fila():
    print("\n=== Exemplo de Fila ===")
    fila = deque()

    fila.append("A")
    fila.append("B")
    fila.append("C")

    print("Fila atual:", list(fila))

    print("Saiu:", fila.popleft())
    print("Fila após remoção:", list(fila))


def exemplo_fila_prioritaria():
    print("\n=== Exemplo de Fila Prioritária ===")
    fila_prioridade = []

    heapq.heappush(fila_prioridade, (2, "Baixa prioridade"))
    heapq.heappush(fila_prioridade, (0, "Alta prioridade"))
    heapq.heappush(fila_prioridade, (1, "Média prioridade"))

    print("Fila interna:", fila_prioridade)

    while fila_prioridade:
        prioridade, item = heapq.heappop(fila_prioridade)
        print(f"Processando: {item} (Prioridade {prioridade})")


def teste_prioridades():
    print("\n=== Teste com 5 altas, 5 médias e 5 baixas ===")
    fila_prioridade = []

    for i in range(5):
        heapq.heappush(fila_prioridade, (0, f"Alta {i+1}"))
    for i in range(5):
        heapq.heappush(fila_prioridade, (1, f"Média {i+1}"))
    for i in range(5):
        heapq.heappush(fila_prioridade, (2, f"Baixa {i+1}"))

    print("Ordem de execução por prioridade:")
    while fila_prioridade:
        prioridade, item = heapq.heappop(fila_prioridade)
        print(f"{item} (prioridade {prioridade})")


def round_robin():
    print("\n=== Simulação Round Robin ===")
    processos = deque([
        ["P1", 5],
        ["P2", 7],
        ["P3", 3]
    ])

    quantum = 2

    while processos:
        processo = processos.popleft()
        pid, tempo = processo
        execucao = min(quantum, tempo)
        tempo -= execucao

        print(f"{pid} executou {execucao} unidades (restam {tempo})")

        if tempo > 0:
            processos.append([pid, tempo])

    print("\nTodos os processos foram concluídos!")


def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Exemplo de Fila")
        print("2 - Exemplo de Fila Prioritária")
        print("3 - Teste com 5 altas, 5 médias e 5 baixas")
        print("4 - Simulação Round Robin")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            exemplo_fila()
        elif opcao == "2":
            exemplo_fila_prioritaria()
        elif opcao == "3":
            teste_prioridades()
        elif opcao == "4":
            round_robin()
        elif opcao == "0":
            print("Saindo...")
            break
        else:
            print("Opção invalida, tente novamente.")


if __name__ == "__main__":
    menu()

