import requests


class GitHub:

    @staticmethod
    def get_user(username: str) -> dict:
        """
        GitHub's user search method
        :param username: set username
        """
        r = requests.get(f'https://api.github.com/users/{username}')
        body = r.json()

        return body

    @staticmethod
    def search_repo(name: str) -> dict:
        """
        GitHub repository search method
        :param name: set repository name
        """
        r = requests.get(
            'https://api.github.com/search/repositories',
            params={"q": name}
        )
        body = r.json()

        return body
