"""
Hari Krishna RL - Interactive Professional Portfolio
Built with Streamlit, Plotly, and Python.
Designed for 1-Click Deployment on Streamlit Community Cloud, Hugging Face Spaces, or Docker.
"""

import os
import base64
import zlib
import re
from datetime import datetime
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

# -----------------------------------------------------------------------------
# PAGE CONFIGURATION
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="Hari Krishna RL | AI & Systems Portfolio",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# -----------------------------------------------------------------------------
# CUSTOM CSS STYLING (Dark Modern Tech Aesthetics)
# -----------------------------------------------------------------------------
CUSTOM_CSS = """
<style>
/* Font and Base Settings */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

code, pre {
    font-family: 'JetBrains Mono', monospace !important;
}

/* Background & Main Layout */
.main .block-container {
    padding-top: 1.8rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}

/* Hero Section Styling */
.hero-container {
    background: linear-gradient(135deg, rgba(22, 27, 34, 0.85) 0%, rgba(13, 17, 23, 0.95) 100%);
    border: 1px solid rgba(56, 139, 253, 0.25);
    border-radius: 16px;
    padding: 2.2rem 2.5rem;
    margin-bottom: 2rem;
    box-shadow: 0 10px 30px -10px rgba(0, 210, 255, 0.15);
    backdrop-filter: blur(12px);
    position: relative;
    overflow: hidden;
}

.hero-container::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 3px;
    background: linear-gradient(90deg, #00D2FF, #3A7BD5, #8A2BE2, #00D2FF);
    background-size: 300% 100%;
    animation: gradientShift 6s ease infinite;
}

@keyframes gradientShift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.hero-name {
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, #ffffff 0%, #00D2FF 60%, #90caf9 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    letter-spacing: -0.5px;
    margin-bottom: 0.25rem;
}

.hero-tagline {
    font-size: 1.25rem;
    font-weight: 500;
    color: #58A6FF;
    margin-bottom: 0.8rem;
}

.hero-bio {
    font-size: 0.98rem;
    line-height: 1.65;
    color: #C9D1D9;
    margin-bottom: 1.2rem;
}

/* Badge & Tag Pills */
.badge-pill {
    display: inline-block;
    padding: 0.3rem 0.8rem;
    border-radius: 20px;
    font-size: 0.78rem;
    font-weight: 600;
    margin-right: 0.5rem;
    margin-bottom: 0.5rem;
    border: 1px solid rgba(255, 255, 255, 0.12);
}

.badge-cyan {
    background: rgba(0, 210, 255, 0.12);
    color: #00D2FF;
    border-color: rgba(0, 210, 255, 0.3);
}

.badge-green {
    background: rgba(46, 160, 67, 0.15);
    color: #3fb950;
    border-color: rgba(46, 160, 67, 0.35);
}

.badge-purple {
    background: rgba(163, 113, 247, 0.15);
    color: #d2a8ff;
    border-color: rgba(163, 113, 247, 0.35);
}

.badge-orange {
    background: rgba(240, 136, 62, 0.15);
    color: #f0883e;
    border-color: rgba(240, 136, 62, 0.35);
}

/* Glassmorphism Project Cards */
.card-box {
    background: rgba(22, 27, 34, 0.7);
    border: 1px solid rgba(48, 54, 61, 0.8);
    border-radius: 14px;
    padding: 1.5rem;
    margin-bottom: 1.5rem;
    transition: all 0.25s ease-in-out;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.card-box:hover {
    border-color: #58A6FF;
    transform: translateY(-2px);
    box-shadow: 0 8px 24px rgba(0, 210, 255, 0.15);
}

.card-title {
    font-size: 1.35rem;
    font-weight: 700;
    color: #F0F6FC;
    margin-bottom: 0.4rem;
}

.card-subtitle {
    font-size: 0.88rem;
    color: #8B949E;
    margin-bottom: 0.8rem;
}

/* Metrics & Stats Card */
.stat-card {
    background: rgba(13, 17, 23, 0.8);
    border: 1px solid #30363D;
    border-radius: 12px;
    padding: 1rem;
    text-align: center;
}

.stat-number {
    font-size: 2rem;
    font-weight: 800;
    color: #00D2FF;
    line-height: 1.1;
}

.stat-label {
    font-size: 0.8rem;
    color: #8B949E;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-top: 0.3rem;
}

/* Timeline Components */
.timeline-item {
    border-left: 2px solid #388BFD;
    padding-left: 1.25rem;
    margin-left: 0.5rem;
    margin-bottom: 1.5rem;
    position: relative;
}

.timeline-item::before {
    content: '';
    position: absolute;
    left: -7px;
    top: 4px;
    width: 12px;
    height: 12px;
    border-radius: 50%;
    background: #00D2FF;
    box-shadow: 0 0 10px #00D2FF;
}

/* Sidebar Styling */
section[data-testid="stSidebar"] {
    background-color: #0D1117;
    border-right: 1px solid #21262D;
}

.sidebar-profile {
    text-align: center;
    padding: 1rem 0;
}

/* Sidebar Profile Image - Circular Avatar with Cyan Glow */
[data-testid="stSidebar"] img {
    border-radius: 50% !important;
    border: 3px solid #00D2FF !important;
    box-shadow: 0 0 25px rgba(0, 210, 255, 0.4) !important;
    margin: 0.5rem auto 1rem auto !important;
    display: block !important;
    object-fit: cover !important;
    aspect-ratio: 1 / 1 !important;
    width: 170px !important;
    height: 170px !important;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

[data-testid="stSidebar"] img:hover {
    transform: scale(1.03);
    box-shadow: 0 0 35px rgba(0, 210, 255, 0.65) !important;
}

/* Streamlit button modern styling */
.stButton>button {
    border-radius: 10px;
    font-weight: 600;
    transition: all 0.2s ease;
}

/* Contact link buttons */
.contact-btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(33, 38, 45, 0.9);
    color: #E6EDF3 !important;
    border: 1px solid #30363D;
    padding: 0.45rem 0.9rem;
    border-radius: 8px;
    font-size: 0.85rem;
    text-decoration: none !important;
    transition: all 0.2s;
    margin-right: 0.4rem;
    margin-bottom: 0.5rem;
}

.contact-btn:hover {
    background: #30363D;
    border-color: #58A6FF;
    color: #58A6FF !important;
}

/* Highlighted Buzzword span */
.highlight-buzzword {
    background-color: rgba(240, 136, 62, 0.35);
    color: #ffa657;
    padding: 2px 6px;
    border-radius: 4px;
    font-weight: 600;
    border-bottom: 2px solid #f0883e;
}
</style>
"""
st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS & DATA ASSETS
# -----------------------------------------------------------------------------
def get_base64_file(file_path):
    """Encodes a local file to base64."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return base64.b64encode(f.read()).decode()
    return None

def get_file_bytes(file_path):
    """Reads binary bytes from a file."""
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            return f.read()
    return None

RESUME_PATH = os.path.join(os.path.dirname(__file__), "assets", "Hari_Krishna_RL_Resume.pdf")
PROFILE_PIC_PATH = os.path.join(os.path.dirname(__file__), "assets", "profile.jpg")

# -----------------------------------------------------------------------------
# SIDEBAR NAVIGATION & PROFILE SUMMARY
# -----------------------------------------------------------------------------
with st.sidebar:
    # Profile Picture
    if os.path.exists(PROFILE_PIC_PATH):
        st.image(PROFILE_PIC_PATH, width=175)
    else:
        st.markdown(
            """
            <div style="width:120px;height:120px;border-radius:50%;background:#1F2937;
            display:flex;align-items:center;justify-content:center;margin:0 auto;font-size:2.8rem;border:2px solid #00D2FF;">
            👨‍💻
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<h2 style='text-align: center; margin-bottom: 0px;'>Hari Krishna RL</h2>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #58A6FF; font-size: 0.9rem;'>AI & ML Engineer | Systems & DevOps</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #8B949E; font-size: 0.8rem;'>📍 Bengaluru, Karnataka, India</p>", unsafe_allow_html=True)

    # Resume Download Button
    resume_bytes = get_file_bytes(RESUME_PATH)
    if resume_bytes:
        st.download_button(
            label="📄 Download Official Resume",
            data=resume_bytes,
            file_name="Hari_Krishna_RL_Resume.pdf",
            mime="application/pdf",
            use_container_width=True
        )
    else:
        st.button("📄 Resume (PDF Ready)", disabled=True, use_container_width=True)

    st.markdown("---")

    # Quick Navigation
    st.markdown("### 🧭 Navigation")
    nav_choice = st.radio(
        "Jump to section:",
        [
            "🌟 Overview & Bio",
            "🚀 Featured Projects",
            "⚡ Interactive Demos",
            "🛠️ Technical Skills",
            "🎓 Education & Journey",
            "🏆 Hackathons & Activities",
            "📬 Contact & Connect"
        ],
        label_visibility="collapsed"
    )

    st.markdown("---")

    # Quick Links in Sidebar
    st.markdown("### 🔗 Connect")
    st.markdown("""
    - [💼 LinkedIn Profile](https://www.linkedin.com/in/hari-krishna-rl-058088298/)
    - [🐙 GitHub (@Harikrishnarl)](https://github.com/Harikrishnarl)
    - [🧩 LeetCode Profile](https://leetcode.com/u/Harikrishnarl/)
    - [📧 Email Me](mailto:hraj488.884@gmail.com)
    """)

    st.markdown("---")
    st.caption("Built with Streamlit & Plotly • 2026")


# =============================================================================
# SECTION 1: OVERVIEW & BIO
# =============================================================================
if nav_choice == "🌟 Overview & Bio":
    # Hero Section
    profile_b64 = get_base64_file(PROFILE_PIC_PATH)
    hero_img_html = ""
    if profile_b64:
        hero_img_html = f"""
        <div style="flex: 0 0 190px; text-align: center;">
            <img src="data:image/jpeg;base64,{profile_b64}" 
                 style="width: 175px; height: 175px; border-radius: 50%; object-fit: cover; border: 3px solid #00D2FF; box-shadow: 0 0 25px rgba(0, 210, 255, 0.45);" 
                 alt="Hari Krishna RL" />
        </div>
        """

    st.markdown(
        f"""
        <div class="hero-container">
            <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 2rem;">
                <div style="flex: 1 1 560px;">
                    <div class="hero-name">HARI KRISHNA RL</div>
                    <div class="hero-tagline">Final-Year B.E. in Artificial Intelligence & Machine Learning</div>
                    <p class="hero-bio">
                        Passionate software and AI engineer with deep hands-on expertise spanning 
                        <strong>production AI/LLM pipelines (RAG, transformers)</strong>, 
                        <strong>low-level networking systems (zero-library DPI, raw PCAP parsing, TLS SNI extraction)</strong>, 
                        and <strong>containerized cloud-native deployments (Docker, GitHub Actions CI/CD, Prometheus, Grafana)</strong>. 
                        Dedicated to engineering robust, automated, and observable architectures.
                    </p>
                    <div>
                        <span class="badge-pill badge-cyan">🤖 AI & LLM Systems</span>
                        <span class="badge-pill badge-green">🐳 Containerized DevOps & CI/CD</span>
                        <span class="badge-pill badge-purple">📡 Deep Packet Inspection</span>
                        <span class="badge-pill badge-orange">⚡ Low-Latency Python & C</span>
                    </div>
                </div>
                {hero_img_html}
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Key Metrics Highlights
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">8.08</div>
                <div class="stat-label">Engineering CGPA (AIML)</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c2:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">3+</div>
                <div class="stat-label">Core Systems & AI Projects</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c3:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">2</div>
                <div class="stat-label">Major Hackathons Attended</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with c4:
        st.markdown(
            """
            <div class="stat-card">
                <div class="stat-number">92.8%</div>
                <div class="stat-label">Pre-University Score</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # Two column overview: Core Pillars & Quick Contact
    col_left, col_right = st.columns([1.6, 1])

    with col_left:
        st.markdown("### 🎯 What I Bring to the Table")
        st.markdown("""
        - **Full-Stack AI Engineering:** From document parsing and FAISS/Chroma vector DB retrieval to Google Gemini and Hugging Face transformer models.
        - **Zero-Dependency Systems Programming:** Decoding raw Ethernet/IPv4/TCP frames with Python `struct` without bulky parsing libraries, parsing RFC 6066 TLS Client Hello headers to classify encrypted traffic.
        - **Concurrency & Multiprocessing:** Lock-free multiprocessing architectures with CRC32 canonical 5-tuple hash sharding for high-throughput packet processing.
        - **Production Observability & CI/CD:** End-to-end automation via Docker multi-stage containers, GitHub Container Registry, automated testing pipelines, and live telemetry exposed to Prometheus and Grafana.
        """)

    with col_right:
        st.markdown("### 📍 Quick Info & Links")
        st.markdown("""
        - **Institution:** CMR Institute of Technology, Bengaluru
        - **Degree:** B.E. Artificial Intelligence & Machine Learning (2027)
        - **Primary Email:** [hraj488.884@gmail.com](mailto:hraj488.884@gmail.com)
        - **College Email:** [harl23aiml@cmrit.ac.in](mailto:harl23aiml@cmrit.ac.in)
        - **Phone:** `+91 9916766556`
        - **Languages:** English, Kannada, Hindi
        - **Hobbies:** Cricket, Football, System Optimization
        """)


# =============================================================================
# SECTION 2: FEATURED PROJECTS
# =============================================================================
elif nav_choice == "🚀 Featured Projects":
    st.markdown("## 🚀 Featured Engineering Projects")
    st.caption("Detailed architectural breakdown of key AI, Networking, and Cloud-native projects.")

    # Project Filter Tabs
    proj_tab1, proj_tab2, proj_tab3 = st.tabs([
        "📡 Deep Packet Inspection (DPI) Engine",
        "🧠 AI Learning Companion (RAG & LLM)",
        "🛡️ AI Slop & Stylometric Detector"
    ])

    # ----------------- PROJECT 1 -----------------
    with proj_tab1:
        st.markdown(
            """
            <div class="card-box">
                <div class="card-title">📡 Deep Packet Inspection (DPI) Engine & Network Classifier</div>
                <div class="card-subtitle">Zero-Library Raw Header Decoding • TLS SNI Extraction • Multiprocessing Sharding • Prometheus & Grafana</div>
                <div>
                    <span class="badge-pill badge-cyan">Python</span>
                    <span class="badge-pill badge-green">Docker & Compose</span>
                    <span class="badge-pill badge-purple">Prometheus / Grafana</span>
                    <span class="badge-pill badge-orange">Multiprocessing</span>
                    <span class="badge-pill badge-cyan">Raw Sockets & Struct</span>
                    <span class="badge-pill badge-purple">GitHub Actions CI/CD</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        p1_c1, p1_c2 = st.columns([1.5, 1])
        with p1_c1:
            st.markdown("#### 🔍 Project Overview & Architectural Highlights")
            st.markdown("""
            A high-performance, containerized Deep Packet Inspection (DPI) system and network traffic classifier built with **zero external packet parsing dependencies** (no Scapy, dpkt, or pyshark).
            
            - **Zero-Dependency Raw Decoding:** Decodes raw PCAP frames, Ethernet II (with 802.1Q VLAN support), IPv4 (variable IHL), TCP (variable data offset & flags), and UDP headers using pure Python `struct`.
            - **Encrypted Traffic Classification:** Dissects unencrypted TLS *Client Hello* handshake records (Content Type `0x16`, Handshake `0x01`). Iterates through variable session IDs and cipher suites to extract TLS Extension `0x0000` (Server Name Indication) per RFC 6066, identifying target domains (e.g. `youtube.com`, `github.com`) without payload decryption.
            - **Lock-Free Concurrency via Multiprocessing:** Groups bidirectional connections into canonical symmetric 5-tuples and shards flows across worker processes using CRC32 consistent hashing:
            """)
            st.latex(r"\text{Worker ID} = \text{hash}(\text{Canonical 5-Tuple}) \pmod N")
            st.markdown("""
            - **Multi-Layer Rule Engine:**
                - Layer 1 (L3): IP address blocking & subnet routing.
                - Layer 2 (L4): TCP/UDP port restrictions.
                - Layer 3 (L7): Application classification (e.g., Video Streaming, Cloud API, Web).
                - Layer 4 (L7): Domain pattern matching & regex filtering.
            - **Cloud-Native Observability:** Exposes custom Prometheus metrics (`packets_per_sec`, `active_flows`, `bytes_per_app`) and displays real-time network health on Grafana dashboards with anomaly alerts.
            - **Containerized CI/CD:** Fully automated test, multi-stage build, and deployment via GitHub Actions to GitHub Container Registry (GHCR).
            """)

        with p1_c2:
            st.markdown("#### 📊 Architecture Pipeline")
            st.info("""
            **1. Raw Ingestion**
            PCAP File / Raw Network Interface
            ⬇️
            **2. Struct Header Parser**
            Ethernet ➡️ IPv4 ➡️ TCP/UDP
            ⬇️
            **3. TLS Dissection**
            Record Layer ➡️ Client Hello ➡️ SNI Ext
            ⬇️
            **4. CRC32 Flow Sharding**
            Worker 0 | Worker 1 | Worker 2 | Worker 3
            ⬇️
            **5. Telemetry & Export**
            Prometheus Metrics (:9090) ➡️ Grafana (:3000)
            """)

            st.markdown("#### 🔗 Repository & Code")
            st.markdown("""
            - [🐙 GitHub: Packet Analyzer Repository](https://github.com/hraj4/packet_analyzer)
            - Includes Python Multiprocessing microservice and C++17 wire-speed multi-threaded core.
            """)

    # ----------------- PROJECT 2 -----------------
    with proj_tab2:
        st.markdown(
            """
            <div class="card-box">
                <div class="card-title">🧠 AI Learning Companion</div>
                <div class="card-subtitle">Retrieval-Augmented Generation (RAG) • Multi-Turn Doubt Solver • Adaptive Quiz Generation • Mastery Dashboards</div>
                <div>
                    <span class="badge-pill badge-cyan">LangChain</span>
                    <span class="badge-pill badge-green">Google Gemini API</span>
                    <span class="badge-pill badge-purple">FAISS / ChromaDB</span>
                    <span class="badge-pill badge-orange">Streamlit</span>
                    <span class="badge-pill badge-cyan">Sentence Transformers</span>
                    <span class="badge-pill badge-purple">Plotly & SQLite</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        p2_c1, p2_c2 = st.columns([1.5, 1])
        with p2_c1:
            st.markdown("#### 🔍 Project Overview & Features")
            st.markdown("""
            An intelligent, context-aware personalized learning platform designed to augment self-paced student education through Retrieval-Augmented Generation (RAG) and conversational AI.

            - **Context-Aware RAG Engine:** Users upload textbooks, course notes, and research PDFs. Documents are chunked, embedded via `sentence-transformers`, and stored in FAISS / Chroma DB vector spaces for hallucination-free factual retrieval.
            - **Google Gemini LLM Integration:** Employs Gemini for dynamic topic explanations, interactive step-by-step doubt clearing, and personalized pedagogical guidance tailored to student comprehension levels.
            - **Automated Quiz & Flashcard Generation:** Automatically analyzes uploaded study material to formulate multiple-choice questions, difficulty-tiered assessments, and flashcards.
            - **Analytics & Knowledge Mastery:** Persists student quiz attempts, question history, and topic mastery scores in an SQLite relational database, rendering interactive Plotly charts tracking learning retention over time.
            - **Conversational Multi-Turn Chatbot:** Maintains context memory across student dialogue sessions for natural question refinement.
            """)
        with p2_c2:
            st.markdown("#### 🛠️ Tech Stack Matrix")
            st.markdown("""
            - **Core Language:** Python 3.11
            - **LLM & Orchestration:** LangChain, Google Gemini API
            - **Vector Indexing:** FAISS, Chroma DB, Hugging Face Embeddings
            - **Document Processing:** PyPDF, LangChain Text Splitters
            - **UI & Analytics:** Streamlit, Plotly, HTML/CSS
            - **Data Persistence:** SQLite3 & Pandas
            """)
            st.success("Try out the interactive Quiz Simulator in the 'Interactive Demos' tab!")

    # ----------------- PROJECT 3 -----------------
    with proj_tab3:
        st.markdown(
            """
            <div class="card-box">
                <div class="card-title">🛡️ AI Slop & Synthetic Content Detector</div>
                <div class="card-subtitle">Dual-Tier Pipeline • Stylometric Burstiness Analysis • Cliché Density • Local Transformer Core</div>
                <div>
                    <span class="badge-pill badge-cyan">Python</span>
                    <span class="badge-pill badge-green">Hugging Face</span>
                    <span class="badge-pill badge-purple">PyTorch</span>
                    <span class="badge-pill badge-orange">NLTK & NumPy</span>
                    <span class="badge-pill badge-cyan">FastAPI</span>
                    <span class="badge-pill badge-purple">Streamlit</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        p3_c1, p3_c2 = st.columns([1.5, 1])
        with p3_c1:
            st.markdown("#### 🔍 Project Overview & Architecture")
            st.markdown("""
            An efficient detection engine engineered to identify machine-generated text, buzzword-heavy marketing fluff, and AI-hallucinated clichés with minimal latency and strict data privacy.

            - **Dual-Tier Classification Pipeline:**
                - **Tier 1 (Fast Statistical Rules):** Runs in under 5ms using statistical stylometrics. Filters obvious human writing and calculates burstiness, vocabulary clichés, and token co-occurrence using NumPy and NLTK.
                - **Tier 2 (Transformer Inference):** Routes complex, ambiguous payloads to local Hugging Face transformer classification models (RoBERTa / DistilBERT) without cloud API costs or privacy leaks.
            - **Stylometric Fingerprinting:**
                - **Burstiness Metric:** Measures standard deviation and variance of sentence lengths (AI tends to produce flat, uniform sentence rhythms).
                - **Lexical Diversity:** Evaluates Type-Token Ratio (TTR) and vocabulary richness.
                - **Cliché Density:** Detects common LLM hallmarks (e.g., *'delve'*, *'testament'*, *'rich tapestry'*, *'pivotal'*, *'paramount'*).
            - **Interactive Dashboard:** Streamlit interface rendering real-time confidence scores, text metric radar charts, and inline highlighting of detected buzzwords.
            """)
        with p3_c2:
            st.markdown("#### ⚡ Latency & Cost Optimization")
            st.markdown("""
            By gating deep transformer inference behind statistical stylometrics, the system eliminates unnecessary GPU computation for ~65% of obvious payloads, enabling fast, local, and private verification.
            """)
            st.info("Check out the Live AI Slop Detector interactive widget in the next tab!")


# =============================================================================
# SECTION 3: INTERACTIVE DEMOS
# =============================================================================
elif nav_choice == "⚡ Interactive Demos":
    st.markdown("## ⚡ Live Interactive Demos")
    st.caption("Experience live interactive implementations of the algorithmic and architectural concepts built into Hari Krishna RL's projects.")

    demo_selector = st.selectbox(
        "Select Interactive Demo:",
        [
            "🛡️ Live Demo 1: Stylometric AI Slop & Buzzword Detector",
            "📡 Live Demo 2: DPI 5-Tuple Normalizer & TLS SNI Classifier",
            "🧠 Live Demo 3: AI Learning Companion Quiz Simulator"
        ]
    )

    # -------------------------------------------------------------------------
    # DEMO 1: AI SLOP DETECTOR
    # -------------------------------------------------------------------------
    if "AI Slop" in demo_selector:
        st.markdown("### 🛡️ Stylometric AI Slop & Buzzword Analyzer")
        st.write("This interactive module runs statistical stylometry to detect AI-generated rhythms, sentence uniformity, and characteristic LLM clichés.")

        # Sample Presets
        sample_ai_text = (
            "In today's rapidly evolving digital landscape, it is paramount to delve into the transformative power "
            "of artificial intelligence. This breakthrough stands as a testament to human ingenuity. "
            "Not only does it foster unprecedented synergy across multifaceted domains, but it also weaves a rich tapestry "
            "of seamless innovation. Navigating this pivotal frontier demystifies the cutting-edge possibilities ahead."
        )

        sample_human_text = (
            "We spent all Tuesday afternoon debugging packet loss on the edge router. Turns out the ring buffer was "
            "too small for 10Gbps bursts. We bumped the descriptor queue from 512 to 4096 and the dropped packet count "
            "immediately dropped to zero. Ran iperf overnight and latency stayed flat at 1.2ms."
        )

        col_presets, _ = st.columns([2, 1])
        with col_presets:
            preset = st.radio("Load Sample Text or Write Your Own:", ["AI Cliché Sample", "Human Engineering Log", "Custom Input"], horizontal=True)

        if preset == "AI Cliché Sample":
            initial_text = sample_ai_text
        elif preset == "Human Engineering Log":
            initial_text = sample_human_text
        else:
            initial_text = "Enter your custom paragraph here to analyze its stylometric fingerprints..."

        user_text = st.text_area("Input Text for Stylometric Analysis:", value=initial_text, height=130)

        if st.button("🔍 Run Stylometric Analysis", type="primary"):
            # Compute stylometrics
            AI_BUZZWORDS = [
                "delve", "tapestry", "testament", "paramount", "pivotal", "demystify",
                "beacon", "transformative", "foster", "synergy", "cutting-edge",
                "revolutionize", "seamless", "rich tapestry", "not only", "multifaceted", "landscape"
            ]

            words = re.findall(r'\b[a-zA-Z]+\b', user_text.lower())
            sentences = [s.strip() for s in re.split(r'[.!?]+', user_text) if s.strip()]

            word_count = len(words)
            sentence_count = len(sentences)

            if word_count > 0 and sentence_count > 0:
                sentence_lengths = [len(re.findall(r'\b[a-zA-Z]+\b', s)) for s in sentences]
                avg_sentence_len = np.mean(sentence_lengths)
                burstiness = float(np.std(sentence_lengths)) if len(sentence_lengths) > 1 else 0.0
                unique_words = set(words)
                ttr = len(unique_words) / word_count  # Type-Token Ratio

                # Buzzword detection
                detected_buzzwords = []
                for b in AI_BUZZWORDS:
                    if " " in b:
                        if b in user_text.lower():
                            detected_buzzwords.append(b)
                    else:
                        if b in words:
                            detected_buzzwords.append(b)

                cliche_score = min(100, int((len(detected_buzzwords) / max(1, sentence_count)) * 55))
                # Burstiness penalty: AI text has low sentence length variance (low burstiness)
                burstiness_penalty = max(0, int((6.0 - min(6.0, burstiness)) * 7))
                ai_slop_probability = min(98, max(5, int(cliche_score * 0.65 + burstiness_penalty * 0.35)))

                # Visual Results
                st.markdown("---")
                st.markdown("#### 📊 Stylometric Diagnostic Report")

                res_c1, res_c2, res_c3, res_c4 = st.columns(4)
                res_c1.metric("Word Count", word_count)
                res_c2.metric("Sentences", sentence_count)
                res_c3.metric("Sentence Burstiness (σ)", f"{burstiness:.2f}")
                res_c4.metric("Lexical Diversity (TTR)", f"{ttr:.2f}")

                gauge_c, text_c = st.columns([1.2, 1.8])

                with gauge_c:
                    fig_gauge = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=ai_slop_probability,
                        title={'text': "AI / Cliché Probability (%)", 'font': {'size': 16, 'color': '#E6EDF3'}},
                        number={'suffix': "%", 'font': {'color': '#00D2FF', 'size': 28}},
                        gauge={
                            'axis': {'range': [0, 100], 'tickcolor': "#8B949E"},
                            'bar': {'color': "#00D2FF"},
                            'steps': [
                                {'range': [0, 35], 'color': "rgba(46, 160, 67, 0.4)"},
                                {'range': [35, 70], 'color': "rgba(240, 136, 62, 0.4)"},
                                {'range': [70, 100], 'color': "rgba(248, 81, 73, 0.4)"}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 3},
                                'thickness': 0.75,
                                'value': 75
                            }
                        }
                    ))
                    fig_gauge.update_layout(
                        paper_bgcolor="rgba(0,0,0,0)",
                        plot_bgcolor="rgba(0,0,0,0)",
                        margin=dict(l=20, r=20, t=40, b=20),
                        height=240
                    )
                    st.plotly_chart(fig_gauge, use_container_width=True)

                with text_c:
                    st.markdown("##### 📝 Highlighted Buzzwords & Verdict")
                    if detected_buzzwords:
                        st.warning(f"Detected {len(detected_buzzwords)} common AI stylistic hallmark(s): **{', '.join(detected_buzzwords)}**")
                    else:
                        st.success("No stereotypical LLM clichés detected. Natural vocabulary diversity observed.")

                    # Highlight buzzwords in text
                    highlighted_html = user_text
                    for b in detected_buzzwords:
                        pattern = re.compile(rf'\b({re.escape(b)})\b', re.IGNORECASE)
                        highlighted_html = pattern.sub(r'<span class="highlight-buzzword">\1</span>', highlighted_html)

                    st.markdown(
                        f"""
                        <div style="background: rgba(13, 17, 23, 0.9); border: 1px solid #30363D; border-radius: 8px; padding: 1rem; font-size: 0.92rem; line-height: 1.6;">
                            {highlighted_html}
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.error("Please enter at least one complete sentence to analyze.")

    # -------------------------------------------------------------------------
    # DEMO 2: DPI PACKET CLASSIFIER SIMULATOR
    # -------------------------------------------------------------------------
    elif "DPI 5-Tuple" in demo_selector:
        st.markdown("### 📡 Deep Packet Inspection & 5-Tuple Sharding Simulator")
        st.write("Demonstrates how raw PCAP frames are decoded, symmetric 5-tuples normalized, flows sharded via CRC32, and encrypted TLS SNI extracted.")

        sim_scenario = st.selectbox(
            "Select Real-World Traffic Flow Scenario:",
            [
                "Streaming Media: TLS Client Hello -> www.youtube.com (Port 443)",
                "Developer API: TLS Client Hello -> api.github.com (Port 443)",
                "Cloud Entertainment: TLS Client Hello -> www.netflix.com (Port 443)",
                "Enterprise Core: TLS Client Hello -> login.microsoftonline.com (Port 443)"
            ]
        )

        flow_configs = {
            "Streaming Media: TLS Client Hello -> www.youtube.com (Port 443)": {
                "src_ip": "192.168.1.105", "dst_ip": "142.250.190.46", "src_port": 54210, "dst_port": 443,
                "proto": "TCP (6)", "sni": "www.youtube.com", "app": "YouTube / Google Video",
                "cat": "Streaming Media", "rule_action": "ALLOW & QoS Tier 1"
            },
            "Developer API: TLS Client Hello -> api.github.com (Port 443)": {
                "src_ip": "192.168.1.105", "dst_ip": "140.82.121.6", "src_port": 49832, "dst_port": 443,
                "proto": "TCP (6)", "sni": "api.github.com", "app": "GitHub API / VCS",
                "cat": "Developer Infrastructure", "rule_action": "ALLOW & Unrestricted"
            },
            "Cloud Entertainment: TLS Client Hello -> www.netflix.com (Port 443)": {
                "src_ip": "192.168.1.144", "dst_ip": "54.154.212.10", "src_port": 61205, "dst_port": 443,
                "proto": "TCP (6)", "sni": "www.netflix.com", "app": "Netflix Streaming",
                "cat": "Entertainment / Video", "rule_action": "ALLOW & Bandwidth Cap"
            },
            "Enterprise Core: TLS Client Hello -> login.microsoftonline.com (Port 443)": {
                "src_ip": "10.0.4.88", "dst_ip": "20.190.159.2", "src_port": 51044, "dst_port": 443,
                "proto": "TCP (6)", "sni": "login.microsoftonline.com", "app": "Microsoft Entra ID",
                "cat": "Authentication / Cloud", "rule_action": "PRIORITY ALLOW"
            }
        }

        cfg = flow_configs[sim_scenario]

        # Compute Symmetric Canonical 5-tuple
        ip_pair = sorted([cfg["src_ip"], cfg["dst_ip"]])
        port_pair = sorted([cfg["src_port"], cfg["dst_port"]])
        canonical_key = f"{ip_pair[0]}:{port_pair[0]} <-> {ip_pair[1]}:{port_pair[1]} | {cfg['proto']}"

        # CRC32 consistent hash
        crc_val = zlib.crc32(canonical_key.encode('utf-8'))
        worker_id = crc_val % 4  # 4 multiprocessing workers

        c1, c2 = st.columns(2)

        with c1:
            st.markdown("#### 📦 Raw Packet Decoding (Struct Simulation)")
            st.code(
                f"""
[ETHERNET II FRAME]
  ├─ Destination MAC : 00:1a:2b:3c:4d:5e
  ├─ Source MAC      : 74:d4:35:e8:12:ab
  └─ EtherType       : 0x0800 (IPv4)

[IPv4 HEADER - 20 Bytes parsed with struct]
  ├─ Version/IHL     : 4 / 5 (20 bytes)
  ├─ Total Length    : 517 bytes
  ├─ TTL / Protocol  : 64 / {cfg['proto']}
  ├─ Source IP       : {cfg['src_ip']}
  └─ Destination IP  : {cfg['dst_ip']}

[TCP HEADER - 20 Bytes parsed with struct]
  ├─ Source Port     : {cfg['src_port']}
  ├─ Dest Port       : {cfg['dst_port']}
  ├─ Sequence Num    : 1048576201
  └─ Flags           : [PSH, ACK]

[TLS RECORD DISSECTION - RFC 6066]
  ├─ Content Type    : 0x16 (Handshake)
  ├─ Handshake Type  : 0x01 (Client Hello)
  ├─ TLS Version     : TLS 1.2 / 1.3 (0x0303)
  └─ Extension 0x0000: Server Name Indication (SNI)
       └─ Extracted Domain: "{cfg['sni']}"
                """,
                language="yaml"
            )

        with c2:
            st.markdown("#### ⚙️ Multiprocessing Sharding & Flow State")
            st.success(f"**Canonical 5-Tuple (Symmetric):**\n`{canonical_key}`")
            st.info(f"**Consistent Hash (CRC32):** `{crc_val:#010x}`")
            st.markdown(
                f"""
                <div style="background: rgba(0, 210, 255, 0.1); border: 1px solid #00D2FF; border-radius: 8px; padding: 1rem; margin-bottom: 1rem;">
                    <div style="font-size: 0.85rem; color: #8B949E;">ASSIGNED WORKER PROCESS</div>
                    <div style="font-size: 1.8rem; font-weight: 800; color: #00D2FF;">Worker Core #{worker_id}</div>
                    <div style="font-size: 0.8rem; color: #C9D1D9;">Guarantees lock-free flow table memory without thread contention.</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown("#### 🎯 Rule Engine Policy Verdict")
            st.markdown(f"- **Detected Application:** `{cfg['app']}`")
            st.markdown(f"- **Traffic Category:** `{cfg['cat']}`")
            st.markdown(f"- **Enforcement Verdict:** `{cfg['rule_action']}`")

    # -------------------------------------------------------------------------
    # DEMO 3: AI LEARNING COMPANION QUIZ SIMULATOR
    # -------------------------------------------------------------------------
    elif "Quiz Simulator" in demo_selector:
        st.markdown("### 🧠 AI Learning Companion - Quiz & Retention Engine")
        st.write("Demonstrates how Hari's RAG and LLM companion generates adaptive assessment questions from ingested course notes.")

        topic = st.selectbox(
            "Select Subject Domain:",
            ["Computer Networking & Protocol Architecture", "Machine Learning & Deep Learning", "Operating Systems & Concurrency"]
        )

        quiz_bank = {
            "Computer Networking & Protocol Architecture": {
                "q": "Why is the Server Name Indication (SNI) extension readable in a TLS handshake before encryption begins?",
                "options": [
                    "A) Because it is part of the initial unencrypted Client Hello payload to let the server present the correct certificate.",
                    "B) Because TLS 1.3 disables encryption on all extension fields by default.",
                    "C) Because the client encrypts it with an insecure static pre-shared key.",
                    "D) Because TCP checksumming requires cleartext hostnames for routing."
                ],
                "correct": 0,
                "explanation": "RFC 6066 defines SNI in the TLS Client Hello handshake record. Because the client does not yet have the server's public key or negotiated cipher suite, the Client Hello must be sent in cleartext, enabling DPI engines to classify encrypted traffic."
            },
            "Machine Learning & Deep Learning": {
                "q": "In a dual-tier text classification pipeline, why calculate statistical burstiness before feeding payloads into a transformer?",
                "options": [
                    "A) Transformers cannot tokenize texts with more than 10 words.",
                    "B) Burstiness filters predictable variance in 5ms, saving expensive transformer inference on obvious cases.",
                    "C) Burstiness automatically optimizes learning rates during backpropagation.",
                    "D) PyTorch requires burstiness weights to compute cross-entropy loss."
                ],
                "correct": 1,
                "explanation": "Stylometric metrics like burstiness and cliché density run via NumPy/NLTK in single-digit milliseconds. Filtering obvious payloads in Tier 1 drastically lowers GPU compute costs and response latency."
            },
            "Operating Systems & Concurrency": {
                "q": "What is the primary advantage of consistent hash sharding (CRC32) across multiprocessing packet workers?",
                "options": [
                    "A) It compresses IPv4 packets to 8 bits.",
                    "B) It maps all packets of a bidirectional flow to the exact same worker, eliminating cross-process locks.",
                    "C) It replaces the operating system kernel network stack entirely.",
                    "D) It converts TCP streams into asynchronous UDP datagrams."
                ],
                "correct": 1,
                "explanation": "Consistent hashing on the canonical 5-tuple guarantees that packets belonging to the same connection are always handled by the same worker core. This achieves 100% lock-free flow tables and linear CPU scaling."
            }
        }

        q_data = quiz_bank[topic]

        st.markdown(f"#### ❓ Question: {q_data['q']}")
        user_choice = st.radio("Choose the correct option:", q_data["options"], index=None)

        if st.button("Submit Answer", type="primary"):
            if user_choice is not None:
                selected_idx = q_data["options"].index(user_choice)
                if selected_idx == q_data["correct"]:
                    st.success("🎉 Correct Answer!")
                else:
                    st.error("❌ Not quite right.")
                st.info(f"**Explanation:** {q_data['explanation']}")
            else:
                st.warning("Please select an answer choice first.")


# =============================================================================
# SECTION 4: TECHNICAL SKILLS
# =============================================================================
elif nav_choice == "🛠️ Technical Skills":
    st.markdown("## 🛠️ Technical Skills & Proficiencies")
    st.caption("Core technical capabilities, tools, and platforms mastered through academic coursework and real-world system builds.")

    col_skill_chart, col_skill_tags = st.columns([1.3, 1])

    with col_skill_chart:
        st.markdown("### 📊 Skill Proficiency Overview")
        skill_categories = [
            "AI / LLMs & RAG",
            "Networking Systems",
            "Containerization & DevOps",
            "Python Development",
            "Low-Level / C",
            "Databases & SQL"
        ]
        skill_scores = [92, 90, 88, 95, 80, 85]

        fig_radar = go.Figure(data=go.Scatterpolar(
            r=skill_scores + [skill_scores[0]],
            theta=skill_categories + [skill_categories[0]],
            fill='toself',
            fillcolor='rgba(0, 210, 255, 0.25)',
            line=dict(color='#00D2FF', width=2),
            marker=dict(size=6, color='#58A6FF')
        ))

        fig_radar.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 100],
                    tickfont=dict(color='#8B949E', size=9),
                    gridcolor='rgba(255, 255, 255, 0.1)'
                ),
                angularaxis=dict(
                    tickfont=dict(color='#E6EDF3', size=11),
                    gridcolor='rgba(255, 255, 255, 0.1)'
                ),
                bgcolor='rgba(13, 17, 23, 0.8)'
            ),
            paper_bgcolor='rgba(0,0,0,0)',
            margin=dict(l=40, r=40, t=30, b=30),
            height=340
        )
        st.plotly_chart(fig_radar, use_container_width=True)

    with col_skill_tags:
        st.markdown("### 💻 Categorized Skillset")

        st.markdown("##### 🤖 AI & Machine Learning")
        st.markdown("""
        `LangChain` `Retrieval-Augmented Generation (RAG)` `Google Gemini API` `Hugging Face` 
        `TensorFlow` `PyTorch` `Scikit-Learn` `FAISS` `Chroma DB` `NumPy` `Pandas` `NLTK`
        """)

        st.markdown("##### 🐳 DevOps & Monitoring")
        st.markdown("""
        `Docker` `Docker Compose` `GitHub Actions (CI/CD)` `Prometheus` `Grafana` 
        `GHCR Container Registry` `Linux / Ubuntu`
        """)

        st.markdown("##### 📡 Networking & Low-Level")
        st.markdown("""
        `TCP/IP` `TLS Handshake Dissection` `PCAP Analysis` `Raw Sockets` 
        `Python Struct` `Multiprocessing` `RFC 6066 SNI`
        """)

        st.markdown("##### 🗄️ Web, Databases & Tools")
        st.markdown("""
        `Python` `C` `JavaScript` `FastAPI` `Flask` `HTML/CSS` 
        `MySQL` `MongoDB` `SQLite` `Power BI` `Git` `Postman`
        """)


# =============================================================================
# SECTION 5: EDUCATION & JOURNEY
# =============================================================================
elif nav_choice == "🎓 Education & Journey":
    st.markdown("## 🎓 Education & Academic Milestones")
    st.caption("Academic journey, degrees, and academic performance track record.")

    st.markdown(
        """
        <div class="timeline-item">
            <div style="font-size: 1.25rem; font-weight: 700; color: #00D2FF;">
                Bachelor of Engineering (B.E.) — Artificial Intelligence & Machine Learning
            </div>
            <div style="font-size: 0.95rem; color: #F0F6FC; margin-bottom: 0.2rem;">
                <strong>CMR Institute of Technology (CMRIT)</strong>, Bengaluru, Karnataka
            </div>
            <div style="font-size: 0.85rem; color: #58A6FF; font-weight: 600;">
                2023 – 2027 (Currently Pursuing) • CGPA: 8.08 / 10.0
            </div>
            <p style="font-size: 0.9rem; color: #C9D1D9; margin-top: 0.5rem;">
                Focused on applied artificial intelligence, deep learning architectures, network protocols, 
                distributed systems, and containerized cloud application engineering. Active member of technical clubs.
            </p>
        </div>

        <div class="timeline-item">
            <div style="font-size: 1.25rem; font-weight: 700; color: #00D2FF;">
                Pre-University Course (PUC) — Science PCMB
            </div>
            <div style="font-size: 0.95rem; color: #F0F6FC; margin-bottom: 0.2rem;">
                <strong>Hassan Public PU College</strong>, Hassan, Karnataka
            </div>
            <div style="font-size: 0.85rem; color: #3FB950; font-weight: 600;">
                Completed 2022 • Score: 92.83%
            </div>
            <p style="font-size: 0.9rem; color: #C9D1D9; margin-top: 0.5rem;">
                Specialized in Physics, Chemistry, Mathematics, and Biology with high distinction. Built strong analytical foundations.
            </p>
        </div>

        <div class="timeline-item">
            <div style="font-size: 1.25rem; font-weight: 700; color: #00D2FF;">
                Secondary School Leaving Certificate (SSLC)
            </div>
            <div style="font-size: 0.95rem; color: #F0F6FC; margin-bottom: 0.2rem;">
                <strong>Brilliant Public School</strong>, Hassan, Karnataka
            </div>
            <div style="font-size: 0.85rem; color: #3FB950; font-weight: 600;">
                Completed 2020 • Score: 89.76%
            </div>
            <p style="font-size: 0.9rem; color: #C9D1D9; margin-top: 0.5rem;">
                Graduated with distinction with top honors in mathematics and physical sciences.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# =============================================================================
# SECTION 6: HACKATHONS & ACTIVITIES
# =============================================================================
elif nav_choice == "🏆 Hackathons & Activities":
    st.markdown("## 🏆 Hackathons, Activities & Certifications")
    st.caption("Competitive hackathons, university technical clubs, professional certifications, and athletic achievements.")

    c1, c2 = st.columns(2)

    with c1:
        st.markdown("### 🚀 Hackathon Competitions")
        st.markdown(
            """
            <div class="card-box">
                <div style="font-size: 1.15rem; font-weight: 700; color: #F0F6FC;">
                    MEMBRAIN AI Hackathon
                </div>
                <div style="font-size: 0.85rem; color: #58A6FF;">CMR Institute of Technology (2026)</div>
                <p style="font-size: 0.88rem; color: #C9D1D9; margin-top: 0.5rem;">
                    Competed in building intelligent, agentic systems leveraging modern generative AI models and real-time knowledge graphs.
                </p>
            </div>

            <div class="card-box">
                <div style="font-size: 1.15rem; font-weight: 700; color: #F0F6FC;">
                    ML Matrix Hackathon
                </div>
                <div style="font-size: 0.85rem; color: #58A6FF;">BMS College of Engineering (BMSCE) (2025)</div>
                <p style="font-size: 0.88rem; color: #C9D1D9; margin-top: 0.5rem;">
                    Participated in rapid ML modeling, feature engineering, and latency-optimized inference pipelines under tight deadlines.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    with c2:
        st.markdown("### 🏅 Certifications & Clubs")
        st.markdown(
            """
            <div class="card-box">
                <div style="font-size: 1.15rem; font-weight: 700; color: #F0F6FC;">
                    📜 Complete ML, NLP, DL, Data Science Bootcamp
                </div>
                <div style="font-size: 0.85rem; color: #3FB950;">Udemy Certified Professional</div>
                <p style="font-size: 0.88rem; color: #C9D1D9; margin-top: 0.5rem;">
                    Comprehensive practical mastery of machine learning, neural architectures, natural language processing, and statistical data pipelines.
                </p>
            </div>

            <div class="card-box">
                <div style="font-size: 1.15rem; font-weight: 700; color: #F0F6FC;">
                    🤖 BrainBot Technical Club
                </div>
                <div style="font-size: 0.85rem; color: #D2A8FF;">CMRIT (2024)</div>
                <p style="font-size: 0.88rem; color: #C9D1D9; margin-top: 0.5rem;">
                    Active contributor to campus robotics and intelligent automation workshops and technical challenges.
                </p>
            </div>

            <div class="card-box">
                <div style="font-size: 1.15rem; font-weight: 700; color: #F0F6FC;">
                    🏐 Ignite 2025 Volleyball Tournament
                </div>
                <div style="font-size: 0.85rem; color: #F0883E;">Inter-Department Athletics</div>
                <p style="font-size: 0.88rem; color: #C9D1D9; margin-top: 0.5rem;">
                    Represented the department in the competitive volleyball tournament; avid cricket and football player.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =============================================================================
# SECTION 7: CONTACT & CONNECT
# =============================================================================
elif nav_choice == "📬 Contact & Connect":
    st.markdown("## 📬 Get In Touch & Hire Me")
    st.write("I am actively seeking software engineering, AI/ML, and systems development roles. Feel free to reach out directly!")

    col_info, col_form = st.columns([1, 1.2])

    with col_info:
        st.markdown("### 📞 Contact Details")
        st.markdown("""
        - **Full Name:** Hari Krishna RL
        - **Primary Email:** [hraj488.884@gmail.com](mailto:hraj488.884@gmail.com)
        - **Academic Email:** [harl23aiml@cmrit.ac.in](mailto:harl23aiml@cmrit.ac.in)
        - **Direct Phone:** `+91 9916766556`
        - **Current Address:** Sri Satya Sai PG, 4th Cross Kundalahalli Colony, AECS Layout, Bengaluru, Karnataka - 560037
        - **Permanent Address:** Salagame Gate, Saraswathi Puram, Hassan, Karnataka
        """)

        st.markdown("### 🌐 Online Profiles")
        st.markdown("""
        - 💼 [LinkedIn Profile](https://www.linkedin.com/in/hari-krishna-rl-058088298/)
        - 🐙 [GitHub Profile](https://github.com/Harikrishnarl)
        - 🧩 [LeetCode Profile](https://leetcode.com/u/Harikrishnarl/)
        """)

    with col_form:
        st.markdown("### 💬 Direct Message Form")
        with st.form("contact_form"):
            sender_name = st.text_input("Your Name / Organization *")
            sender_email = st.text_input("Your Email Address *")
            sender_subject = st.text_input("Subject", value="Opportunity / Collaboration Inquiry")
            sender_message = st.text_area("Your Message *", height=120)

            submitted = st.form_submit_button("🚀 Send Message", type="primary", use_container_width=True)

            if submitted:
                if sender_name and sender_email and sender_message:
                    st.success(f"Thank you, {sender_name}! Your inquiry has been registered. You can also send this directly via your email client using the link below.")
                    mailto_link = f"mailto:hraj488.884@gmail.com?subject={sender_subject}&body=From:%20{sender_name}%20({sender_email})%0A%0A{sender_message}"
                    st.markdown(f'<a href="{mailto_link}" target="_blank" class="contact-btn">✉️ Open in Email Client</a>', unsafe_allow_html=True)
                else:
                    st.error("Please fill in all required fields (Name, Email, and Message).")

# -----------------------------------------------------------------------------
# FOOTER
# -----------------------------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align: center; color: #8B949E; font-size: 0.85rem; padding: 1rem 0;">
        Crafted by <strong>Hari Krishna RL</strong> • Built with <strong>Streamlit</strong> & <strong>Plotly</strong> • Ready for Cloud Deployment
    </div>
    """,
    unsafe_allow_html=True
)
