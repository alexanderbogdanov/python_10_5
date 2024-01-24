import json

import pytest
from selene import browser, be, have

from data.TestData import FilePaths
from helpers.common_helpers import remove
from helpers.forms_helper import fill_form


@pytest.fixture(scope="session")
def data():
    with open(FilePaths.USER_DATA_PATH) as file:
        return json.load(file)


def test_practice_form(data):
    browser.open('automation-practice-form')
    remove("#fixedban")
    remove("footer")
    fill_form(data['user_data'])
    browser.element(".modal-dialog").should(be.existing)
    browser.element(".table").all('td:nth-child(2)').should(have.exact_texts(list(data['user_data_check'].values())))
