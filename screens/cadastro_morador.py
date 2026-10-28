import streamlit as st

def render():
    if st.button("← Voltar para o Login"):
        st.session_state['pagina'] = 'login'
        st.rerun()

    st.subheader("FORMULÁRIO DE CADASTRO")
    st.title("Preencha os dados abaixo")
    st.write("Todos os campos são obrigatórios para concluir o cadastro.")
    
    with st.form("form_morador"):
        st.subheader("Dados pessoais")
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.text_input("Nome completo", placeholder="Digite seu nome completo")
        with col2:
            st.text_input("E-mail", placeholder="Digite seu e-mail")
        with col3:
            st.text_input("CPF", placeholder="000.000.000-00")
        
        st.subheader("Endereço")
        col1, col2 = st.columns([1, 3])
        with col1:
            st.text_input("CEP", placeholder="00000-000")
        with col2:
            st.text_input("Rua", placeholder="Nome da rua")
            
        col1, col2 = st.columns([1, 3])
        with col1:
            st.text_input("N°", placeholder="000")
        with col2:
            st.text_input("Complemento", placeholder="Apto, bloco, etc.")
            
        col1, col2, col3 = st.columns([2, 2, 1])
        with col1:
            st.text_input("Bairro", placeholder="Nome do bairro")
        with col2:
            st.text_input("Cidade", placeholder="Nome da cidade")
        with col3:
            st.text_input("UF", placeholder="Sigla do estado")
            
        st.subheader("Senha")
        col1, col2 = st.columns(2)
        with col1:
            st.text_input("Crie sua senha", type="password", placeholder="Digite a senha")
        with col2:
            st.text_input("Repita a senha", type="password", placeholder="Digite a senha novamente")
            
        st.form_submit_button("Cadastrar", use_container_width=True, type="primary")