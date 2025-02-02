"""
Projeto Para a seleção de estágio da Target Sistemas
Nome: Paulo Mauricio Pereira Patricio
Estudante: Análise e Desenvolvimento de Sistemas

Atualize o número da versão aqui
Versão: 1.0.1

Descrição da Versão:
- Melhorada a legibilidade da saída com inclusão de "\n".
- Adicionado "input()" para pausar a tela e permitir melhor leitura dos resultados.
- Alteração nos parâmetros do construtor, para que não sombrêm as variáveis globais.
"""


class Distribuidora:
    def __init__(self, sp, rj, mg, es, outras_regioes):
        # Inicializamos os valores de faturamento por estado
        self.faturamento_sp = sp
        self.faturamento_rj = rj
        self.faturamento_mg = mg
        self.faturamento_es = es
        self.faturamento_outras_regioes = outras_regioes

        # Inicializamos os atributos que serão calculados depois
        self.total = 0
        self.percentual_sp = 0
        self.percentual_rj = 0
        self.percentual_mg = 0
        self.percentual_es = 0
        self.percentual_outras_regioes = 0

    def calcular_percentuais(self):
        # Calcula o faturamento total
        self.total = (self.faturamento_sp + self.faturamento_rj + self.faturamento_mg +
                      self.faturamento_es + self.faturamento_outras_regioes)

        # Calcula o percentual de cada estado
        self.percentual_sp = (self.faturamento_sp / self.total) * 100
        self.percentual_rj = (self.faturamento_rj / self.total) * 100
        self.percentual_mg = (self.faturamento_mg / self.total) * 100
        self.percentual_es = (self.faturamento_es / self.total) * 100
        self.percentual_outras_regioes = (self.faturamento_outras_regioes / self.total) * 100

    @staticmethod
    def formatar_valor_br(valor):
        # Formata o valor no estilo brasileiro.
        return f"R$ {valor:,.2f}".replace(',', 'v').replace('.', ',').replace('v', '.')

    def exibir_percentuais(self):
        print("*" * 3 + " Faturamento Total/Percentual de Filiais " + 3 * "*")
        # Exibe o faturamento total formatado
        print(f"\nFaturamento total: -------------- {self.formatar_valor_br(self.total)}")

        # Exibe os percentuais calculados
        print(f"\nPercentual de SP: ---------------------- {self.percentual_sp:.2f}%")
        print(f"Percentual de RJ: ---------------------- {self.percentual_rj:.2f}%")
        print(f"Percentual de MG: ---------------------- {self.percentual_mg:.2f}%")
        print(f"Percentual de ES: ---------------------- {self.percentual_es:.2f}%")
        print(f"Percentual de Outras Regiões: ---------- {self.percentual_outras_regioes:.2f}%")


# Valores de faturamento fornecidos
faturamento_sp = 67836.43
faturamento_rj = 36678.66
faturamento_mg = 29229.88
faturamento_es = 27165.48
faturamento_outras_regioes = 19849.53

# Instancia da classe Distribuidora
distribuidora = Distribuidora(faturamento_sp, faturamento_rj, faturamento_mg, faturamento_es,
                              faturamento_outras_regioes)

# Calcula os percentuais
distribuidora.calcular_percentuais()

# Exibe os percentuais e o faturamento total formatado
distribuidora.exibir_percentuais()
input()
