import streamlit as st

def render():
    st.title("Faça o seu login!")
    st.write("Entre na sua conta e faça a solicitação de onde está o problema.")
    
    # Dropdown de tipo de usuário
    tipo_usuario = st.selectbox("Tipo de usuário", ["Morador", "Técnico", "Gestor"])
    
    # Campos de login
    email = st.text_input("E-mail", placeholder="exemplo@gmail.com")
    senha = st.text_input("Senha", type="password", placeholder="Digite a sua senha")
    
    # Botões
    st.button("Entrar", use_container_width=True, type="primary")
    
    col1, col2 = st.columns(2)
    with col1:
        st.checkbox("Lembrar de mim")
    with col2:
        st.markdown("<div style='text-align: right;'><a href='#'>Esqueci a minha senha</a></div>", unsafe_allow_html=True)
    
    st.markdown("<hr>", unsafe_allow_html=True)
    st.write("Ou entrar com")
    st.button("Google", use_container_width=True, icon="🔍")
    st.button("Apple", use_container_width=True, icon="🍎")
    
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # Lógica para direcionar para a tela de cadastro correta
    st.write("Ainda não tem uma conta?")
    
    if tipo_usuario == "Morador":
        if st.button("Crie sua conta como Morador"):
            st.session_state['pagina'] = 'cadastro_morador'
            st.rerun()
    elif tipo_usuario == "Técnico":
        if st.button("Crie sua conta como Técnico"):
            st.session_state['pagina'] = 'cadastro_tecnico'
            st.rerun()
    elif tipo_usuario == "Gestor":
        if st.button("Crie sua conta como Gestor"):
            st.session_state['pagina'] = 'cadastro_gestor'
            st.rerun()