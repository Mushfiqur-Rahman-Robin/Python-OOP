from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://coreyms.com/').text

csv_file = open('cms_scrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'video_link'])



soup = BeautifulSoup(source, 'lxml')
# print(soup.prettify())

article = soup.find('article')

# print(article.prettify())

headline = article.h2.a.text
# print(headline)

summary = article.find('div', class_ = 'entry-content').p.text
# print(summary)

for article in soup.find_all(article):
    headline = article.h2.a.text
    print(headline)

    summary = article.find('div', class_ = 'entry-content').p.text

    video_source = article.find('iframe', class_ = 'youtube-player')['src']

    vid_id = video_source.split('/')[4]
    vid_id = vid_id.split('?')[0]

    yt_link = f'https://youtube.com/watch?v={vid_id}'
    print(yt_link)

    try:
        video_source = article.find('iframe', class_ = 'youtube-player')['src']
        vid_id = video_source.split('/')[4]
        vid_id = vid_id.split('?')[0]
        yt_link = f'https://youtube.com/watch?v={vid_id}'
    except Exception as e:
        yt_link = None

    print(yt_link)
    print()

    csv_writer.writerow([headline, summary, yt_link])

csv_file.close()
