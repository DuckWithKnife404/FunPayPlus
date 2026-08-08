import re

import requests
from bs4 import BeautifulSoup


class Account:
    def __init__(self, token: str, user_agent: str = ""):
        self.token = token
        self.user_agent = user_agent
        self.username = ""
        self.balance = 0.0
        self.active_sell = 0
        self.active_buy = 0
        self.active_message = 0
        self.rating = 0.0
        self.data = ""
        self.id = 0
        self.unread = 0

    def _safe_text(self, element):
        return element.text.strip() if element else ""

    def _safe_int(self, element):
        if not element:
            return 0
        try:
            text = "".join(filter(str.isdigit, element.text))
            return int(text) if text else 0
        except ValueError:
            return 0

    def get(self):
        headers = {
            "cookie": f"golden_key={self.token}",
            "user-agent": self.user_agent,
        }

        try:
            response = requests.get("https://funpay.com/", headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            self.username = self._safe_text(
                soup.find("div", {"class": "user-link-name"})
            )

            self.balance = self._safe_int(
                soup.find("span", {"class": "badge badge-balance"})
            )

            self.active_sell = self._safe_int(
                soup.find("span", {"class": "badge badge-trade"})
            )

            self.active_buy = self._safe_int(
                soup.find("span", {"class": "badge badge-orders"})
            )

            self.active_message = self._safe_int(
                soup.find("span", {"class": "badge badge-chat"})
            )

            user_link = soup.find("a", {"class": "user-link-dropdown"})
            if user_link and user_link.get("href"):
                id_match = re.search(r"/users/(\d+)/", user_link["href"])
                if id_match:
                    self.id = int(id_match.group(1))

            if self.id:
                profile_response = requests.get(
                    f"https://funpay.com/users/{self.id}/",
                    headers=headers,
                    timeout=10,
                )
                profile_soup = BeautifulSoup(profile_response.text, "html.parser")

                self.data = self._safe_text(
                    profile_soup.find("div", {"class": "text-nowrap"})
                )

                rating_elem = profile_soup.find("span", {"class": "big"})
                if rating_elem:
                    try:
                        self.rating = float(rating_elem.text.strip())
                    except ValueError:
                        self.rating = 0.0

            return True

        except Exception as e:
            print(f"Ошибка парсинга: {e}")
            return False

    def event(self):
        headers = {
            "cookie": f"golden_key={self.token}",
            "user-agent": self.user_agent,
        }

        try:
            response = requests.get("https://funpay.com/chat/", headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, "html.parser")

            unread = soup.find("a", {"class": "contact-item unread"})
            if unread:
                badge = unread.find("span", {"class": "badge"})
                self.unread = self._safe_int(badge) or 1
            else:
                self.unread = 0

            return True

        except Exception as e:
            print(f"Ошибка проверки чата: {e}")
            self.unread = 0
            return False

    def __str__(self):
        return f"Account(id={self.id}, username='{self.username}', balance={self.balance}₽)"