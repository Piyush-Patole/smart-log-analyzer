🧠 Disclaimer
This project was created based on my original idea and developed with the assistance of AI tools, including ChatGPT by OpenAI. I used AI primarily to help with code generation, bug fixing, and writing documentation. All architectural decisions, problem statements, and final integrations were made by me, demonstrating my ability to leverage advanced tools effectively in real-world software development.



## 🔍 Smart Log Analyzer with AI Suggestions

An intelligent log file analysis tool that parses unstructured logs, classifies errors using NLP, and generates fix suggestions—automating part of the debugging process. Designed for DevOps, SREs, and developers to save time on log analysis and issue resolution.

---

## 🚀 Project Motivation

I built this project as a **Tech Associate** with 1 year of experience, with the goal of:
- Strengthening skills in Python, NLP, and data engineering
- Creating a job-ready portfolio project
- Solving a real-world problem: **debugging logs efficiently**

---

## 💡 Key Features

| Feature | Description |
|--------|-------------|
| 🔎 Log Parsing | Supports reading plain-text logs |
| 🧠 AI-based Classification | Uses NLP to group and label error types |
| 🧰 Auto Suggestions | Maps known patterns to likely fixes |
| 📊 Summary Reporting | Saves visual summary and detailed CSV/JSON reports |
| 🔗 Helpful Resources | Links error patterns to relevant docs or Stack Overflow |
| 🧩 Modular Design | Easy to extend for multiple log formats or error types |

---

## 🏗️ Project Architecture

```

smart-log-analyzer/
│
├── logs/               # Sample or user log files
├── reports/            # Output reports (CSV, JSON, PNG)
├── src/
│   ├── reader.py       # Reads log file into DataFrame
│   ├── parser.py       # Extracts and structures error info
│   ├── classifier.py   # Categorizes errors with NLP
│   ├── suggester.py    # Suggests fixes based on rules/patterns
│   ├── reporter.py     # Saves reports & visualizations
│   └── main.py         # Entry point
├── requirements.txt
└── README.md

````

---

## 🧠 Tech Stack & Justification

| Tool/Library | Purpose | Why this tool? | Alternatives |
|--------------|---------|----------------|--------------|
| **Python** | Primary language | Fast prototyping, strong ecosystem | Java, Go |
| **Pandas** | Log storage and analysis | Data manipulation is easy | Dask, Polars |
| **spaCy** | NLP for error classification | Lightweight, production-ready | NLTK, HuggingFace |
| **Regex** | Pattern matching | Ideal for extracting timestamps/errors | Parsers, PyParsing |
| **Seaborn & Matplotlib** | Visualization of errors | Easy for summaries | Plotly, Bokeh |
| **JSON, CSV** | Report formats | Standard for log/reporting data | XML, YAML |

> 🔗 **Inspiration/Reference:** [Salesforce LogAI](https://github.com/salesforce/logai)

---

## 🔧 Installation & Setup

### 🛠️ Prerequisites
- Python 3.9+
- Git
- Conda (Recommended) or virtualenv

### 📥 Step-by-Step Setup

```bash
# Step 1: Clone the repo
git clone https://github.com/yourusername/smart-log-analyzer.git
cd smart-log-analyzer

# Step 2: Create environment
conda create -n loganalyzer python=3.9
conda activate loganalyzer

# Step 3: Install dependencies
pip install -r requirements.txt

# Step 4: Download spaCy model
python -m spacy download en_core_web_sm
````

---

## 🔍 How to Use

### 📁 Prepare Logs

Place your `.log` files in the `logs/` folder. Example file: `logs/plain.log`

### ▶️ Run the Analyzer

```bash
python -m src.main logs/plain.log default
```

### 📤 Output

| File                  | Location   | Description                          |
| --------------------- | ---------- | ------------------------------------ |
| `enriched_output.csv` | `reports/` | Logs with categories and suggestions |
| `error_summary.json`  | `reports/` | Counts of each error type            |
| `error_summary.png`   | `reports/` | Bar chart of error distribution      |

---

## 📸 Sample Output Preview

```
Input Log:
[2024-05-10 11:35:26] ERROR: Database connection failed
[2024-05-10 11:35:45] WARNING: Deprecated API used

Output CSV:
timestamp                | level   | message                       | category        | suggestion
------------------------|---------|-------------------------------|------------------|----------------------------
2024-05-10 11:35:26     | ERROR   | Database connection failed    | Database Error   | Check database settings.
2024-05-10 11:35:45     | WARNING | Deprecated API used           | Unknown          | Refer to docs or StackOverflow
```

---

## 🔬 Under the Hood

### 1. `reader.py`

Reads a plain log file and loads lines into a Pandas DataFrame.

### 2. `parser.py`

Uses regex to extract timestamps, error levels, and messages.

### 3. `classifier.py`

Uses spaCy’s NLP model to classify log lines into categories like:

* Database Error
* Timeout
* Not Found
* Unknown

### 4. `suggester.py`

Maps each category to predefined suggestions. Can be extended with GPT API or retrieval-augmented generation.

### 5. `reporter.py`

Generates:

* A CSV with full details
* JSON summary
* PNG chart using Seaborn

---

## 🌱 Future Enhancements

* [ ] Support JSON, syslog & Apache formats
* [ ] Integrate GPT for smarter suggestions
* [ ] Real-time log stream analysis
* [ ] GUI or web dashboard (Streamlit/FastAPI)

---

## 🧠 Learning Outcomes

* 🧩 Modular Python architecture
* 🤖 NLP classification using spaCy
* 🐍 Pandas data engineering
* 📊 Automated visualization
* 📁 Real-world log parsing and debugging

---

## 📚 Credits & Resources

* [Salesforce LogAI](https://github.com/salesforce/logai)
* [spaCy NLP](https://spacy.io/)
* [Pandas Documentation](https://pandas.pydata.org/)
* [Seaborn Visualization](https://seaborn.pydata.org/)
* Stack Overflow patterns dataset (self-curated)

---

## 💼 Use in Your Resume or Portfolio

You can showcase this project as:

> **"Built a Smart Log Analyzer in Python using NLP and data visualization to automate log parsing, classification, and solution mapping. Inspired by Salesforce LogAI. Delivered modular design with CSV/JSON reports and visual charts."**

---

## 📬 Contact

**Author**: Piyush Patole
**Email**: [your.email@example.com](mailto:your.email@example.com)
**LinkedIn**: [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)

---

```

---

### ✅ Next Steps
- Replace `your.email@example.com` and GitHub links with your info.
- Want me to turn this into a GitHub `README.md` with badges and interactive demo support? I can help with that too.

Would you like a one-liner version of this project for your resume as well?
```
