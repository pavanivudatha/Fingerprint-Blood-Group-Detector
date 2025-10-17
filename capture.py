import streamlit as st

def run():
    st.markdown("<h1 style='color:#E11584;'>👆 Capture Fingerprint</h1>", unsafe_allow_html=True)
    st.caption("Follow the steps below to capture fingerprint data from your SecuGen device.")

    st.info("Ensure your SecuGen device is plugged in and the WebAPI service is running before you begin.")

    st.markdown("### Step 1️⃣: Open the Capture Link")
    st.write("This will open the SecuGen WebAPI service on your system.")
    st.link_button("Open SecuGen Capture Page", "https://localhost:8000/SGIFPCapture", type="primary")

    st.markdown("---")
    st.markdown("### Step 2️⃣: Run the JavaScript Code in Console")
    st.write("After opening the page, press **F12 → Console → Paste the code below**:")
    
    js_code = """
async function getFingerprintData() {
  const SECUGEN_API_URL = "https://localhost:8000/SGIFPCapture";
  try {
    const response = await fetch(SECUGEN_API_URL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ "Timeout": 10000 })
    });
    const data = await response.json();
    if (data.ErrorCode === 0 && data.BMPBase64) {
      navigator.clipboard.writeText(data.BMPBase64);
      console.log("✅ Capture Successful! Base64 copied to clipboard.");
    } else {
      console.error(`❌ Capture Failed: ${data.ErrorDesc}`);
    }
  } catch (error) {
    console.error("❌ Connection Failed. Is the SecuGen service running?", error);
  }
}
getFingerprintData();
"""
    st.code(js_code, language='javascript')

    st.markdown("---")
    st.markdown("### Step 3️⃣: Paste the Data in Prediction Page")
    st.write("Go to **🔬 Predict Blood Group → Paste Scanned Data tab**, and paste your Base64 string there.")
