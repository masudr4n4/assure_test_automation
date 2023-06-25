# Assure test automation
Run Test Case
```behave --tags="login_org" -D headless=true  -f allure_behave.formatter:AllureFormatter -o allure-result```

View Reports
```
allure generate --clean allure-result && allure open
```
