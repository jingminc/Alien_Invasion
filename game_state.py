class GameStats():
    """初始化统计信息"""
    def __init__(self, ai_settings):
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False # 游戏刚开始时处于非活动状态
        # 任何情况下都不重置最高分 
        self.high_score = 0

    """初始化在游戏运行期间可能变化的统计信息"""
    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
    
    