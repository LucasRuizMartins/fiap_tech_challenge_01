# tech_challenge_01

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

NPA Data Project

================================================================================
ESTRUTURA DO PROJETO
================================================================================
📁 tech_challenge_01/
├── 📄 Makefile                    - Comandos convenientes (make data, make lint, etc)
├── 📄 pyproject.toml              - Configuração do projeto e dependências
├── 📄 README.md                   - Documentação do projeto
├── 📄 requirements.txt            - Dependências Python
├── 📁 data/
│   ├── external/                  - Dados de terceiros
│   ├── interim/                   - Dados transformados
│   ├── processed/                 - Dados finais para modelagem
│   └── raw/
│       └── desafio_nps_fase_1.csv - Dataset principal do desafio
├── 📁 docs/                       - Documentação (mkdocs)
├── 📁 models/                     - Modelos treinados e serializados
├── 📁 notebooks/
│   └── teach_challenge.ipynb      - Notebook principal de análise
├── 📁 references/                 - Dicionários de dados e materiais explicativos
├── 📁 reports/
│   └── figures/                   - Gráficos e figuras geradas
└── 📁 tech_challenge_01/          - Código fonte do projeto
    ├── __init__.py
    ├── config.py                  - Variáveis e configuração
    ├── dataset.py                 - Scripts de download/geração de dados
    └── features.py                - Código para criar features

--------

# 📊 Predição de NPS em E-commerce

## 📝 Sobre o Projeto
Este projeto tem como objetivo prever o **Net Promoter Score (NPS)** atribuído por clientes de um e-commerce após a jornada de compra. Através de um modelo de regressão em Python, analisamos variáveis como valor do pedido, valor do frete e tempo de atraso na entrega para entender e prever a satisfação do cliente, permitindo ações proativas de melhoria contínua.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Linguagem:** Python
* **Manipulação e Análise de Dados:** Pandas, NumPy, SciPy (Shapiro-Wilk)
* **Visualização:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Pipeline, StandardScaler, Random Forest, Gradient Boosting, Linear Regression, Metrics, GridSearchCV), XGBoost

## ⚙️ Estrutura do Fluxo de Trabalho
1. **Análise Exploratória de Dados (EDA):** Verificação de distribuições, testes de normalidade e entendimento das variáveis de negócio (`order_value`, `delivery_delay_days`, etc.).
2. **Pré-processamento:** Limpeza de dados, codificação de variáveis categóricas (One-Hot Encoding) e separação em treino e teste.
3. **Modelagem Baseline:** Estabelecimento de um modelo ingênuo (previsão da média) para servir de base comparativa.
4. **Treinamento de Modelos:** 
   * Regressão Linear
   * Random Forest Regressor (com e sem `StandardScaler` em Pipeline)
   * Gradient Boosting Regressor
   * XGBoost Regressor
5. **Otimização:** Busca pelos melhores hiperparâmetros utilizando `GridSearchCV`.
6. **Avaliação e Interpretação:** Comparação de performance utilizando métricas estatísticas robustas (MAE, RMSE e R²). Extração das variáveis mais importantes (*Feature Importances*) e simulações de cenários de negócio (ex: impacto ao reduzir dias de atraso ou contatos de SAC).
7. **Acionabilidade:** Criação de sistema para classificar o risco de detratores com base na nota prevista, auxiliando a atuação preventiva das equipes de CX.

## 🚀 Como Executar o Projeto

1. Clone este repositório:
   ```bash
   git clone https://github.com/LucasRuizMartins/fiap_tech_challenge_01

   pip install pandas numpy scipy scikit-learn xgboost matplotlib seaborn jupyter

   jupyter notebook teach_challenge.ipynb


<br>
<br>
<br>
<br>

------

![Resultados da Regressão Linear](.\docs\images\resultado_linear_regression.png)

   📈 Próximos Passos e Melhorias Planejadas (Roadmap)
Como parte da evolução contínua deste modelo de dados, os seguintes refinamentos estão mapeados:

[ ] Tratamento Avançado de Outliers: Aplicação de Z-Score em variáveis contínuas (como valor de frete e atraso) para estabilizar modelos lineares.

[ ] Feature Scaling: Implementação de StandardScaler ou MinMaxScaler para equalizar as grandezas das variáveis independentes.

[ ] Estratificação de Dados: Utilização de bins e do parâmetro stratify no train-test split para garantir a representatividade das notas na validação.

[ ] Limitação Dimensional (Clipping): Trava estatística nas predições de regressão para mantê-las estritamente no intervalo lógico de 0 a 10.

[ ] Abordagem de Classificação: Teste de uma modelagem paralela focada em prever a categoria do cliente (Detrator, Passivo, Promotor) para gerar insights mais acionáveis para as equipes de CX.