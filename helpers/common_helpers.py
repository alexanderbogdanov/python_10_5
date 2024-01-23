from selene import browser, command


def remove(element_selector):
    js_code = f"document.querySelector(\"{element_selector}\").remove();"
    browser.driver.execute_script(js_code)


def scroll_to(element_selector):
    browser.element(element_selector).perform(command.js.scroll_into_view)
