
# coding: utf-8

# In[14]:


from time import time

# main 表示主字符串，pattern表示需要匹配的字符串
def bf(main,pattern):
    n = len(main)
    m = len(pattern)
    if n <= m :
        return 0 if pattern==main else -1
    
    for i in range(n-m+1):
        for j in range(m):
            if main[i+j] == pattern[j]: # pattern的每个字符与main的i后面的字符逐一比较
                if j ==m-1:   #如果字符相等，并且j是pattern的最后一个字符相等，则全部相等
                    return i
                else:
                    continue # 如果字符相等，但j 不是pattern的最后一个字符，则继续比较
            else:
                break   # 如果有一个字符不相等，则直接退出
    return -1
            
    
def simple_hash(s,start,end):  # 添加hash算法
    '''
       计算子串的哈希值
    每个字符取acs-ii码后求和
    '''
    
    assert start<=end
    ret = 0
    
    for c in s[start:end+1]:
        ret += ord(c)
    return ret

def rk(main,pattern):
    n = len(main)
    m = len(pattern)
    
    if n <= m :
        return 0 if pattern==main else -1

    # 子串哈希值表
    hash_memo = [None] * (n-m+1)
    hash_memo[0] = simple_hash(main,0,m-1)
    
    for i in range(1,n-m+1):
        hash_memo[i] = hash_memo[i-1] -simple_hash(main,i-1,i-1)+simple_hash(main,i+m-1,i+m-1)
        
    
    # 模式串哈希值
    hash_p = simple_hash(pattern, 0, m-1)
    
    for i,h in enumerate(hash_memo):
        # 可能存在哈希冲突
        if h == hash_p:
            if pattern == main[i:i+m]:
                return i
            else:
                continue
    return -1



if __name__ == '__main__':
    m_str = 'a'*10000
    p_str = 'a'*200+'b'

    print('--- time consume ---')
    t = time()
    print('[bf] result:', bf(m_str, p_str))
    print('[bf] time cost: {0:.5}s'.format(time()-t))

    t = time()
    print('[rk] result:', rk(m_str, p_str))
    print('[rk] time cost: {0:.5}s'.format(time()-t))

    print('')
    print('--- search ---')
    m_str = 'thequickbrownfoxjumpsoverthelazydog'
    p_str = 'jump'
    print('[bf] result:', bf(m_str, p_str))
    print('[rk] result:', rk(m_str, p_str))

