
import unittest
from settings import Settings


class TestSettings(unittest.TestCase):

    def test_screen_width(self):
        ai_settings = Settings()
        self.assertEqual(ai_settings.screen_width, 1300)
        self.assertEqual(ai_settings.score_scale, 1.5)
        self.assertEqual(ai_settings.screen_height, 700)
        self.assertEqual(ai_settings.ship_limit, 3)
        self.assertIn(ai_settings.ship_speed_factor, [1.5, 2.25, 3.375, 5.0625 ])
        self.assertIn(ai_settings.alien_points, [50, 75, 112.5, 168.75 ])

# 运行单元测试
if __name__ == '__main__':
    unittest.main()