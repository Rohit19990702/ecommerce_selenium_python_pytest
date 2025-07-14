class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = "username"
        self.password_input = "password"
        self.login_button = "submit"

    def do_login(self, username, password):
        self.driver.find_element("id", self.username_input).send_keys(username)
        self.driver.find_element("id", self.password_input).send_keys(password)
        self.driver.find_element("id", self.login_button).click()