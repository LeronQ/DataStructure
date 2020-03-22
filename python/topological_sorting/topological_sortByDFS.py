from collections import deque
from itertools import filterfalse

class Graph:
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]
    
    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)

    
# 利用DFS算法进行拓扑排序的核心是构建邻接矩阵和逆邻接矩阵。
# 先输出它可达的所有顶点，也就是说，先把它依赖的所有的顶点输出了，然后再输出自己
    def tsort_by_dfs(self):
        inverse_adjacency = [[] for _ in range(self._num_vertices)]
        for v in range(self._num_vertices):
            if len(self._adjacency[v]):
                for neighbour in self._adjacency[v]:
                    inverse_adjacency[neighbour].append(v)
        visited = [False] * self._num_vertices

        def dfs(vertex: int):  # 输出所有父节点
            if len(inverse_adjacency[vertex]):
                for v in inverse_adjacency[vertex]:
                    if not visited[v]:
                        visited[v] = True
                        dfs(v)   # 递归输出
            print(f"{vertex} -> ", end="")  # 输出所有父节点，最后输出自己
        
        for v in range(self._num_vertices):
            if not visited[v]:
                visited[v] = True
                dfs(v)
        
        print("\b\b\b   ")


if __name__ == "__main__":

    dag = Graph(4)
    dag.add_edge(1, 0)
    dag.add_edge(2, 1)
    dag.add_edge(1, 3)
    dag.tsort_by_dfs()