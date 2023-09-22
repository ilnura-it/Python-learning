def list_manipulation(list, cmd, loc, val=None):
    if cmd == "remove" and loc == "end":
        return list.pop()
    elif cmd == "remove" and loc == "beginning":
        return list.pop(0)
    elif cmd == "add" and loc == "beginning":
        list.insert(0, val)
        return list
    elif cmd == "add" and loc == "end":
        list.append(val)
        return list
    
print(list_manipulation([1,2,3], "remove", "end")) # 3
print(list_manipulation([1,2,3], "remove", "beginning")) #  1
print(list_manipulation([1,2,3], "add", "beginning", 20)) #  [20,1,2,3]
print(list_manipulation([1,2,3], "add", "end", 30)) #  [1,2,3,30]