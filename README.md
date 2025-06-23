# 📈 GitHub Trending Repositories Scraper

This Python script scrapes the **top 5 trending repositories** from [GitHub Trending](https://github.com/trending) and saves their names and links into a CSV file.

Perfect for anyone learning web scraping or automating data collection using Python!

---

## 🛠️ Technologies Used

- 🐍 Python 3
- 🌐 `requests` – to fetch the web page
- 🧼 `BeautifulSoup` – to parse and extract HTML elements
- 📄 `csv` – to store the output data in CSV format

---

## 📂 Output File

- **`trending.csv`**
  - `repository_name` – Full name of the repository (e.g., `vercel/next.js`)
  - `link` – URL to the repository on GitHub

Example CSV content:

| repository_name     | link                                      |
|---------------------|-------------------------------------------|
| vercel/next.js      | https://github.com/vercel/next.js         |
| facebook/react      | https://github.com/facebook/react         |

---

## 🚀 How to Run This Script
 **Clone this repository:**

   ```bash
   git clone https://github.com/VIHARI1106/github-trending-scraper.git
   cd github-trending-scraper
pip install requests beautifulsoup4
python scraper.py
Open the generated trending.csv file to view the list of top 5 trending repositories.
