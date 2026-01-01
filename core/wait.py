from playwright.sync_api import TimeoutError

class Wait:
    @staticmethod
    def until(page, condition, timeout=5000):
        try:
            page.wait_for_function(condition, timeout=timeout)
        except TimeoutError:
            raise AssertionError("Wait condition failed: " + condition)
