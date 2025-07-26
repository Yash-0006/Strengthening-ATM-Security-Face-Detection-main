# Project Name: **Strengthening ATM Security – Face Recognition Enhancement**

This project strengthens ATM security by integrating face detection and recognition alongside traditional PIN-based authentication. It uses computer vision techniques to verify the user's identity before allowing ATM access, reducing the risk of unauthorized withdrawals.

---

## Table of Contents

1. [Project Setup](#project-setup)  
2. [Technologies Used](#technologies-used)  
3. [Running the Project](#running-the-project)  
4. [Project Structure](#project-structure)  

---

## Project Setup

Ensure the following prerequisites are installed:

- **Python 3.x**
- **OpenCV library**
- **NumPy**
- **(Optional) Tkinter** if GUI is used
- **(Optional) Twilio API credentials** for OTP integration

---

## Technologies Used

- **Language:** Python  
- **Computer Vision:** OpenCV (LBPH / Haar Cascades / DNN)  
- **Database (if used):** MySQL or SQLite  
- **GUI (if applicable):** Tkinter  
- **Optional SMS Verification:** Twilio API

---

## Running the Project

1. **Clone the repository:**

    ```bash
    git clone https://github.com/Yash-0006/Strengthening-ATM-Security-Face-Detection-main.git
    cd Strengthening-ATM-Security-Face-Detection-main
    ```

2. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Train or load the face recognition model (if applicable):**

    ```bash
    python train_model.py
    ```

4. **Run the main application script:**

    ```bash
    python main.py
    ```

5. **Access the application GUI or console interface** and follow prompts for card + PIN + face verification.

---

## Project Structure

```bash
Strengthening-ATM-Security-Face-Detection-main/
├── requirements.txt
├── train_model.py            # for training face recognition
├── main.py                   # primary application script
├── capture_face.py          # captures user face
├── authenticate.py          # face + PIN authentication logic
├── dataset/                  # stored face images for training/testing
├── models/                   # saved trained models (LBPH, CNN, etc.)
└── README.md
```
