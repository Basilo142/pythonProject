import pytest
import selenium
import time
import math

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = selenium.webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('lin', ['https://stepik.org/lesson/236895/step/1'])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, lin):
        print('1')
        link = f"{lin}"
        browser.get(link)
        # browser.implicity_wait(5)
        browser.find_element_by_tag_name('textarea')
        print(type('text_area'))
        browser.find_element_by_css_selector("Correct!")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, lin):
        pass# этот тест тоже запустится дважды

answer = math.log(int(time.time()))
