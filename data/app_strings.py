from enum import StrEnum


class OnboardingChoices:
    class MainGoal(StrEnum):
        LOSE_WEIGHT = 'Lose weight'
        MAINTAIN_WEIGHT = 'Maintain weight'
        GAIN_WEIGHT = 'Gain weight'
        BUILD_MUSCLE = 'Build muscle'
        SOMETHING_ELSE = 'Something else'

    class Gender(StrEnum):
        MALE = 'Male'
        FEMALE = 'Female'

    class SecondaryGoal(StrEnum):
        LIVE_HEALTHIER = 'Eat and live healthier'
        BOOST_ENERGY = 'Boost my energy and mood'
        STAY_MOTIVATED = 'Stay motivated and consistent'
        FEEL_BETTER = 'Feel better about my body'

    class UsagePurpose(StrEnum):
        CALORIE_COUNT = 'Calorie Counting'
        ACTIVITY_TRACK = 'Activity Tracking'
        EAT_HEALTHY = 'Healthy Eating'
        STATISTICS = 'Analyses & Statistics'
        FASTING = 'Intermittent Fasting'

    class KnowledgeLevel(StrEnum):
        BEGINNER = 'Beginner'
        INTERMEDIATE = 'Intermediate'
        ADVANCED = 'Advanced'

    class Habits(StrEnum):
        PORTIONS = 'Portion Control'
        SNACKING = 'Snacking'
        BALANCE = 'Balance'
        HYDRATION = 'Hydration'
        EXERCISE = 'Exercise'

    class Stopper(StrEnum):
        INCONSISTENCY = 'Lack of consistency'
        WRONG_HABITS = 'Unhealthy eating habits'
        NO_SUPPORT = 'Lack of support'
        NO_TIME = 'Busy schedule'
        NO_INSPIRATION = 'Lack of meal inspiration'

    class ActivityLevel(StrEnum):
        LIGHT = 'Lightly active'
        MODERATE = 'Moderately active'
        ACTIVE = 'Active'
        VERY_ACTIVE = 'Very active'

    class Diet(StrEnum):
        CLASSIC = 'Classic'
        PESCATARIAN = 'Pescatarian'
        VEGETARIAN = 'Vegetarian'
        VEGAN = 'Vegan'

    class Choice(StrEnum):
        YES = 'Yes'
        NO = 'No'

    class Trigger(StrEnum):
        FOOD_AROUND = 'Being around food'
        BOREDOM = 'Being bored'
        PEOPLE_EAT = 'Seeing other people eat'
        OTHER = 'Something else'

    class Strategy(StrEnum):
        MINDFULNESS = 'Make more mindful decisions about food'
        HEALTHY_EATING = 'Eat more fruit and vegetables'
        MORE_WATER = 'Drink more water'
        LEARNING = 'Learn more about nutrition and health'
        CONSCIOUSNESS = 'Pay attention to hunger cues and portion sizes'

    class MealTactics(StrEnum):
        LOG_BEFORE = 'Log a meal before eating it'
        LOG_AFTER = 'Log a meal right after finishing it'
        LOG_ALL_MORNING = 'Log all meals for the day first thing in the morning'
        LOG_ALL_EVENING = 'Log all meals at the end of the day'
        DO_NOT_KNOW = 'I don\'t know yet'

    class ActivityTactics(StrEnum):
        NEW_ACTIVITY = 'Try new activities and sports'
        STEPS_ACHIEVEMENT = 'Reach a daily step goal'
        WALKING = 'Choose walking over driving if possible'
        WORKOUT = 'Start a new workout routine'
        SCHEDULE_ACTIVITY = 'Set fixed times for activities'

    class Metrics(StrEnum):
        WEIGHT_RECORD = 'Document my weight regularly'
        MEASUREMENTS = 'Track my body measurements'
        APP_METRICS = 'Monitor health metrics with a fitness app'
        ENERGY = 'Look out for changes in my energy level'
        CLOTHES = 'Compare the fit of my clothes to before'
        OTHER = 'Something else'

    class Celebration(StrEnum):
        SHOPPING = 'Buy new clothes'
        TRIP = 'Go on a trip'
        SPA = 'Treat myself to a spa day'
        FRIENDS = 'Celebrate with friends'
        OTHER = 'Something else'

    class HasChildren(StrEnum):
        YES_CLOSE = 'Yes, we live together.'
        YES_FAR = 'Yes, but we live separately.'
        NO = 'No, I don’t have children.'

    class Schedule(StrEnum):
        FREE = 'I can choose my work hours freely'
        STANDARD = 'I work a nine-to-five'
        SHIFTS = 'I work in alternating shifts'
        SEASONAL = 'I have a seasonal schedule'
        OTHER = 'Other'

    class MatesHabits(StrEnum):
        REGULAR = 'They eat healthily on a regular basis.'
        IRREGULAR = 'They eat healthily from time to time.'
        UNHEALTHY = 'They mostly eat unhealthily.'
        DO_NOT_KNOW = 'I don’t know.'

    class SupportPreference(StrEnum):
        PEOPLE_AROUND = 'Having supportive people around me'
        SHARING = 'Telling others about my journey'
        TAKE_BREAK = 'Taking a break to get my motivation back'
        NOTHING = 'Nothing, I’ll make it on my own'


class Buttons(StrEnum):
    GET_STARTED = 'Get Started'
    LETS_GO = "Let's Go"
    NEXT = 'Next'
    GOT_IT = 'Got It'
    ADJUST_GOAL = 'Adjust Goal Weight'
    CONTINUE_ANYWAY = 'CONTINUE ANYWAY'
    CONTINUE = 'Continue'
    CANNOT_WAIT = "I Can't Wait"
    GREAT = 'Great'
    CREATE_PLAN = 'Create My Plan'
    LOVE_IT = 'Love It'
    SKIP = 'Skip'
    CM = 'cm'
    KG = 'kg'
