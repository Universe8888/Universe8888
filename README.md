<div align="center">

<!-- Typing SVG tagline -->
<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=Boris+Manzov+%F0%9F%91%8B;Lead+IT+Ops+%C3%97+AI+Engineer;Building+agents+that+audit+knowledge+bases;Local-first+%C2%B7+Evaluated+%C2%B7+No+vendor+lock" alt="Typing SVG" />

**Lead IT Operations @ DraftKings Inc. · AI Engineer · Python Practitioner**

*Bridging enterprise IT operations with software engineering, building agentic systems, automation pipelines, and data-driven knowledge tools.*

[![LinkedIn](https://img.shields.io/badge/LinkedIn-boris--manzov-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/boris-manzov-47775623a/)
[![GitHub](https://img.shields.io/badge/GitHub-Universe8888-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Universe8888)
[![Email](https://img.shields.io/badge/Email-bobibobcho%40gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white)](mailto:bobibobcho@gmail.com)
[![Profile Views](https://komarev.com/ghpvc/?username=Universe8888&label=Profile+Views&color=58a6ff&style=for-the-badge)](https://github.com/Universe8888)

</div>

---

## About Me

- 🏢 Managing global IT operations & procurement at **DraftKings Inc.** — EMEA fleet, vendor negotiations, ISO 27001 compliance, Freshservice automation
- 🤖 Building **local-first AI agents** with reproducible evals — if it can't be benchmarked, it doesn't ship
- 🌱 Deep in **RAG architectures**, agentic pipelines, and knowledge graph tooling
- 💬 Ask me about **Python automation**, **IT asset management**, or **Obsidian knowledge systems**
- ⚡ Fun fact: I wrote a tool that found contradictions in my own notes — and it was right

---

## ✨ Featured Project

<div align="center">

### [wikilens](https://github.com/Universe8888/wikilens) &nbsp;·&nbsp; `pip install wikilens`

**8 evaluated agents. One command. Any Markdown vault.**

*Turns a folder of notes into a queryable, auditable, self-aware knowledge system.*

[![Stars](https://img.shields.io/github/stars/Universe8888/wikilens?style=for-the-badge&logo=starship&color=58a6ff&labelColor=1F2937)](https://github.com/Universe8888/wikilens)
[![License](https://img.shields.io/github/license/Universe8888/wikilens?style=for-the-badge&color=10b981&labelColor=1F2937)](https://github.com/Universe8888/wikilens/blob/main/LICENSE)
[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=1F2937)](https://github.com/Universe8888/wikilens)
[![PyPI](https://img.shields.io/badge/PyPI-wikilens-orange?style=for-the-badge&logo=pypi&logoColor=white&labelColor=1F2937)](https://pypi.org/project/wikilens/)

</div>

<table>
<tr>
<td width="50%" valign="top">

**8 agents, each with published benchmarks:**

| Agent | What it finds | Best score |
|-------|--------------|-----------|
| `audit` | Broken wikilinks, orphans, shadowed basenames | **F1 = 1.00** |
| `query` | Semantic search · dense + BM25 + RRF + rerank | **Hit@5 = 1.00** |
| `gap` | Unanswered questions implied by vault content | **Recall = 1.00** |
| `confidence` | Claims below epistemic threshold (5-level scale) | **F1 = 0.89** |
| `contradict` | Conflicting claim pairs across notes | F1 = 0.82 |
| `answer` | Drafts cited stub notes for identified gaps | Pass = 0.80 |
| `drift` | Beliefs that shifted over git history | P ≥ 0.80 target |
| `concepts` | Notes circling an unnamed concept | F1 ≥ 0.70 target |

</td>
<td width="50%" valign="top">

**Why it's different:**

- 🏠 **Local-first** — notes never leave your machine unless you opt into a remote LLM
- 📊 **Evaluated, not vibes** — every agent ships with hand-labeled fixtures and a published F1/recall score
- 🔀 **No vendor lock** — swappable embeddings (BAAI/bge), vector stores (LanceDB/Chroma), LLM backends (OpenAI / Claude)
- 🔍 **Hybrid retrieval** — dense + BM25 + RRF fusion + cross-encoder reranking; Hit@5 = 1.00 in every mode
- 🚦 **CI-gate ready** — `audit` exits 0/1/2, drop it straight into pre-commit or GitHub Actions
- 📝 **Proof-carrying answers** — every drafted note stub carries `[^N]` citations resolving to vault chunk IDs; attribution rate = 1.00

```bash
pip install wikilens
wikilens ingest ./my-vault
wikilens audit ./my-vault
wikilens query "what did I conclude about X"
```

</td>
</tr>
</table>

---

## 🔬 Other Projects

<table>
<tr>
<td width="50%" valign="top">

### [Pre-Viral Tracker](https://github.com/Universe8888/pre-viral)
**Detect accelerating niche topics before they hit mainstream.**

A full-stack trend discovery engine using derivative calculus (velocity & acceleration scoring) on Google Trends data.

`Python` `FastAPI` `SQLite` `NumPy` `SciPy` `React` `Vite` `Recharts`

- 📐 d²V/dt² acceleration as core ranking signal
- 🌍 8 geo zones — Global, US, UK, EU Big 4, BG
- 🧪 60+ unit tests across math, DB, API, and ingestion
- 🎨 Glassmorphism dark-mode dashboard

[![Stars](https://img.shields.io/github/stars/Universe8888/pre-viral?style=flat-square&labelColor=1F2937)](https://github.com/Universe8888/pre-viral)
[![Issues](https://img.shields.io/github/issues/Universe8888/pre-viral?style=flat-square&labelColor=1F2937)](https://github.com/Universe8888/pre-viral/issues)

</td>
<td width="50%" valign="top">

### [Job Hunt Automator](https://github.com/Universe8888/job-hunt-automator)
**AI-powered job scraping with resume matching.**

Automated scraper for LinkedIn & Jobs.bg with NLP-driven resume comparison and stealth browser automation.

`Python` `Playwright` `NLP` `CSV`

- 🕵️ Stealth browser automation with session persistence
- 🧠 AI-powered resume-to-job matching scores
- 📊 Structured CSV export for analysis
- ⚠️ Built for small-scale educational use

[![Stars](https://img.shields.io/github/stars/Universe8888/job-hunt-automator?style=flat-square&labelColor=1F2937)](https://github.com/Universe8888/job-hunt-automator)
[![Issues](https://img.shields.io/github/issues/Universe8888/job-hunt-automator?style=flat-square&labelColor=1F2937)](https://github.com/Universe8888/job-hunt-automator/issues)

</td>
</tr>
</table>

---

## 🛠️ Tech Stack

<div align="center">

#### Languages
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)
![TypeScript](https://img.shields.io/badge/T--SQL-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)
![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)

#### Frameworks & Libraries
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=nodedotjs&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![SciPy](https://img.shields.io/badge/SciPy-8CAAE6?style=flat-square&logo=scipy&logoColor=white)

#### AI & ML
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![Anthropic](https://img.shields.io/badge/Anthropic-Claude-CC785C?style=flat-square&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![LanceDB](https://img.shields.io/badge/LanceDB-Vector_Store-58a6ff?style=flat-square&logoColor=white)

#### Data & Automation
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33?style=flat-square&logo=playwright&logoColor=white)
![Recharts](https://img.shields.io/badge/Recharts-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)

#### Enterprise & Workflow
![ServiceNow](https://img.shields.io/badge/ServiceNow-62D84E?style=flat-square&logo=servicenow&logoColor=white)
![Jira](https://img.shields.io/badge/Jira-0052CC?style=flat-square&logo=jira&logoColor=white)
![Microsoft 365](https://img.shields.io/badge/Microsoft_365-D83B01?style=flat-square&logo=microsoft&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

</div>

---

## 📊 GitHub Stats

<div align="center">
  <!-- GitHub Stats (Using a more stable community endpoint) -->
  <img src="https://github-readme-stats-tau-six.vercel.app/api?username=Universe8888&show_icons=true&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=58a6ff&icon_color=58a6ff&text_color=c9d1d9&ring_color=58a6ff" alt="GitHub Stats" height="165" />
  
  <!-- GitHub Streak -->
  <img src="https://github-readme-streak-stats.demolab.com?user=Universe8888&theme=tokyonight&hide_border=true&background=0d1117&ring=58a6ff&fire=58a6ff&currStreakLabel=58a6ff" alt="GitHub Streak" height="165" />
</div>

<div align="center">
  <!-- Top Languages (Using the alternative endpoint) -->
  <img src="https://github-readme-stats-tau-six.vercel.app/api/top-langs/?username=Universe8888&layout=compact&theme=tokyonight&hide_border=true&bg_color=0d1117&title_color=58a6ff&text_color=c9d1d9" alt="Top Languages" height="130" />
</div>

---

## 🎓 Certifications (2025)

<details>
<summary><strong>🤖 AI & Generative AI</strong></summary>

| Certification | Issuer | Date |
|--------------|--------|------|
| AI Agent Developer Specialization | Vanderbilt University | Jun 2025 |
| Advanced RAG with Vector Databases and Retrievers | IBM | Oct 2025 |
| Vector Databases for RAG: An Introduction | IBM | Oct 2025 |
| Build RAG Applications: Get Started | IBM | Sep 2025 |
| Develop Generative AI Applications: Get Started | IBM | Sep 2025 |
| Exploratory Data Analysis for Machine Learning | IBM | Jul 2025 |

</details>

<details>
<summary><strong>📊 Data Analytics & Visualization</strong></summary>

| Certification | Issuer | Date |
|--------------|--------|------|
| Advanced Data Visualization with Tableau | Tableau | Jul 2025 |
| Data Visualization with Tableau | Tableau | May 2025 |
| Introduction to Tableau | Tableau | May 2025 |
| Data Ecosystem | Tableau | May 2025 |
| Business Analysis Process | Tableau | May 2025 |
| Introduction to Business Analytics | Tableau | May 2025 |
| Python Data Analytics | Meta | May 2025 |

</details>

<details>
<summary><strong>🐍 Python & Systems</strong></summary>

| Certification | Issuer | Date |
|--------------|--------|------|
| Using Python to Interact with the Operating System | Google | Jun 2025 |
| Crash Course on Python | Google | Jun 2025 |

</details>

<details>
<summary><strong>📦 Supply Chain & Operations</strong></summary>

| Certification | Issuer | Date |
|--------------|--------|------|
| Leverage Data Science for a More Agile Supply Chain (Specialization) | UC Irvine | May 2025 |
| Supply Chain Optimization | UC Irvine | May 2025 |
| Inventory Management | UC Irvine | May 2025 |

</details>

<details>
<summary><strong>💻 Software Engineering (SoftUni)</strong></summary>

| Certification | Issuer |
|--------------|--------|
| Programming Advanced with JavaScript | Software University |
| Programming Fundamentals with JavaScript | Software University |
| Programming Basics with JavaScript | Software University |
| MS SQL (T-SQL) | Software University |
| Microsoft Excel Advanced | Software University |
| Microsoft Excel Fundamentals | Software University |

</details>

---

## 🌐 Languages

| Language | Level |
|----------|-------|
| 🇧🇬 Bulgarian | Native |
| 🇬🇧 English | Fluent |
| 🇮🇹 Italian | Intermediate |
| 🇩🇪 German | Intermediate |

---

<div align="center">

*Building tools that know what they don't know.* 🚀

**Plovdiv, Bulgaria · DraftKings Inc.**

</div>
