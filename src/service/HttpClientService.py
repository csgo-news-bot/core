import requests


class HttpClientService:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
    }

    def get_html_page(self, url: str) -> str:
        response = requests.get(url, headers=self.headers)

        return response.text

    def get_blob_from_url(self, url: str):
        req = requests.get(url, headers=self.headers)
        return req.content

