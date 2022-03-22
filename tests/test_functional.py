from framework.pages.authenticate_page import AuthenticatePage
from framework.pages.main_page import MainPage
from framework.utils.random_utils import RandomUtils
from framework.constants.random import COUNT_INTERESTS

class TestFunctional(object):

    def test_authenticate(self, create_browser, base_fix):
        main_page = MainPage()
        main_is_open = main_page.is_opened()
        assert main_is_open, 'Main page is not open'
        main_page.click_button_here_to_go()
        auth_page = AuthenticatePage()
        auth_is_open = auth_page.is_opened()
        assert auth_is_open, 'Auth page is not open'
        auth_page.send_password()
        auth_page.send_email()
        auth_page.send_domain()
        auth_page.click_button_other()
        auth_page.send_other_value()
        auth_page.click_button_do_not_accept()
        auth_page.click_button_next()

    def test_help_exit(self, create_browser, base_fix):
        main_page = MainPage()
        main_is_open = main_page.is_opened()
        assert main_is_open, 'Main page is not open'
        main_page.click_button_here_to_go()
        auth_page = AuthenticatePage()
        auth_is_open = auth_page.is_opened()
        assert auth_is_open, 'Auth page is not open'
        auth_page.exit_help_window()
        import time
        time.sleep(5)

    def test_add_cookies(self, create_browser, base_fix):
        main_page = MainPage()
        main_is_open = main_page.is_opened()
        assert main_is_open, 'Main page is not open'
        main_page.click_button_here_to_go()
        auth_page = AuthenticatePage()
        auth_is_open = auth_page.is_opened()
        assert auth_is_open, 'Auth page is not open'
        cookie = auth_page.accept_cookies()
        assert cookie, 'Cookies не приняты'
