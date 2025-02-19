# DocuGenius Pro 
Demo Video Link: https://www.linkedin.com/posts/sivamahendranath-ragimanu-68a94823b_ai-machinelearning-documentprocessing-activity-7297922732371914753-71-o?utm_source=share&utm_medium=member_desktop&rcm=ACoAADvDGcoB0zRF3XGC2XoPR3VSw0RN6dCCCNo

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
# Creating a Gemini API Key in Google AI Studio

To interact with Google's Gemini API, you'll need to generate an API key through Google AI Studio. Follow the steps below to create your API key:

## Prerequisites

- A Google account. If you don't have one, you can create it [here](https://accounts.google.com/).

## Steps to Generate the API Key

1. **Sign In to Google AI Studio**

   - Navigate to the [Google AI Studio](https://aistudio.google.com/).
   - Click on the "Sign In" button at the top right corner and log in with your Google account.

2. **Access the Gemini API Section**

   - Once signed in, locate and click on the "Gemini API" tab or the "Learn more about the Gemini API" button on the homepage.

3. **Initiate API Key Creation**

   - Click on the "Get API key in Google AI Studio" button prominently displayed on the Gemini API page.

4. **Review and Accept Terms**

   - A pop-up will appear prompting you to agree to the Google APIs Terms of Service and Gemini API Additional Terms of Service.
   - Check the required boxes to accept the terms. Optionally, you can subscribe to updates and research participation.
   - Click "Continue" to proceed.

5. **Create the API Key**

   - Choose to create the API key in a new project or select an existing project from your Google Cloud projects.
   - After selection, click on "Create API key."
   - Your new API key will be generated and displayed. **Ensure you copy and store it securely**, as it will not be displayed again.

## Setting Up Your API Key Locally

For security and convenience, it's recommended to store your API key as an environment variable.

### On Linux/macOS (Bash)

1. **Open or Create the Bash Configuration File**

   ```bash
   touch ~/.bashrc
   open ~/.bashrc
   ```

2. **Add the API Key**

   Add the following line to the file:

   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```

3. **Apply the Changes**

   ```bash
   source ~/.bashrc
   ```

### On macOS (Zsh)

1. **Open or Create the Zsh Configuration File**

   ```bash
   touch ~/.zshrc
   open ~/.zshrc
   ```

2. **Add the API Key**

   Add the following line to the file:

   ```bash
   export GEMINI_API_KEY=your_api_key_here
   ```

3. **Apply the Changes**

   ```bash
   source ~/.zshrc
   ```

### On Windows

1. **Access Environment Variables**

   - Search for "Environment Variables" in the system settings.

2. **Create a New User Variable**

   - Click on "New" under "User variables."
   - Set the "Variable Name" to `GEMINI_API_KEY`.
   - Set the "Variable Value" to your API key.
   - Click "OK" to save.

## Important Security Considerations

- **Keep your API key confidential**. Do not share it publicly or include it in source control.
- **Restrict API key usage** to specific IP addresses or referrer URLs to prevent unauthorized access.
- **Regularly rotate your API keys** and update your applications accordingly.

For more detailed information, refer to the [Google AI for Developers documentation](https://ai.google.dev/gemini-api/docs/api-key). 
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

