# 🛒 E-commerce Automation Framework (SauceDemo)

Automation testing framework for an e-commerce web application using Selenium, PyTest, and POM design pattern.

## 🔧 Tech Stack
- Python
- Selenium WebDriver
- PyTest

## 🚀 Features
- Page Object Model (POM)
- Data Driven Testing (Excel)
- Cross Browser Testing (Chrome, Edge)
- Parallel Execution (pytest-xdist)
- Logging
- HTML Reports
- Screenshot on Failure
- Config Management (config.ini)

## 📂 Project Structure
- pageObjects/ → Page classes (POM)
- testCases/ → Test scripts
- utilities/ → Helper functions (logger, config, etc.)
- testData/ → Excel test data
- configurations/ → Config file

## ▶️ Run Tests
```bash
pytest -n auto

## 📌 Notes
- Logs, reports, and screenshots are generated during execution and are not committed to the repository.
