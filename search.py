
import requests
import json
import sys
import datetime
import easygui


def main():
    query = sys.argv[1]
    print(query)
    key = 'api key'

    doc = requests.get(f"https://www.googleapis.com/youtube/v3/search?q={query}&key={key}&part=snippet&type=video")
    res = json.loads(doc.text)

    date = datetime.date.today()

    if res['items'][0]['snippet']['publishedAt'].split('T')[0] == date.strftime('%Y-%m-%d'):
        easygui.msgbox('New video on  youtube.com/watch?v='+res['items'][0]['id']['videoId'])


if __name__ == '__main__':
    main()
