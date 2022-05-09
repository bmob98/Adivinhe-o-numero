# Chutar um número gerado pelo programa até acertar

# Vai gerar um número ineiro aleatório
import random

# Criada a classe foi chamada a função construtora
# Irá iniciar com 0, e o chute tem que ser do valor 1 até o 100 
# será pedido chute até o acerto do usuario
class ChuteNumero:
  def __init__(self):
    self.valor_aleatorio = 0
    self.valor_minimo = 1
    self.valor_maximo = 100
    self.tentar_novamente = True
  
  # Função Pedindo pra o usuario chutar
  def PedirValorAleatorio(self):
    self.valor_do_chute = int(input
    ("Chute um número: "))

  # Função que irá gerar um numero e será armazenado na variavel self.valor_aleatorio
  # para manter o numero em sigilo até que seja acertado
  def GerarNumeroAleatorio(self):
    self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)


  # O jogo iniciará: gerará o numero, depois irá pedir e vai entrar no loop e só sairá quando o usario acertar o numero
  def Iniciar(self):

  
    self.GerarNumeroAleatorio()
    self.PedirValorAleatorio()
    try:
      while self.tentar_novamente == True:
        if int(self.valor_do_chute) > self.valor_aleatorio:
          print("O chute foi alto, tente chutar um número mais baixo! ")
          self.PedirValorAleatorio()
        elif int(self.valor_do_chute)<self.valor_aleatorio:
          print("Chute um valor mais alto")
          self.PedirValorAleatorio()
        if int(self.valor_do_chute) == self.valor_aleatorio:
            self.tentar_novamente = False
            print("AEEE!! Acertou!!!!!! ")
    except:
      print("Por favor, chute um número")



# Instanciando para chamar o jogo

chute = ChuteNumero()
chute.Iniciar()