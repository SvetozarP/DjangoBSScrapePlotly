from datetime import datetime, timedelta
from typing import List

from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests

from core.models import Fixture


class Command(BaseCommand):
    help = 'Scrape results from the BBC website'

    def handle(self, *args, **kwargs):
        urls = self.construct_urls()
        for url in urls:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')

            # find fixtures

            results = soup.find_all('div', class_='ssrcss-1bjtunb-GridContainer e1efi6g55')
            for result in results:
                home = result.select_one('.ssrcss-bon2fo-WithInlineFallback-TeamHome .ssrcss-1f39n02-VisuallyHidden')
                home = home.get_text(strip=True)
                away = result.select_one('.ssrcss-nvj22c-WithInlineFallback-TeamAway .ssrcss-1f39n02-VisuallyHidden')
                away = away.get_text(strip=True)
                home_score = result.select_one('.ssrcss-qsbptj-HomeScore')
                home_score = home_score.get_text(strip=True)
                away_score = result.select_one('.ssrcss-fri5a2-AwayScore')
                away_score = away_score.get_text(strip=True)

                Fixture.objects.get_or_create(
                    team1=home,
                    team2=away,
                    team1_goals=home_score,
                    team2_goals=away_score,
                )

    def construct_urls(self) -> List[str]:

        BASE_URL = 'https://www.bbc.co.uk/sport/rugby-union/scores-fixtures/'
        START_DATE = datetime(2025, 4, 29)
        END_DATE = datetime(2025, 5, 27)
        delta = (END_DATE - START_DATE).days

        urls = []
        for i in range(delta + 1):
            date = START_DATE + timedelta(days=i)
            date = date.strftime('%Y-%m-%d')
            urls.append(f'{BASE_URL}{date}')

        return urls
