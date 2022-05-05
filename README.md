# API RISCO DE CRÉDITO

### objetivos

API tem como objetivo classificar se conseder credito bancario ao um cliente é arriscado ou não em resumo quando API retornar o valor de 1 siginifica que é arriscado dar credito ao cliente se for 0 não possui risco. Além disso podemos salvar os resultados em um banco de dados SQL, listar todas as classificações e pesquisar classificações por nome.

### Descrição das variaveis de entrada 

- name: nome do cliente
- loan: Comprometimento de renda 
- income: Renda
- age: Idade 
- date: Dia e horario da classificação

### Modelos de Machine learning treinados

Além da API disponibilizamos o notebook com o processo de treinamento do modelo, dados que foram usados e também os modelos treinados serializados, segue as abordagens usadas no notebook

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



