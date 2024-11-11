# Reuters Gold News Search Content

`Reuters_Gold_News_Search_Content` is a Python script that scrapes Reuters for gold-related news articles, collecting details such as article titles, publication dates, authors, tags, and content. The script navigates through multiple pages of search results, applying Selenium for dynamic interaction, and saves the extracted data into a CSV file.

## Table of Contents
- [Features](#features)
- [Requirements](#requirements)
- [Setup](#setup)
- [Usage](#usage)
- [Output](#output)
- [Potential Issues](#potential-issues)
- [License](#license)

## Features

- Automates browser actions to search for "commodity gold" on Reuters.
- Collects data from multiple pages, scrolling up and down to load all elements.
- Extracts the following data fields from each article:
  - URL Address
  - Page Title
  - News Title
  - News Date
  - News Tag
  - News Author
  - News Content
- Saves all extracted data in a structured CSV file named `Reuters_Gold_News_Search_Content_Data.csv`.

## Requirements

Ensure you have the following installed:

- Python 3.10+
- Required Python libraries:
  - `selenium`
  - `webdriver-manager`

You can install the required packages using:

```bash
pip install selenium webdriver-manager
```

## Setup

1. **Clone the repository** (if applicable):

    ```bash
    git clone https://github.com/Ali-Dabiri/Portfolio_Python-Django/tree/main/News_Pipeline/Reuters_Scraper/Reuters_Gold_News_Search_Content
    ```
    ```bash
    cd Reuters_Gold_News_Search_Content
    ```


2. **Run the script**:

    ```bash
    python Reuters_Gold_News_Search_Content.py
    ```

## Usage

The script will:

1. Open the Reuters search page for "commodity gold."
2. Accept cookies and close any pop-ups (if they appear). (It is improving)
3. Collect news article details over multiple pages and save them to a CSV file.

### Important Notes

- **Date Filtering**: The script filters articles from the past six months based on the publication date.
- **Cookie Handling**: The script retrieves cookies, applies them across sessions, and refreshes pages as needed. (It is improving)
- **XPath Elements**: Ensure the specified XPath expressions match the current HTML structure on Reuters, as websites may occasionally update their layout.

## Output

The resulting CSV file, `Reuters_Gold_News_Search_Content_Data.csv`, includes columns for URL Address, Page Title, News Title, News Date, News Tag, News Author, and News Content.

## Potential Issues

If the script encounters errors during navigation or data collection, it might be due to:
- Changes in Reuters' HTML structure.
- Pop-ups or CAPTCHA challenges.
  
Review the console output for troubleshooting information, as error messages will help identify the specific steps that failed.

## License

This project is licensed under the MIT License.
