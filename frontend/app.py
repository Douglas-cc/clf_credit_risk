import requests
import streamlit as st

router = "http://backend:8000/classified"

st.image('assets/cartão.jpeg')
st.title('Classificação de Risco de Crédito')
st.subheader('Insira seus dados pessoais:')

name = st.text_input('Nome:')        
age = st.number_input('Idade:')
loan = st.number_input('Comprometimento de Renda Mensal:')
income = st.number_input('Renda Mensal:')

endpoint = {
    "name": name,
	"income": income,
	"age": age,
	"loan": loan
}

if st.button('predict'):  
    res = requests.post(router, json = endpoint)
  
    if float(res.text) == 0.0:
        st.write('Solicitacão de crédito aprovada')
        st.image('assets/cristiano-ronaldo-ronaldo-feliz.gif')
    if float(res.text) == 1.0:
        st.write('Solicitacão de não foi crédito aprovada')
        st.image('assets/ronaldo-cr7-triste.gif')