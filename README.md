# tech_challenge_01

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

NPA Data Project

## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         tech_challenge_01 and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── tech_challenge_01   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes tech_challenge_01 a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

# 📊 Predição de NPS em E-commerce

## 📝 Sobre o Projeto
Este projeto tem como objetivo prever o **Net Promoter Score (NPS)** atribuído por clientes de um e-commerce após a jornada de compra. Através de um modelo de regressão em Python, analisamos variáveis como valor do pedido, valor do frete e tempo de atraso na entrega para entender e prever a satisfação do cliente, permitindo ações proativas de melhoria contínua.

## 🛠️ Tecnologias e Bibliotecas Utilizadas
* **Linguagem:** Python
* **Manipulação e Análise de Dados:** Pandas, NumPy, SciPy (Shapiro-Wilk)
* **Visualização:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn (Random Forest, Linear Regression, Metrics), XGBoost

## ⚙️ Estrutura do Fluxo de Trabalho
1. **Análise Exploratória de Dados (EDA):** Verificação de distribuições, testes de normalidade e entendimento das variáveis de negócio (`order_value`, `delivery_delay_days`, etc.).
2. **Pré-processamento:** Limpeza de dados e separação do conjunto em treino e teste (`train_test_split`).
3. **Modelagem Baseline:** Estabelecimento de um modelo ingênuo (previsão da média) para servir de base comparativa.
4. **Treinamento de Modelos:** * Regressão Linear
   * Random Forest Regressor
   * XGBoost Regressor
5. **Otimização:** Busca pelos melhores hiperparâmetros utilizando `GridSearchCV`.
6. **Avaliação:** Comparação de performance utilizando métricas estatísticas robustas (MAE, RMSE e R²).

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