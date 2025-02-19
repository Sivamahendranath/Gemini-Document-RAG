import streamlit as st
import PyPDF2
import pandas as pd
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai
import os
import time
import plotly.express as px
import plotly.graph_objs as go
from datetime import datetime
import json
import re
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from dotenv import load_dotenv
from reportlab.lib.units import inch
from theme_manager import ThemeManager

load_dotenv()
# Theme Manager Initialization
theme_manager = ThemeManager()
# Streamlit Page Configuration
st.set_page_config(
    page_title="DocuGenius Pro",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)
# Initialize Session States
def initialize_session_states():
    default_states = {
        'extracted_text': "",
        'processing_status': None,
        'history': [],
        'usage_stats': {
            'total_processed': 0,
            'successful_queries': 0,
            'processing_dates': [],
            'file_types': {'PDF': 0, 'CSV': 0, 'URL': 0, 'Text': 0}
        }
    }
    for key, value in default_states.items():
        if key not in st.session_state:
            st.session_state[key] = value
# Application Header
def render_header():
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1>📄 DocuGenius Pro</h1>
        <p style="font-size: 18px; opacity: 0.8;">Transform Documents into Intelligent Insights</p>
    </div>
    """, unsafe_allow_html=True)
# Sidebar Configuration
def render_sidebar():
    with st.sidebar:
        st.image("https://www.netlabsglobal.com/wp-content/uploads/2020/04/netlabs1-1920x960.jpg", caption="🤖 AI Document Assistant 🧠", use_container_width=True)
        st.markdown("### 🔑 API Configuration")
        api_key = st.text_input("Enter Gemini API Key", type="password")
        if api_key:
            try:
                genai.configure(api_key=api_key)
                st.success("✅ API Key Validated Successfully!")
                os.environ["GEMINI_API_KEY"] = api_key
            except Exception as e:
                st.error("❌ Invalid API Key. Please check and retry.")
        st.markdown("### 📊 Usage Dashboard")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Files Processed", st.session_state.usage_stats['total_processed'])
        with col2:
            st.metric("Successful Queries", st.session_state.usage_stats['successful_queries'])
        file_types = st.session_state.usage_stats['file_types']
        if sum(file_types.values()) > 0:
            fig = px.pie(
                values=list(file_types.values()), 
                names=list(file_types.keys()), 
                title="Document Type Distribution",
                color_discrete_sequence=px.colors.sequential.Viridis
            )
            fig.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                font=dict(color=theme_manager.themes["Dark"]["text_color"]),
                margin=dict(l=10, r=10, t=30, b=10)
            )
            st.plotly_chart(fig, use_container_width=True)
# Text Processing Function
def process_text_input(text_input):
    if text_input:
        with st.spinner("Processing text..."):
            progress_bar = st.progress(0)
            for i in range(100):
                time.sleep(0.01)
                progress_bar.progress(i + 1)
            st.session_state.extracted_text = text_input
            st.session_state.usage_stats['file_types']['Text'] += 1
            st.session_state.usage_stats['total_processed'] += 1
            st.success("✅ Text processed successfully!")
            return True
    return False
# PDF Processing Function
def process_pdf_input(pdf_file):
    if pdf_file:
        with st.spinner("Processing PDF..."):
            try:
                pdf_reader = PyPDF2.PdfReader(pdf_file)
                text = ""
                progress_bar = st.progress(0)
                for i, page in enumerate(pdf_reader.pages):
                    text += page.extract_text() + "\n"
                    progress_bar.progress((i + 1) / len(pdf_reader.pages))
                st.session_state.extracted_text = text
                st.session_state.usage_stats['file_types']['PDF'] += 1
                st.session_state.usage_stats['total_processed'] += 1
                col1, col2, col3 = st.columns(3)
                with col1:
                    st.metric("Pages", len(pdf_reader.pages))
                with col2:
                    st.metric("Words", len(text.split()))
                with col3:
                    st.metric("Characters", len(text))
                st.success("✅ PDF processed successfully!")
                return True
            except Exception as e:
                st.error(f"❌ Error processing PDF: {str(e)}")
    return False
# CSV Processing Function
def process_csv_input(csv_file):
    if csv_file:
        with st.spinner("Processing CSV..."):
            try:
                # Try different CSV parsing options if the default fails
                try:
                    df = pd.read_csv(csv_file)
                except pd.errors.ParserError:
                    # Try with different separator
                    try:
                        df = pd.read_csv(csv_file, sep=';')
                    except:
                        # Try with error handling
                        df = pd.read_csv(csv_file, error_bad_lines=False, warn_bad_lines=True)
                
                st.session_state.extracted_text = df.to_string()
                st.session_state.usage_stats['file_types']['CSV'] += 1
                st.session_state.usage_stats['total_processed'] += 1
                preview_tab, stats_tab, viz_tab = st.tabs(["Preview", "Statistics", "Visualization"])
                with preview_tab:
                    st.dataframe(df.head(), use_container_width=True)
                with stats_tab:
                    st.markdown("#### 📊 Data Statistics")
                    col1, col2 = st.columns(2)
                    with col1:
                        st.metric("Rows", df.shape[0])
                        st.metric("Columns", df.shape[1])
                    with col2:
                        st.metric("Missing Values", df.isna().sum().sum())
                        st.metric("Duplicate Rows", df.duplicated().sum())
                with viz_tab:
                    if df.select_dtypes(include=['float64', 'int64']).columns.any():
                        numeric_col = st.selectbox("Select column for visualization", 
                            df.select_dtypes(include=['float64', 'int64']).columns)
                        fig = px.histogram(df, x=numeric_col)
                        fig.update_layout(
                            paper_bgcolor='rgba(0,0,0,0)',
                            plot_bgcolor='rgba(0,0,0,0)',
                            font=dict(color=theme_manager.themes["Dark"]["text_color"]),
                            margin=dict(l=20, r=20, t=30, b=20)
                        )
                        st.plotly_chart(fig, use_container_width=True)
                st.success("✅ CSV processed successfully!")
                return True
            except Exception as e:
                # Provide a more user-friendly error message
                st.error(f"❌ Error processing CSV: The file appears to be invalid or corrupted. Please check the format and try again.")
                st.info("Try checking for: irregular delimiters, mixed data types, or special characters in your CSV file.")
    return False
# URL Processing Function
def process_url_input(url_input):
    if url_input:
        with st.spinner("Processing URL..."):
            try:
                response = requests.get(url_input)
                soup = BeautifulSoup(response.text, 'html.parser')
                text = " ".join([p.get_text() for p in soup.find_all(['p', 'article', 'div'])])
                st.session_state.extracted_text = text
                st.session_state.usage_stats['file_types']['URL'] += 1
                st.session_state.usage_stats['total_processed'] += 1
                st.success("✅ URL content extracted successfully!")
                with st.expander("📱 Page Preview"):
                    st.markdown(f""" 
                    <iframe src="{url_input}" width="100%" height="400" 
                    style="border: 1px solid #ddd; border-radius: 8px;"> </iframe> 
                    """, unsafe_allow_html=True)
                return True
            except Exception as e:
                st.error(f"❌ Error processing URL: {str(e)}")
    return False
# Document Analysis Function
def analyze_document(api_key, query):
    if not api_key:
        st.warning("⚠️ Please configure your Gemini API Key in the sidebar first!")
        return None
    with st.spinner("🧠 Analyzing document..."):
        try:
            model = genai.GenerativeModel('gemini-1.5-flash-latest')
            prompt = f"""
            Based on the following content, provide a detailed and accurate answer to the question.
            Content: {st.session_state.extracted_text}
            Question: {query}
            Please provide a clear and concise answer based only on the provided content.
            """
            response = model.generate_content(prompt)
            answer = response.text
            # Store in history
            st.session_state.history.append({
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                'query': query,
                'answer': answer,
                'type': st.session_state.input_type
            })
            st.session_state.usage_stats['successful_queries'] += 1
            return answer
        except Exception as e:
            st.error(f"❌ Error during analysis: {str(e)}")
            return None
# Reset Usage Statistics Function
def reset_usage_stats():
    st.session_state.usage_stats = {
        'total_processed': 0,
        'successful_queries': 0,
        'processing_dates': [],
        'file_types': {'PDF': 0, 'CSV': 0, 'URL': 0, 'Text': 0}
    }
    st.session_state.history = []
    st.success("Usage statistics and history have been reset!")
# PDF Report Generation Function
def generate_pdf_report(history, filename="docugenius_history_report.pdf"):
    try:
        doc = SimpleDocTemplate(filename, pagesize=letter)
        elements = []
        styles = getSampleStyleSheet()
        # Define custom styles
        title_style = ParagraphStyle(
            'CustomTitle',
            parent=styles['Title'],
            fontSize=16,
            spaceAfter=20
        )
        heading_style = ParagraphStyle(
            'Heading',
            parent=styles['Heading2'],
            fontSize=14,
            spaceAfter=10
        )
        normal_style = ParagraphStyle(
            'CustomNormal',
            parent=styles['Normal'],
            fontSize=10,
            spaceAfter=5
        )
        # Add title
        elements.append(Paragraph("DocuGenius Pro Analysis History Report", title_style))
        elements.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", normal_style))
        elements.append(Spacer(1, 0.25*inch))       
        # Add summary info
        elements.append(Paragraph("Summary", heading_style))
        elements.append(Paragraph(f"Total Queries: {len(history)}", normal_style))
        file_types = {}
        for entry in history:
            if entry['type'] in file_types:
                file_types[entry['type']] += 1
            else:
                file_types[entry['type']] = 1
        file_type_text = ", ".join([f"{doc_type}: {count}" for doc_type, count in file_types.items()])
        elements.append(Paragraph(f"Document Types: {file_type_text}", normal_style))
        elements.append(Spacer(1, 0.25*inch))
        # Add history entries
        elements.append(Paragraph("Analysis History", heading_style))
        for idx, entry in enumerate(history):
            elements.append(Paragraph(f"Entry #{idx+1} - {entry['timestamp']} ({entry['type']})", heading_style))
            elements.append(Paragraph(f"<b>Query:</b> {entry['query']}", normal_style))
            elements.append(Paragraph(f"<b>Answer:</b> {entry['answer']}", normal_style))
            elements.append(Spacer(1, 0.15*inch))
        # Build and save PDF
        doc.build(elements)
        return filename
    except Exception as e:
        st.error(f"Failed to generate PDF report: {str(e)}")
        return None
# Main Application
def main():
    initialize_session_states()
    render_header()
    tab1, tab2, tab3, tab4 = st.tabs([
        "📤 Document Upload", 
        "🔍 Smart Analysis", 
        "📚 History", 
        "⚙️ Settings"
    ])
    with tab1:
        st.markdown("### 📥 Document Input")
        input_type = st.radio(
            "Choose Document Source", 
            ["Text Input", "PDF Upload", "CSV Upload", "Web URL"],
            horizontal=True
        )
        st.session_state.input_type = input_type
        processing_success = False
        if input_type == "Text Input":
            text_input = st.text_area("Enter Your Text", height=200)
            if st.button("Process Text"):
                processing_success = process_text_input(text_input)
        elif input_type == "PDF Upload":
            pdf_file = st.file_uploader("Drop your PDF here", type=["pdf"])
            if st.button("Process PDF"):
                processing_success = process_pdf_input(pdf_file)
        elif input_type == "CSV Upload":
            csv_file = st.file_uploader("Drop your CSV here", type=["csv"])
            if st.button("Process CSV"):
                processing_success = process_csv_input(csv_file)
        elif input_type == "Web URL":
            url_input = st.text_input("Enter URL")
            if st.button("Process URL"):
                processing_success = process_url_input(url_input)
        if processing_success and st.session_state.extracted_text:
            with st.expander("📋 Processed Content Preview"):
                preview_text = st.session_state.extracted_text[:1000] + "..." \
                    if len(st.session_state.extracted_text) > 1000 \
                    else st.session_state.extracted_text
                st.text_area("Preview", preview_text, height=200, disabled=True)
    with tab2:
        st.markdown("### 🔍 Document Analysis")
        if st.session_state.extracted_text:
            query = st.text_input(
                "What would you like to know about your document?",
                placeholder="e.g., 'Summarize the main points' or 'What are the key insights?'"
            )
            if st.button("🤖 Analyze", key="analyze_btn"):
                answer = analyze_document(os.environ.get("GEMINI_API_KEY"), query)
                if answer:
                    selected_theme = st.session_state.get("theme_selector", "Dark")
                    accent_color = theme_manager.themes[selected_theme]["accent_color"]
                    st.markdown(f"""
                    <div style='background-color: {theme_manager.themes[selected_theme]["sidebar_background"]}; 
                         padding: 20px; 
                         border-radius: 10px; 
                         box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                         border-left: 4px solid {accent_color};'>
                    <h4 style='margin-top: 0;'>🎯 Analysis Result:</h4>
                    <div style='line-height: 1.6;'>{answer}</div>
                    </div>
                    """, unsafe_allow_html=True)
        else:
            st.info("Please process a document first before analysis")
    with tab3:
        st.markdown("### 📚 Analysis History")
        if st.session_state.history:
            for idx, entry in enumerate(reversed(st.session_state.history)):
                selected_theme = st.session_state.get("theme_selector", "Dark")
                bg_color = theme_manager.themes[selected_theme]["sidebar_background"]
                accent_color = theme_manager.themes[selected_theme]["accent_color"]
                primary_color = theme_manager.themes[selected_theme]["primary_color"]
                st.markdown(f"""
                <div style='background-color: {bg_color}; padding: 15px; 
                border-radius: 10px; margin-bottom: 15px; border-left: 3px solid {primary_color};'>
                <div style='display: flex; justify-content: space-between; margin-bottom: 5px;'>
                    <span style='font-weight: 600; color: {accent_color};'>{entry['timestamp']}</span>
                    <span style='background-color: {primary_color}; padding: 2px 8px; border-radius: 12px; font-size: 12px;'>{entry['type']}</span>
                </div>
                <p style='font-weight: 600; margin-bottom: 5px;'>Query: {entry['query']}</p>
                <p>Answer: {entry['answer'][:200]}{'...' if len(entry['answer']) > 200 else ''}</p>
                <button onclick="this.nextElementSibling.style.display='block';this.style.display='none'" 
                style="border: none; background-color: {accent_color}; color: #fff; padding: 5px 10px; border-radius: 4px; cursor: pointer; font-size: 12px;">
                Show full answer
                </button>
                <div style="display: none; margin-top: 10px; padding: 10px; background-color: rgba(0,0,0,0.05); border-radius: 5px;">{entry['answer']}</div>
                </div>
                """, unsafe_allow_html=True)
        else:
            selected_theme = st.session_state.get("theme_selector", "Dark")
            info_color = theme_manager.themes[selected_theme]["secondary_color"]
            st.markdown(f"""
            <div style='background-color: rgba(0, 123, 255, 0.1); 
                 border-left: 3px solid {info_color}; 
                 padding: 15px; 
                 border-radius: 5px;'>
            <p style='margin: 0;'>No analysis history yet. Perform an analysis to see it here.</p>
            </div>
            """, unsafe_allow_html=True)
    with tab4:
        st.markdown("### ⚙️ Application Settings")
        settings_tabs = st.tabs(["General", "Appearance", "Export"])
        with settings_tabs[0]:
            st.markdown("#### 🔧 General Settings")
            default_model = st.selectbox(
                "Default AI Model", 
                ["Gemini 1.5 Flash", "Gemini Pro", "Custom Model"]
            )
            max_history = st.slider(
                "Maximum Analysis History", 
                min_value=5, 
                max_value=100, 
                value=50
            )
            st.markdown("#### 🔒 Privacy Options")
            st.checkbox("Automatically clear history after session")
            st.checkbox("Anonymize document content")
        with settings_tabs[1]:
            st.markdown("#### 🎨 Appearance Customization")
            theme_options = st.selectbox(
                "Color Theme", 
                list(theme_manager.themes.keys()),
                key="theme_selector"
            )
            font_options = st.selectbox(
                "Font Style", 
                list(theme_manager.fonts.keys()),
                key="font_selector"
            )
            # Apply theme and font on button click
            if st.button("Apply Theme"):
                selected_theme = st.session_state.theme_selector
                selected_font = st.session_state.font_selector
                theme_manager.apply_theme(selected_theme, selected_font)
                st.success(f"Applied {selected_theme} theme with {selected_font} font!")
        with settings_tabs[2]:
            st.markdown("#### 📤 Data Export")
            export_format = st.multiselect(
                "Export Formats", 
                ["CSV", "JSON", "PDF Report"],
                default=["CSV"]
            )
            if st.button("Export Analysis History"):
                try:
                    if len(st.session_state.history) == 0:
                        st.warning("No history data to export!")
                    else:
                        export_success_messages = []
                        
                        if "CSV" in export_format:
                            history_df = pd.DataFrame(st.session_state.history)
                            csv_filename = "docugenius_history.csv"
                            history_df.to_csv(csv_filename, index=False)
                            export_success_messages.append(f"✓ Exported as CSV: {csv_filename}")
                        if "JSON" in export_format:
                            json_filename = "docugenius_history.json"
                            with open(json_filename, "w") as f:
                                json.dump(st.session_state.history, f, indent=4)
                            export_success_messages.append(f"✓ Exported as JSON: {json_filename}")
                        if "PDF Report" in export_format:
                            pdf_filename = "docugenius_history_report.pdf"
                            pdf_path = generate_pdf_report(st.session_state.history, pdf_filename)
                            if pdf_path:
                                export_success_messages.append(f"✓ Exported as PDF Report: {pdf_filename}")
                        if export_success_messages:
                            st.success("Export completed successfully!\n" + "\n".join(export_success_messages))
                except Exception as e:
                    st.error(f"Export failed: {str(e)}")
    render_sidebar()
# Optional: Add a reset button in sidebar
def add_reset_functionality():
    with st.sidebar:
        if st.button("🔄 Reset Usage Stats", key="reset_button"):
            reset_usage_stats()
# Apply default theme at the start
theme_manager.apply_theme("Dark", "Roboto")
# Run the application
def run():
    main()
    add_reset_functionality()
if __name__ == "__main__":
    run()
