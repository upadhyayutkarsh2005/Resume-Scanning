import streamlit as st
import pickle
import docx  
import PyPDF2  
import re

# Load pre-trained model and TF-IDF vectorizer
svc_model = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open('encoder.pkl', 'rb'))

# Function to clean resume text
def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape(r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText

# Function to extract text from files
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''.join([page.extract_text() for page in pdf_reader.pages])
    return text

def extract_text_from_docx(file):
    doc = docx.Document(file)
    return '\n'.join([paragraph.text for paragraph in doc.paragraphs])

def extract_text_from_txt(file):
    try:
        return file.read().decode('utf-8')
    except UnicodeDecodeError:
        return file.read().decode('latin-1')

def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        return extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        return extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        return extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")

def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text]).toarray()
    predicted_category = svc_model.predict(vectorized_text)
    return le.inverse_transform(predicted_category)[0]

# Streamlit app layout
def main():
    st.set_page_config(page_title="Resume Category Prediction", page_icon="📄", layout="wide")

    # Enhanced CSS for modern UI
    st.markdown(
        """
        <style>
            /* Gradient Background */
            .stApp {
                background: linear-gradient(to right, #8E2DE2, #4A00E0);
                color: white;
                font-family: 'Poppins', sans-serif;
            }

            /* Title & Headers */
            .stTitle, .stMarkdown {
                color: white !important;
                text-align: center;
            }

            /* Upload Section */
            .stFileUploader {
                border-radius: 15px !important;
                padding: 10px;
                background: rgba(255, 255, 255, 0.2);
                backdrop-filter: blur(10px);
                border: 2px solid rgba(255, 255, 255, 0.3);
                color: white !important;
            }

            /* Extracted Text */
            .stTextArea {
                background: rgba(255, 255, 255, 0.2);
                backdrop-filter: blur(10px);
                border-radius: 10px;
                padding: 10px;
                color: white;
            }

            /* Buttons */
            .stButton>button {
                background: #FF416C;
                color: white;
                border-radius: 8px;
                font-size: 18px;
                font-weight: bold;
                padding: 10px 20px;
                transition: 0.3s ease-in-out;
                border: none;
            }

            .stButton>button:hover {
                background: #FF4B2B;
                transform: scale(1.05);
            }

            /* Prediction Box */
            .prediction-box {
                background: rgba(255, 255, 255, 0.2);
                backdrop-filter: blur(20px);
                padding: 15px;
                border-radius: 12px;
                color: white;
                font-size: 22px;
                font-weight: bold;
                text-align: center;
                box-shadow: 0 4px 10px rgba(255, 255, 255, 0.3);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.title("✨ Resume Screening App ✨")
    st.markdown("🚀 Upload a resume in **PDF, TXT, or DOCX** format and get the predicted job category.")

    uploaded_file = st.file_uploader("📂 Upload a Resume", type=["pdf", "docx", "txt"])

    if uploaded_file is not None:
        try:
            resume_text = handle_file_upload(uploaded_file)
            st.success("✅ Successfully extracted text from the uploaded resume!")

            if st.checkbox("📜 Show Extracted Text", False):
                st.text_area("Extracted Resume Text", resume_text, height=300)

            st.subheader("🔮 Predicted Category")
            category = pred(resume_text)
            st.markdown(f"<div class='prediction-box'>{category}</div>", unsafe_allow_html=True)

        except Exception as e:
            st.error(f"🚨 Error processing the file: {str(e)}")

if __name__ == "__main__":
    main()
