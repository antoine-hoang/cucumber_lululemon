# cucumber_lululemon
Results:

![api](https://github.com/antoine-hoang/cucumber_lululemon/assets/151917085/4d9e0894-5064-47b0-85a4-909583da640b)


![room](https://github.com/antoine-hoang/cucumber_lululemon/assets/151917085/cd011461-70c8-4064-bd8d-21b6ac968b8c)


Structure of the project is as follows:
###############################################################
            Files related to exercice 1 are:
            
            - page_object
              -base_page.py
              -booking_page.py
              -login_page.py
            -steps
              -login_fail.py
              -scenario_fail_room_number.py
              -scenario_fail_room_price.py
              -scenario_success.py
            roomcreation.feature
            
            All tests have been implemented with Cucumber's feature and can be run with the command:
            behave features\roomcreation.feature
            

###############################################################
            Files related to exercice 2 are:
            
            -steps
              -api_automate.py
            api_automation.feature
            
            All tests have been implemented with Cucumber's feature and can be run with the command:
            behave features\api_automation.feature

###############################################################
           
            All requirements to run the project are in the requirements.txt



- Project has been implemented using the page object model design pattern where every page of the application (in our cases, the ones
  pertaining to the exercices only) have their own page class that contain operations related to that page only to promote modularity, reusability
  and code maintenance.
- Base page is the parent page to Booking and Login pages, which contain their own specific higher-level functions

> Additional explanations for Ex1:
- Assertion for the login success has been done with an element located on a deeper page
- Assertion for a failed login has been done with a visual change around the username and password fields, as a cue for erronous input
- Assertion for a successful room creation has been done by observing the difference in length in the booking list, which has been captured with a general xpath
  encapsulating all of them
- A second assertion for a successful room creation has been done by specifically targetting the last 2 entries on the booking list and validating their room number values
  Since this assertion is second to an assertion of length, we can be sure that the entries are newly added
- Assertion for a failed room creation by entering an erronous number has been done by checking the id corresponding to the error message for room number
- Assertion for a failed room creation by entering an erronous price has been done by checking the id corresponding to the error message for room price
  
> Additional explanations for Ex2:
- none, everything is relatively straightforward in the instructions

> Notes to the reviewer
- I could have added more failed paths but they somewhat ressemble each other so I hope the ones provided will be enough
- There are many more kickout cases that I could have put in, for example validating the text for when we input prices larger than 999, or lower than 0
      - Fatal bugs that could have been tested, like inputing letters into the room number and room price field breaks the application
      - Instances where the checkboxes don't register correctly after multiple room creations
      - Instances where the checkboxes register as numbers and not as room details
- I have done the exercices twice, one normally with pytest, selenium, python - and another refactoring including Cucumber and Gherkins
- Having not necessarily an extensive training on Cucumber, I had to spend a lot of time looking at how to refactor my code (which worked without Cucumber already)
  and I may have some complexity issues in some functions because of that. 
    - I haven't figured out how to combine my conftest.py file with Cucumber yet
    - I haven't figured out how to use the same grouping suites as pytest and the mark decoration with Cucumber
- I would be looking to add a report generator, similar to the one provided with pytest, but with Cucumber - need to investigate this matter.
- Overall an interesting exercice, especially because of the refactoring with Cucumber, which took almost 80% of the total time spent on this project.
  





  
