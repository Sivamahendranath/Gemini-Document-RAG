import streamlit as st

class ThemeManager:
    def __init__(self):
        self.themes = {
            "Dark": {
                "background": "#121212",
                "sidebar_background": "#1E1E1E",
                "primary_color": "#BB86FC",
                "secondary_color": "#03DAC6",
                "text_color": "#FFFFFF",
                "accent_color": "#CF6679"
            },
            "Light": {
                "background": "#FFFFFF",
                "sidebar_background": "#F5F5F5",
                "primary_color": "#6200EE",
                "secondary_color": "#03DAC6",
                "text_color": "#000000",
                "accent_color": "#018786"
            },
            "Blue": {
                "background": "#0A192F",
                "sidebar_background": "#172A45",
                "primary_color": "#64FFDA",
                "secondary_color": "#8892B0",
                "text_color": "#E6F1FF",
                "accent_color": "#FF5757"
            },
            "Green": {
                "background": "#0C1D0C",
                "sidebar_background": "#1E3323",
                "primary_color": "#4CAF50",
                "secondary_color": "#8BC34A",
                "text_color": "#F1F8E9",
                "accent_color": "#FF5722"
            }
        }
        self.fonts = {
            "Roboto": "'Roboto', sans-serif",
            "Open Sans": "'Open Sans', sans-serif",
            "Poppins": "'Poppins', sans-serif",
            "Inter": "'Inter', sans-serif",
            "Montserrat": "'Montserrat', sans-serif"
        }
    def apply_theme(self, theme_name, font_name):
        selected_theme = self.themes.get(theme_name, self.themes["Dark"])
        selected_font = self.fonts.get(font_name, "'Roboto', sans-serif")
        theme_css = f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family={font_name.replace(" ", "+")}:wght@300;400;600;700&display=swap');
        .stApp {{
            background-color: {selected_theme['background']};
            color: {selected_theme['text_color']};
            font-family: {selected_font};
        }}
        .stSidebar {{
            background-color: {selected_theme['sidebar_background']};
            color: {selected_theme['text_color']};
        }}
        .stButton>button {{
            background-color: {selected_theme['primary_color']} !important;
            color: {selected_theme['text_color']} !important;
            border-radius: 6px !important;
            font-weight: 600 !important;
            transition: all 0.3s ease !important;
        }}
        .stButton>button:hover {{
            background-color: {selected_theme['accent_color']} !important;
            box-shadow: 0 4px 8px rgba(0,0,0,0.2) !important;
        }}
        h1, h2, h3, .stMarkdown {{
            color: {selected_theme['text_color']} !important;
            font-family: {selected_font};
        }}
        h1 {{
            font-weight: 700 !important;
            letter-spacing: -0.01em !important;
        }}
        h2, h3 {{
            font-weight: 600 !important;
        }}
        .stTextInput>div>div>input, .stTextArea>div>div>textarea {{
            color: {selected_theme['text_color']} !important;
            background-color: {selected_theme['background']} !important;
            border: 1px solid {selected_theme['secondary_color']} !important;
            border-radius: 6px !important;
        }}
        .stTabs {{
            background-color: {selected_theme['background']} !important;
        }}
        .stTabs [data-baseweb="tab-list"] {{
            background-color: {selected_theme['sidebar_background']} !important;
            border-radius: 8px !important;
        }}
        .stTabs [data-baseweb="tab"] {{
            color: {selected_theme['text_color']} !important;
            background-color: {selected_theme['sidebar_background']} !important;
        }}
        .stTabs [aria-selected="true"] {{
            background-color: {selected_theme['primary_color']} !important;
            color: {selected_theme['text_color']} !important;
            font-weight: 600 !important;
        }}
        .stFileUploader {{
            border: 1px dashed {selected_theme['secondary_color']} !important;
            border-radius: 8px !important;
            padding: 10px !important;
        }}
        .stExpander {{
            border-radius: 8px !important;
            background-color: {selected_theme['sidebar_background']} !important;
        }}
        .stExpander summary span svg path {{
            fill: {selected_theme['primary_color']} !important;
        }}
        .stDataFrame {{
            border-radius: 8px !important;
            overflow: hidden !important;
        }}
        .stProgress > div > div > div > div {{
            background-color: {selected_theme['primary_color']} !important;
        }}
        .stSelectbox {{
            color: {selected_theme['text_color']} !important;
        }}
        div[data-baseweb="select"] {{
            background-color: {selected_theme['background']} !important;
            border: 1px solid {selected_theme['secondary_color']} !important;
            border-radius: 6px !important;
        }}
        </style>
        """
        st.markdown(theme_css, unsafe_allow_html=True)