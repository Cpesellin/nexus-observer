import streamlit as st
from groq import Groq

# 🎨 Configuración de la página
st.set_page_config(page_title="Nexus Observer", page_icon="🤖", layout="wide")

# Título
st.title("🤖 NEXUS OBSERVER")
st.markdown("### Agente Autónomo de Inteligencia Artificial")
st.divider()

# 🔑 API Key en barra lateral
api_key = st.sidebar.text_input("🔑 Tu API Key de Groq", type="password")

# 📝 Pregunta del usuario
st.header("🔍 ¿Qué quieres investigar?")
pregunta = st.text_input("", placeholder="Ej: Compara las mejores herramientas de IA 2026")

# 🔘 Botón de acción
if st.button("🚀 Investigar", type="primary", use_container_width=True):
    
    if not api_key:
        st.error("⚠️ Por favor ingresa tu API Key en el panel lateral")
    
    else:
        # Barra de progreso
        progress_bar = st.progress(0)
        status = st.empty()
        
        try:
            # Paso 1: Conectar con Groq
            status.text("🔗 Conectando con IA...")
            progress_bar.progress(25)
            
            client = Groq(api_key=api_key)
            
            # Paso 2: Preparar la pregunta
            status.text("🧠 Pensando...")
            progress_bar.progress(50)
            
            prompt = f"""
            Eres un experto en tecnología. Responde de forma clara y profesional:
            
            {pregunta}
            
            Incluye:
            - Un resumen ejecutivo
            - 3-5 puntos clave con emojis
            - Recomendaciones prácticas
            
            Formato: Usa markdown, negritas y emojis para que sea fácil de leer.
            """
            
            # Paso 3: Obtener respuesta
            status.text("✨ Generando respuesta...")
            progress_bar.progress(75)
            
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=2000
            )
            
            respuesta = response.choices[0].message.content
            
            # Paso 4: Mostrar resultado
            progress_bar.progress(100)
            status.text("✅ ¡Listo!")
            
            st.divider()
            st.success("🎉 Investigación completada")
            st.markdown(respuesta)
            
            # 📊 Métricas bonitas
            col1, col2, col3 = st.columns(3)
            col1.metric("⚡ Velocidad", "Instantáneo")
            col2.metric("📝 Palabras", len(respuesta.split()))
            col3.metric("🧠 Modelo", "Llama 3.3")
            
            # 💾 Botón de descarga
            st.divider()
            st.download_button(
                label="📥 Descargar Reporte",
                data=respuesta,
                file_name="reporte_nexus.md",
                mime="text/markdown",
                use_container_width=True
            )
            
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
            st.info("💡 Verifica que tu API Key sea correcta")

# Footer
st.divider()
st.markdown("<div style='text-align: center; color: gray; padding: 20px;'>🤖 Nexus Observer - Powered by Groq</div>", unsafe_allow_html=True)
