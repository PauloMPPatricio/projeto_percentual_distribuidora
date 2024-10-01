class Distribuidora:
    def __init__(self, faturamento_sp, faturamento_rj, faturamento_mg, faturamento_es, faturamento_outras_regioes):
        # Inicializamos os valores de faturamento por estado
        self.faturamento_sp = faturamento_sp
        self.faturamento_rj = faturamento_rj
        self.faturamento_mg = faturamento_mg
        self.faturamento_es = faturamento_es
        self.faturamento_outras_regioes = faturamento_outras_regioes

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
        # Exibe o faturamento total formatado
        print(f"Faturamento total: {self.formatar_valor_br(self.total)}")

        # Exibe os percentuais calculados
        print(f"Percentual de SP: {self.percentual_sp:.2f}%")
        print(f"Percentual de RJ: {self.percentual_rj:.2f}%")
        print(f"Percentual de MG: {self.percentual_mg:.2f}%")
        print(f"Percentual de ES: {self.percentual_es:.2f}%")
        print(f"Percentual de Outras Regiões: {self.percentual_outras_regioes:.2f}%")


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
