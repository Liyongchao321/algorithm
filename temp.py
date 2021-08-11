

def int_to_char(x):
    base = ord('a') - 1
    return chr(x + base)

def translate(x):
    s = str(x)
    count = 0
    stack = [s]
    while len(stack) > 0:
        temp = stack.pop()
        if len(temp) >= 1 :
            if int(temp[0]) != 0:
                stack.append(temp[1:])
                if len(temp) >= 2 and  int(s[:2]) <= 26:
                    stack.append(temp[2:])                
        else:
            count = count + 1
    return count



if __name__ == '__main__':
    inputs = [0, 1, 27, 123, 333]
    for i in inputs:
        print(translate(i))
    