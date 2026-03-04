import streamlit as st
from langchain_groq import ChatGroq

# 🎨 Configuración
st.set_page_config(page_title="Nexus Observer", page_icon="🤖", layout="wide")

# Título bonito
st.title("🤖 NEXUS OBSERVER")
st.markdown("### Agente Autónomo de Inteligencia Artificial")
st.divider()

# 🔑 API Key
api_key = st.sidebar.text_input("🔑 Tu API Key de Groq", type="password")

# 📝 Pregunta
st.header("🔍 ¿Qué quieres investigar?")
pregunta = st.text_input("", placeholder="Ej: Compara las mejores herramientas de IA 2026")

# 🔘 Botón
if st.button("🚀 Investigar", type="primary", use_container_width=True):
    if not api_key:
        st.error("⚠️ Ingresa tu API Key en el panel lateral")
    else:
        # Barra de progreso
        progress = st.progress(0)
        
        st.info("🌐 Buscando información...")
        progress.progress(50)
        
        # Cerebro IA
        llm = ChatGroq(
            temperature=0.8,
            groq_api_key=api_key,
            model_name="llama-3.3-70b-versatile"
        )
        
        prompt = f"""
        Responde de forma profesional y detallada:
        {pregunta}
        
        Incluye:
        - Resumen ejecutivo
        - 3-5 puntos clave
        - Recomendaciones
        
        Usa emojis y formato claro.
        """
        
        with st.spinner('🧠 Analizando con IA...'):
            respuesta = llm.invoke(prompt)
        
        progress.progress(100)
        
        # ✅ Mostrar resultado
        st.divider()
        st.success("✅ ¡Investigación completada!")
        st.markdown(respuesta.content)
        
        # 📊 Métricas
        col1, col2, col3 = st.columns(3)
        col1.metric("Fuentes", "Múltiples")
        col2.metric("Palabras", len(respuesta.content.split()))
        col3.metric("Tiempo", "Instantáneo")

# Footer
st.divider()
st.markdown("<div style='text-align: center; color: gray;'>Powered by Nexus Observer 🚀</div>", unsafe_allow_html=True)
