from selene import browser, be, have, by, command

from data.TestData import FilePaths


def test_practice_form():
    browser.open('automation-practice-form')
    browser.driver.execute_script("document.querySelector('#fixedban').remove();")
    browser.driver.execute_script("document.querySelector('footer').remove();")
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
    browser.element("#submit").perform(command.js.scroll_into_view)
    browser.element("#uploadPicture").send_keys(FilePaths.PHOTO_PATH)
    browser.element("#currentAddress").should(be.blank).type("221b, Baker Str.")
    browser.element("#state").click()
    browser.element(by.text('NCR')).click()
    browser.element("#city").click()
    browser.element(by.text('Delhi')).click()
    browser.element("#submit").click()
    browser.element(".modal-dialog").should(be.existing)
    browser.element(".table").all('td:nth-child(2)').should(have.exact_texts(
        'Benedict Cumberbatch',
        'benya@mail.ru',
        'Male',
        '0123456789',
        '24 September,1977',
        'Maths',
        'Reading',
        'bkb.jpeg',
        '221b, Baker Str.',
        'NCR Delhi',
    ))
