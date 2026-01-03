Unlimited Lead Finder 🚀
AI‑powered automation tool to generate unlimited business leads from public directories using a simple query and page range, and export them as a clean, de‑duplicated CSV ready for outreach.
​

🔍 Problem
At Pixel Global, the team had to use multiple paid tools and manual processes to generate leads.
This led to:

High recurring subscription costs

Time‑consuming data collection

Duplicate and noisy leads that required manual cleanup
​

✅ Solution
This project is an automated lead generation engine that:

Takes a query (e.g. "dentist", "clinic") and page range

Scrapes public business listings from a target directory

Cleans and removes duplicate entries using Pandas

Applies smart filtering rules to keep only relevant leads

Exports everything into a structured CSV file for sales/marketing teams
​
​

✨ Features
🔎 Query‑based search (keyword driven)

📄 Multi‑page scraping with configurable page range

🧹 Data cleaning & de‑duplication (Pandas)

🎯 Smart filtering logic for higher‑quality leads

📁 One‑click CSV export

⚙️ Fully scriptable & automatable (can be run on a schedule / as a backend job)
​
​

🧰 Tech Stack
Language: Python

Scraping & Automation: Selenium, BeautifulSoup, Requests

Data Processing: Pandas (cleaning, deduplication), CSV

Others: Time, logging, environment variables (for config)
​
​

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/<your-repo-name>.git
cd <your-repo-name>
2️⃣ Create & Activate Virtual Environment
bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate
3️⃣ Install Dependencies
bash
pip install -r requirements.txt
If you don’t have requirements.txt yet, a sample could be:

text
selenium
beautifulsoup4
pandas
requests
python-dotenv
⚙️ Configuration
Most options can be set via command‑line arguments or inside a config section in main.py (you can adjust this to match your code).
​

Typical parameters:

query → business category/keyword (e.g. "dentist")

start_page, end_page → page range to scrape

output_file → CSV path (default: leads.csv)

Example (if you’re using argparse):

python main.py --query "dentist" --start-page 1 --end-page 10 --output leads_dentists.csv
🧠 How It Works (High Level)
Builds target URLs based on query + page range

Uses Selenium to load each page and handle dynamic content

Parses the HTML with BeautifulSoup and extracts relevant fields

Name

Address

Phone

Website / Email (if available)

Loads all records into a Pandas DataFrame

Applies deduplication logic (e.g. by name + phone + address)

Applies basic filtering rules (e.g. drop empty rows, invalid entries)

Saves the final clean dataset as a CSV file
​
​

📊 Example Usage
bash
python main.py --query "clinic" --start-page 1 --end-page 5 --output uae_clinics.csv
Example output columns:

name

category

address

city

phone

website

source_url

🎥 Demo
You can attach your LinkedIn / YouTube demo link here:

Demo Video: [Watch here](<https://www.linkedin.com/posts/abhishek-dey-19aa47360_python-selenium-beautifulsoup-activity-7412924956855939075-oJwd?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFna7EYBK-I4jdr0HBgJx-_wACOGoQCvNHo>)

LinkedIn Post:(<https://www.linkedin.com/posts/abhishek-dey-19aa47360_python-selenium-beautifulsoup-activity-7412924956855939075-oJwd?utm_source=share&utm_medium=member_desktop&rcm=ACoAAFna7EYBK-I4jdr0HBgJx-_wACOGoQCvNHo>)
