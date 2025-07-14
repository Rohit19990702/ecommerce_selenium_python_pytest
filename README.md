
markdown
Copy
Edit
# 🛒 eCommerce Selenium Automation Framework (Python + PyTest)

![Python](https://img.shields.io/badge/Python-3.9-blue.svg)
![Selenium](https://img.shields.io/badge/Selenium-Automation-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

A robust, maintainable automation framework built using **Selenium WebDriver**, **Python**, and **PyTest** following the **Page Object Model (POM)** design pattern.

> 🎯 This project automates login functionality on a demo eCommerce site using real-world practices like reporting, logging, and screenshot capture.

---

## 📁 Project Structure

ecommerce_automation/
│
├── tests/ # Test cases
│ └── test_login.py
│
├── pages/ # Page Object classes
│ └── login_page.py
│
├── utils/ # WebDriver setup, logger
│ ├── webdriver_setup.py
│ └── logger.py
│
├── data/ # Test data (JSON format)
│ └── testdata.json
│
├── reports/ # HTML reports & screenshots (auto-generated)
│
├── logs/ # Execution logs
│
├── conftest.py # PyTest configuration (screenshots on failure)
├── requirements.txt # Dependencies
└── README.md # Project overview

yaml
Copy
Edit

---

## 🚀 Features

✅ Login Automation (Valid & Invalid Scenarios)  
✅ Page Object Model (POM)  
✅ PyTest Fixture for WebDriver Lifecycle  
✅ HTML Reports (`pytest-html`)  
✅ Screenshots on Failure  
✅ Structured Logging (`logging` module)  
✅ Real-time Demo Site Tested  
✅ GitHub-ready Structure

---

## 🧪 Technologies Used

- 🐍 Python 3.9
- 🌐 Selenium WebDriver
- 🧪 PyTest
- 🧾 JSON for test data
- 📊 PyTest-HTML (Reporting)
- 📷 Screenshots on failure
- 🧾 Logging via built-in `logging`

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ecommerce-automation.git
cd ecommerce-automation
2. Create a Virtual Environment (Optional)
bash
Copy
Edit
python -m venv env
env\Scripts\activate    # On Windows
3. Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
▶️ Running the Tests
bash
Copy
Edit
pytest tests/test_login.py --html=reports/report.html
✔️ Example:
Valid login test (student / Password123)

Invalid login test (wronguser / wrongpass)