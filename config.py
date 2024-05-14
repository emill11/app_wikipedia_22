import os

from appium.options.android import UiAutomator2Options
from utils import file


class Config:

    def __init__(self):
        self.url = os.getenv('URL')
        self.device_name = os.getenv('DEVICE_NAME')
        self.platform_version = os.getenv('PLATFORM_VERSION')
        self.remote_app = os.getenv('REMOTE_APP')
        self.user_name = os.getenv('LOGIN')
        self.access_key = os.getenv('PASSWORD')
        self.app_wait_activity = os.getenv('APP_WAIT_ACTIVITY')
        self.local_app = os.getenv('LOCAL_APP')

        self.timeout = float(os.getenv('TIMEOUT', '10'))

    def to_driver_options(self, context):

        options = UiAutomator2Options()
        if context == 'bstack':
            options.set_capability('remote_url', self.url)
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
            options.set_capability("remote_url", self.url)
            options.set_capability('app', file.path_apk(self.local_app))
            options.set_capability('appWaitActivity', self.app_wait_activity)

        return options


config_app = Config()
