from bs4 import BeautifulSoup
import os
import pandas as pd

d = {'title': [], 'link': [], 'phone_number': []}

for file in os.listdir("data"):
    try:
        with open(f"data/{file}") as f:
            html_doc = f.read()

        soup = BeautifulSoup(html_doc, 'html.parser')
        t = soup.find("h3")

        if t:
            title = t.get_text()

            # Extract phone number
            phone_span = soup.find("span", text=lambda x: x and x.startswith("+"))
            phone_number = phone_span.get_text() if phone_span else "Not Found"

            # Extract link
            link_tag = t.find("a")
            link = link_tag['href'] if link_tag else "Not Found"

            print(f"Title: {title}, Phone: {phone_number}, Link: {link}")
            d['title'].append(title)
            d['link'].append(link)
            d['phone_number'].append(phone_number)
        else:
            print(f"Skipping file {file}: No <h3> tag found.")
    except Exception as e:
        print(f"Error processing file {file}: {e}")

# Save data to CSV
if d['title']:
    df = pd.DataFrame(data=d)
    df.to_csv("data3.csv", index=False)
else:
    print("No valid data found to save.")