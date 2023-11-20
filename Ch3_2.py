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


#判断链表是否回文
#首先链表的值存放在数组中，用数组形式判断是否回文
def isPalindrome2(head):
    value = []  
    current = head  
    while current:
        value.append(current[0])  
        current = current[1] 
    return value == value[::-1] #判断

head = (1, (3, (3, (1, None))))
print(isPalindrome2(head))  

head = (1, (2, None))
print(isPalindrome2(head)) 
