import streamlit as st
import requests
import os

# ================== 🔗 BACKEND API ==================
API_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000/predict"  # fallback for local dev
)

# ================== ⚙️ PAGE CONFIG ==================
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
    /* --------- Cards --------- */
    div.css-1r6slb0.e1tzin5v2, [data-testid="stForm"] {
        background-color: var(--secondary-background-color);
        border: 1px solid var(--text-color);
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    /* --------- Typography --------- */
    h1, h2, h3, h4, h5, h6, p, label {
        color: var(--text-color) !important;
    }

    .subtitle {
        opacity: 0.75;
        font-size: 1.1rem;
        margin-bottom: 20px;
    }

    /* --------- Result Cards --------- */
    .result-card {
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white !important;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.25);
    }

    .low-bg { background: linear-gradient(135deg, #11998e, #38ef7d); }
    .medium-bg { background: linear-gradient(135deg, #f2994a, #f2c94c); }
    .high-bg { background: linear-gradient(135deg, #eb3349, #f45c43); }

    /* --------- Footer --------- */
    .footer {
        text-align: center;
        opacity: 0.5;
        font-size: 0.85rem;
        margin-top: 40px;
        padding-top: 15px;
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

st.info(
    "ℹ️ This app runs on a free cloud tier. "
    "If inactive, the backend may take **30–60 seconds** to wake up on the first request."
)

# ================== 📝 INPUT FORM ==================
with st.form("prediction_form"):
    st.subheader("🧾 Your Profile")

    st.markdown("**1️⃣ Health Metrics**")
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input("Age", 18, 100, 30)
    with col2:
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
    with col3:
        height = st.number_input("Height (m)", 0.5, 2.5, 1.75)

    if height > 0:
        bmi = weight / (height ** 2)
        st.info(f"💡 Calculated BMI: **{bmi:.1f}**")

    st.markdown("---")

    st.markdown("**2️⃣ Lifestyle & Details**")
    col_a, col_b = st.columns(2)

    with col_a:
        income_lpa = st.number_input("Annual Income (LPA)", 0.0, 100.0, 10.0)
        occupation = st.selectbox(
            "Occupation",
            [
                "Student",
                "Private Job",
                "Government Job",
                "Business Owner",
                "Freelancer",
                "Unemployed",
                "Retired"
            ]
        )

    with col_b:
        city = st.text_input("City", "Mumbai").strip().title()
        st.write("")
        smoker = st.toggle("Do you smoke?", value=False)

    submit_btn = st.form_submit_button("🔍 Analyze Premium", type="primary")

# ================== 🚀 PREDICTION ==================
if submit_btn:
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
            response = requests.post(API_URL, json=payload, timeout=10)

        if response.status_code == 200:
            data = response.json()

            category = data.get("predicted_category", "Unknown")
            confidence = data.get("confidence", 0.0)
            probs = data.get("class_probabilities", {})

            ui_config = {
                "Low": {
                    "bg": "low-bg",
                    "icon": "🟢",
                    "msg": "You are eligible for standard insurance rates."
                },
                "Medium": {
                    "bg": "medium-bg",
                    "icon": "🟡",
                    "msg": "Moderate risk profile. Premium may be average."
                },
                "High": {
                    "bg": "high-bg",
                    "icon": "🔴",
                    "msg": "Higher risk detected. Premium may include a surcharge."
                }
            }

            style = ui_config.get(
                category,
                {"bg": "medium-bg", "icon": "❓", "msg": "Risk analysis in progress."}
            )

            st.markdown(f"""
            <div class="result-card {style['bg']}">
                <h2>{style['icon']} {category} Premium</h2>
                <p style="font-size:1.1rem;">Confidence: <b>{confidence*100:.1f}%</b></p>
                <p style="font-size:0.9rem;">{style['msg']}</p>
            </div>
            """, unsafe_allow_html=True)

            with st.expander("📊 Probability Distribution"):
                for cat, prob in probs.items():
                    st.progress(prob, text=f"{cat}: {prob*100:.1f}%")

        elif response.status_code in (502, 503, 504):
            st.warning(
                "⏳ **Backend is waking up**\n\n"
                "This app runs on a free cloud tier. "
                "Please wait **30–60 seconds** and try again."
            )

        else:
            st.error(
                f"⚠️ Server returned unexpected status ({response.status_code}). "
                "Please try again later."
            )

    except requests.exceptions.Timeout:
        st.warning(
            "⏳ **Request timed out**\n\n"
            "The backend may be starting up. Please retry shortly."
        )

    except requests.exceptions.ConnectionError:
        st.error(
            "🔌 **Unable to reach backend service**\n\n"
            "Please try again in a moment."
        )

    except Exception:
        st.error(
            "⚠️ **Unexpected error occurred**\n\n"
            "Please refresh the page and try again."
        )

# ================== 🦶 FOOTER ==================
st.markdown(
    "<div class='footer'>⚠️ AI estimates are for informational purposes only. "
    "Consult an insurance advisor for actual quotes.</div>",
    unsafe_allow_html=True
)
