import pytest
import os
from datetime import datetime

# Hook for adding screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("reports/failures") else "w"
        with open("reports/failures", mode):
            driver = item.funcargs['setup']
            screenshot_name = f"reports/screenshot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
            driver.save_screenshot(screenshot_name)
            if "pytest_html" in item.config.pluginmanager.plugins:
                extra = getattr(rep, "extra", [])
                extra.append(pytest_html.extras.png(screenshot_name))
                rep.extra = extra
