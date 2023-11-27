### Simulação de crescimento de populações de insetos
# Talvez dê para colocar um pouco de aleatoriedade na simulação, variando os valores de r um pouco a cada iteração
# O programa começa pela função main(), que chama as outras funções.

## Função para pegar o valor de r da tabela. O arquivo vai ser lido em "main()"
def get_r_from_table(temperature, strain):
    # se "strain" for "", considerar que só tem 1 variedade na tabela, talvez
    pass

def simulate_growth(N, duration, temp_changes, max_target_pop, control_duration, strain = ""):
    ## strain = "" significa que o parâmetro é opcional e o valor padrão é uma string vazia
    """ simulate_growth
    Essa função vai receber os seguintes parâmetros:
    - N: população inicial
    - duration: duração da simulação
    - temp_changes: dicionário com as mudanças de temperatura
    - max_target_pop: população máxima
    - control_duration: duração do controle
    - strain: variedade (pode ou não ser incluído)
    ...?
    """

    #pegar o valor de r da tabela e a população inicial, iniciar variáveis (armazenar em variáveis os resultados que queremos)

    resultados = [] # lista de listas ou dicionário com os resultados que queremos

    # um loop com duração "duration"
    for t in range(duration):
        # ver mudanças no valor de r que queremos (por exemplo pela temperatura ou qualquer outra coisa)
        # calcular a mudança na população (usando a fórmula)
        # atualizar a população
        # atualizar a variável que armazena os resultados que queremos
        pass

    
    return resultados #retorna os resultados que queremos. Prossivelmente uma lista de listas ou um dicionário

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
    ## Se o programa for executado diretamente, executa isso aqui (chama a função main(), no caso)
    ## isso serve para se o programa for importado como um módulo (como o import sys, por exemplo), não executar a função main()
    ## Já que o que interessa normalmente não é a função "main", mas sim as outras.
    main()