import time, math, pytest


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('language', ['https://stepik.org/lesson/236895/step/1',
                                      'https://stepik.org/lesson/236896/step/1',
                                      'https://stepik.org/lesson/236897/step/1',
                                      'https://stepik.org/lesson/236898/step/1',
                                      'https://stepik.org/lesson/236899/step/1',
                                      'https://stepik.org/lesson/236903/step/1',
                                      'https://stepik.org/lesson/236904/step/1',
                                      'https://stepik.org/lesson/236905/step/1'])
class TestLogin:
    def test_guest_should_see_login_link(self, browser, language):
        link = f"{language}"
        browser.get(link)
        browser.implicity_wait(10)
        browser.find
        browser.find_element_by_css_selector("Correct!")
        # этот тест запустится 2 раза

    def test_guest_should_see_navbar_element(self, browser, language):
        pass# этот тест тоже запустится дважды

answer = math.log(int(time.time()))
