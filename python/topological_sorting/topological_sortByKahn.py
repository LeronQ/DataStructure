from collections import deque
from itertools import filterfalse

'''
Kahn 算法实际上用的是贪心算法思想。定义数据结构的时候，
如果 s 需要先于 t 执行，那就添加一条 s 指向 t 的边。所以，如果某个顶点入度为 0， 
也就表示，没有任何顶点必须先于这个顶点执行，那么这个顶点就可以执行了。
我们先从图中，找出一个入度为 0 的顶点，将其输出到拓扑排序的结果序列中（对应代码中就是把它打印出来），
并且把这个顶点从图中删除（也就是把这个顶点可达的顶点的入度都减 1）。
我们循环执行上面的过程，直到所有的顶点都被输出。最后输出的序列，就是满足局部依赖关系的拓扑排序 
'''
class Graph:
    def __init__(self, num_vertices: int):
        self._num_vertices = num_vertices
        self._adjacency = [[] for _ in range(num_vertices)]
    
    def add_edge(self, s: int, t: int) -> None:
        self._adjacency[s].append(t)

       

    def tsort_by_kahn(self):
        in_degree = [0] * self._num_vertices
        for v in range(self._num_vertices):
            if len(self._adjacency[v]):
                for neighbour in self._adjacency[v]:
                    in_degree[neighbour] += 1
        q = deque(filterfalse(lambda x: in_degree[x], range(self._num_vertices)))
        while q:
            v = q.popleft()
            print(f"{v} -> ", end="")
            for neighbour in self._adjacency[v]:
                in_degree[neighbour] -= 1
                if not in_degree[neighbour]:
                    q.append(neighbour)
        print("\b\b\b   ")

    


if __name__ == "__main__":

    dag = Graph(4)
    dag.add_edge(1, 0)
    dag.add_edge(2, 1)
    dag.add_edge(1, 3)
    dag.tsort_by_kahn()
    #dag.tsort_by_dfs()