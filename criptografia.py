'''
Escribe una función desplazar que dado un carácter ch, un alfabeto alf y un número natural k,
devuelve el carácter resultante de desplazar ch de manera circular, un total de k posiciones
dentro del alfabeto alf, siempre que ch sea un carácter de dicho alfabeto, o, en caso contrario,
devuelve el propio carácter ch.
La función debe tener un aspecto así:
def desplazar (ch, alf, k)





def get_alf(): 
    return ['a','b','c','d','e','i','k','l','m','n','u','f','s','z','x']

def get_ch(): 
    ch = input("Enter a letter from alfabet: ")
    try: 
        int(ch)
    except: 
        return ch

def get_k(): 
    try: 
        k = int(input("Enter an integer: "))
        return k
    except: 
        print("You did not enter an integer")


def desplazar(ch, alf, k): 
   for i in range(len(alf)): 
       if alf[i] == ch: 
           m = alf[i+k-len(alf)] 
           alf[i+k-len(alf)] = ch
           return m
        
    



def main(): 
    alf = get_alf()
    ch = get_ch()
    
    k = get_k()

    if ch in alf: 
        print(desplazar(ch, alf, k))
    else: 
        print(ch)



if __name__ == '__main__':
    main()

'''
#desplazar with recursividad 
'''
def get_alf(): 
    return ['a','b','c','d','e','i','k','l','m','n','u','f','s','z','x']

def get_ch(): 
    ch = input("Enter a letter from alfabet: ")
    try: 
        int(ch)
    except: 
        return ch

def get_k(): 
    try: 
        k = int(input("Enter an integer: "))
        return k
    except: 
        print("You did not enter an integer")


def desplazar(ch, alf, k, index = 0): 
    if index == len(alf):
        return ch 
    if alf[index] == ch: 
        return alf[index+k-len(alf)] 

    return desplazar(ch, alf, k, index +1)
    

def main(): 
    alf = get_alf()
    ch = get_ch()
    
    k = get_k()

    print(desplazar(ch, alf, k))
    



if __name__ == '__main__':
    main()
    

    


'''



'''

Escribe una función alfInv que dado un String, devuelva la cadena inversa.
La función debe tener un aspecto así:
def alfInv (alf)
La salida si introducimos “abcdef” debe de ser “fedcba”




def get_string():
   string = input("Enter a string: ")
   return string
        
def alfInv(sent):
   
    if len(sent) == 1:
        return sent[0]
   
    

    char =  alfInv(sent[1:]) + sent[0]
        
    return char
        
  
   
   
def main(): 
     #a = get_string()

    a = 'sjgff'
    
    print(alfInv(a))
    
main()




Actividad 3: La función codificar
Escribe una función codCes que, dado un mensaje, un alfabeto y una clave (número natural),
devuelve el String resultante de codificar el mensaje según el alfabeto dado usando el método
César con la clave proporcionada.
El perfil de la función debe ser:
def codCes (m, alf, k)
El método deberá codificar uno a uno los caracteres del mensaje m, para lo cual se deberá
invocar al método desplazar
'''


def get_alphabet():
    import string
    string.ascii_lowercase
    return list(string.ascii_lowercase)


def get_frase(): 
    f = input("Enter a frase: ")
    if f.isdigit(): 
        print("You should enter some words")
        return get_frase()
    elif f.isspace(): 
        print("You should enter some words")
        return get_frase()
    else: 
        return f

def get_key():
    try: 
        key = int(input("Enter an integer as a key that is smaller than 26: "))
        if key  < len(get_alphabet()): 
            return key 
        else: 
            print("You entered somethimg big")
            return get_key()
    except: 
        print("You entered somethimg else")
        return get_key()
   

def codCes (m, alf, k): 
    code_m = m[0]

    for item in m[1:]:
       
            
        if item in alf: 
            for i in range(len(alf)): 
                if alf[i] == item: 
                    position = i 
                    break 
            code_m += alf[position+k-len(alf)]
        else: 
             code_m += item

    return code_m


def main():
    m = get_frase()
    alf = get_alphabet()
    k = get_key()

    print(codCes (m, alf, k))


if __name__ == '__main__': 
    main()
        






'''
Actividad 4: La función decodificar
Escribe una función decCes que decodifica un mensaje utilizando el método César.
El perfil del método debe ser:
def decCes (m, alf, k)
CONSEJO: Ten en cuenta que decodificar un mensaje con el método César es lo mismo que
codificar el mensaje, pero utilizando el alfabeto inverso.


def get_alphabet():
    #import string
    #string.ascii_lowercase
    #return list(string.ascii_lowercase)
    return list("abcdefghijklmnñopqrstuvwxyz")


def get_frase(): 
    f = input("Enter a frase: ")
    if f.isdigit(): 
        print("You should enter some words")
        return get_frase()
    elif f.isspace(): 
        print("You should enter some words")
        return get_frase()
    else: 
        return f

def get_key():
    try: 
        key = int(input("Enter an integer as a key that is smaller than 26: "))
        if key  < len(get_alphabet()): 
            return key 
        else: 
            print("You entered somethimg big")
            return get_key()
    except: 
        print("You entered somethimg else")
        return get_key()
   

def desplazar(ch, alf, k, index): 
    if index < 0:
        return ch 
    if alf[index] == ch: 
        return alf[index-k] 

    return desplazar(ch, alf, k, index -1)


def deCodCes (m, alf, k): 
    index = len(alf)-1
    code_m = m[0]
    for item in m[1:]: 
        r = desplazar(item, alf, k, index)
        code_m += r
    return code_m

def main():
    m = get_frase()
    alf = get_alphabet()
    k = get_key()

    print(deCodCes (m, alf, k))


if __name__ == '__main__': 
    main()

'''



