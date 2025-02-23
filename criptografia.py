'''
Escribe una función desplazar que dado un carácter ch, un alfabeto alf y un número natural k,
devuelve el carácter resultante de desplazar ch de manera circular, un total de k posiciones
dentro del alfabeto alf, siempre que ch sea un carácter de dicho alfabeto, o, en caso contrario,
devuelve el propio carácter ch.
La función debe tener un aspecto así:
def desplazar (ch, alf, k)


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