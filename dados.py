import pandas as pd
import os

print("Script iniciado")

# Define as colunas que serão carregadas
colunas_necessarias = ['TP_SEXO', 'NU_NOTA_REDACAO', 'SG_UF_PROVA', 'TP_ESCOLA', 
                        'TP_ST_CONCLUSAO', 'NU_NOTA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 
                        'NU_NOTA_LC', 'TP_FAIXA_ETARIA']

# Caminho relativo ao diretório
caminho_arquivo = os.path.join('MICRODADOS_ENEM_2021.csv')

# Verifica se o arquivo existe
if not os.path.exists(caminho_arquivo):
    print(f"O arquivo não foi encontrado em: {caminho_arquivo}")
else:
    try:
        # Carrega o arquivo CSV com as colunas necessárias e em chunks para evitar erro de memória
        chunksize = 100000  # Tamanho do chunk ajustavel
        df_chunks = pd.read_csv(caminho_arquivo, sep=';', encoding='ISO-8859-1', 
                                usecols=colunas_necessarias, chunksize=chunksize)

        # Concatena os chunks em um dataframe único
        df = pd.concat(df_chunks)

        print("Arquivo carregado com sucesso")

    except FileNotFoundError:
        print(f"Erro: O arquivo '{caminho_arquivo}' não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo CSV está vazio.")
    except pd.errors.ParserError:
        print("Erro: Não foi possível analisar o arquivo CSV. Verifique a codificação e o separador.")
    except Exception as e:
        print(f"Erro inesperado: {e}")

    else:
        # Contagem de participantes por gênero com percentual
        conteo_sexo = df['TP_SEXO'].value_counts()
        total_participantes = len(df)
        percentual_sexo = (conteo_sexo / total_participantes) * 100

        print("\nNúmero de participantes por gênero e percentual:")
        for sexo, conteo in conteo_sexo.items():
            percentual = percentual_sexo[sexo]
            print(f"Gênero: {sexo}, Contagem: {conteo}, Percentual: {percentual:.2f}%")

        # Média da nota de redação por gênero
        media_redacao_por_genero = df.groupby('TP_SEXO')['NU_NOTA_REDACAO'].mean()
        print("\nMédia da nota de redação por gênero:")
        print(media_redacao_por_genero)

        # Estado com a nota mais alta de redação
        estado_mais_alta_nota = df.groupby('SG_UF_PROVA')['NU_NOTA_REDACAO'].max()
        estado_max_nota = estado_mais_alta_nota.idxmax()
        nota_max = estado_mais_alta_nota.max()
        print(f"\nEstado com a nota do ENEM mais alta: {estado_max_nota} : {nota_max}")

        # Comparativo entre escola pública e privada
        dict_escola = {
            1: 'Não Respondeu',
            2: 'Pública',  
            3: 'Privada'
        }
        df['TP_ESCOLA'] = df['TP_ESCOLA'].map(dict_escola)
        desempenho_escola = df.groupby('TP_ESCOLA')['NU_NOTA_REDACAO'].mean()
        print("\nDesempenho médio de redação por tipo de escola:")
        print(desempenho_escola)

        # Estatísticas (média, desvio padrão e mediana) das notas por estado
        colunas_notas = ['NU_NOTA_REDACAO', 'NU_NOTA_MT', 'NU_NOTA_CN', 'NU_NOTA_CH', 'NU_NOTA_LC']
        estatisticas_estado = df.groupby('SG_UF_PROVA').agg({col: ['mean', 'std', 'median'] for col in colunas_notas})
        print("\nEstatísticas (média, desvio padrão e mediana) das notas por estado:")
        print(estatisticas_estado)

        # Desempenho médio de redação por status de conclusão do ensino médio
        dict_conclusao = {
            1: 'Já concluí o Ensino Médio',
            2: 'Estou cursando e concluirei o Ensino Médio em 2021',
            3: 'Estou cursando e concluirei o Ensino Médio após 2021',
            4: 'Não concluí e não estou cursando o Ensino Médio'
        }
        df['TP_ST_CONCLUSAO'] = df['TP_ST_CONCLUSAO'].map(dict_conclusao)

        desempenho_conclusao = df.groupby('TP_ST_CONCLUSAO')['NU_NOTA_REDACAO'].mean()

        # Separando o desempenho de quem já concluiu o ensino médio (código 1) e os demais
        media_concluido = desempenho_conclusao.get('Já concluí o Ensino Médio', 0)
        media_nao_concluido = desempenho_conclusao[desempenho_conclusao.index != 'Já concluí o Ensino Médio'].mean()
        
        # Evitando divisão por zero
        if media_nao_concluido == 0:
            percentual_diferenca = float('inf')
        else:
            percentual_diferenca = ((media_concluido - media_nao_concluido) / media_nao_concluido) * 100

        # Exibindo o resultado
        print("\nDesempenho médio de redação por status de conclusão do ensino médio:")
        for conclusao, media in desempenho_conclusao.items():
            print(f"Status de Conclusão: {conclusao}, Média de Nota de Redação: {media:.2f}")

        print(f"\nA média de nota de redação dos alunos que já concluíram o ensino médio é {percentual_diferenca:.2f}% maior do que a dos demais alunos." if media_nao_concluido != 0 else "Não há dados suficientes para calcular a diferença percentual.")

        # Dicionário para mapear faixas etárias
        dicionario_faixas = {
            1: 'Menor de 17 anos',
            2: '17 anos',
            3: '18 anos',
            4: '19 anos',
            5: '20 anos',
            6: '21 anos',
            7: '22 anos',
            8: '23 anos',
            9: '24 anos',
            10: '25 anos',
            11: 'Entre 26 e 30 anos',
            12: 'Entre 31 e 35 anos',
            13: 'Entre 36 e 40 anos',
            14: 'Entre 41 e 45 anos',
            15: 'Entre 46 e 50 anos',
            16: 'Entre 51 e 55 anos',
            17: 'Entre 56 e 60 anos',
            18: 'Entre 61 e 65 anos',
            19: 'Entre 66 e 70 anos',
            20: 'Maior de 70 anos'
        }

        # Aplicando o dicionário de mapeamento
        df['FAIXA_ETARIA_DESCRITA'] = df['TP_FAIXA_ETARIA'].map(dicionario_faixas)

        # Função para agrupar faixas etárias em intervalos de 10 anos
        def agrupar_faixas_etarias(faixa):
            if faixa == 'Menor de 17 anos':
                return 'Menor de 17 anos'
            elif faixa in ['17 anos', '18 anos', '19 anos', '20 anos', '21 anos']:
                return '17 a 21 anos'
            elif faixa in ['22 anos', '23 anos', '24 anos', '25 anos']:
                return '22 a 25 anos'
            elif faixa == 'Entre 26 e 30 anos':
                return '26 a 30 anos'
            elif faixa == 'Entre 31 e 35 anos':
                return '31 a 35 anos'
            elif faixa == 'Entre 36 e 40 anos':
                return '36 a 40 anos'
            elif faixa == 'Entre 41 e 45 anos':
                return '41 a 45 anos'
            elif faixa == 'Entre 46 e 50 anos':
                return '46 a 50 anos'
            elif faixa == 'Entre 51 e 55 anos':
                return '51 a 55 anos'
            elif faixa == 'Entre 56 e 60 anos':
                return '56 a 60 anos'
            elif faixa == 'Entre 61 e 65 anos':
                return '61 a 65 anos'
            elif faixa == 'Entre 66 e 70 anos':
                return '66 a 70 anos'
            elif faixa == 'Maior de 70 anos':
                return 'Maior de 70 anos'
            else:
                return 'Desconhecido'

        # Aplicando a função de agrupamento de faixas etárias
        df['FAIXA_ETARIA_AGRUPADA'] = df['FAIXA_ETARIA_DESCRITA'].map(agrupar_faixas_etarias)

        # Comparação de desempenho entre diferentes faixas etárias agrupadas
        desempenho_faixa_etaria_agrupada = df.groupby('FAIXA_ETARIA_AGRUPADA')['NU_NOTA_REDACAO'].mean()

        # Exibindo os resultados
        print("\nDesempenho médio de redação por faixa etária (agrupada em intervalos de 10 anos):")
        for faixa, media in desempenho_faixa_etaria_agrupada.items():
            print(f"Faixa Etária: {faixa}, Média de Nota de Redação: {media:.2f}")

print("Script finalizado")
