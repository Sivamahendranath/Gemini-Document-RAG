# DocuGenius Pro

## 📄 Transform Documents into Intelligent Insights

DocuGenius Pro is a Streamlit-based AI-powered document processing application that extracts insights from various document formats, including Text, PDF, CSV, and Web URLs.

---

## 🚀 Features

- 📤 **Multi-Format Document Processing**
  - Text, PDFs, CSVs, and Web URLs
- 🧠 **AI-Powered Analysis**
  - Uses Gemini API for smart document insights
- 📊 **Data Visualization**
  - Graphs and statistics for CSV processing
- 🔎 **Named Entity Recognition (NER)**
  - Extracts key entities and attributes
- 📚 **Query-Based Analysis**
  - Ask questions and get AI-powered responses
- 🎨 **Customizable Themes**
  - Dark, Light, Blue, and Green modes
- 📥 **Export Analysis History**
  - Supports CSV, JSON, and PDF report generation

---

## 🛠 Installation

### Prerequisites
- Python 3.8+
- Virtual Environment (Recommended)
- API Key for Gemini AI

### Setup
```sh
# Clone the repository
git clone https://github.com/your-repo/docugenius-pro.git
cd docugenius-pro

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt
```

---

## 🔑 Configuration

1. Set up your **Gemini AI API Key** in the `.env` file:
   ```sh
   GEMINI_API_KEY=your_api_key_here
   ```
2. Run the application:
   ```sh
   streamlit run app.py
   ```

---

## 🖥️ Usage

1. Upload a document (Text, PDF, CSV, or URL)
2. Select processing mode (Extract, Analyze, Visualize)
3. Query the document using AI-powered insights
4. Export results in CSV, JSON, or PDF format

---

## 🏗️ Project Structure
```
📂 docugenius-pro
├── 📄 app.py            # Main application file
├── 📄 theme_manager.py  # Theme customization module
├── 📄 requirements.txt  # Dependencies
├── 📄 .env              # API Key configuration
├── 📂 assets/           # Static assets (logos, images)
├── 📂 modules/          # Processing modules (PDF, CSV, URL, Text)
└── 📂 exports/          # Exported reports and data
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a new branch (`feature/your-feature`)
3. Commit your changes (`git commit -m 'Add new feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📝 License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## 🌟 Acknowledgments

- **Streamlit** - Interactive UI framework
- **Google Gemini API** - AI-powered insights
- **Plotly** - Data visualization

### ⭐ Star this repo if you find it useful!

