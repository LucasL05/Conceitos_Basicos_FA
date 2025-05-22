def area_retangulo(lado1: float, lado2 : float) -> float:
    '''Calcula a área de um retângulo a partir do
    *lado1* e do *lado2*
    Exemplos:
    >>> area_retangulo(2.5,40000)
    100000.0
    >>> area_retangulo(0.01,5)
    0.05
    '''
    return lado1 * lado2


def produto_anterior_posterior(n: int) -> int:
    '''Calcula o produto entre um número inteiro *n*, o seu
    antecessor e o seu sucessor.
    Exemplos:
    >>> produto_anterior_posterior(2)
    6
    >>> produto_anterior_posterior(-5)
    -120
    '''
    return (n-1)*n*(n+1)


def calcula_porcentagem(a: float, porcent: float) -> float:
    '''Retorna *a* somado ao valor de *a* com a porcentagem *b* aplicada a ele.
    Exemplos:
    >>> calcula_porcentagem(5, 10)
    5.5
    >>> calcula_porcentagem(100,50)
    150.0
    >>> calcula_porcentagem(-10, 20)
    -12.0
    >>> calcula_porcentagem(10,-20)
    8.0
    >>> calcula_porcentagem(-10,-20)
    -8.0
    >>> calcula_porcentagem(7.5, 50)
    11.2
    '''
    r = round(a + (a*porcent/100),1) 
    return r


def zera_dezena_e_unidade(n: int) -> int:
    '''Retorna *n* com os algarismos das dezenas e unidades zerados
    Exemplos:
    >>> zera_dezena_e_unidade(2301)
    2300
    >>> zera_dezena_e_unidade(12)
    0
    >>> zera_dezena_e_unidade(345600)
    345600
    '''
    return (n//100)*100


def exclamacao(frase: str, n: int) -> str:
    '''Adiciona *n* exclamações ao final da *frase*
    >>> exclamacao('Queijada', 3)
    'Queijada!!!'
    >>> exclamacao('Catapimbas', 0)
    'Catapimbas'
    '''
    return frase+('!'*n)


def primeira_maiuscula(frase: str) -> str:
    '''Retorna a *frase* com a primeira letra,
    e somente a primeira letra, maiúscula.
    Exemplos:
    >>> primeira_maiuscula('jorGe')
    'Jorge'
    >>> primeira_maiuscula('Ouro fino')
    'Ouro fino'
    '''
    return frase[:1].upper() + frase[1:].lower()


def censura(frase: str, n: int) -> str:
    '''Retorna a *frase* com as *n* primeiras letras
    substituídas por x.
    Exemplos:
    >>> censura('Garfield', 3)
    'xxxfield'
    >>> censura('Gaude', 1)
    'xaude'
    >>> censura('dominus', 0)
    'dominus'
    '''
    return ('x'*n) + (frase[n:])


def  par(n: int) -> bool:    
    '''Retorna True ou False se *n* for par ou ímpar, respectivamente.
    Exemplos:
    >>> par(4)
    True
    >>> par(11)
    False
    '''
    assert n>=0, 'Informe um número positivo'
    return n%2 == 0


def tres_digitos(n: int) -> bool:
    '''Retorna True se *n* tem exatamente três dígitos.
    Exemplos:
    >>> tres_digitos(3566)
    False
    >>> tres_digitos(22)
    False
    >>> tres_digitos(777)
    True
    >>> tres_digitos(1)
    False
    '''
    return 1000>n>99


#  11)Funcao que recebe uma string s e indica se s termina com a letra 'z'.
def termina_z(s: str) -> bool:
    '''Retorna True se *s* termina com z ou Z.
    Exemplos:
    >>> termina_z('Arroz')
    True
    >>> termina_z('Toyota')
    False
    '''
    return s[-1].lower() == 'z'


#  Para os próximos exercícios, escreva primeiro os exemplos
#(e deixe como comentários) e depois faça a função.

#  12)Funcao que verifica se o caractere do meio de uma string é '-'.
# Arara-preta(True) / Colcheia(False) / batata-quente(True)
def traco_no_meio(s: str) -> bool:
    '''Retorna True se o caractere do meio de *s* é um hífen. Se não, ou se
    *s* for divisível por 2, retorna False.
    Exemplos:
    >>> traco_no_meio('Arara-preta')
    True
    >>> traco_no_meio('Colcheia')
    False
    >>> traco_no_meio('batata-quente')
    True
    '''
    tamanho = len(s)
    verifica = s[tamanho//2] == '-'
    existe_metade = tamanho % 2 != 0
    return  (existe_metade and verifica) 


def hipotenusa_triangulo_ret(a: float, b: float) -> float:
    '''Retorna o valor da hipotenusa de um triângulo retângulo
    de lados *a* e *b*.
    Exemplos:
    >>> hipotenusa_triangulo_ret(3.0,4.0)
    5.0
    >>> hipotenusa_triangulo_ret(5.0,12.0)
    13.0
    '''
    return (a**2+b**2)**0.5


def data(dia: str, mes: str, ano: str) -> str:
    '''retorna *dia*, *mes* e *ano* no formato *ano*/*mes*/*dia*
    Exemplos:
    >>> data('31','08','2004')
    '2004/08/31'
    >>> data('12','5','1999')
    '1999/5/12'
    '''
    return ano+'/'+mes+'/'+dia


def nome_mediano(nome: str) -> bool:
    '''Retorna True se *nome* tem tamanho mediano - de 4 a 8 letras.
    Se não, retorna False.
    Exemplos:
    >>> nome_mediano('Carlo')
    True
    >>> nome_mediano('Ekaterina')
    False
    '''
    return 3<len(nome)<9


def unidade(n: int) -> int:
    '''Retorna a unidade de um número inteiro positivo *n*.
    Exemplos:
    >>> unidade(152)
    2
    >>> unidade(160)
    0
    >>> unidade(1)
    1
    '''
    return n%10


def dezena(n: int) -> int:
    '''Retorna a dezena de um número intereiro positivo *n*.
    Exemplos:
    >>> dezena(198)
    9
    >>> dezena(0)
    0
    >>> dezena(45)
    4
    '''
    dez_un = n%100
    d = dez_un//10
    return d


def centena(n: int) -> int:
    '''Retorna a cenena de um número inteiro positivo *n*.
    Exemplos:
    >>> centena(7777)
    7
    >>> centena(250)
    2
    >>> centena(39)
    0
    ''' 
    cent_dez_un = n%1000
    cent = cent_dez_un//100
    return cent


def zerozero(n: int) -> bool:
    '''Retorna True se os dois últimos digitos de *n* são 00. Caso *n* só tenha
    um algarismo, considera-se também o zero à esquerda omitido em *n*
    Exemplos:
    >>> zerozero(133)
    False
    >>> zerozero(1000)
    True
    >>> zerozero(0)
    True
    '''
    dez_un = n%100
    return dez_un == 0


def e_Paula(nome: str) -> bool:
    '''Retorna True se o primeiro nome em *nome* é Paula ou paula.
    Exemplos:
    >>> e_Paula('Paula Maria')
    True
    >>> e_Paula('Paola')
    False
    '''
    return nome[:5].lower() == 'paula'


def triangulo(a: float, b: float, c: float) -> bool:
    '''Retorna True se os lados *a*, *b* e *c* dados obedecem á lei de formação
    de triângulos.
    Exemplos:
    >>> triangulo(3,4,5)
    True
    >>> triangulo(1,20,500)
    False
    >>> triangulo(2.5,2.5,2.5)
    True
    '''
    return a+b>c and a+c>b and c+b>a


def Silva(nome: str) -> bool:
    '''Retorna True se o último nome em *nome* é Silva ou silva.
    Exemplos:
    >>> Silva('Almeida Silva')
    True
    >>> Silva('Silva Ramos')
    False
    '''
    return nome[-5:].lower() == 'silva'


def qual_maior(a: float, b: float) -> float:
    '''Retorna o maior valor entre *a* e *b*
    Exemplos:
    >>> qual_maior(30.0,9.0)
    30.0
    >>> qual_maior(9.0,30.0)
    30.0
    >>> qual_maior(-2.0,7.0)
    7.0
    >>> qual_maior(7.0,-2.0)
    7.0
    '''
    return (a>b and a) or b






