# 🩸 Fingerprint Blood Group Detector

This project is a web application built with Streamlit that uses a Deep Learning model (ResNet34) to predict a person's blood group (A, B, AB, O, positive/negative) from an image of their fingerprint. The application features a custom pink and white theme and provides multiple ways to input a fingerprint for analysis.

-----

## \#\# ✨ Features

  * **Multi-Page Interface:** A clean navigation banner to switch between Home, Prediction, and Capture pages.
  * **Dual Input Methods:**
    1.  Upload a fingerprint image directly from your device.
    2.  Manually capture fingerprint data using the SecuGen WebAPI and paste the resulting Base64 string.
  * **AI-Powered Prediction:** Utilizes a pre-trained TensorFlow/Keras model to analyze the image and predict the blood group.
  * **Custom Theming:** A beautiful pink and white theme applied across all pages and components.

-----

## \#\# 🛠️ Tech Stack

  * **Framework:** Streamlit
  * **Deep Learning:** TensorFlow, Keras
  * **Image Processing:** Pillow
  * **Core Language:** Python

-----

## \#\# 🚀 Setup and Installation

Follow these steps to set up and run the project locally.

### \#\#\# Prerequisites: Install SecuGen WebAPI

For **Method 2 (Manual WebAPI Capture)** to work, you must first download and install the SecuGen WebAPI software on your computer. This allows your browser to communicate with the fingerprint scanner.

1.  **Download:** Go to the official SecuGen developer download page. You may need to register for a free developer account to access the files.

      * **Link:** [**SecuGen webapi Downloads**](https://webapi.secugen.com/)

2.  **Select the Software:** On the download page, find and download the installer for the **"SecuGen WebAPI"**.

3.  **Install:** Run the downloaded installer and follow the on-screen instructions. This will install the necessary drivers and start the local WebAPI service that runs on `https://localhost:8000`.

4.  **Verify:** After installation, ensure your SecuGen device is plugged into your computer. The service should start automatically in the background.

### \#\#\# 1. Clone the Repository

First, clone this repository to your local machine.

```bash
git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name
```

### \#\#\# 2. Create a `requirements.txt` File

Create a file named `requirements.txt` in the main project folder and add the following lines. This file defines the exact packages needed for the project to run correctly.

```
streamlit
numpy==1.19.5
seaborn==0.11.1
matplotlib==3.4.2
tensorflow==2.4.1
pandas==1.2.4
scikit-learn==0.24.2
glob2


```

### \#\#\# 3. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to keep your project's dependencies separate.

```bash
# Create a new environment named 'venv'
python -m venv venv

# Activate the environment
# On Windows:
.\venv\Scripts\activate
# On macOS/Linux:
# source venv/bin/activate
```

### \#\#\# 4. Install Dependencies

With your virtual environment active, install all the required packages from your `requirements.txt` file.

```bash
# First, upgrade pip
python -m pip install --upgrade pip

# Then, install the packages
pip install -r requirements.txt
```


# 🩸 Fingerprint Blood Group Detector

This project uses deep learning and image processing to **detect a person’s blood group using a fingerprint image**.  
It leverages a **Convolutional Neural Network (CNN)** based on the **InceptionV3** architecture for classification.

---

## 🧠 Model Training Details

### 🧩 Overview
The model was trained using **transfer learning** with the InceptionV3 architecture to classify fingerprint patterns into 8 blood group categories.

### 🧬 Training Pipeline

1. **Data Collection**
   - A custom dataset of fingerprint images labeled with blood groups (A+, A−, B+, B−, AB+, AB−, O+, O−) was used.
   - Images were captured using a fingerprint scanner and augmented for variety.

2. **Preprocessing**
   - Images resized to **224×224 pixels**
   - Normalized pixel values between **0 and 1**
   - Applied **rotation**, **zoom**, and **brightness adjustments** to improve generalization

3. **Model Architecture**
   - **Base Model:** InceptionV3 (pre-trained on ImageNet)
   - **Added Layers:**
     - GlobalAveragePooling2D
     - Dense(512, activation='relu')
     - Dropout(0.5)
     - Dense(8, activation='softmax')
   - **Optimizer:** Adam  
   - **Learning Rate:** 0.0001  
   - **Loss Function:** Categorical Crossentropy  
   - **Epochs:** 25–50  
   - **Batch Size:** 32  
   - **Validation Accuracy:** ≈ 95%

4. **Output Files**
   - `model_final.keras` → Trained model in TensorFlow Keras format  
   - `model_compatible.h5` → Backward-compatible version  
   - `sgfplib.dll` → Native fingerprint capture driver for Windows systems

---

## 📁 Dataset Information

> **Dataset Link:**  
> [Fingerprint Blood Group Dataset (Kaggle)]([https://www.kaggle.com/datasets/](https://www.kaggle.com/datasets/rajumavinmar/finger-print-based-blood-group-dataset))  

If you built your own dataset, mention this:
> The dataset was **self-collected** using a SecuGen fingerprint sensor. Each blood group has a balanced set of samples.  
> Data augmentation techniques (flipping, rotation, and zoom) were applied to enhance dataset diversity.

### 🗂️ Dataset Structure
dataset/
├── A+/
├── A-/
├── B+/
├── B-/
├── AB+/
├── AB-/
├── O+/
└── O-/


---

## ⚙️ Re-Training the Model

If you wish to retrain the model from scratch:

```bash
python train.py




### \#\#\# 5. Place the Model File

Make sure you have the trained model file, `model_final.keras`, and place it inside the `test` folder. The project structure should look like this:

```
your-repository-name/
├── main.py
├── home.py
├── predict.py
├── capture.py
├── requirements.txt
└── test/
    └── model_final.keras
```

-----

## \#\# ▶️ How to Run the App

With your virtual environment active (`(venv)` should be at the start of your terminal prompt), run the following command from the main project directory:

```bash
python -m streamlit run main.py
```

The application should now be running and accessible in your web browser, usually at `http://localhost:8501`.

-----

## \#\# 📖 How to Use the App

After running the app, navigate to the **🔬 Predict Blood Group** page. You have two options for prediction.

### \#\#\# Method 1: Upload an Image File

1.  Select the **"📁 Upload an Image File"** tab.
2.  Click the "Browse files" button and select a fingerprint image (`.jpg`, `.png`, or `.bmp`) from your device.
3.  The prediction will appear automatically.

### \#\#\# Method 2: Manual WebAPI Capture (for SecuGen devices)

1.  Make sure you have installed the **SecuGen WebAPI** software (see prerequisites above) and that your device is plugged in.
2.  Navigate to the **"👆 Capture Fingerprint"** page in the app.
3.  Follow the instructions to open the SecuGen link (`https://localhost:8000/SGIFPCapture`). You may need to accept a security warning in your browser the first time.
4.  Open the browser's developer console (F12), copy the provided JavaScript code, paste it into the console, and press Enter.
5.  Touch your fingerprint scanner when prompted. The Base64 string will be automatically copied to your clipboard.
6.  Go back to the **"🔬 Predict Blood Group"** page in the app.
7.  Select the **"📋 Paste Scanned Data"** tab.
8.  Paste (`Ctrl+V`) the long string into the text box.
9.  Click the **"Predict from Pasted Data"** button.
10. The prediction will appear.
