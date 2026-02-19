import streamlit as st
import webbrowser

st.set_page_config(page_title="KD Master Assistant", page_icon="🤖")

st.markdown("""
    <style>
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #ff4b4b; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 KD Master Assistant")
st.write("नमस्ते सचिन, आपका पर्सनल AI अब वेब पर लाइव है।")

tab1, tab2, tab3 = st.tabs(["🚀 Instagram", "📍 Tracker", "🛡️ Hacker Mode"])

with tab1:
    st.subheader("Insta Growth Tool")
    if st.button("Generate Viral Tags"):
        st.code("#viral #trending #reelsindia #editing #kdsachin #explore")
        st.success("Caption: New Reel Out! 🔥 Wait for it.. 😱")
    st.markdown("[Click here to Edit Video](https://www.canva.com/video-editor/)")

with tab2:
    st.subheader("Location Tracker")
    number = st.text_input("Mobile Number (+91):")
    if st.button("Track Location"):
        if number:
            st.info(f"Tracking {number}...")
            st.markdown(f"[View on Map](https://www.google.com/maps/search/{number})")

with tab3:
    st.subheader("Hacking Shortcuts")
    if st.button("Nmap Command"):
        st.code("nmap -v -A localhost")
    if st.button("Metasploit"):
        st.code("msfconsole")
      
