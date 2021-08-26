import pytest
import selenium
import time
import math















#
# lis_t = [
#     'https://stepik.org/lesson/236895/step/1',
#     'https://stepik.org/lesson/236896/step/1'
#     'https://stepik.org/lesson/236897/step/1',
#     'https://stepik.org/lesson/236898/step/1',
#     'https://stepik.org/lesson/236899/step/1',
#     'https://stepik.org/lesson/236903/step/1',
#     'https://stepik.org/lesson/236904/step/1',
#     'https://stepik.org/lesson/236905/step/1'
# ]
#
#
# @pytest.fixture(scope="function")
# def browser():
#     print("\nstart browser for test..")
#     browser = selenium.webdriver.Chrome()
#     yield browser
#     print("\nquit browser..")
#     browser.quit()
#
#
# @pytest.mark.parametrize('lin', lis_t)
# class TestLogin:
#     def test_guest_should_see_login_link(self, browser, lin):
#         print('1')
#         link = f"{lin}"
#         browser.get(link)
#         # browser.implicity_wait(5)
#         browser.find_element_by_tag_name('textarea')
#         print(type('text_area'))
#         browser.find_element_by_css_selector("Correct!")
#         # этот тест запустится 2 раза
#
#     def test_guest_should_see_navbar_element(self, browser, lin):
#         pass# этот тест тоже запустится дважды
#
# answer = math.log(int(time.time()))
#
#
