# Zoomit Scraper

This project is a web scraper built with Scrapy to extract product information from the Zoomit website. The scraper is designed to gather data on various categories of electronic products, including mobile phones, tablets, laptops, TVs, wearables, headphones, HDDs, and gaming consoles.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Data Extracted](#data-extracted)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ali-Dabiri/Portfolio_Django/tree/main/News_Pipeline/Zoomit_Scraper
   cd Zoomit_Scraper
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv Zoomit_Scraper
   ```

3. **Activate the virtual environment:**
   - On Windows:
     ```bash
     Zoomit_Scraper\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```bash
     source Zoomit_Scraper/bin/activate
     ```

4. **Install required packages:**
   ```bash
   pip install scrapy
   ```

## Usage

To run the scraper, use the following command:
```bash
scrapy crawl Zoomit_Spider -o Zoomit_Product_Data.json
```
OR
```bash
scrapy crawl Zoomit_Spider -o Zoomit_Product_Data.csv #for excel
```

This will output the scraped data into a JSON file named `Zoomit_Product_Data.json`.

## Data Extracted

The scraper extracts the following data for each product:

- Source URL
- Product Name
- Product Price
- Product Score
- Product Image URL
- Product Specifications:
  - Specification 1
  - Specification 2
  - Specification 3
  - Specification 4
  - Specification 5
  - Specification 6
  - Specification 7
  - Specification 8

## Contributing

Contributions are welcome! If you have suggestions or improvements, please create an issue or submit a pull request.

## License

This project is licensed under the MIT License.
