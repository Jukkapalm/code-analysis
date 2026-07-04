import streamlit as st

# Sivun asetukset
st.set_page_config(
    page_title="Genetic Code Analysis",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS tyylit
custom_css = """
<style>
    html, body, [data-testid="stAppViewContainer"] {
        font-family: 'Courier New', Courier, monospace !important;
    }
    .sidebar-title {
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #111111;
        margin-bottom: 5px;
    }
    .sidebar-status {
        font-family: monospace;
        font-size: 0.85rem;
        color: #444444;
        margin-bottom: 5px;
    }
    .sidebar-section {
        font-family: 'Courier New', Courier, monospace;
        font-weight: bold;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #111111;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    [data-testid="stSidebar"] hr {
        border: 1px solid #0077FF !important;
        margin-top: 15px;
        margin-bottom: 15px;
    }
    .main-title {
        font-family: 'Courier New', Courier, monospace !important;
        font-weight: bold !important;
        text-transform: uppercase !important;
        letter-spacing: 2px !important;
        font-size: 2.5rem !important;
        margin-bottom: 25px !important;
        color: #111111 !important;
    }
    .main-title span {
        color: #0077FF !important;
        display: inline !important;
    }
    .stButton>button {
        background-color: transparent !important;
        color: #0077FF !important;
        border: 1px solid #0077FF !important;
        border-radius: 4px !important;
        font-family: monospace !important;
        font-weight: bold !important;
        letter-spacing: 1px !important;
        width: 100% !important;
        transition: all 0.3s ease !important;
        margin-top: 10px;
    }
    .stButton>button:hover {
        background-color: #0077FF !important;
        color: #FFFFFF !important;
        border-color: #0077FF !important;
    }
    [data-testid="stNotification"] p {
        color: #222222 !important;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

#Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-title">Control Panel</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-text">Access level: Unrestricted</div>', unsafe_allow_html=True)
    st.markdown('<div class="status-text">System status: Ready</div>', unsafe_allow_html=True)

    st.divider()

    # Näytteenotto
    st.markdown('<div class="sidebar-section">Sample Acquisition</div>', unsafe_allow_html=True)
    username_input = st.text_input("Target User ID", placeholder="Enter GitHub username...")

    # Scan button
    scan_button = st.button("START SCAN")

# Main content
st.markdown(
    '<div class="main-title"><span>G</span>enetic <span>C</span>ode <span>A</span>nalysis</div>', 
    unsafe_allow_html=True
)

# Mittarit
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Repositories Scanned", value="0")
with col2:
    st.metric(label="Primary Language", value="None")
with col3:
    st.metric(label="Analysis Status", value="INACTIVE")

st.warning("SYSTEM NOTICE: Awaiting target user ID input")