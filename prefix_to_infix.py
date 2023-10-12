def tokenize(prefix) :
    operator = "[]{}()+-*/"
    tokens = []
    currentNum = ""
    
    for _ in prefix :
        # print(_)
        if str(_).isdigit():
            currentNum += _ 
        elif _ in operator :
            if currentNum :
                if "." in currentNum :
                    tokens.append(float(currentNum))
                else :
                    tokens.append(int(currentNum))
                currentNum = ""
            tokens.append(_)
        elif _ == " " or _ == ",": 
            if currentNum :
                if "." in currentNum :
                    tokens.append(float(currentNum))
                else :
                    tokens.append(int(currentNum))
                currentNum = ""
        elif _ == "." :
            currentNum += "."
    
    if currentNum :
        if "." in currentNum :
            tokens.append(float(currentNum))
        else :
            tokens.append(int(currentNum))
        
    return tokens

def evaluate(prefix_array) :
    
    value = 0
    stack = []
    
    for i in range(len(prefix_array)) :
        operand = "(){}[]+-*/"
        
        _ = prefix_array[len(prefix_array)-i-1]
        
        # print(i,_,stack)
        
        if str(_) not in operand :
            stack.append(_)
            
        else :
            if _ in ')}]' :
                stack.append(_)
                continue
            
            
            a = stack.pop()
            b = stack.pop()
            
            # print("a : "+str(a)+" b : "+str(b))
            
            if _ in "+-/*" and not (str(a) not in operand and str(b) not in operand) :
                # print("a and b are not digits")
                raise Exception("Invalid prefix")
            
            if _ == "/" and b == 0:
                print("Division by 0")
                raise Exception("Division by zero error")
            
            
            
            if _ == '+':
                value = a + b
                stack.append(value)
            elif _ == '-':
                value = a - b
                stack.append(value)
            elif _ == '*':
                value = a * b
                stack.append(value)
            elif _ == '/':
                value = a / b
                stack.append(value)
            elif _ == '(' or _ == '{' or _ == '[':
                if _ == '(' and  str(a) not in operand and b == ")"  :
                    stack.append(a)
                elif _ == '{' and  str(a) not in operand and b == "}"  :
                    stack.append(a)
                elif _ == '[' and  str(a) not in operand and b == "]"  :
                    stack.append(a)
                else :
                    raise Exception("Invalid prefix")
    
    value = stack.pop()
    return value      

# console input
prefix = "[ *   [ /  4  2]  [ +   8  7]]"


# print(prefix)

prefix_array = tokenize(prefix)

# print(prefix_array)

value = evaluate(prefix_array)
print(value)