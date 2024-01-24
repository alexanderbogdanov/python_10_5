from selene import browser, be, by

from data.TestData import FilePaths
from helpers.common_helpers import scroll_to


def fill_form(user_data):
    browser.element('#firstName').should(be.blank).type(user_data['first_name'])
    browser.element('#lastName').should(be.blank).type(user_data['last_name'])
    browser.element('#userEmail').should(be.blank).type(user_data['email'])
    browser.element("[for='gender-radio-1']").click()
    browser.element('#userNumber').should(be.blank).type(user_data['phone'])
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element(".react-datepicker__year-select").click().element(
        by.text(user_data['year'])
    ).click()
    browser.element(".react-datepicker__month-select").click().element(
        by.text(user_data['month'])
    ).click()
    browser.element(".react-datepicker__day--024").click()
    browser.element("#subjectsInput").should(be.blank).click().type(user_data['subjects']).press_enter()
    browser.element("[for='hobbies-checkbox-2']").click()
    scroll_to("#submit")
    browser.element("#uploadPicture").send_keys(FilePaths.PHOTO_PATH)
    browser.element("#currentAddress").should(be.blank).type(user_data['address'])
    browser.element("#state").click()
    browser.element(by.text(user_data['state'])).click()
    browser.element("#city").click()
    browser.element(by.text(user_data['city'])).click()
    browser.element("#submit").click()
