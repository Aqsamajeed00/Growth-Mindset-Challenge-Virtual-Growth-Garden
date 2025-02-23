import streamlit as st
import time
import random

# Page Configuration
st.set_page_config(page_title="Virtual Growth Garden 🌱", layout="wide")

# Session State for Garden Progress
if "plant_growth" not in st.session_state:
    st.session_state["plant_growth"] = {"Tree 🌳": 1, "Flower 🌸": 1, "Cactus 🌵": 1}
if "last_watered" not in st.session_state:
    st.session_state["last_watered"] = time.time()

# Watering Logic
current_time = time.time()
time_since_last_water = current_time - st.session_state["last_watered"]
if time_since_last_water > 86400:  # 1 day in seconds
    for plant in st.session_state["plant_growth"]:
        st.session_state["plant_growth"][plant] = max(1, st.session_state["plant_growth"][plant] - 1)

# Sidebar Navigation
st.sidebar.title("🌱 Virtual Growth Garden")
page = st.sidebar.radio("Navigate", ["🏡 Home", "📊 Dashboard", "📞 Contact"])

# Home Page
if page == "🏡 Home":
    st.title("Growth Mindset Challenge: Virtual Growth Garden 🌱🌿")
    st.write("A fun and interactive way to track your learning and achievements through plant growth!")
    
    st.subheader("Your Garden")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.write("🌳 **Tree Progress:**", "🟢" * st.session_state["plant_growth"]["Tree 🌳"])
    with col2:
        st.write("🌸 **Flower Progress:**", "🟢" * st.session_state["plant_growth"]["Flower 🌸"])
    with col3:
        st.write("🌵 **Cactus Progress:**", "🟢" * st.session_state["plant_growth"]["Cactus 🌵"])
    
    st.subheader("Water Your Plants 💧")
    if st.button("Water Now 💦"):
        for plant in st.session_state["plant_growth"]:
            st.session_state["plant_growth"][plant] += random.randint(1, 2)
        st.session_state["last_watered"] = time.time()
        st.success("Plants watered successfully! 🌱")
        time.sleep(1)
        st.rerun()

# Dashboard Page
elif page == "📊 Dashboard":
    st.title("📊 User Progress Dashboard")
    st.write("Monitor your plant growth and achievements here!")
    
    st.subheader("Garden Growth Levels")
    for plant, level in st.session_state["plant_growth"].items():
        st.progress(level / 10)
        st.write(f"{plant}: Level {level}")
    
# Contact Page
elif page == "📞 Contact":
    st.title("📞 Contact & Socials")
    st.write("Connect with me!")
    
    st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-Profile-blue?logo=github)](https://github.com/Aqsamajeed00)")
    st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?logo=linkedin)](https://www.linkedin.com/in/aqsa-majeed-181a69304/)")
    st.markdown("📧 Email: aqsamajeedking313@gmail.com")

st.sidebar.write("🚀 Keep growing, keep learning!")

st.markdown("<div class='footer'>Developed By Aqsa Majeed💻❤</div>", unsafe_allow_html=True)

