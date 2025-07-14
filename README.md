<<<<<<< HEAD

# 🔥 Forest Fire Detection Using AI

This project detects forest fires using Convolutional Neural Networks (CNN) and performs real-time fire detection via a mobile camera. It can optionally send email alerts when fire is detected and includes geolocation information.

## 📁 Project Structure

```
Forest-Fire-Detection-AI/
├── model_training/
│   ├── Forest_Fire_Detection_Train_Test_model.ipynb      # CNN model training notebook (Google Colab)           
├── live_detection/
│   ├── fire_detection_live.py      # Real-time fire detection using webcam
├── requirements.txt                # Python package dependencies
├── README.md                       # Project overview and usage
└── .gitignore                      # Files to ignore in GitHub
```

## 🧠 Model Details

- **Model**: Custom CNN 
- **Input size**: 224x224 pixels RGB
- **Output**: Binary classification (Fire / No Fire)

## 🏗️ How to Use

### 🔹 1. Train the Model (Colab)
Run `Forest_Fire_Detection_Train_Test_model` in Google Colab to train the model on fire and non-fire images. You can save the model as `.keras`.

### 📱 2. Using Mobile as a Webcam

This project also supports using a mobile phone as a webcam using the **IP Webcam** app (Android):

1. Install the IP Webcam app from the [Play Store](https://play.google.com/store/apps/details?id=com.pas.webcam).
2. Connect your mobile and laptop to the **same Wi-Fi or mobile hotspot**.
3. Open the app, scroll down, and tap "Start Server".
4. Note the streaming URL (e.g., `http://192.168.0.101:8080/video`).
5. In `fire_detection_live.py`, replace the webcam line:

```python
cap = cv2.VideoCapture("http://192.168.0.101:8080/video")


### 🔹 3. Real-Time Detection (VS Code or Local Python)
Use `nforest_fire_detection.py` to detect fire from your mobile camera.

```bash
python nforest_fire_detection.py
```

Press `q` to quit the webcam stream.

### 🔥 Download Pre-trained Model

To use the real-time fire detection without training, download the pre-trained model from the link below:

👉 [Download fire_model.keras](https://drive.google.com/file/d/15JtREgJEkg1ZKANT9VjiaKsKp4-RKzAQ/view?usp=sharing)

Place the downloaded file in the project folder before running `live_detection.py`.


## 📦 Installation

```bash
pip install -r requirements.txt
```

## 📥 Dataset

- [Forest Fire Dataset (Kaggle)](https://www.kaggle.com/datasets/alik05/forest-fire-dataset)
- You can also use your own dataset with two folders: `Fire/` and `Non-Fire/`

## ✅ Requirements

- TensorFlow 2.x
- OpenCV
- NumPy
- Matplotlib

(Install via `requirements.txt`)


## 🔐 Notes

- Don't upload large datasets to GitHub. Use links instead.
- Store sensitive credentials (like email passwords) securely.

## 👨‍💻 Author

VENKAT RAMANAN R  
B.Tech ECE, VIT-AP University  
Edunet-Microsoft AI Internship Project

## 📃 License

This project is open-source under the MIT License.
=======
# Forest-Fire-Detection-AI
🔥 AI-based forest fire detection system using CNN and real-time webcam monitoring with email alerts
>>>>>>> 9d1a01909a67ae67aa827c7eb83bf5252d045441
