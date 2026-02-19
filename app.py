import streamlit as st
import datetime

# --- पेज कॉन्फ़िगरेशन ---
st.set_page_config(page_title="KD Master Assistant", page_icon="🤖", layout="centered")

# --- कस्टम डिजाइन (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button { 
        width: 100%; 
        border-radius: 15px; 
        height: 3.5em; 
        background-color: #ff4b4b; 
        color: white; 
        font-weight: bold;
        border: none;
        box-shadow: 0px 4px 10px rgba(255, 75, 75, 0.3);
    }
    .stButton>button:hover { background-color: #ff3333; border: none; }
    .status-card {
        padding: 15px;
        border-radius: 12px;
        background: linear-gradient(135deg, #1e1e1e 0%, #2d2d2d 100%);
        border: 1px solid #ff4b4b;
        color: white;
        margin-bottom: 25px;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# --- हेडर और लाइव स्टेटस ---
st.title("🤖 KD Master Assistant")
now = datetime.datetime.now().strftime("%I:%M %p")
st.markdown(f"""
<div class="status-card">
    <b>सचिन का पर्सनल AI</b><br>
    ⏰ समय: {now} | 🌐 स्टेटस: ऑनलाइन | ⚡ मोड: सुपर यूजर
</div>
""", unsafe_allow_html=True)

# --- वॉयस कमांड (JavaScript Integration) ---
st.subheader("🎙️ वॉयस कमांड")
if st.button("🎤 बोलने के लिए यहाँ क्लिक करें"):
    st.info("सुन रही हूँ... कृपया अपनी कमांड बोलें।")
    st.components.v1.html("""
        <script>
        var recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
        recognition.lang = 'hi-IN';
        recognition.onresult = function(event) {
            var voiceText = event.results[0][0].transcript;
            alert("सचिन, आपने कहा: " + voiceText);
        };
        recognition.start();
        </script>
    """, height=0)

st.divider()

# --- मुख्य फीचर्स (Tabs) ---
tab1, tab2, tab3 = st.tabs(["🚀 इंस्टाग्राम", "📍 ट्रैकर", "🛡️ हैकर मोड"])

with tab1:
    st.subheader("📈 Instagram Growth")
    if st.button("वायरल हैशटैग जनरेट करें"):
        st.code("#viral #trending #reelsindia #editing #kdsachin #hacker #explore")
        st.success("कैप्शन: Don't miss the end! 🔥💯")
    st.markdown("[🎥 वीडियो एडिटिंग (Canva) खोलें](https://www.canva.com/video-editor/)")

with tab2:
    st.subheader("🔍 Location Tracker")
    number = st.text_input("मोबाइल नंबर डालें (+91):", placeholder="98XXXXXXXX")
    if st.button("लोकेशन ट्रैक करें"):
        if number:
            st.warning(f"नंबर {number} की जानकारी खोजी जा रही है...")
            st.markdown(f"[📍 यहाँ क्लिक करके मैप पर देखें](https://www.google.com/maps/search/{number})")
        else:
            st.error("कृपया नंबर दर्ज करें!")

with tab3:
    st.subheader("💻 Hacker Shortcuts")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Nmap Scan"):
            st.code("nmap -v -A localhost")
    with col2:
        if st.button("Metasploit"):
            st.code("msfconsole")
    st.info("इन कमांड्स को सीधे Termux में कॉपी-पेस्ट करें।")

# --- फुटर ---
st.divider()
st.caption("© 2026 KD Assistant | सचिन कानवाड़िया द्वारा विकसित")

