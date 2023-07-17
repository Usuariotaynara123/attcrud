import streamlit as st

import controller.cliente as cliente

def deletar():
    st.title('Deletar dados')

    with st.form(key='delete'):
        input_delete= st.number_input(label='Insira sua matrícula',format='%d', step=1)
       
       
        
        buttom_submit = st.form_submit_button('Enviar')
        
        if buttom_submit:
            cliente.deletar(input_delete)
            st.success('Aluno deletado com sucesso')


            