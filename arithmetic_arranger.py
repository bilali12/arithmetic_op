def is_limit_five(list_of_strings):
    """
        this function determinate if the limit of the operations is correct
    """
    if  len(list_of_strings) >= 1 and len(list_of_strings) <= 5:
        return True
    return False

def is_valid_operator(operation):
    """
        this function determinate if an operator is a valid operator
    """
    operation = operation.split()
    if operation[1] == '+' or operation[1] == '-':
        return True
    return False
    

def is_digit(operand:str):
    """
        this function determinate if an operand is a digit
    """
    try:
        operand = int(operand)
        return True
    except:
        return False

def is_valid_digit(operand:str):
    """
        this function determinate if an operand is a valid digit
    """
    if is_digit(operand) and len(operand) >= 1 and len(operand) <= 4:
        return True
    return False

def max_lenght_str(operation:list):
    """
        this function determinate which operand is more large(talking about the lenght)
        and it return the biggest lenght
    """
    if len(operation[0]) > len(operation[2]):
        return len(operation[0])
    return len(operation[2])

def format_operand_1(operations:dict):
    """
        this function format the first operand
    """
    for operation in operations.values():
        max_lenght = max_lenght_str(operation)
        if len(operation[0]) >= len(operation[2]):
            print(' '*2 + operation[0], end=' '*4) 
        else:
            if len(operation[0]) == 1:
                print(' '*(max_lenght+len(operation[0])) + operation[0], end=' '*4)
            else:
                print(' '*(max_lenght+len(operation[0]) -2 ) + operation[0], end=' '*4)
    print('', end='\n\n')

def format_operand_2(operations:dict):
    """
        this function format the second operand and the operator at the same time
    """
    for operation in operations.values():
        max_lenght = max_lenght_str(operation)
        if len(operation[0]) >= len(operation[2]):
            print(f'{operation[1]}' + ' '*((max_lenght-len(operation[2])) + 1) + operation[2], end=' '*4)     
        else:
            print(f'{operation[1]}' + ' ' + operation[2], end=' '*4)
    print('', end='\n\n')

def format_lines(operations:dict):
    for operation in operations.values():
        max_lenght = max_lenght_str(operation)
        print('-'*(max_lenght+2), end=' '*4)
    print(' ', end='\n\n')

def format_operation(operations:dict):
    """
        this function format all the operation(s)
    """
    format_operand_1(operations)
    
    format_operand_2(operations)

    format_lines(operations)
   

def sum_ar(operand_1, operand_2):
    """
        this function return the result of operand_1 + operand_2
    """
    return int(operand_1) + int(operand_2)

def sustrac(operand_1, operand_2):
    """
        this function return the result of operand_1 - operand_2
    """
    return int(operand_1) - int(operand_2)

def arithmetic_arranger(list_arithmetic:list, state=False):
    if is_limit_five(list_arithmetic) is False:
        print("Error: Too many problems.")
        return

    operations = dict()
    dict_key = 0
    for operation in list_arithmetic:
        if is_valid_operator(operation) is False:
            print("Error: Operator must be '+' or '-'.")
            return
        operation = operation.split()
        if is_digit(operation[0]) is False or is_digit(operation[2]) is False:
            print("Error: Numbers must only contain digits.")
            return
        if is_valid_digit(operation[0]) is False or is_valid_digit(operation[2]) is False:
            print("Error: Numbers cannot be more than four digits.")
            return
        dict_key = str(dict_key)
        operations[dict_key] = operation
        dict_key = int(dict_key)
        dict_key+=1

    if state is False:
        format_operation(operations)
        
    if state is True:
       results = dict()
       format_operation(operations)
       key_nu = 0
       for operation in operations.values():
            maxi = max_lenght_str(operation)
           
            if operation[1] == '+':
                key_nu = str(key_nu)
                results[key_nu] = (str(sum_ar(operation[0], operation[2])), maxi)
                key_nu = int(key_nu)
                key_nu+=1
            else:
                key_nu = str(key_nu)
                results[key_nu] = (str(sustrac(operation[0], operation[2])), maxi)
                key_nu = int(key_nu)
                key_nu+=1
    
       for i, j   in results.items():
            if len(j[0]) < j[1]:
                 print(' '*3 + j[0], end=' '*4)
            if len(j[0]) > j[1]:
                print(' '*(j[1]-3) + j[0], end=' '*4)
            if len(j[0]) == j[1]:
                print(' '*2 + j[0], end=' '*4)

if __name__ == '__main__':
    arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
    arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
    
    
    
