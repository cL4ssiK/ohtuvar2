import unittest
from statistics_service import StatisticsService
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )

    def test_search_eiLoydy(self):
        self.assertEqual(self.stats.search("selanne"), None)

    def test_search_loytyy(self):
        self.assertEqual(self.stats.search("Kurri").name, "Kurri")
        self.assertEqual(self.stats.search("kuRri").name, "Kurri")

    def test_team_loytyy(self):
        result = self.stats.team("EDM")
        expected = list([
            Player("Semenko", "EDM", 4, 12),
            Player("Kurri",   "EDM", 37, 53),
            Player("Gretzky", "EDM", 35, 89)
        ])
        self.assertCountEqual(
            [(p.name, p.team, p.goals, p.assists) for p in result],
            [(p.name, p.team, p.goals, p.assists) for p in expected]
        )
    
    def test_team_eiLoydy(self):
        result = self.stats.team("RAN")
        expected = list([])
        self.assertCountEqual(result, expected)

    