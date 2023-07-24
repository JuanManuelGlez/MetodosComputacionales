%%Juan Manuel González Ascencio
%%A00572003

%%counting positive numbers
contar_positivos([], 0). % Caso base: la lista está vacía, no hay números positivos.
contar_positivos([X|Resto], Cantidad) :-
    X > 0, % Si el número X es positivo
    contar_positivos(Resto, CantidadResto), % Contar positivos en el resto de la lista
    Cantidad is CantidadResto + 1. % Incrementar la cantidad de positivos en 1.

contar_positivos([X|Resto], Cantidad) :-
    X =< 0, % Si el número X no es positivo
    contar_positivos(Resto, Cantidad). % Contar positivos en el resto de la lista




% Predicado para contar cuántas veces se repite un número X en una lista
contar_repeticiones(_, [], 0). % Caso base: la lista está vacía, no hay repeticiones.

contar_repeticiones(X, [X|Resto], Cantidad) :-
    contar_repeticiones(X, Resto, CantidadResto), % Contar repeticiones en el resto de la lista
    Cantidad is CantidadResto + 1. % Incrementar la cantidad de repeticiones en 1.

contar_repeticiones(X, [Y|Resto], Cantidad) :-
    X \= Y, % Si el número X no es igual a Y
    contar_repeticiones(X, Resto, Cantidad). % Contar repeticiones en el resto de la lista sin modificar la cantidad.




% Predicado para duplicar un elemento
duplicar_elemento(X, [X, X]).

% Predicado para duplicar todos los elementos de una lista
duplicar_lista([], []).
duplicar_lista([X|Resto], Duplicados) :-
    duplicar_elemento(X, DX), % Duplicar el elemento X
    duplicar_lista(Resto, DuplicadosResto), % Duplicar el resto de la lista
    append(DX, DuplicadosResto, Duplicados). % Concatenar DX con DuplicadosResto para obtener la lista Duplicados



% Predicado para filtrar números positivos en una lista
filtrar_positivos([], []). % Caso base: la lista está vacía, no hay números positivos.

filtrar_positivos([X|Resto], [X|PositivosResto]) :-
    X > 0, % Si el número X es positivo
    filtrar_positivos(Resto, PositivosResto). % Filtrar positivos en el resto de la lista.

filtrar_positivos([X|Resto], Positivos) :-
    X =< 0, % Si el número X no es positivo
    filtrar_positivos(Resto, Positivos). % Filtrar positivos en el resto de la lista sin incluir X.



% Predicado para calcular el producto punto entre dos listas
producto_punto([], [], 0). % Caso base: ambas listas están vacías, el producto punto es 0.

producto_punto([X|Resto1], [Y|Resto2], ProductoPunto) :-
    producto_punto(Resto1, Resto2, ProductoPuntoResto), % Calcular el producto punto en el resto de las listas
    ProductoPunto is X * Y + ProductoPuntoResto. % Sumar el producto de los elementos actuales al producto punto.
