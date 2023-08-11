# Gerador-de-CPF
Código simples em Python que irá gerar CPFs aleatórios, já de acordo com a validação do Ministério da Fazenda.

Os primeiros 9 digitos são aleatórios, e serão gerados pela biblioteca random do Python.
OBS: O 9º dígito representa o estado em que a pessoa reside, vide a lista a seguir:
0 – RS
1 – DF, GO, MS, MT e TO
2 – AC, AM, AP, PA, RO e RR
3 – CE, MA e PI
4 – AL, PB, PE, RN
5 – BA e SE
6 – MG
7 – ES e RJ
8 – SP
9 – PR e SC  

Os últimos dois digitos passam por um cálculo mais rigoroso. Para o décimo digito, tem-se:

soma = 10*d1+9*d2+8*d3+7*d4+6*d5+5*d6+4*d7+3*d8+2*d9, em que d1 é primeiro dígito, d2 o segundo, etc.

Por seguinte, dividimos 'soma' por 11 e analisamos o valor inteiro do resto:
- Se for 0 ou 1, d10 = 0.
- Se for maior que 1, d10 = 11-resto.

Para o décimo primeiro digito, a forma é semelhante, mas com uma pequena diferença:

soma = 10*d2+9*d3+8*d4+7*d5+6*d6+5*d7+4*d8+3*d9+2*d10

A única mudança é que a soma se inicia no segundo digito e termina no décimo.
Para gerar d11, o cálculo final é o mesmo:
- Se o resto da divisão inteira de soma por 11 for 0 ou 1, d11 = 0.
- Se for maior que 1, d11 = 11-resto.
