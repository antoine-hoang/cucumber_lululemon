Feature: Automate API GET

    Scenario: Successful API GET - Status 200
        Given the user pings the API and gets status 200
        Then the user validates the JSON output

