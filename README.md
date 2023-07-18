# Assure test automation
Run Test Case
```behave --tags="login_org" -D headless=true  -f allure_behave.formatter:AllureFormatter -o allure-result```

View Reports
```
allure generate --clean allure-result && allure open
```
Report should open in default browser and it will loook like below:
<img width="1512" alt="image" src="https://github.com/masudr4n4/assure_test_automation/assets/34313493/fac81249-4b4f-49e9-b8f4-e79a2a5b9b68">

<img width="1512" alt="image" src="https://github.com/masudr4n4/assure_test_automation/assets/34313493/572b5d10-0802-4319-aa53-cbe89678aae1">
<img width="1512" alt="image" src="https://github.com/masudr4n4/assure_test_automation/assets/34313493/4556743d-bcd2-4bd5-b3f1-e108e70409be">

