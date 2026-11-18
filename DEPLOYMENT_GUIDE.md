# 🚀 1-Click Deployment Guide for Streamlit Portfolio

This portfolio is configured to deploy effortlessly across multiple cloud platforms. Follow the option that best fits your workflow.

---

## 🌟 Option 1: Streamlit Community Cloud (Recommended — 100% Free, 2 Minutes)

Streamlit Community Cloud is the fastest, cleanest, and officially supported platform.

### Step 1: Push This Folder to GitHub
Open your terminal inside this folder (`d:\portfolio`) and run:
```bash
git init
git add .
git commit -m "feat: portfolio for Hari Krishna RL"
git branch -M main
git remote add origin https://github.com/<your-github-username>/portfolio.git
git push -u origin main
```
*(Replace `<your-github-username>` with your GitHub username, e.g. `Harikrishnarl`)*

### Step 2: Deploy on Streamlit Cloud
1. Go to [share.streamlit.io](https://share.streamlit.io/) and log in with your GitHub account.
2. Click the **"Create app"** or **"New app"** button.
3. Select your repository: `Harikrishnarl/portfolio`.
4. Set the **Main file path** to: `app.py`.
5. (Optional) Under **Advanced settings**, ensure Python version is set to `3.10` or `3.11`.
6. Click **Deploy!**

> ⏱️ **Build Time:** ~45 seconds.  
> Your portfolio will be live at `https://<your-custom-subdomain>.streamlit.app` with free SSL, automatic reloads whenever you push code, and zero maintenance!

---

## 🤗 Option 2: Hugging Face Spaces (Free Alternative)

1. Create a free account at [Hugging Face](https://huggingface.co/).
2. Click **New Space** (`https://huggingface.co/new-space`).
3. Choose:
   - **Space Name:** `hari-krishna-portfolio`
   - **Space SDK:** `Streamlit`
   - **Space Hardware:** Free (CPU Basic)
4. Clone your Space repo locally and copy all files from this folder into it, then push:
   ```bash
   git add .
   git commit -m "Deploy portfolio to HF Spaces"
   git push
   ```
5. Hugging Face automatically detects `requirements.txt` and runs `app.py`.

---

## 💻 Option 3: Run Locally on Your Machine

To test or run locally:

```bash
# 1. Create and activate a virtual environment (optional but recommended)
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/macOS:
source venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Launch Streamlit
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

---

## 🐳 Option 4: Docker & Docker Compose

If you want to run or deploy via Docker:

### Using Docker Compose (Easiest):
```bash
docker compose up -d
```
Access the application at `http://localhost:8501`.

### Using Docker CLI:
```bash
docker build -t hari-portfolio .
docker run -d -p 8501:8501 --name portfolio-app hari-portfolio
```

---

## 🌐 Option 5: Render (Free Tier Web Service)

1. Create a free account on [Render](https://render.com/).
2. Click **New +** -> **Web Service**.
3. Connect your GitHub repository.
4. Set configurations:
   - **Runtime:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
5. Click **Create Web Service**.

---

## 📁 File Structure Reference
```
portfolio/
├── .streamlit/
│   └── config.toml           # Modern dark UI theme configuration
├── assets/
│   ├── Hari_Krishna_RL_Resume.pdf  # Extracted official resume for 1-click download
│   └── profile.jpg                 # Extracted profile headshot photo
├── app.py                    # Main full-featured Streamlit portfolio application
├── requirements.txt          # Clean, ultra-fast cloud dependencies
├── Dockerfile                # Production multi-stage Dockerfile
├── docker-compose.yml        # Docker compose service definition
├── .gitignore                # Git ignore rules
├── .dockerignore              # Docker ignore rules
├── README.md                 # Project documentation
└── DEPLOYMENT_GUIDE.md       # Step-by-step deployment guide
```
