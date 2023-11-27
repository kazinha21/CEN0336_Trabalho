### Simulação de crescimento de populações de insetos
# Talvez dê para colocar um pouco de aleatoriedade na simulação, variando os valores de r um pouco a cada iteração

## Função para pegar o valor de r da tabela
def get_r_from_table(temperature, strain):
    # se "strain" for "", considerar que só tem 1 variedade na tabela
    pass

""" simulate_growth
    Essa função vai receber os seguintes parâmetros:
    - N: população inicial
    - duration: duração da simulação
    - temp_changes: dicionário com as mudanças de temperatura
    - max_target_pop: população máxima
    - control_duration: duração do controle
    - strain: variedade (pode ou não ser incluído)
"""
def simulate_growth(N, duration, temp_changes, max_target_pop, control_duration, strain = ""):
    #pegar o valor de r da tabela e a população inicial, iniciar variáveis (armazenar em variáveis os resultados que queremos)

    # um loop com duração "duration"
    for t in range(duration):
        # ver mudanças no valor de r que queremos (por exemplo pela temperatura ou qualquer outra coisa)
        # calcular a mudança na população (usando a fórmula)
        # atualizar a população
        # atualizar a variável que armazena os resultados que queremos
        pass

    
    return resultados

def graph_results(resultados):
    # plotar os resultados, provavelmente usando matplotlib
    pass

def main():
    ## pegar os parâmetros da simulação
    # usar a biblioteca argparse para pegar os parâmetros da linha de comando?
    # usar a biblioteca input para pegar os parâmetros do usuário?
    # usar um arquivo de configuração?
    
    ## testar os parametros fornecidos pelo usuário.
    # se algum parâmetro estiver errado, mostrar uma mensagem de erro e sair do programa

    ## chamar a função simulate_growth
    ## chamar a função graph_results
    pass

if __name__ == "__main__":
    main()