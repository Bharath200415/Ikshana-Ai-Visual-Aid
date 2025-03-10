import google.generativeai as genai
import speech_recognition as sr
import cv2
import itertools
import sys
import time
import base64
import threading
import tempfile
import pyttsx3 
import speech_recognition as sr

genai.configure(api_key="YOUR KEY")
TTSengine = pyttsx3.init()

def speak_text(text):
    """Function to read the text aloud."""
    TTSengine.say(text)
    TTSengine.runAndWait()


def animation(message, stop_event):
    
    for frame in itertools.cycle([f"{message}.", f"{message}..", f"{message}..."]):
        if stop_event.is_set():
            break
        sys.stdout.write(f"\r{frame}")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\r")


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        stop_event = threading.Event()
        animation_thread = threading.Thread(target=animation, args=("Listening", stop_event))
        animation_thread.start()

        try:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            stop_event.set()
            animation_thread.join()

            text = recognizer.recognize_google(audio)
            print(f"\nYou said: {text}")
            return text

        except sr.UnknownValueError:
            print("\nSorry, I could not understand your speech. Please try again.")
            stop_event.set()
            animation_thread.join()
            return None
        except sr.RequestError as e:
            print(f"\nCould not request results; {e}")
            stop_event.set()
            animation_thread.join()
            return None

def capture_image():
    """Capture an image using the webcam."""
    cap = cv2.VideoCapture(0)  # 0 is the webcam index
    if not cap.isOpened():
        print("Error: Could not open the webcam.")
        return None

    print("Press 'Space' to capture the image or 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # Displaying the stream
        cv2.imshow("Capture Image", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord(' '):  # Space key to capture
            with tempfile.NamedTemporaryFile(suffix=".jpg", delete=False) as temp_file:
                image_path = temp_file.name
                cv2.imwrite(image_path, frame)
                print(f"Image captured and saved at: {image_path}")
                cap.release()
                cv2.destroyAllWindows()
                return image_path
        elif key == ord('q'):  #'q' key to quit
            print("Exiting image capture.")
            break

    cap.release()
    cv2.destroyAllWindows()
    return None

def process_and_send_image():
    """Capture an image and process it using Generative AI."""
    image_path = capture_image()  #Capturing image
    if image_path is None:
        return

    prompt = recognize_speech()
    if not prompt:
        print("No valid question provided. Exiting image processing.")
        return

    try:
        # Reading the captured image and ENCODING it as Base64
        with open(image_path, "rb") as img_file:
            image_data = base64.b64encode(img_file.read()).decode("utf-8")

        model = genai.GenerativeModel(model_name="gemini-1.5-pro")

        # CREATING inputs for the API calls
        inputs = [
            {"mime_type": "image/jpeg", "data": image_data},  #Image input
            prompt  # SPEECH PROMPT
        ]

        response = model.generate_content(inputs)

        # Displaying the generated response
        if response and hasattr(response, 'text'):
            print("Generated Caption:\n", response.text)
            speak_text(response.text)
            return response.text
        else:
            print("Error: No response text generated.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    """Main function for user interaction."""
    while True:
        print("\nChoose an action:")
        print("1. Capture and process an image")
        #print("2. Ask a question")
        print("2. Exit")

        choice = input("Enter your choice (1/2): ").strip()
        if choice == "1":
            process_and_send_image()

            
        elif choice == "2":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
