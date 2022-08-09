# Assure test automation

```behave --tags="login_org" -D headless=true  -f allure_behave.formatter:AllureFormatter -o allure-result```

```
allure generate --clean allure-result && allure open
```