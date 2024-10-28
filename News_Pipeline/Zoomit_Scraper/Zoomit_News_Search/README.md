
# Zoomit News Search Spider

This is a Scrapy project that uses Selenium to scrape news data from [Zoomit.ir](https://www.zoomit.ir/), specifically from its news search section. The script extracts information such as news titles, publication dates, images, and estimated reading times from the search results page.

## Table of Contents
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Scrapy-Selenium Integration**: Uses Selenium within a Scrapy Spider for enhanced dynamic content handling.
- **Data Extraction**: Scrapes titles, dates, images, and reading times for each news item on the page.
- **JSON Output**: Outputs the extracted data as JSON for further processing or analysis.

## Prerequisites
- Python 3.7+
- Google Chrome installed
- Chrome WebDriver compatible with your Chrome version

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/Ali-Dabiri/Portfolio_Django/tree/main/News_Pipeline/Zoomit_Scraper/Zoomit_News_Search
    ```
2. Navigate to the project directory:
    ```bash
    cd ZoomitNewsSearchSpider
    ```
3. Install the required packages:
    ```bash
    pip install scrapy selenium webdriver-manager
    ```

## Usage
To run the spider, use the following command:
```bash
scrapy crawl Zoomit_News_Search_Spider -o output.json
```
This will start the spider and save the scraped data to `output.json`.

## Output
The spider yields JSON data structured as follows:
```json
{
    "URL Source": "https://www.zoomit.ir/search/news/",
    "News Title": "Sample News Title",
    "News Date": "Sample Date",
    "News Image": "https://sample-image-url.com",
    "News Study Time": "5 min read"
}
```

## Project Structure
- `ZoomitNewsSearchSpider.py`: Main spider script that contains all functionality.
- `output.json`: The default output file to store the scraped data.
  
## Contributing
Feel free to fork this repository, submit issues, or make pull requests if you’d like to improve the project!

## License
This project is licensed under the MIT License.
