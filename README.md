# Plant Disease Detection using CNN 🌿

This project implements a **Convolutional Neural Network (CNN)** to automatically detect plant diseases from leaf images.

The model is trained on image data of plant leaves and is capable of classifying diseases with high accuracy. This solution can help farmers and agricultural organizations **identify diseases early and reduce crop loss**.

---

# Project Background

This project was developed during my undergraduate final year (2023), presented at International Conference on Soft Computing: Theories and Applications (SoCTA 2023), held at Indian Institute of Information Technology (IIIT) Una, Himachal Pradesh, India, during 21–23 December 2023., and published online on 22 August 2024.

It demonstrates the application of **deep learning in agriculture**, specifically for plant disease detection using image classification.

---

# Problem Statement

Plant diseases significantly affect crop yield and quality. Manual detection:

- Requires expertise  
- Is time-consuming  
- Is prone to human error  

This project aims to build an automated system that can:

- Detect plant diseases from leaf images  
- Classify the type of disease  
- Assist in early intervention  

---

# Dataset

The dataset consists of labeled images of plant leaves belonging to different disease categories:

- Tomato – Bacterial Spot  
- Potato – Early Blight  
- Corn – Common Rust  

Each class contains approximately **300 images**, ensuring a balanced dataset.

---

# Tools & Libraries Used

- Python  
- TensorFlow / Keras  
- NumPy  
- Pandas  
- OpenCV  
- Matplotlib  
- Scikit-learn  
- Streamlit (for deployment)

---

# Project Workflow

## 1. Data Loading & Visualization

- Dataset loaded   
- Random samples visualized to understand image distribution  
- Images resized to **256 × 256**

---

## 2. Data Preprocessing

- Converted images to NumPy arrays  
- Normalized pixel values (0–255 → 0–1)  
- Created labels for classification  
- Verified class balance  

---

## 3. Train-Test Split

- 80% Training Data  
- 20% Testing Data  
- Further split into validation set  

---

## 4. Model Architecture (CNN)

The model uses a **Convolutional Neural Network** with the following layers:

- Conv2D (32 filters, ReLU)
- MaxPooling2D
- Conv2D (16 filters, ReLU)
- MaxPooling2D
- Flatten
- Dense (8 neurons, ReLU)
- Output Layer (Softmax – 3 classes)

---

## 5. Model Training

- Loss Function: Categorical Crossentropy  
- Optimizer: Adam  
- Epochs: 50  
- Batch Size: 128  

The model was trained with validation monitoring to track performance.

---

## 6. Model Performance

- **Test Accuracy: ~99.44%**

The model achieved very high accuracy, indicating strong classification capability on the dataset.

---

## 7. Predictions

The model successfully predicts plant diseases on unseen test images.

Example:

- Original Label: Tomato-Bacterial Spot  
- Predicted Label: Tomato-Bacterial Spot  

---

## 8. Model Saving

The trained model is saved as:
plant_disease_model.h5

This allows reuse without retraining.

---

## 9. Visualization

- Training vs Validation Accuracy  
- Loss curves  
- Sample predictions  

---

## 10. Deployment (Streamlit)

A **Streamlit web application** was developed to:

- Upload plant leaf images  
- Predict disease in real time  
- Provide an easy-to-use interface  

---

# Project Structure

```
Plant-Disease-Detection-CNN
│
├── Dataset
│   ├── Corn_(maize)___Common_rust_
│   ├── Potato___Early_blight
│   ├── Tomato___Bacterial_spot
│
├── Conference certificate
│   └── SoCTA certificate of appreciation.pdf
│
├── Streamlit
│   ├── main_app.py
|   ├── plant_disease_model.h5
│   ├── requirements.txt
│   └── Random images for testing
│
├── Conference paper
|   ├── Pre Publishing Version_Automated Plant disease detection CNN for corn maize tomato and potato.pdf
│   └── Conference paper link.pdf   
│
└── README.md
```

## Running the Streamlit Application

Follow the steps below to run the Plant Disease Detection application locally.

Navigate to the Streamlit Folder

Open Anaconda Prompt and move to the project directory.

```bash
cd /path/to/your/project/Streamlit
conda create -n plant_env python=3.10 -y
conda activate plant_env
pip install -r requirements.txt
streamlit run main_app.py
```
Once the app starts, Streamlit will provide a local URL.
Open the link in your browser to use the application.

# Application Workflow
- Upload a plant leaf image.
- The image is processed using OpenCV.
- The trained CNN model (plant_disease_model.h5) predicts the disease.
- The application displays the predicted plant disease.

# Supported Plant Diseases

## The model can detect diseases in the following crops:
- Tomato – Bacterial Spot
- Potato – Early Blight
- Corn (Maize) – Common Rust

# Future Improvements

## Possible enhancements to this project include:
- Expanding the dataset to include more plant species
- Deploying the application on cloud platforms
- Improving model accuracy using transfer learning
- Building a mobile application for farmers
