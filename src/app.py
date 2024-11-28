import streamlit as st
from services.blob_service import upload_blob
from services.credit_card_service import analise_credit_card


def configure_interface():
    st.title("Upload de Arquivo DIO - Desafio 1 - Azure - Validaçao de Cartao de Credito")
    uploaded_file = st.file_uploader("Escolha um arquivo", type=["png", "jpg", "jpeg"])

    if uploaded_file is not None:
        fileName = uploaded_file
        # Enviar para o Blob Storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage")
            credit_card_info = analise_credit_card(blob_url) # Chamar a funçao de detecçao de informaçoes de carta de credito
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Imagem enviada")
    st.write("Resultado da validaçao:")
    if credit_card_info and credit_card_info["card_name"]:
        st.markdown(f"<h1 style='color: green;'>Cartao Valido</h1>", unsafe_allow_html=True)
        st.write(f"Nome do Titular: {credit_card_info['card_name']}")
        st.write(f"Banco Emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de Validade: {credit_card_info['expiry_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>Cartao Invalido</h1>", unsafe_allow_html=True)
        st.write("Este nao e um cartao de credito valido.")

if __name__ == "__main__":
    configure_interface()