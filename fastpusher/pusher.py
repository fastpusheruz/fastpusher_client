import requests


class FastPusher(object):
    def __init__(
            self,
            url,
            token,
            *args,
            **kwargs
    ):
        self.url = url
        self.token = token

    def push(self, channel: str, data: dict):
        url = f"{self.url}/api/partners/push"
        headers = {"Authorization": f"Bearer {self.token}"}
        response = requests.post(url=url, headers=headers, json={
            "client_id": channel,
            "data": data
        })
        response.raise_for_status()
        data = response.json()
        return data
