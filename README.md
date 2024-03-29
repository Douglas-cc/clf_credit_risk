<div align="center">

# Automatic Credit Risk Classification System
![Alt Text](https://raw.githubusercontent.com/Douglas-cc/credit_risk_api/main/frontend/assets/cap-youtube.png)
## ⭐  Quick Start  ⭐

</div>


## 🎯 Objectives

The system aims to classify the risk of granting bank credit to a customer. Essentially, the user provides input data, and the system returns whether there is a risk or not in granting bank credit to that customer. Additionally, the API has endpoints where we can save the results in a SQL database, list all classifications, and search for classifications already performed by name.

## Project Stages

**1. Problem Definition:**
   - Identify the business problem that Machine Learning needs to solve.
   - Define project objectives and success criteria.
   - Understand the problem context and stakeholder requirements.

**2. Data Collection:**
   - Gather the necessary data for training and testing the model.
   - Perform initial data analysis to assess data quality and relevance.
   - Handle missing data, outliers, and other anomalies.

**3. Data Preprocessing:**
   - Normalize or standardize data if necessary.
   - Encode categorical variables.
   - Split data into training, validation, and test sets.

**4. Feature Engineering:**
   - Create relevant features for the problem.
   - Select the most important features.
   - Perform data transformations if needed.

**5. Model Selection:**
   - Choose appropriate Machine Learning algorithms for the problem.
   - Consider different models and approaches.
   - Split the training data into subsets for model training and validation.

**6. Model Training:**
   - Train the model using the training data.
   - Tune hyperparameters to optimize performance.
   - Validate the model using the validation data.


**7. Deployment:**
   - Implement the model in a production environment.
   - Monitor the model's performance in production and make adjustments as needed.

## 📝 Description of Input Variables

- name: customer's name
- loan: income commitment
- income: income
- age: age
- date: date and time of classification

## 📈 Machine Learning Model Techniques Used

Our REST API was created in FastAPI to consume trained machine learning models that were saved in serialized .pkl files. However, it is worth noting that our data is sparse in information, and in real life, we would have many other features to explore and train, which gives the model the power to generalize. We could also apply feature engineering techniques. However, this project aimed to explore the end-to-end design process as much as possible. In essence, we counted on an MVP. Below are some models explored, as you can see in our notebook:

- Gradient Boost Models
- LOGISTIC REGRESSION
- KNN
- RANDOM FOREST
- SVM
- NAIVE BAYES

## 🛠️ Technologies Used

- Python
- Streamlit
- Docker
- FastAPI
- Alembic
- Scikit-learn 
- XGBOOST
- LIGHTGBM
- CATBOOST

## ⚙️ Installation

```bash
pip install virtualenv
python3.11 -m virtualenv .venv --python=python3.11
source .venv/bin/activate
```
Or with docker-compose: 

```bash
docker compose up 
```

### Run Frontend and API Locally
Inside the app directory, execute the command to start the API:

```bash
uvicorn server:app --reload
```
Inside the frontend directory, execute the command:

```bash
streamlit run app.py
```
OUTPUT: 
  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.103:8501


Inside the src directory, execute the command:

```bash
uvicorn server:app --reload
```

<div align="center">

## 📺 SOLUTION DEMONSTRATION VIDEO
![Alt Text](https://raw.githubusercontent.com/Douglas-cc/credit_risk_api/main/frontend/assets/cap2.png)](https://youtu.be/4zGlipi8SW0)

</div>

<div align="center">

### API Documentation and Endpoints
And then test the endpoints to generate classification, search for classifications by name, and list all classifications already performed.
![Alt Text](https://raw.githubusercontent.com/Douglas-cc/credit_risk_api/main/frontend/assets/doc_api.gif)

</div>
