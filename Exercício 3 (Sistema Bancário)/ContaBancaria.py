class ContaBancaria :
  numero = None
  cliente = None
  saldo = None
  senha = None

  def __init__(self,pNumero,pCliente,pSaldo,pSenha):
    self.numero = pNumero
    self.cliente = pCliente
    self.__saldo = pSaldo
    self.__senha = pSenha
    
##################### OPÇÕES ########################
  def depositar(self,valor):
    if valor > 0 :
      self.__saldo += valor
    else :
      print("Valor digitado é inválido! ")
       
  def sacar(self,valor):
    if self.__saldo > 0 and self.__saldo >= valor :
      self.__saldo -= valor
    else :
      print("\n--------------------")
      print("Saldo insuficiente! ")

  def imprimirExtrato(self):
    print("O seu Saldo é: R$",self.__saldo)

##################### Login #########################
  def login(self,lNumero,lSenha):
    if lNumero == self.numero and lSenha == self.__senha :
      return True
      print("Logado")
    else :
      return False

 ################# Autentica Usuário ################
  def autenticarUsuario(self):
    usuarioLogado = None

    while(usuarioLogado != True):
      numeroConta = int(input("Digite o número da sua conta: "))
      senha = input("Digite sua senha: ")
      print("--------------------")
      
      usuarioLogado = self.login(numeroConta,senha)
  
      if usuarioLogado == True :
        print("Usuário Autenticado!")
      else :
        print("Número de conta ou senha incorreto!\n")
        
#####################################################################
  def escolherOpcao(self):
    self.autenticarUsuario()
    op = None
    while op != 'S' :
      print("--------------------")
      op = input("\nDigite uma opção:\n1-Sacar\n2-Depositar\n3-Consultar saldo\nS-Sair\n")
      print("--------------------")
      if op == '1' :
        valor = int(input("Digite um valor para sacar: "))
        self.sacar(valor)
      elif op == '2' :
        valor = int(input("Digite um valor para Depositar:")) 
        self.depositar(valor)
      elif op == '3' :
       self.imprimirExtrato()
