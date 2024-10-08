from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

    def add_to_cart(self, product_name):
        self.driver.find_element(
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button"
        ).click()

    def go_to_cart(self):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
