import heapq
from typing import List

class Solution:
    def trapRainWater(self, mapa_alturas: List[List[int]]) -> int:
        if not mapa_alturas or not mapa_alturas[0]:
            return 0

        linhas, colunas = len(mapa_alturas), len(mapa_alturas[0])
        visitado = [[False] * colunas for _ in range(linhas)]
        heap_minimo = []

        # Define as bordas da matriz
        for x in range(linhas):
            for y in range(colunas):
                if x in (0, linhas - 1) or y in (0, colunas - 1):
                    nivel = mapa_alturas[x][y]
                    heapq.heappush(heap_minimo, (nivel, x, y))
                    visitado[x][y] = True

        direcoes = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        agua_retida = 0

        # Expansão estilo Prim: sempre a partir da menor “barreira”
        while heap_minimo:
            nivel, x, y = heapq.heappop(heap_minimo)

            for dir_x, dir_y in direcoes:
                novo_x, novo_y = x + dir_x, y + dir_y
                if 0 <= novo_x < linhas and 0 <= novo_y < colunas and not visitado[novo_x][novo_y]:
                    visitado[novo_x][novo_y] = True
                    nivel_vizinho = mapa_alturas[novo_x][novo_y]
                    # acumula água se o vizinho for mais baixo que o nível atual
                    agua_retida += max(0, nivel - nivel_vizinho)
                    # insere no heap com o novo nível de barreira
                    heapq.heappush(
                        heap_minimo,
                        (max(nivel, nivel_vizinho), novo_x, novo_y)
                    )

        return agua_retida
