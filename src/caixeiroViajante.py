from evolucao import Evolucao


QUANTIDADE_CIDADES = 10
TAMANHO_POPULACAO = 6
LIMITE_GERACOES = 100

evol = Evolucao( QUANTIDADE_CIDADES, TAMANHO_POPULACAO, LIMITE_GERACOES )

evol.evoluir()