from os import path

from selene import browser, be, have, by, command


def test_practice_form():

    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector("#fixedban").remove()')
    browser.execute_script('document.querySelector("footer").remove()')
    browser.element('#firstName').should(be.blank).type('Benedict')
    browser.element('#lastName').should(be.blank).type('Cumberbatch')
    browser.element('#userEmail').should(be.blank).type('benya@mail.ru')
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type('0123456789')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text("1977")
    ).click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text("September")
    ).click()
    browser.element(".react-datepicker__day--024").click()
    browser.element("#subjectsInput").should(be.blank).click().type('Maths').press_enter()
    browser.element("[for='hobbies-checkbox-2']").click()
    browser.element("#uploadPicture").send_keys(
        path.abspath("resources/bkb.jpeg"))
    # browser.element("#currentAddress").click()

    # browser.execute_script()
    # react-datepicker__month-container
    browser.open('/automation-practice-form')
#fixedban

# def remove(element)

