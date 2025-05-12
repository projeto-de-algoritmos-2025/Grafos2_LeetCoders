import heapq

class Solution:
    def minCost(self, maxTime: int, edges: list[list[int]], passingFees: list[int]) -> int:
        total_cidades = len(passingFees)

        # lista de adjacência: cidade_vizinha, tempo_de_viagem
        adj = [[] for _ in range(total_cidades)]
        for a, b, dur in edges:
            adj[a].append((b, dur))
            adj[b].append((a, dur))

        # custo_por_tempo = menor custo para alcançar 'cidade' usando exatamente 'tempo'
        custo_por_tempo = [[float('inf')] * (maxTime + 1) for _ in range(total_cidades)]
        custo_por_tempo[0][0] = passingFees[0]

        # Heap de prioridades: (custo_total, tempo_gasto, cidade_atual)
        heap = [(passingFees[0], 0, 0)]

        while heap:
            custo, tempo, cidade = heapq.heappop(heap)

            # se o custo não for bom é ignorado
            if custo > custo_por_tempo[cidade][tempo]:
                continue

            # visitou todos os nós
            if cidade == total_cidades - 1:
                return custo

            # explora os vizinhos
            for vizinha, duracao in adj[cidade]:
                novo_tempo = tempo + duracao
                if novo_tempo > maxTime:
                    continue

                nova_taxa = custo + passingFees[vizinha]
                # se o custo for menor ele é atualizado
                if nova_taxa < custo_por_tempo[vizinha][novo_tempo]:
                    custo_por_tempo[vizinha][novo_tempo] = nova_taxa
                    heapq.heappush(heap, (nova_taxa, novo_tempo, vizinha))

        return -1
