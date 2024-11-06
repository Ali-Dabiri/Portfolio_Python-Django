# Reuters Gold News Search (Enhanced Version)

This project is an advanced Python-based web scraper developed using Selenium, designed to extract news articles related to commodities, specifically gold, from the Reuters website. The scraper navigates pages, extracts data, filters news from the past six months, and saves the results in a structured CSV file.

## Table of Contents
- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Output](#output)
- [License](#license)

## Installation
Clone this repository and navigate into the project folder.

```bash
git clone https://github.com/Ali-Dabiri/Portfolio_Django/tree/main/News_Pipeline/Reuters_Scraper/Reuters_Gold_News_Search
```

```bash
cd Reuters_Gold_News_Search
cd Reuters_Gold_News_Search
cd spiders
```

## Requirements
Install the necessary Python packages:

```bash
pip install -r requirements.txt
```

**Requirements include:**
- `selenium`: For web interaction automation with Reuters.
- `webdriver_manager`: For automatic ChromeDriver management.
- `chromedriver_autoinstaller`: To ensure the latest version of ChromeDriver is always available.

## Usage
To execute the script, run:

```bash
python Reuters_Gold_News_Search.py
```

The script performs the following steps:
1. Navigates to the Reuters search page for "commodity gold."
2. Handles cookies and pop-ups for smooth navigation.
3. Scrolls through pages, retrieves article titles, and filters news from the last six months.
4. Saves the extracted data into a CSV file named `Reuters_Gold_News_Search_Data.csv`.

## Project Structure
- `Reuters_Gold_News_Search.py`: The main script, including methods for page navigation, data extraction, and date-based filtering.
- `Reuters_Gold_News_Search_Data.csv`: Output file containing page URL, title, news titles, and publication dates.

## Output
The extracted data is saved in a CSV file with the following columns:
- **URL Address**: The URL of each Reuters page.
- **Page Title**: The title of each Reuters page.
- **News Title**: Extracted news titles.
- **News Date**: Publication date of each news article, limited to the last six months.

## License
This project is licensed under the MIT License.
