import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input
import numpy as np
from PIL import Image
import base64, io

@st.cache_resource
def load_blood_model():
    return load_model("test/model_final.keras")

def run():
    st.markdown("<h1 style='color:#E11584;'>🔬 Predict Blood Group</h1>", unsafe_allow_html=True)
    st.caption("Upload your fingerprint or paste your Base64 data to predict your blood group using our trained AI model.")

    model = load_blood_model()
    class_labels = ['A+', 'A-', 'AB+', 'AB-', 'B+', 'B-', 'O+', 'O-']

    st.markdown("### Choose your input method:")
    tab1, tab2 = st.tabs(["📁 Upload an Image File", "📋 Paste Scanned Data"])
    image_pil = None

    with tab1:
        st.write("Upload your fingerprint image (BMP, JPG, PNG).")
        uploaded_file = st.file_uploader("", type=["bmp", "jpg", "png"])
        if uploaded_file:
            image_pil = Image.open(uploaded_file).convert('RGB')
            st.image(image_pil, caption="Preview", use_container_width=False, width=250)

    with tab2:
        base64_string = st.text_area("Paste the BMPBase64 string here", height=200)
        predict_button = st.button("Predict from Pasted Data")
        if predict_button and base64_string:
            try:
                image_bytes = base64.b64decode(base64_string)
                image_pil = Image.open(io.BytesIO(image_bytes)).convert('RGB')
                st.image(image_pil, caption="Preview", width=250)
            except Exception:
                st.error("Invalid Base64 string.")

    st.markdown("---")
    st.markdown("### 🩸 Prediction Result")

    if image_pil:
        try:
            image_for_model = image_pil.resize((256, 256))
            img_array = image.img_to_array(image_for_model)
            img_array = np.expand_dims(img_array, axis=0)
            img_array = preprocess_input(img_array)

            prediction = model.predict(img_array)[0]
            predicted_class = class_labels[np.argmax(prediction)]
            confidence = np.max(prediction) * 100

            st.success("✅ Prediction Complete!")
            st.metric(label="Predicted Blood Group", value=predicted_class)
            st.progress(int(confidence))
            st.write(f"**Confidence:** {confidence:.2f}%")
        except Exception as e:
            st.error(f"An error occurred during prediction: {e}")
    else:
        st.info("Upload or paste data to generate a prediction.")
