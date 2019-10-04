
# coding: utf-8

# In[44]:


graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D","F"],
    "F":["D","G"],
    "G":["F"]
}

# BFS 广度优先搜索：用一个队列来记录节点
def BFS(graph,s):   #graph是存储节点关系的字典，s是初始节点
    queue = []
    queue.append(s) # 选取一个初始节点(类似于二叉树的根节点)，放入数组
    seen = set()  # 用一个集合来保存已经计算的节点-默认是去重的
    seen.add(s)
    
    # 进一步输出最短路径,建立映射关系
    parent = {s: None}
    
    while (len(queue))>0:
        vertex = queue.pop(0) # 用队列表示,去掉头部
        nodes = graph[vertex] # 找到该节点的所有邻节点
        for n in nodes:
            if n not in seen: # 如果该节点没有出现过
                queue.append(n)
                seen.add(n)
                parent[n] = vertex
        print(vertex)
    return parent

print('---1：输出遍历后的所有点----')
parent = BFS(graph,"B")
print('--2：输出所有点的父子关系-----')

for key in parent:
    print(key,parent[key])
    
print('--3：输出最短路径-----')
v = 'G'  # 起始点S 到v的最短路径
short_len = []
while v != None:
    short_len.append(v)
    print(v)
    v = parent[v]
    
print('--4:最短路径长度为----')
print(len(short_len)-1)

