import heapq
from typing import List

class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        linha, col = len(grid), len(grid[0])
        direcoes = [(0,1), (0,-1), (1,0), (-1,0)]
        dist = [[float('inf')] * col for _ in range(linha)]
        dist[0][0] = 0
        heap = [(0, 0, 0)]
        while heap:
            custo, i, j = heapq.heappop(heap)
            if custo > dist[i][j]:
                continue
            if i == linha-1 and j == col-1:
                return custo
            for direcao, (dx, dy) in enumerate(direcoes):
                nova_linha = i + dx
                nova_coluna = j + dy
                if 0 <= nova_linha < linha and 0 <= nova_coluna < col:
                    peso = 0 if direcao == grid[i][j] - 1 else 1
                    novo = custo + peso
                    if novo < dist[nova_linha][nova_coluna]:
                        dist[nova_linha][nova_coluna] = novo
                        heapq.heappush(heap, (novo, nova_linha, nova_coluna))
        return dist[linha-1][col-1]
