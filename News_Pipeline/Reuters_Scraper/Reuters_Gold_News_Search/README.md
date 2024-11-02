# Reuters Gold News Search

A Python-based web scraping project using Selenium to search for and extract news articles related to commodities, specifically gold, from the Reuters website. The script automates the process of navigating through pages, handling pop-ups, and saving extracted news data into a CSV file.

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
1. Open the Reuters search page for "commodity gold."
2. Handle cookie consent and pop-up windows.
3. Scroll through the page to load news articles.
4. Extract article titles from multiple pages.
5. Save the extracted data to `Reuters_Gold_News_Search_Data.csv`.

## Project Structure
- `Reuters_Gold_News_Search.py`: The main script for scraping Reuters.
- `Reuters_Gold_News_Search_Data.csv`: The output file with URL, page title, and extracted news titles.

## Output
The extracted news titles are saved in a CSV file with the following columns:
- **URL Address**: URL of the Reuters search page.
- **Page Title**: Title of the Reuters page.
- **News Title**: Titles of the news articles found on the page.

## License
This project is licensed under the MIT License.
