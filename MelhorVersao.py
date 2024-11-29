class ECommerce:
    def __init__(self):
        self.carrinho = []
        self.pontos = 0

    def calcular_total_produto(self):
        try:
            valor_produto = float(input("Digite o valor do produto: R$ "))
            tipo_produto = int(input("Qual o tipo do produto?\n[1] Nacional\n[2] Importado\nEscolha: "))
            
            if tipo_produto not in [1, 2]:
                print("Erro: digite uma opção válida: [1] Nacional ou [2] Importado.")
                return

            cupom = int(input("Você tem cupom de frete grátis?\n[1] Sim\n[2] Não\nEscolha: "))
            if cupom not in [1, 2]:
                print("Erro: digite uma opção válida: [1] Sim ou [2] Não.")
                return
            
            frete = 0
            if tipo_produto == 1:  # nacional
                frete = 15.90 if cupom == 2 else 0 # o if e else do cupom simplificam
                #if cupom == 2:  Não tem cupom de frete grátis 
                    #frete = 15.90 
                #else:  Tem cupom de frete grátis 
                    # frete = 0                  
            elif tipo_produto == 2:  # importado
                frete = 19.90 if cupom == 2 else 0
                valor_produto += valor_produto * 0.17  # adiciona ICMS de 17%

            total_produto = valor_produto + frete
            self.carrinho.append(total_produto)
            self.pontos += (total_produto // 10) * 5 #cálculo que adiciona 5 pontos a cada 10 reais gastos 
            print(f"O valor a ser pago pelo produto é: R${total_produto:.2f}.")
        except ValueError:
            print("Erro: insira um valor numérico válido.")

    def mostrar_carrinho(self):
        if not self.carrinho:
            print("O carrinho está vazio.")
        else:
            valor_total = sum(self.carrinho) # determina o valor total do carrinho somando os produtos da lista
            print(f"Total de produtos no carrinho: {len(self.carrinho)}")
            print(f"Valor total do carrinho: R${valor_total:.2f}")
            print(f"Pontos acumulados: {self.pontos}")

    def realizar_resgate(self):
        if self.pontos < 100:
            print(f"Você possui {self.pontos} pontos, a quantidade mínima necessária é de 100 pontos para um desconto de R$100 numa compra acima de R$500, continue comprando!")
        elif sum(self.carrinho) > 500:
            print("Resgatando R$100 com seus pontos!")
            self.pontos -= 100 
            desconto = 100
            print(f"Novo total do carrinho: R${sum(self.carrinho) - desconto:.2f}")
        else:
            print("O total do carrinho precisa ser superior a R$500 para resgatar os pontos.")

    def menu(self):
        while True:
            print("\nMenu:")
            print("[1] Adicionar produto ao carrinho")
            print("[2] Mostrar carrinho")
            print("[3] Realizar resgate de pontos")
            print("[4] Finalizar compra")
            escolha = input("Escolha uma opção: ")

            if escolha == '1':
                self.calcular_total_produto()
            elif escolha == '2':
                self.mostrar_carrinho()
            elif escolha == '3':
                self.realizar_resgate()
            elif escolha == '4':
                print("Compra finalizada!")
                break
            else:
                print("Opção inválida. Tente novamente!")
ecommerce = ECommerce()
ecommerce.menu()
