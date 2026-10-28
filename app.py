import streamlit as st
from screens import login, cadastro_morador, cadastro_tecnico, cadastro_gestor

# Configuração da página
st.set_page_config(page_title="Sistema de Chamados", page_icon="🛠️", layout="centered")

# Inicializa o estado da sessão para controle de navegação
if 'pagina' not in st.session_state:
    st.session_state['pagina'] = 'login'

def main():
    if st.session_state['pagina'] == 'login':
        login.render()
    elif st.session_state['pagina'] == 'cadastro_morador':
        cadastro_morador.render()
    elif st.session_state['pagina'] == 'cadastro_tecnico':
        cadastro_tecnico.render()
    elif st.session_state['pagina'] == 'cadastro_gestor':
        cadastro_gestor.render()

if __name__ == "__main__":
    main()