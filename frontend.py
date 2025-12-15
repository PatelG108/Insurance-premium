import streamlit as st
import requests

# ================== ⚙️ CONFIG ==================
API_URL = "http://backend:8000/predict"

st.set_page_config(
    page_title="Insurance Premium Predictor",
    page_icon="🛡️",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ================== 🎨 THEME-ADAPTIVE CSS ==================
def local_css():
    st.markdown("""
    <style>
    /* Use Streamlit's native variables for colors so it works in Dark & Light mode */
    
    /* Main container adjustments */
    .stApp {
        /* This uses the theme's background color automatically */
    }

    /* --------- Custom Cards --------- */
    /* We use 'var(--secondary-background-color)' so the card is 
       light grey in Light Mode and dark grey in Dark Mode */
    div.css-1r6slb0.e1tzin5v2, [data-testid="stForm"] {
        background-color: var(--secondary-background-color);
        border: 1px solid var(--text-color);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    /* --------- Headings & Text --------- */
    h1, h2, h3, h4, h5, h6, p, label {
        color: var(--text-color) !important;
    }
    
    .subtitle {
        color: var(--text-color);
        opacity: 0.7;
        font-size: 1.1rem;
        margin-bottom: 30px;
    }
    
    /* --------- Result Banners (Fixed Colors) --------- */
    /* These keep their specific colors because they are status indicators */
    .result-card {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white !important; /* Always white text on colored banners */
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    
    .low-bg { background: linear-gradient(135deg, #11998e, #38ef7d); }
    .medium-bg { background: linear-gradient(135deg, #f2994a, #f2c94c); }
    .high-bg { background: linear-gradient(135deg, #eb3349, #f45c43); }

    /* --------- Footer --------- */
    .footer {
        text-align: center;
        color: var(--text-color);
        opacity: 0.5;
        font-size: 0.85rem;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid var(--text-color);
    }
    </style>
    """, unsafe_allow_html=True)

local_css()

# ================== 🏠 HEADER ==================
st.title("🛡️ Insurance Premium Predictor")
st.markdown(
    "<div class='subtitle'>AI-powered analysis to estimate your insurance risk category.</div>", 
    unsafe_allow_html=True
)

# ================== 📝 INPUT FORM ==================
with st.form("prediction_form"):
    st.subheader("🧾 Your Profile")
    
    # --- Section 1: Health Metrics ---
    st.markdown("**1️⃣ Health Metrics**")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age", 18, 100, 30, help="Age in years")
    with col2:
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    with col3:
        height = st.number_input("Height (m)", 0.5, 2.5, 1.75)

    # Dynamic BMI Display
    if height > 0:
        bmi = weight / (height ** 2)
        st.info(f"💡 Calculated BMI: **{bmi:.1f}**")

    st.markdown("---")

    # --- Section 2: Lifestyle ---
    st.markdown("**2️⃣ Lifestyle & Details**")
    col_a, col_b = st.columns(2)
    
    with col_a:
        income_lpa = st.number_input("Annual Income (LPA)", 0.0, 100.0, 10.0)
        occupation = st.selectbox(
            "Occupation",
            ["Student", "Private Job", "Government Job", "Business Owner", "Freelancer", "Unemployed", "Retired"]
        )
        
    with col_b:
        city = st.text_input("City", "Mumbai").strip().title()
        st.write("") # Spacer
        st.write("") # Spacer
        smoker = st.toggle("Do you smoke?", value=False)

    # Submit Button
    submit_btn = st.form_submit_button("🔍 Analyze Premium", type="primary")

# ================== 🚀 PREDICTION LOGIC ==================
if submit_btn:
    # Prepare payload
    payload = {
        "age": age,
        "weight": weight,
        "height": height,
        "income_lpa": income_lpa,
        "smoker": smoker,
        "city": city,
        "occupation": occupation.lower().replace(" ", "_")
    }

    try:
        with st.spinner("🤖 Consulting the AI model..."):
            response = requests.post(API_URL, json=payload, timeout=5)
            
        if response.status_code == 200:
            data = response.json()
            
            category = data.get("predicted_category", "Unknown")
            confidence = data.get("confidence", 0.0)
            probs = data.get("class_probabilities", {})

            # UI Mapping
            ui_config = {
                "Low": {"bg": "low-bg", "icon": "🟢", "msg": "Great! You are eligible for standard rates."},
                "Medium": {"bg": "medium-bg", "icon": "🟡", "msg": "Moderate risk. Premium will be average."},
                "High": {"bg": "high-bg", "icon": "🔴", "msg": "High risk detected. Expect a surcharge."}
            }
            
            style = ui_config.get(category, {"bg": "medium-bg", "icon": "❓", "msg": "Processing..."})

            # --- Result Display ---
            st.markdown(f"""
            <div class="result-card {style['bg']}">
                <h2 style="color: white !important;">{style['icon']} {category} Premium</h2>
                <p style="font-size: 1.1rem; opacity: 0.9; color: white !important;">Confidence: <b>{confidence*100:.1f}%</b></p>
                <p style="margin-top:10px; font-size: 0.9rem; color: white !important;">{style['msg']}</p>
            </div>
            """, unsafe_allow_html=True)

            # --- Probability Breakdown ---
            with st.expander("📊 View Detailed Probabilities", expanded=True):
                for cat, prob in probs.items():
                    st.progress(prob, text=f"{cat}: {prob*100:.1f}%")
        
        else:
            st.error(f"❌ Server Error: {response.status_code}")

    except requests.exceptions.ConnectionError:
        st.error("🔌 API Unreachable. Make sure the backend server is running.")
    except Exception as e:
        st.error(f"⚠️ An unexpected error occurred: {e}")

# ================== 🦶 FOOTER ==================
st.markdown(
    "<div class='footer'>⚠️ AI estimates are for informational purposes only. Consult an agent for actual quotes.</div>", 
    unsafe_allow_html=True
)