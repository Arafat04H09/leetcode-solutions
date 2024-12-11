pointer = head
num = 0
while pointer:
    pointer = pointer.next
    num+=1
    if num > 99999:
        return True

return False