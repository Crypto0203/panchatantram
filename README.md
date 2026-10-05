# 🐰 Panchatantra Kids — 100-Episode Master Production Suite

Welcome to the **Panchatantra Kids Animation Production Suite**, a comprehensive studio-grade framework for producing 100 high-retention 3D animated shorts (Instagram Reels / YouTube Shorts) based on timeless Panchatantra, Hitopadesha, and Jataka tales.

---

## 🌟 Overview & Architecture

- **Total Episodes:** 100 Fully Scripted & Timed Stories
- **Video Format:** 30.0 Seconds Total Runtime $\rightarrow$ Exact **$3 \times 10\text{s}$ Clip Breakdown**:
  - **Clip 1 (00:00 – 00:10):** Thumb-Stopper Hook & The Trap
  - **Clip 2 (00:10 – 00:20):** Concrete Physical "Upayam" (Action Trick)
  - **Clip 3 (00:20 – 00:30):** Cause-and-Effect Climax, Moral, Next-Episode Bridge Teaser & Follow CTA
- **Visual Style:** 3D Disney-Pixar Animation (9:16 Vertical Ratio, 8K Unreal Engine 5 aesthetic)
- **Audio Language:** Authentic Spoken Telugu Voiceover + English Synchronized Subtitles + Detailed SFX Foley

---

## 🔒 Security & Vault Protection

The production dashboard features an encrypted **Security Vault**:
- Protected by salted **SHA-256 cryptographic hashing**.
- Zero plaintext PIN exposure in client code or network payloads.
- Includes automatic session timeout and quick-lock controls.

---

## 📁 Repository Structure

```
├── docs/                                          # Production Word Documents
│   ├── Panchatantra_Kids_Complete_30s_Production_Scripts.docx
│   └── Panchatantra_Kids_100_Episode_Master_Plan.docx
├── src/
│   ├── episodes.js                               # All 100 production scripts (300 clips)
│   ├── main.js                                   # Interactive dashboard logic & PIN vault
│   └── style.css                                 # Premium glassmorphic UI design system
├── index.html                                    # Main entry point
├── generate_100_accurate_scripts.py              # Script generator & validation pipeline
└── package.json                                  # Dependencies & build scripts
```

---

## 🚀 Running Locally

```bash
# Install dependencies
npm install

# Start local development server
npm run dev

# Build for production
npm run build
```

---

## ☁️ Deploying to Vercel

This repository is optimized for one-click deployment on **Vercel**:
1. Go to [vercel.com](https://vercel.com/) and click **Add New Project**.
2. Import the GitHub repository: `https://github.com/Crypto0203/panchatantram`.
3. Framework Preset: **Vite**.
4. Click **Deploy**.
