#判断一个链表是否为回文链表。

#输入：1→2 输出：False

#输入：1→2→2→1 输出：True

def isPalindrome(head):
    values = []  

    current = head  #将链表的值存储到数组中
    while current:
        values.append(current[0])  # 获取节点值，值在index0处
        current = current[1]  #取下一个节点，下一个节点在index1处

    return values == values[::-1] #判断

head = (1, (2, (2, (1, None))))
print(isPalindrome(head))  

head = (1, (2, None))
print(isPalindrome(head)) 
