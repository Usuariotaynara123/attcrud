import streamlit as st

import controller.cliente as cliente

def inserir():
    st.title('Tabela AlunEs')
    turno = ['Vespertino', 'Matutino']
    
    
    with st.form(key='insert'):
        input_name = st.text_input(label='Insira o nome:')
        input_age = st.number_input(label='Insira a idade', format='%d', step=1)
        input_turno = st.selectbox(label='Insira a Turno', options=turno)
        input_matrícula = st.number_input(label='Insira sua matrícula',format='%d', step=1)
        input_periodo =st.number_input (label='Insira o seu periodo',  format='%d', step=1)
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.incluir(input_name, input_age, input_turno,input_matrícula,input_periodo)
            st.success('Aluno cadastrado com sucesso')