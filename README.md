FIAP - Faculdade de Informática e Administração Paulista


Cana Eficiente

Grupo Arthur

Integrantes
1. Arthur Peixoto

Professores: Sabrina Otoni

📜 Descrição
O Cana-Eficiente é uma solução Agrotech desenvolvida em Python para combater um dos grandes problemas do agronegócio brasileiro: a perda de até 15% da produção de cana-de-açúcar durante a colheita mecanizada.

Através de uma interface de linha de comando simples, o sistema permite que produtores rurais registrem dados de cada colheita. Com base nessas informações, a ferramenta gera relatórios analíticos que identificam os principais focos de desperdício, como máquinas com baixo desempenho ou operadores que precisam de treinamento.

O objetivo é transformar dados brutos em insights práticos, ajudando o produtor a tomar decisões mais eficientes para reduzir perdas e aumentar a lucratividade da safra.

# Projeto: Cana-Eficiente

1. Problema do Agronegócio Tratado

O Brasil é o líder mundial na produção de cana-de-açúcar. No entanto, enfrenta um grave problema de produtividade: as perdas durante a colheita mecanizada podem chegar a **15% da produção**, um prejuízo milionário para os produtores e para a economia.

Este projeto, **Cana-Eficiente**, ataca diretamente essa "dor" do agronegócio. Ele se posiciona como uma solução **Agrotech** simples e acessível, projetada para que produtores rurais possam registrar, monitorar e analisar dados de cada colheita. O objetivo é identificar os principais focos de perda (ex: qual máquina, operador ou talhão gera mais prejuízo) e fornecer insights para otimizar o processo, reduzindo o desperdício e aumentando a lucratividade.

2. Inovação da Proposta

A inovação do **Cana-Eficiente** não está em criar uma tecnologia disruptiva, mas em **democratizar o acesso à análise de dados** no campo. Diferente de sistemas de gestão (ERPs) complexos e caros, nossa solução oferece uma ferramenta de fácil usabilidade (via prompt de comando) que gera valor imediato. O produtor pode, de forma rápida, transformar dados brutos de colheita em informações estratégicas para a tomada de decisão.

3. Como Executar a Solução

1.  Certifique-se de ter o Python 3 instalado.
2.  Salve o arquivo `main.py` em uma pasta no seu computador.
3.  Abra um terminal ou prompt de comando.
4.  Navegue até a pasta onde você salvou o arquivo.
5.  Execute o comando: `python main.py`
6.  O sistema irá iniciar e o menu principal será exibido. O arquivo de dados `colheitas.json` será criado automaticamente no primeiro salvamento.


4. Atendimento aos Requisitos Técnicos da Disciplina

A solução foi desenvolvida contemplando todos os conteúdos técnicos exigidos:

* **Subalgoritmos (Funções e Procedimentos):** O código é totalmente modularizado.
    * `menu_principal()`: Exibe as opções para o usuário.
    * `registrar_colheita(registros)`: Procedimento que coleta os dados da colheita, valida-os e os adiciona à base de dados (passagem de parâmetro `registros`).
    * `listar_colheitas(registros)`: Apresenta os dados de forma limpa e organizada.
    * `gerar_relatorio_analitico(registros)`: Calcula estatísticas (ex: perda média) e identifica os pontos críticos.
    * `salvar_dados_json(registros)` e `carregar_dados_json()`: Funções para manipulação de arquivos.
    * `salvar_simulado_oracle(registro)`: Demonstra a lógica de conexão com um banco de dados.

* **Estruturas de Dados:**
    * **Lista e Dicionário:** A base de dados principal (`registros`) é uma **lista de dicionários**, onde cada dicionário representa uma colheita com seus respectivos dados (ex: `{'id': 1, 'talhao': 'A1', 'maquina': 'JD-01', 'perda_perc': 10.5}`).
    * **Tupla:** Utilizada para definir os cabeçalhos das tabelas de exibição, garantindo que sejam imutáveis.

* **Manipulação de Arquivos:**
    * **JSON:** O sistema utiliza o arquivo `colheitas.json` para persistir os dados entre as sessões. A aplicação carrega os dados deste arquivo ao iniciar e salva as alterações ao final de cada operação de registro.
    * **Texto (.txt):** A funcionalidade de "Relatório Analítico" gera um arquivo `relatorio_analitico.txt` com um resumo claro e objetivo das perdas, facilitando a partilha e impressão.

* **Conexão com Banco de Dados (Oracle):**
    * Para cumprir o requisito sem a necessidade de um ambiente Oracle configurado, foi criada a função `salvar_simulado_oracle(registro)`.
    * Esta função **simula** o que seria uma inserção no banco de dados. Ela imprime na tela uma mensagem indicando a conexão e o comando SQL que seria executado. Isso demonstra o entendimento do processo de integração com um banco de dados real. Em um ambiente de produção, esta função seria substituída pela biblioteca `cx_Oracle`.

* **Consistência de Dados e Usabilidade:**
    * Todas as entradas numéricas (toneladas, perdas, etc.) são tratadas com blocos `try-except` para garantir que o usuário não insira um tipo de dado indesejado (como texto em um campo numérico).
    * As saídas de dados são formatadas em tabelas alinhadas, proporcionando uma interface limpa e de claro entendimento, mesmo sendo via prompt de comando.
