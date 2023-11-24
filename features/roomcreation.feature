Feature: Create two rooms

    Scenario: Successful room creation
        Given the user has logged in successfully
        When the user creates its two rooms
        Then the booking list shows the newly created rooms
        And close the browser - success

    Scenario: Unsuccessful login
        Given the user has incorrect credentials
        When the user tries to log in
        Then the application indicates an error
        And close the browser - unsuccessful login

    Scenario: Successful login - Unsuccessful room creation - Room number
        Given the user has logged in successfully - Room number scenario
        When the user creates its two rooms - Room number scenario
        Then the application indicates an error - Room number scenario
        And close the browser - unsuccessful room creation - Room number scenario

    Scenario: Successful login - Unsuccessful room creation - Room price
        Given the user has logged in successfully - Room price scenario
        When the user creates its two rooms - Room price scenario
        Then the application indicates an error - Room price scenario
        And close the browser - unsuccessful room creation - Room price scenario
