# rest-api-automation

How to generate allure report?
1. Install allure for pytest - https://docs.qameta.io/allure/#_pytest
2. Execute tests via: pytest -s run.py --alluredir=/tmp/allure_reports/
3. After executing tests execute: allure serve /tmp/allure_reports/

And report will be generated :)
