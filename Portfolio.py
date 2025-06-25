import streamlit as st
from streamlit_option_menu import option_menu
import requests
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(layout="wide", page_title="Sriram Portfolio")
st.markdown("<style>footer {visibility: hidden;}</style>", unsafe_allow_html=True)

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_code = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_zrqthn6o.json")  
lottie_code1 = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_w51pcehl.json")
lottie_code2 = load_lottieurl("https://assets9.lottiefiles.com/packages/lf20_gjmecwii.json")
lottie_code3 = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_kkflmtur.json")
image = Image.open("assets/obito.jpeg")

with st.container():
        coll, col = st.columns((2,1)) 
        with coll:   
            st.title("I'm SRIRAM SAI LAGGISETTI")
            st.subheader("This is My Portfolio Website")
            st.subheader("""
            I'm a 4th-year B.Tech student at Aditya Engineering College, passionate about Data Science, AI, ML, and building smart web apps.
            """)
            st.markdown("📄 [Download Resume](assets/resume.pdf)", unsafe_allow_html=True)
            
        with col:
            st.image(image,use_container_width=True)
st.write('---')

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['About', 'Projects', 'Contact'],
        icons=['person', 'code-slash', 'chat-left-text-fill'],
        orientation='horizontal'
    )

if selected == "About":
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.write("##")
            st.write("""
I'm Sriram Sai Laggisetti, a final-year B.Tech student from Aditya Engineering College, with a strong passion for Data Science, Machine Learning, and building impactful web applications.

I’m naturally curious, self-driven, and enjoy solving real-world problems using technology. Over the past year, I’ve worked on multiple hands-on projects including an AI Chatbot using LLMs, a PDF Q&A assistant, and interactive dashboards in Power BI.
My greatest strengths are:
- **Adaptability** – I’m quick to learn new tools and technologies.
- **Consistency** – I believe in showing up and improving steadily, even with small steps.
- **Collaboration** – I enjoy working with others, sharing ideas, and growing together.

Currently, I’m actively looking for internship or full-time roles in AI/ML, and I’m open to opportunities where I can contribute, learn, and grow.
Beyond tech, I’m someone who values simplicity, discipline, and the joy of building things that work.
""")
            
        with col2:
            st_lottie(lottie_code3, height=300)

    st.write("---")

    with st.container():
        col3, col4 = st.columns(2)
        with col3:
            st.subheader("🎓 Education")
            st.markdown("""
- **Aditya Engineering College**
    - B.Tech in Computer Science
    - CGPA: 7.33  
- **Sri Chaitanya Jr College**
    - MPC(Intermediate)
    - Grade: 77%  
- **Sri Swamy Vivekananda School**
    - SSC (10th)
    - Grade: 95%
""")
        with col4:
            st.subheader("💼 Experience")
            st.markdown("""
- **Infinitude Internship**  
  _May 5 – June 20, 2025_  
  Hyderabad
- **SkillDzire Internship**  
  _July 5 – Aug 2, 2024_  
  Online
- **Cognifyz Internship**  
  _June 1 – July 3, 2025_  
  Online                                        
""")

    with st.container():
        st.write("---")
        st.write("##")
        c1,c2,c3 = st.columns(3)
        with c1:
            st.markdown("""<div style='display: flex; justify-content: left; gap: 15px; flex-wrap: wrap;'>
    <a href="https://www.linkedin.com/in/sriram-sai-laggisetti/" target="_blank">
        <button style="padding: 10px 20px; border-radius: 8px; border: none; background-color: #0A66C2; color: white; font-size: 16px; cursor: pointer;">
            💼 LinkedIn
        </button>
    </a></div>""",unsafe_allow_html=True)
        with c2:
           st.markdown("""<div style='display: flex; justify-content: left; gap: 15px; flex-wrap: wrap;'> <a href="https://github.com/sriramsai18" target="_blank">
        <button style="padding: 10px 20px; border-radius: 8px; border: none; background-color: #24292E; color: white; font-size: 16px; cursor: pointer;">
            💻 GitHub
        </button>
    </a></div>""",unsafe_allow_html=True)
        with c3:
            st.markdown("""
    <a href="tel:+917207559694">
        <button style="padding: 10px 20px; border-radius: 8px; border: none; background-color: #EA4335; color: white; font-size: 16px; cursor: pointer;">
            📱Phone
        </button></a></div>""", unsafe_allow_html=True)

elif selected == "Projects":
    with st.container():
        st.header("🤖AI TURBO chat Using LLM’s")
        st.write("##")
        col5, col6 = st.columns((1, 2))
        with col5:
            st_lottie(lottie_code1,height=250)
        with col6:
            st.subheader("Q&A Chatbot using Streamlit + TinyLlama")
            st.write("An AI chatbot built using HuggingFace Transformers, Streamlit, and LangChain.Developed an AI-powered chatbot leveraging Large Language Models (LLMs) to provide intelligent responses to user queries in real-time.")
            st.markdown("<a href='https://github.com/sriramsai18/LLMS/blob/main/Chatbot.py' style='font-size: 22px; color: blue;' target='_blank'>GitHub</a> 🔗", unsafe_allow_html=True)

    st.write("---")
    with st.container():
        st.header("📄 PDF Q&A Bot Using RAG+PIPELINE")
        col7, col8 = st.columns((1,2))
        with col7:
            st.subheader("Ask questions on any PDF!")
            st.write(
    """
    This project leverages **LangChain**, **PyPDF2**, and **FAISS** to create an intelligent chatbot that can read and answer questions from any uploaded PDF document. 
    The chatbot splits documents into manageable chunks, embeds them into a vector database for similarity search, and uses an LLM to generate accurate, context-aware answers."""
        )
        st.markdown("<a herf='https://github.com/sriramsai18/LLMS/blob/main/PDF%20Q%26A.py' style='font-size: 22px; color: blue;' target='_blank'>GitHub</a> 🔗", unsafe_allow_html=True)
        with col8:
            st_lottie(lottie_code, height=250)

# --- CONTACT ---
elif selected == "Contact":
    st.header("📬 Get in Touch")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/sriramsailaggisetti@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required style="width:100%; padding:8px;"><br><br>
        <input type="email" name="email" placeholder="Your email" required style="width:100%; padding:8px;"><br><br>
        <textarea name="message" placeholder="Your message here" required style="width:100%; padding:8px;"></textarea><br><br>
        <button type="submit" style="padding:10px 20px;background-color:red; border-radius:8px;">Submit</button>
    </form>
    """

    left_col, right_col = st.columns((2, 1))
    with left_col:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_col:
        st_lottie(lottie_code2,height=300)
