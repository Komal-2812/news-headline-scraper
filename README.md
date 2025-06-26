📰 India TV News Headlines Scraper

A simple Python script to scrape the latest news headlines from [India TV News](https://www.indiatvnews.com/) website.  
It extracts headlines from the `<h2>` and `<h3>` HTML tags and saves them into a daily text file for easy tracking and analysis.

 🧰  Tools & Requirements
      Tool             Purpose                          
      `Python 3.x`     Core programming language        
      `requests`       To send HTTP requests            
      `BeautifulSoup`  To parse HTML and extract data   
      `datetime`       To generate filenames with dates 

  🚀  Features
      🌐 Fetches realtime news headlines directly from India TV News homepage  
      🏷️ Extracts headlines from both `<h2>` and `<h3>` tags  
      📅 Automatically saves headlines to a dated `.txt` file (format: `indiatv_headlines_DDMMYY.txt`)  
      ✍️ Appends headlines in a clean numbered list  
      ⚠️ Handles network errors and empty results gracefully  

