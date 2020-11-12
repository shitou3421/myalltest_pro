from test_interface.src.utils.handle_config import Utils


class Test:

    def setup(self):
        self.tools = Utils()

    def teardown(self):
        pass

    def test_handleenv(self):
        self.tools.handle_env()