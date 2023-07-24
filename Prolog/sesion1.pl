%%Juan Manuel González Ascencio
%%A00572003

%%pow(X, Y, Resultado) define la función de potencia de X elevado a la Y
pow(_, 0, 1).
pow(X, Y, Resultado) :-
    Y > 0,
    Y1 is Y - 1,
    pow(X, Y1, Temp),
    Resultado is X * Temp.


%%fibonacci(N, Resultado) define la función de fibonacci de N
fib(1, 1) :- !.
fib(2, 1) :- !.
fib(N, F) :-
        N > 2,
        N1 is N-1,
        N2 is N-2,
        fib(N1, F1),
        fib(N2, F2),
        F is F1+F2.
