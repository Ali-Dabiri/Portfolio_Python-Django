
# Zoomit News Search Content Spider

A web scraping spider built with Scrapy and Selenium to extract news articles from the Zoomit website. This spider retrieves links to news articles from the Zoomit news search page and extracts details like title, date, author, tags, study time, and content from each article page.

## Table of Contents
- [Features](#features)
- [Requirement](#requirements)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Code Overview](#code-overview)
- [Output](#output)
- [Sample Output](#sample-output)
- [Notes](#notes)
- [License](#license)

## Features
- Extracts a list of news articles from Zoomit's search page.
- Retrieves article details including title, date, author, tags, and main content.
- Uses Selenium to dynamically interact with the page elements like "View More" buttons and ads.

## Requirements

- Python 3.6+
- Scrapy
- Selenium
- webdriver-manager
- ChromeDriver (compatible with the installed version of Google Chrome)

To install the required packages, run:
```bash
pip install scrapy selenium webdriver-manager
```

## Project Structure

```
├── spiders
    └── ZoomitNewsSearchContentSpider.py   # Main spider for Zoomit news    
```

## Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/Ali-Dabiri/Portfolio_Django/tree/main/News_Pipeline/Zoomit_Scraper/Zoomit_News_Search_Content
    ```
    
2. **Navigate to the project directory**:
   ```bash
   cd Zoomit_News_Search_Content
   cd spider
   ```

3. **Run the spider**:
   To start scraping and save the output to a JSON file:
   ```bash
   scrapy crawl spiders/ZoomitNewsSearchContentSpider.py -o output.json
   ```

## Code Overview

### Spider Initialization
The spider initializes with Selenium’s `Chrome` to handle JavaScript elements, such as closing ads and clicking on "View More" buttons to load additional news articles.

### Main Methods
- **`parse`**: Opens the main news search page, loads additional articles by clicking "View More," and collects links to each article.
- **`page_parse`**: Follows each article link to extract details like title, date, author, tags, study time, and main content.

### Output
The scraped data is stored in a structured JSON format with the following fields:
- `News Page Url Source`: The URL of the article page.
- `News Page Title`: Title of the article.
- `News Page Date`: Publication date.
- `News Page Author`: Article author's name.
- `News Page Tags`: List of tags related to the article.
- `News Page Study Time`: Estimated reading time.
- `News Page Content`: Main content of the article.

## Sample Output

```json
{
    "News Page Url Source": "https://www.zoomit.ir/news/123456/",
    "News Page Title": "Sample Article Title",
    "News Page Date": "2024-10-29",
    "News Page Author": "Author Name",
    "News Page Tags": ["Tag1", "Tag2"],
    "News Page Study Time": "5 min read",
    "News Page Content": "The main content of the article goes here..."
}
```

## Notes
- Running this spider extensively may result in your IP being temporarily blocked by the website.

## License

This project is open-source and available under the MIT License.
