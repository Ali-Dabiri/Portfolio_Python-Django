# Reuters Gold News Search

This project is an enhanced Python-based web scraping tool using Selenium to extract news articles related to commodities, specifically gold, from the Reuters website. The script automates page navigation, scrolling, and extraction of news data from multiple pages, saving the results in a structured CSV file.

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
- `selenium`: To automate interactions with the Reuters website.
- `webdriver_manager`: For automatically downloading and managing the ChromeDriver.
- `chromedriver_autoinstaller`: To keep the driver updated.

## Usage
To run the script, simply execute the following command:

```bash
python Reuters_Gold_News_Search.py
```

The script will:
1. Navigate to the Reuters search page for "commodity gold."
2. Manage cookies and dismiss pop-ups.
3. Scroll through pages, navigate to the next page, and gather article titles.
4. Save extracted data from multiple pages into `Reuters_Gold_News_Search_Data.csv`.

## Project Structure
- `Reuters_Gold_News_Search.py`: The main script for scraping Reuters across multiple pages.
- `Reuters_Gold_News_Search_Data.csv`: Output file containing page URL, title, and news article titles.

## Output
The extracted news titles are saved in a CSV file with the following columns:
- **URL Address**: The URL of each Reuters page.
- **Page Title**: Title of the Reuters page.
- **News Title**: Titles of news articles extracted from each page.

## License
This project is licensed under the MIT License.
