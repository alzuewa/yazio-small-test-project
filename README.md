# <p align="center"> UI mobile automation project <a href="https://www.yazio.com/en"> YAZIO </a></p>
<p align="center">
    <img title="App Home Screen" src="media/screenshot.png">
</p>

## Contents

>  [Technology Stack](#technology-stack)
>
>  [Covered Functionality](#covered-functionality)
>
>  [Allure Report](#allure-report)
>
>  [Test Run Record Example](#test-run-record-example)

## Technology Stack and Instruments
<p  align="center">
    <code><img width="5%" title="Python" src="media/icons/python.svg"></code>
    <code><img width="5%" title="Pytest" src="media/icons/pytest.svg"></code>
    <code><img width="5%" title="Selene" src="media/icons/selene.png"></code>
    <code><img width="5%" title="Selenium" src="media/icons/selenium.png"></code>
    <code><img width="5%" title="Appium" src="media/icons/appium.svg"></code>
    <code><img width="5%" title="Allure Report" src="media/icons/allure.svg"></code>
    <code><img width="5%" title="PyCharm" src="media/icons/pycharm.svg"></code>
    <code><img width="5%" title="Poetry" src="media/icons/poetry.svg"></code>
    <code><img width="5%" title="Android Studio" src="media/icons/android_studio.svg"></code>
    <code><img width="5%" title="Android" src="media/icons/android.svg"></code>
</p>

## Covered Functionality 
#### UI tests check:

* ✅ Pass onboarding
* ✅ Add meals to diary
* ✅ Start, stop and cancel fasting tracker
* ✅ Add recipe to favorites and delete


## Run tests locally

Local run requires [Python](https://www.python.org/downloads/release/python-3126/)
and [Poetry](https://python-poetry.org/docs/#installation) installed.

1. Download the project and `cd` to its directory
2. In project root create virtual environment and install dependencies

```bash
python3 -m venv .venv && source .venv/bin/activate
poetry install --no-root
```

3. In project root create `resources` directory and put the app `.apk` file into it.  


4. Run tests

```bash
pytest --context local
```

When run is finished `allure-results` directory will be generated in project root. If Allure Report is [installed](https://allurereport.org/docs/install/), a report can be generated
```bash
allure serve allure-results
```

## Allure Report
Clicking on the Allure Report link we get a full overview of finished run.
It includes:
- Summary
<p align="center">
    <img title="Allure Report Summary" src="media/overview.png">
</p> 

- Detailed steps of each test and screenshot
<p align="center">
    <img title="Attachments" src="media/attachments.png">
</p>  


## Test Run Record Example
<p align="center">
    <img title="Video" src="media/1.onboarding.gif">
    <img title="Video" src="media/2.favorites.gif">
</p>
<p align="center">
    <img title="Video" src="media/3.tracker.gif">
    <img title="Video" src="media/4.meal.gif">
</p>