# Ikshana - AI-Powered Visual Aid

## 🌟 Introduction
**Ikshana** is an AI-integrated assistive technology designed for visually impaired individuals. It utilizes a webcam to capture real-world images, analyze text within them, and read aloud the translated content using advanced AI models. 

## 🛠️ Features
- 📷 **Real-time image capture** via webcam
- 🧠 **AI-based text detection & translation** from various languages
- 🔊 **Text-to-Speech (TTS) integration** for spoken output
- ⚡ **Lightweight and efficient** implementation using modern AI libraries

## 🚀 Tech Stack
- **Programming Language:** Python
- **Frameworks/Libraries:** OpenCV, Tesseract OCR, SpeechRecognition, gTTS, Flask
- **AI Model:** ChatGPT for natural language processing

## 🔧 Installation & Setup
1. Clone the repository & follow the below mentioned steps:
   ```bash
   git clone https://github.com/yourusername/ikshana.git
   cd ikshana
2. Install dependencies:
   ```bash
   pip3 install -r requirements.txt
3️. Set Up API Keys
👉 Google Gemini API Key (For Image Processing)
   Go to Google AI Studio and sign in.
   Navigate to the API Keys section.
   Generate a new API key.
   Copy the API key and insert it into the genai.configure(api_key="YOUR_API_KEY") line in Main.py.
   
   
📷 Usage
Start the application and allow webcam access.
Position text in front of the camera.
The AI detects, translates (if needed), and reads aloud the text.
💡 Future Enhancements
🔍 Improved text detection accuracy
🌎 Support for more languages and dialects
📡 Integration with IoT devices for standalone operation
🤝 Contributing
Contributions are welcome! Feel free to fork the repository, submit pull requests, or suggest improvements.

