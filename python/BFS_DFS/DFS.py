
# coding: utf-8

# In[2]:


graph = {
    "A":["B","C"],
    "B":["A","C","D"],
    "C":["A","B","D","E"],
    "D":["B","C","E","F"],
    "E":["C","D"],
    "F":["D"]
}

# DFS 深度优先搜寻： 用栈来保持遍历过的节点

def DFS(graph,s):
    stack =[]
    stack.append(s)
    seen=set()
    seen.add(s)
    
    while (len(stack)>0):
        vertex = stack.pop()  # 将最后一个节点压出
        nodes = graph[vertex]
        for n in nodes:
            if n not in seen:
                stack.append(n)
                seen.add(n)
        print(vertex)
        
DFS(graph,"A")

