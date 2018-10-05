# nn-draft

Neural Network Draft

Parâmetros de entrada inteiros:
- `in`
- `out`
- `hidden`

Matrizes de pesos reais
- W1, `in` linhas e `hidden` colunas
- W2, `hidden` linhas e `out` colunas

Neurônios reais:
- I, `1` linha e `in` colunas
- H, `1` linha e `hidden` coluna
- O, `1` linha e `out` colunas

Calcule
$$
para i=1..hidden
H_i = \sum_(j=1..in) [I_j W1_j_i]

para i=1..out
O_i = \sum_(j=1..hidden) [sigmoid( H_j W2_j_i)]
$$

Use seus conhecimentos e algoritmos de matrizes em python para realizar esta tarefa.
