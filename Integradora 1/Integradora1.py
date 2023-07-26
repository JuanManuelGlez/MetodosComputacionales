class Estado:
    """
    Representa un estado en un autómata finito no determinista (NFA).

    Atributos:
        transiciones (dict): Un diccionario que almacena las transiciones del estado.
        es_final (bool): Un indicador que indica si el estado es un estado final.
    """

    def __init__(self, es_final=False):
        """
        Constructor de la clase Estado.

        Args:
            es_final (bool, optional): Indica si el estado es un estado final. Por defecto, es False.
        """
        self.transiciones = {}
        self.es_final = es_final

    def add_transicion(self, char, estado):
        """
        Agrega una transición desde el estado actual hacia otro estado.

        Args:
            char (str): El carácter de entrada que activa la transición.
            estado (Estado): El estado de destino al que se realizará la transición.
        """
        if char not in self.transiciones:
            self.transiciones[char] = []
        self.transiciones[char].append(estado)


class NFA:
    """
    Representa un autómata finito no determinista (NFA).

    Atributos:
        inicio (Estado): El estado inicial del NFA.
        fin (Estado): El estado final del NFA.
    """

    def __init__(self, inicio=None, fin=None):
        """
        Constructor de la clase NFA.

        Args:
            inicio (Estado, optional): El estado inicial del NFA. Si no se proporciona, se crea uno nuevo.
            fin (Estado, optional): El estado final del NFA. Si no se proporciona, se establece como el estado inicial.
        """
        self.inicio = inicio if inicio else Estado()
        self.fin = fin if fin else self.inicio
        self.fin.es_final = True

    @property
    def estados(self):
        """
        Obtiene una lista de todos los estados alcanzables desde el estado inicial del NFA mediante transiciones epsilon.

        Returns:
            list: Una lista de los estados alcanzables desde el estado inicial.
        """
        estados = {self.inicio}
        estados_a_examinar = [self.inicio]
        while estados_a_examinar:
            estado = estados_a_examinar.pop()
            for nuevos_estados in estado.transiciones.values():
                for nuevo_estado in nuevos_estados:
                    if nuevo_estado not in estados:
                        estados.add(nuevo_estado)
                        estados_a_examinar.append(nuevo_estado)
        return list(estados)


class DFA:
    """
    Representa un autómata finito determinista (DFA).

    Atributos:
        estados (list): Una lista que almacena los estados del DFA.
    """

    def __init__(self):
        """
        Constructor de la clase DFA.
        """
        self.estados = []


def e_closure(estado):
    """
    Calcula el cierre-épsilon de un estado dado en un autómata finito no determinista (NFA).

    Args:
        estado (Estado): El estado para el cual se calculará el cierre-épsilon.

    Returns:
        set: Un conjunto de estados alcanzables desde el estado dado mediante transiciones epsilon.
    """
    cierre = {estado}
    if "#" in estado.transiciones:
        for estado_epsilon in estado.transiciones["#"]:
            cierre.update(e_closure(estado_epsilon))
    return cierre


def move(estados, char):
    """
    Realiza el movimiento desde un conjunto de estados dados en un autómata finito no determinista (NFA)
    utilizando un carácter de entrada.

    Args:
        estados (set): El conjunto de estados desde los cuales se realizará el movimiento.
        char (str): El carácter de entrada para el movimiento.

    Returns:
        set: Un conjunto de estados alcanzables desde el conjunto de estados de entrada mediante el carácter dado.
    """
    movimientos = set()
    for estado in estados:
        if char in estado.transiciones:
            movimientos.update(estado.transiciones[char])
    return movimientos


def infix_to_postfix(regex):
    """
    Convierte una expresión regular en notación infija a notación posfija.

    Args:
        regex (str): La expresión regular en notación infija.

    Returns:
        str: La expresión regular en notación posfija.
    """
    prec = {
        "*": 3,
        ".": 2,
        "|": 1,
    }
    output = []
    stack = []
    for char in regex:
        if char in prec:
            while stack and stack[-1] in prec and prec[char] <= prec[stack[-1]]:
                output.append(stack.pop())
            stack.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            output.append(char)
    while stack:
        output.append(stack.pop())
    return "".join(output)


def parse_regex_to_nfa(regex):
    """
    Convierte una expresión regular en notación posfija a un autómata finito no determinista (NFA).

    Args:
        regex (str): La expresión regular en notación posfija.

    Returns:
        NFA: El autómata finito no determinista (NFA) equivalente a la expresión regular dada.
    """


    #     //      Steps for conversion is:
    # // ************************************
    # // ************************************
    # // 1. If you get a character, create a NFA for the single character and push the NFA to the stack.
    # // 2. If you get a keyword (any one from * | . +):
    # //  2.a. If the keyword is '*':
    # //      2.a.i.  if the stack is empty, return failed conversion(-1)
    # //      2.a.ii. else pop the top from stack, apply Klene closure and push back to stack
    # //  2.b. If the keyword is '+':
    # //      2.b.i.  if the stack is empty, return failed conversion(-1)
    # //      2.b.ii. else pop the top from stack, apply Klene plus and push back to stack
    # //  2.c. If keyword is '.':
    # //      2.c.i   if the stack has less than 2 elements, return failed conversion(-1)
    # //      2.c.ii. else pop two elements apply concatenation and push the result in stack.
    # //  2.d. If keyword is '|':
    # //      2.d.i   if the stack has less than 2 elements, return failed conversion(-1)
    # //      2.e.ii. else pop two elements apply NFA(1)|NFA(2) and push the result in stack.
    # // 3. Check the stack, if it contains exactly 1 element, return it as result, else failed conversion.
    # // ************************************

    pila = []
    for char in regex:
        if char not in {'|', '*', '.'}:
            estado_inicial = Estado()
            estado_final = Estado(es_final=True)
            estado_inicial.add_transicion(char, estado_final)
            pila.append(NFA(estado_inicial, estado_final))
            #print("Hola")
        elif char == '*':
            nfa1 = pila.pop()
            estado_inicial = Estado()
            estado_final = Estado(es_final=True)
            estado_inicial.add_transicion("#", nfa1.inicio)
            estado_inicial.add_transicion("#", estado_final)
            nfa1.fin.es_final = False
            nfa1.fin.add_transicion("#", nfa1.inicio)
            nfa1.fin.add_transicion("#", estado_final)
            pila.append(NFA(estado_inicial, estado_final))
        elif char == '.':
            nfa2 = pila.pop()
            nfa1 = pila.pop()
            nfa1.fin.es_final = False
            nfa1.fin.add_transicion("#", nfa2.inicio)
            pila.append(NFA(nfa1.inicio, nfa2.fin))
        elif char == '|':
            nfa2 = pila.pop()
            nfa1 = pila.pop()
            estado_inicial = Estado()
            estado_inicial.add_transicion("#", nfa1.inicio)
            estado_inicial.add_transicion("#", nfa2.inicio)
            estado_final = Estado(es_final=True)
            nfa1.fin.es_final = False
            nfa2.fin.es_final = False
            nfa1.fin.add_transicion("#", estado_final)
            nfa2.fin.add_transicion("#", estado_final)
            pila.append(NFA(estado_inicial, estado_final))
    else:  # handle case where char is a letter
            estado_inicial = Estado()
            estado_final = Estado(es_final=True)
            estado_inicial.add_transicion(char, estado_final)
            pila.append(NFA(estado_inicial, estado_final))
            #print("letra")
    return pila[0] 

def nfa_to_dfa(nfa, alphabet):
    """
    Convierte un autómata finito no determinista (NFA) en un autómata finito determinista (DFA).

    Args:
        nfa (NFA): El autómata finito no determinista (NFA) a convertir.
        alphabet (set): El conjunto de caracteres del alfabeto del NFA.

    Returns:
        DFA: El autómata finito determinista (DFA) equivalente al NFA dado.
    """
    dfa = DFA()
    unmarked_states = [e_closure(nfa.inicio)]
    dfa.estados = unmarked_states[:]
    while unmarked_states:
        current_state = unmarked_states.pop()
        for char in alphabet:
            moves = set.union(*(move({s}, char) for s in current_state))
            epsilon_closure_moves = set.union(*[e_closure(m) for m in moves])
            if epsilon_closure_moves not in dfa.estados:
                dfa.estados.append(epsilon_closure_moves)
                unmarked_states.append(epsilon_closure_moves)
    return dfa


def print_automata(nfa, dfa, alphabet):
    """
    Imprime los autómatas finitos no deterministas (NFA) y deterministas (DFA) dados.

    Args:
        nfa (NFA): El autómata finito no determinista (NFA) a imprimir.
        dfa (DFA): El autómata finito determinista (DFA) a imprimir.
        alphabet (set): El conjunto de caracteres del alfabeto de los autómatas.

    """
    print("NFA:")
    for i, estado in enumerate(nfa.estados):
        for char, destinos in estado.transiciones.items():
            for destino in destinos:
                print(f"{i} => [{(nfa.estados.index(destino), char)}]")
    print(f"Accepting state: {nfa.estados.index(nfa.fin)}")

    print("\nDFA:")
    for i, estados in enumerate(dfa.estados):
        for char in alphabet:
            moves = set.union(*(move({s}, char) for s in estados))
            if moves:
                epsilon_closure_moves = set.union(*[e_closure(m) for m in moves])
                matched_state = next((cierre for cierre in dfa.estados if cierre == epsilon_closure_moves), None)
                if matched_state is not None:
                    print(f"{chr(65+i)} => [{(chr(65+dfa.estados.index(matched_state)), char)}]")
    print(f"Accepting states: {[chr(65+i) for i, estados in enumerate(dfa.estados) if any(estado.es_final for estado in estados)]}")


# Función principal para probar el código

alphabet = {'a', 'b'}
regex = "(a|b)*.a.b.b"
regex_postfix = infix_to_postfix(regex)
nfa = parse_regex_to_nfa(regex_postfix)
dfa = nfa_to_dfa(nfa, alphabet)
print_automata(nfa, dfa, alphabet)