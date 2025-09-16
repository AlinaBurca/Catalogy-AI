# 🐾 Catology: AI-Powered Cat Breed Identification

**Catology** is an AI-driven system designed to identify a cat’s breed based on textual and numerical attributes.  
It automates the pipeline from **raw survey data → preprocessing → machine learning → AI-generated summaries**, delivering both **breed predictions** and **human-readable insights**.

---

## ✨ Features

### 📊 Dataset Augmentation & Translation
- Translates **French entities** into English.  
- Expands dataset using **SMOTE** to balance breed classes.  

### 🧠 Natural Language Processing (NLP)
- Parses survey text to extract relevant cat attributes.  
- Generates concise **breed summaries** in plain English.  
- Enables **natural-language comparisons** between breeds.  

### 🔧 Data Preprocessing & Validation
- Handles **missing values, duplicates, and inconsistent entries**.  
- Converts categorical fields into numeric codes.  
- Reports **instance counts per breed** and unique attribute values.  

### 📈 Statistical Analysis & Visualization
- Generates **histograms, box plots, and distribution graphs** for each attribute.  
- Identifies **correlations** between attributes and breeds.  

### 🤖 Machine Learning Models
- Encodes categorical & textual features numerically.  
- Trains and evaluates **neural networks & tree-based models** for breed prediction.  
- Reports key metrics: **precision, recall, F1-score, confusion matrices**.  

### 💡 AI-Driven Description & Comparison
- Uses **Hugging Face** / **Google Gemini APIs** for breed descriptions.  
- Produces **side-by-side breed comparisons** in natural language.  

---

## 🛠️ Technologies & Tools

- **Language:** Python 3.8+  
- **Data Processing:** pandas, numpy, openpyxl  
- **NLP & Translation:** NLTK, spaCy, Hugging Face Transformers, MarianMT  
- **Machine Learning:** scikit-learn, imbalanced-learn, PyTorch  
- **Visualization:** matplotlib, seaborn  

---

## 📊 Results & Interpretation

- **Data Insights:** Key breed traits and attribute distributions.  
- **Model Performance:** Classification reports & confusion matrices.  
- **Visualization:** Automatically generated plots showcasing data patterns.  
- **AI Summaries:** Plain-English breed descriptions and comparisons.  

---

## 🚀 Getting Started

```bash
# Clone repository
git clone https://github.com/your-username/catology.git
cd catology

# Install dependencies
pip install -r requirements.txt

# Run preprocessing
python preprocess.py

# Train model
python train.py

# Generate AI summaries
python generate_summary.py
