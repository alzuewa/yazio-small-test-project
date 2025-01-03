import os

from dotenv import load_dotenv

from utils import helpers


def get_env(context: str):
    if context == 'local':
        load_dotenv(dotenv_path=helpers.get_path_from_root('.env.local_emulator'))

    elif context == 'bstack':
        load_dotenv()
        load_dotenv(dotenv_path=helpers.get_path_from_root('.env.bstack'))

    capabilities = {
        'platformVersion': os.getenv('ANDROID_PLATFORM_VERSION'),
        'deviceName': os.getenv('ANDROID_DEVICE_NAME'),
        'appActivity': os.getenv('APP_ACTIVITY'),
        'appWaitActivity': os.getenv('APP_WAIT_ACTIVITY'),
        'app': os.getenv('APP') if context == 'bstack' else helpers.get_path_from_root(os.getenv('APP')),
        'remote_url': os.getenv('DRIVER_REMOTE_URL'),
        'noReset': 'true',
        'fullReset': 'false'
    }

    return capabilities


DRIVER_TIMEOUT = '10.0'
