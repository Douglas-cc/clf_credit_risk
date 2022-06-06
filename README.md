# API RISCO DE CRÉDITO

### objetivos

API foi desenvolvida em fastapi tem como objetivo classificar o risco de conceder credito bancario ao um cliente basicamente voce disponibiliza dados de e a API retorna dizendo se é arriscado ou não concerder credito aquele cliente. Além disso podemos salvar os resultados em um banco de dados SQL, listar todas as classificações e pesquisar classificações já realizadas por nome.

### Descrição das variaveis de entrada 

- name: nome do cliente
- loan: Comprometimento de renda 
- income: Renda
- age: Idade 
- date: Dia e horario da classificação

### Modelos de Machine learning treinados

Além da API disponibilizamos o notebook e os dados que foram usados e também os modelos treinados serializados, segue as abordagens de machine learning usadas, vale destacar que por conta dos dados serem muito poucos e precisarmos de mais variavies de entrada não é só isso que aplicamos em um cenario do mundo real e por conta disso esse projeto tinha mais como objetivo apresentar um MVP:

- XGBOOST
- LIGHTGBM
- CATBOOST
- REGRESSÃO LOGISTICA
- KNN
- RANDOM FOREST
- SVM
- NAIVE BAYES

### Executar localmente a API

Dentro do diretorio src execute o comando:

```bash
uvicorn server:app --reload
```

### Em seguida pode acessar a documentação da API em http://127.0.0.1:8000/docs

E em seguida testar os endpoits de gerar classificação, buscar classificações por nome e listar todas as classificações já realizadas.

![Alt Text](https://github.com/Douglas-cc/credit_risk_api/blob/main/2022-05-04%2020-52-07.gif)

### ideias Futuras 
- Salvar os modelos com MLFLOW e fazer controle de versão

