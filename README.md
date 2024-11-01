# EPCC
Estudo de Coordenação de Proteção para Subestações

Este projeto disponibiliza um Jupyter Notebook para a execução de estudos de coordenação da proteção em subestações de clientes, utilizando informações de curto-circuito fornecidas pela concessionária. Com esse estudo, é possível configurar e ajustar os sistemas de proteção de forma precisa, assegurando a operação eficiente e a segurança da subestação.
Objetivo

O objetivo principal deste notebook é fornecer uma ferramenta prática e interativa para profissionais de engenharia elétrica realizarem análises detalhadas da proteção em subestações. Com as informações de curto-circuito da concessionária, o notebook facilita:

    Cálculo e análise de correntes de curto-circuito.
    Definição de ajustes adequados de relés de proteção.
    Verificação da coordenação entre os dispositivos de proteção para minimizar o impacto de falhas.

Funcionalidades

    Cálculo automático de corrente de curto-circuito para diferentes cenários de falhas.
    Ajuste e análise de relés de proteção com base nos dados fornecidos.
    Simulação e visualização gráfica da operação dos dispositivos de proteção.
    Geração de relatórios com as conclusões do estudo de coordenação.

Estrutura dos Arquivos

    Library.py - Arquivo de bibliotecas necessárias para execução
    Dados_Entrada_Concessionária.py - Dados de curto circuito da Concessionária de Energia
    Subestação_Cliente.py - Dados da Subestação de Energia do Cliente
    Estudo_Proteção_P1_R00.ipynb - Jupyter Notebook parte 1 Revisão 00
    Estudo_Proteção_P2_R00.ipynb - Jupyter Notebook parte 2 Revisão 00
    Verificar_Seletividade.py - Função que verifica a seletividade
    Tratamento_Plotagem.py - Função que realiza a plotagem