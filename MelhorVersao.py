class ECommerce:
    def __init__(self):
        self.carrinho = []
        self.pontos = 0
        self.desconto = 0 

    def calcular_total_produto(self):
        try:
            valor_produto = float(input("\nDigite o valor do produto: R$ "))
            tipo_produto = int(input("\nQual o tipo do produto?\n[1] Nacional\n[2] Importado\nEscolha: "))
            
            if tipo_produto not in [1, 2]:
                print("\nErro: Digite uma opção válida: [1] Nacional ou [2] Importado.")
                return

            cupom = int(input("\nVocê tem cupom de frete grátis?\n[1] Sim\n[2] Não\nEscolha: "))

            if cupom not in [1, 2]:
                print("\nErro: Digite uma opção válida: [1] Sim ou [2] Não.")
                return
            
            if tipo_produto == 1:  # nacional
                if cupom == 2:     # sem cupom
                    frete = 15.90
                else:
                    frete = 0

            elif tipo_produto == 2:  # importado
                if cupom == 2:       # sem cupom
                    frete = 19.90
                else:
                    frete = 0
                valor_produto += valor_produto * 0.17  # adiciona ICMS de 17%

            total_produto = valor_produto + frete
            self.carrinho.append(total_produto)
            self.pontos += (total_produto // 100) * 10 # cálculo que adiciona 10 pontos a cada 100 reais gastos 
            print(f"\nO valor a ser pago pelo produto é: R${total_produto:.2f}.")
            
        except ValueError:
            print("\nErro: insira um valor numérico válido.")

    def mostrar_carrinho(self):
        if not self.carrinho:
            print("\nO carrinho está vazio.")

        else:
            valor_total = sum(self.carrinho)  # calcula o valor total sem desconto
            print(f"\nTotal de produtos no carrinho: {len(self.carrinho)}")
            print(f"Valor total do carrinho (sem descontos): R${valor_total:.2f}")
            if self.desconto > 0:
                print(f"\nDescontos aplicados: R${self.desconto:.2f}")
                print(f"Valor total com descontos: R${valor_total - self.desconto:.2f}")
            print(f"\nPontos acumulados: {self.pontos}")

    def realizar_resgate(self):
        if self.pontos < 100:
            print(f"\nVocê possui {self.pontos} pontos, a quantidade mínima necessária é de 100 pontos para um desconto de R$100 numa compra acima de R$500. Continue comprando!")

        elif sum(self.carrinho) > 500:
            self.pontos -= 100
            self.desconto += 100  
            print(f"\nDesconto de R$100 aplicado!")
        else:
            print("\nO total do carrinho precisa ser superior a R$500 para resgatar os pontos.")

    def menu(self):
        while True:
            print("\n----------Menu----------")
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
                if self.carrinho:  # verifica se tem produtos no carrinho
                    valor_total = sum(self.carrinho) - self.desconto
                    print(f"\nCompra finalizada! O valor total pago é R${valor_total:.2f}.")
                else:
                    print("\nO carrinho está vazio, nenhuma compra foi realizada.")
                break

            else:
                print("\nOpção inválida. Tente novamente!")

ecommerce = ECommerce()
ecommerce.menu()
