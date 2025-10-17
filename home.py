import streamlit as st

def run():
    st.markdown("<h1 style='color:#E11584; text-align:center;'>Welcome to the Fingerprint Blood Group Detector</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; font-size:18px; color:#555;'>An intelligent AI system to determine your blood group using your fingerprint pattern.</p>", unsafe_allow_html=True)

    st.markdown("---")
    #st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmbYA4x6nTOYjk5JPcUZ0_hKOmlZNpjCVVYQ&s", width=1000)
    st.markdown("""
        ### 💡 How It Works
        1. **👆 Capture Fingerprint** — Use your SecuGen scanner or API service to get your fingerprint data.  
        2. **🔬 Predict Blood Group** — Upload or paste your fingerprint data to let the AI analyze and predict your blood group.  
        3. **📊 Get Results** — Instantly view predictions with confidence levels.

        ---

        ### 🧠 Powered By:
        - Deep Learning (CNN - InceptionV3)
        - TensorFlow / Keras
        - Streamlit for interactive UI
        """)
    
    st.markdown("---")
    st.info("Navigate using the top banner to begin your journey.")
