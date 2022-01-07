# Bot de Telegram de Analise de Dados
=======================================

Este projeto foi documentado aqui no GitHub e no meu canal do Youtube, sendo uma forma de compartilhar os desafios e aprendizados que tive com esse projeto para outras pessoas.

Assista a playlist:

[![Bot Telegram de Analise de Dados com Python](http://img.youtube.com/vi/IJGGPkNg8ZI/0.jpg)](https://www.youtube.com/playlist?list=PLshkB4NQEfC7ZJqmnKcjsJBzv9p2CeNNr "Bot Telegram de Analise de Dados com Python")

## Escopo do Projeto
O produto final deve ser um bot de Telegram que retornará visualizações de dados solicitadas pelo usuário. Essas visualizações são geradas a partir de dados que devem ser extraídos de uma base de dados presente em um Google Planilhas dentro do Google Drive da empresa, de forma automatizada. A implementação do bot de Telegram deve ser feita na linguagem Python, com o uso da API de bots do Telegram. As visualizações e a automação de extração de dados também deve ser feita via Python.

Os dados são ficticios e simulam uma situação do RH da empresa. 

**Situação Simulada e Ficticia**: O RH da empresa mensalmente realiza a coleta de feedbacks entre os funcionários da empresa. Cada funcionário irá avaliar seu colega de equipe com uma nota de 0 a 10, tendo a opção de colocar um comentário. As respostas são coletadas de forma anônima. Todo mês essas respostas são registradas neste mesmo Google Planilhas (sempre sobrescrevendo os dados do mês anterior). Para auxiliar as analises desejadas pelo RH e, ao mesmo tempo, não sobrecarregar o time de Dados foi pensada essa automação, sendo esta a motivação desse projeto.

## Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>

---------
## Visualizações desejadas
- NPS interno mensal médio por setor 
- NPS interno mensal médio por contratação
- Distribuição do NPS interno
