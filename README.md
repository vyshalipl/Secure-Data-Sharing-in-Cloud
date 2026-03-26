# 🔐 Secure Data Sharing in Cloud using ABE
A secure cloud data sharing system using Attribute-Based Encryption (ABE) for fine-grained access control with user and attribute-level revocation.
## 📌 Overview
This project implements a secure cloud storage system where files are encrypted before storage and can only be accessed by users whose attributes match the required policy.
## 🚀 Features

* 🔐 Attribute-Based Encryption (ABE) simulation
* 👥 Fine-grained access control
* 🚫 User-level access revocation
* 🧩 Attribute-based authorization
* ☁️ Secure file storage (local cloud simulation)
* ⚡ Lightweight and efficient encryption

## 🛠️ Tech Stack

* Python
* Flask
* Cryptography (Base64 simulation)
* HTML/CSS

## 📂 Project Structure

secure-cloud-abe/
│
├── app.py
├── abe.py
├── models.py
├── config.py
├── requirements.txt
│
├── storage/
├── templates/
└── static/

## ⚙️ Installation

1. Clone the repository
   git clone https://github.com/vyshalipl/secure-cloud-abe.git

2. Navigate to project
   cd secure-cloud-abe

3. Install dependencies
   pip install -r requirements.txt

4. Run the application
   python app.py

5. Open browser
   http://127.0.0.1:5000

## 🧪 How It Works

### 🔼 Upload

* File is uploaded
* Encrypted using ABE logic
* Stored securely

### 🔽 Download

* User enters username
* System checks attributes
* If matched → file is decrypted
* Else → access denied

## 🔑 Example Access

| User  | Attributes  | Access    |
| ----- | ----------- | --------- |
| admin | HR, Manager | ✅ Allowed |
| user1 | Employee    | ❌ Denied  |

## 🔒 Security Concepts

* Attribute-Based Encryption (ABE)
* Access Control Policies
* Data Confidentiality
* User Revocation

---

## 🚀 Future Enhancements

* Real ABE using Charm Crypto
* AWS Cloud Integration
* Login System (JWT)
* React Frontend

## 👩‍💻 Author

Vyshali 
## 📜 License

This project is for educational purposes.
