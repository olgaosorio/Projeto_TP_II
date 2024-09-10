# Análise dos Dados do ENEM 2021

Este script em Python realiza uma análise dos dados do ENEM 2021, focando em diferentes aspectos das notas e características dos participantes. Abaixo estão os detalhes sobre o que o script faz e como usá-lo.

## Requisitos

- Python 3.x
- Bibliotecas Python: `pandas`

## Instruções de Uso

1. **Certifique-se de que o arquivo CSV está disponível**: O script espera um arquivo chamado `MICRODADOS_ENEM_2021.csv` no mesmo diretório em que o script é executado.

2. **Execute o Script**: Execute o script Python. Ele irá carregar os dados e realizar várias análises, exibindo os resultados no console.

## O que o Script Faz

1. **Carrega os Dados**:
   - O script carrega o arquivo CSV em chunks para evitar problemas de memória.
   - As colunas carregadas são: `TP_SEXO`, `NU_NOTA_REDACAO`, `SG_UF_PROVA`, `TP_ESCOLA`, `TP_ST_CONCLUSAO`, `NU_NOTA_MT`, `NU_NOTA_CN`, `NU_NOTA_CH`, `NU_NOTA_LC`, `TP_FAIXA_ETARIA`.

2. **Análises Realizadas**:
   - **Contagem e Percentual de Participantes por Gênero**: Mostra a distribuição dos participantes por gênero.
   - **Média da Nota de Redação por Gênero**: Calcula a média da nota de redação para cada gênero.
   - **Estado com a Nota mais Alta de Redação**: Identifica o estado com a nota de redação mais alta.
   - **Comparativo entre Escolas Públicas e Privadas**: Compara a média das notas de redação entre escolas públicas e privadas.
   - **Estatísticas das Notas por Estado**: Calcula a média, desvio padrão e mediana das notas para diferentes estados.
   - **Desempenho por Status de Conclusão do Ensino Médio**: Compara a média das notas de redação entre alunos que já concluíram o ensino médio e os demais.
   - **Desempenho por Faixa Etária**: Agrupa faixas etárias e calcula a média das notas de redação para cada grupo.

## Mapeamentos e Funções

- **Dicionário de Faixas Etárias**: Mapeia os códigos de faixa etária para descrições mais legíveis.
- **Função de Agrupamento de Faixa Etária**: Agrupa as faixas etárias em intervalos de 10 anos para facilitar a análise.

## Resultados

Os resultados das análises serão exibidos no console. Certifique-se de revisar as saídas para obter as informações detalhadas.

## Tratamento de Erros

O script inclui tratamento de erros para lidar com situações como:
- Arquivo não encontrado.
- Arquivo CSV vazio.
- Problemas na análise do arquivo CSV.

## Autores

- **Luiz Gomes**
[GitHub](https://github.com/) | [LinkedIn](https://www.linkedin.com/in/lucgomes1)

- **Jonathas**
[GitHub](https://github.com/) | [LinkedIn](https://www.linkedin.com/in//)

- **Matheus Gouveia**  
  [GitHub](https://github.com/gouveiamdb) | [LinkedIn](https://www.linkedin.com/in/gouveiamdb)

- **Olga Osorio Aburto**  
  [GitHub](http://github.com/olgaosorio/) | [LinkedIn](http://linkedin.com/in/olga-osorio-aburto/)

## Apresentação

https://prezi.com/p/dnhg0qdgcy6n/analise-de-dados-em-grupo/?present=1