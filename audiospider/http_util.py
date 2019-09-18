import time
import html
import requests

html_parser = html.parser.HTMLParser()


def get_req(url, headers=None):
    time.sleep(0.5)
    if headers is None:
        headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 ' \
                            '(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
    try:
        req = requests.get(url, headers=headers)
    except Exception as e:
        print(Exception, ':', e, '; Try request again: ', url)
        req = get_req(url)
    return req

