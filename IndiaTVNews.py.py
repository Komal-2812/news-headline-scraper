import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_india_tv_news():
    url = "https://www.indiatvnews.com/"
    
    try:
        # Step 1: Send HTTP GET request
        response = requests.get(url)
        response.raise_for_status()
        
        # Step 2: Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Step 3: Extract both <h2> and <h3> headlines
        headlines = set()
        
        for tag in soup.find_all(["h2", "h3"]):
            text = tag.get_text(strip=True)
            if text:
                headlines.add(text)  # Set automatically removes duplicates
        
        if not headlines:
            print("⚠️ No <h2> or <h3> headlines found.")
            return
        
        # Step 4: Save to file with date
        date_str = datetime.now().strftime("%d-%m-%y")
        filename = f"indiatv_headlines_{date_str}.txt"
        
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"\n🗓️ India TV News Headlines – {date_str}\n\n")
            for i, headline in enumerate(sorted(headlines), 1):
                f.write(f"{i}. {headline}\n")
            f.write("\n" + "=" * 60 + "\n")
        
        print(f"✅ Saved {len(headlines)} headlines to '{filename}'")
    
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except Exception as e:
        print(f"❌ Something went wrong: {e}")

# Run the function
if __name__ == "__main__":
    scrape_india_tv_news()
