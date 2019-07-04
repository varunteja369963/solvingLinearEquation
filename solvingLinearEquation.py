def solvingSimpleEquations(exp):
    lhs = ''
    rhs = ''
    # START: shifting rhs to lhs 
    splitted_equ = exp.split('=')
    lhs = splitted_equ[0]
    rhs = int(splitted_equ[1])*-1
    equ = lhs + str(rhs) + '=0'
    # END: shifting rhs to lhs  

    #taking variable on one array and digits in other array
    varArray = []
    digitArray = []
    storeVar = ''
    sign = 'positive'
    for char in equ:
      if char == '+' or char == '-' or char == '=':
        if (storeVar.isdigit()):
          if (sign == 'negative'):
            storeVar = '-' + storeVar
          digitArray.append(storeVar)
          storeVar = ''
        else:
          if (sign == 'negative'):
            storeVar = '-' + storeVar
          varArray.append(storeVar)
          storeVar = ''
        if (char == '-'):
          sign = 'negative'
      else:
        storeVar = storeVar + char
      #taking variable on one array and digits in other array

    print(varArray)
    print(digitArray)

solvingSimpleEquations('a+2a=5')
