class Settings():
    """A class to store all settings for Alien Invasion."""
    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 900
        self.screen_height = 600
        self.bg_color = (130, 130, 230)

        #ship settings
        self.ship_speed_factor = 0.3
        self.ship_speed_increase_factor = 0.000

        #bullet settings
        self.bullet_speed_factor = 0.3
        self.bullet_width = 800
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 10

        #alien settings
        self.alien_speed_factor = 0.3
        self.fleet_drop_speed = 10

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1


#img = pygame.transform.scale(img, (35, 35))