# Resume Scanning  App

*A Machine Learning-based Resume Classification App using Streamlit*  

## 🚀 Project Overview
This **Resume Screening and Category Prediction App** is a machine learning-powered tool that categorizes resumes based on their content. Users can upload resumes in **PDF, DOCX, or TXT format**, and the app extracts text, cleans it, and predicts the job category using an **SVM (Support Vector Machine) model** trained with **TF-IDF vectorization**.

## ✨ Features
✅ **Upload resumes** (PDF, DOCX, TXT)  
✅ **Extract text** from resumes  
✅ **Clean and preprocess** the extracted text  
✅ **Predict job category** using a pre-trained SVM model  
✅ **User-friendly UI** with Streamlit  

## 🛠 Tech Stack
- **Python** (for backend logic)
- **Streamlit** (for UI development)
- **Scikit-Learn** (for ML modeling)
- **TF-IDF Vectorization** (for text feature extraction)
- **Git & GitHub** (for version control)
- **PyPDF2 & python-docx** (for document text extraction)

## 📌 Installation
Follow these steps to set up the project on your local system:

1️⃣ **Clone the Repository**  
```bash
git clone https://github.com/upadhyayutkarsh2005/Resume-Scanning.git
cd Resume-Scanning
```

2️⃣ **Create a Virtual Environment (Optional but Recommended)**  
```bash
python -m venv myenv
source myenv/bin/activate  # On macOS/Linux
myenv\Scripts\activate    # On Windows
```

3️⃣ **Install Dependencies**  
```bash
pip install -r requirements.txt
```

## 🚀 Usage
1️⃣ **Run the Streamlit App**  
```bash
streamlit run app.py
```
2️⃣ **Upload a Resume** (PDF, DOCX, or TXT)  
3️⃣ **View Extracted Text & Prediction**  
4️⃣ **Check the Predicted Job Category**  

## 🔍 Model Details
- **TF-IDF Vectorization** is used to convert text into numerical features.
- **SVM Model** is trained on a labeled dataset to predict resume categories.
- **Label Encoding** is used to map categories to numerical values.

## 🏗 Project Structure
```
Resume-Scanning/
│── app.py               # Streamlit App Code
│── requirements.txt     # Dependencies
│── clf.pkl             # Trained ML Model (Not included in repo)
│── encoder.pkl         # Label Encoder
│── tfidf.pkl           # TF-IDF Vectorizer
│── resume.ipynb        # Notebook for training the model
│── UpdatedResumeDataSet.csv  # Dataset used
│── .gitignore          # Ignore unnecessary files
```

## ⚠️ Troubleshooting
### Large File Issue (GitHub Push Failure)
If you're facing errors while pushing due to large files (`clf.pkl` exceeding 100MB), use **Git LFS**:
```bash
git lfs install
git lfs track "*.pkl"
git add .gitattributes
```
Then re-add and push the changes:
```bash
git add .
git commit -m "Added LFS tracking for large files"
git push origin master
```

## 📌 To-Do (Future Enhancements)
- [ ] Improve UI with better **CSS styling** ✨
- [ ] Add **more categories** for better predictions 📂
- [ ] Implement **real-time resume feedback** 🔍

## 🤝 Contributing
Feel free to fork this repository and improve the project. Contributions are welcome! 🚀

## 📜 License
This project is **MIT Licensed**. You are free to use, modify, and distribute it.

---
🔗 **GitHub Repository:** [Resume-Scanning](https://github.com/upadhyayutkarsh2005/Resume-Scanning)  
📧 **Contact:** uutkarsh952@gmail.com 
🚀 **Happy Coding!**

