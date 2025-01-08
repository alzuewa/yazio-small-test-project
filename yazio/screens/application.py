from .components.tabbar import Tabbar
from .fasting_screen import FastingScreen
from .home_screen import HomeScreen
from .meal_screen import AddMealScreen
from .onboarding_screen import OnboardingScreen
from .recipes_screen import RecipesScreen


class Application:
    def __init__(self):
        self.onboarding_screen = OnboardingScreen()
        self.home_screen = HomeScreen()
        self.recipies_screen = RecipesScreen()
        self.meal_screen = AddMealScreen()
        self.tabbar = Tabbar()
        self.fasting_screen = FastingScreen()


app = Application()
