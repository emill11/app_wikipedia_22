import os

from dotenv import load_dotenv
from appium.options.android import UiAutomator2Options
from utils import file

load_dotenv()


class Config:
    remote_url = os.getenv('REMOTE_URL')
    device_name = os.getenv('DEVICE_NAME')
    platform_version = os.getenv('PLATFORM_VERSION')
    remote_app = os.getenv('REMOTE_APP')
    user_name = os.getenv('LOGIN')
    access_key = os.getenv('PASSWORD')

    local_url = os.getenv('LOCAL_URL')
    app_wait_activity = os.getenv('APP_WAIT_ACTIVITY')
    local_app = os.getenv('LOCAL_APP')

    timeout = float(os.getenv('TIMEOUT', '10'))

    def to_driver_options(self, context):
        options = UiAutomator2Options()

        if context == 'bstack':
            options.set_capability('remote_url', self.remote_url)
            options.set_capability('deviceName', self.device_name)
            options.set_capability('platformVersion', self.platform_version)
            options.set_capability('app', self.remote_app)

            options.set_capability(
                'bstack:options',
                {
                    "projectName": "First Pyack-build-1",
                    "sessionName": "BStack fthon project",
                    "buildName": "browserstirst_test",

                    "userName": self.user_name,
                    "accessKey": self.access_key
                })

        if context == 'local':
            options.set_capability('local_url', self.local_url)
            options.set_capability('appWaitActivity', self.app_wait_activity)
            options.set_capability('app', file.path_apk(self.local_app))

        return options


config_app = Config()
