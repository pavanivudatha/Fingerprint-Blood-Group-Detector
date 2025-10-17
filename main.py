import streamlit as st
import home
import predict
import capture

# ---------------------------
# Page Configuration
# ---------------------------
st.set_page_config(
    page_title="Fingerprint Blood Group Detector",
    page_icon="🩸",
    layout="wide"
)

# ---------------------------
# Custom CSS — Beautiful Background + Sidebar
# ---------------------------
st.markdown("""
<style>
    /* ---- Background ---- */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #fff0f5 0%, #ffe4ec 50%, #ffffff 100%);
        font-family: 'Poppins', sans-serif;
        background-attachment: fixed;
        background-size: cover;
    }

    /* Optional: If you want an image background instead of gradient, replace above with:
    background-image: url("https://i.imgur.com/bh6lK0H.jpg");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    */

    /* ---- Sidebar Styling ---- */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 240, 245, 0.95);
        border-right: 2px solid #FFC2D9;
        padding-top: 2rem;
        box-shadow: 4px 0 12px rgba(225, 21, 132, 0.1);
        backdrop-filter: blur(5px);
    }

    /* Sidebar Title */
    [data-testid="stSidebar"] h1 {
        color: #E11584;
        text-align: center;
        font-size: 1.6rem;
        font-weight: 700;
        margin-bottom: 1.5rem;
    }

    /* Navigation Items */
    div[role="radiogroup"] > label {
        display: flex;
        align-items: center;
        background-color: #FFFFFF;
        color: #4F4F4F;
        padding: 0.7rem 1rem;
        margin: 0.3rem 0;
        border-radius: 12px;
        border: 1px solid #FFC2D9;
        transition: all 0.3s ease;
        font-weight: 500;
        cursor: pointer;
        box-shadow: 0 1px 3px rgba(225, 21, 132, 0.08);
    }

    div[role="radiogroup"] > label:hover {
        background-color: #FFC2D9;
        color: #E11584;
        border-color: #E11584;
        transform: translateX(3px);
    }

    /* Active (selected) navigation item */
    div[role="radiogroup"] > label[data-selected="true"] {
        background-color: #E11584 !important;
        color: white !important;
        border-color: #E11584 !important;
        font-weight: 600;
        box-shadow: 0 2px 6px rgba(225, 21, 132, 0.25);
    }

    /* Buttons inside pages */
    .stButton > button {
        background-color: #FFC2D9 !important;
        color: #4F4F4F !important;
        border: 1px solid #FFC2D9 !important;
        border-radius: 10px !important;
        transition: all 0.3s ease;
        font-weight: 500;
    }
    .stButton > button:hover {
        background-color: #E11584 !important;
        color: #FFFFFF !important;
        border-color: #E11584 !important;
        box-shadow: 0 3px 6px rgba(225, 21, 132, 0.3);
    }

    /* Progress Bars */
    [data-testid="stProgressBar"] > div > div {
        background-image: linear-gradient(to right, #FFC2D9, #E11584);
    }

    /* Tabs Styling */
    [data-testid="stTabs"] button[aria-selected="true"] {
        background-color: #FFC2D9;
        color: #E11584 !important;
        font-weight: 600;
    }

    /* Page titles */
    h1, h2, h3, p, li, label {
        color: #4F4F4F;
    }

</style>
""", unsafe_allow_html=True)

# ---------------------------
# Sidebar Navigation
# ---------------------------
st.sidebar.title("🩸 Blood Group Detector")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Home", "🔬 Predict Blood Group", "👆 Capture Fingerprint"],
    index=0,
    label_visibility="collapsed"
)

# ---------------------------
# Routing Logic
# ---------------------------
if page == "🏠 Home":
    home.run()
elif page == "🔬 Predict Blood Group":
    predict.run()
elif page == "👆 Capture Fingerprint":
    capture.run()
