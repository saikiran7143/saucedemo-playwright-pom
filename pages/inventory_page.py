class InventoryPage:
    def __init__(self, page):
        self.page = page
        self.add_backpack_btn = "#add-to-cart-sauce-labs-backpack"
        self.cart_icon = ".shopping_cart_link"
        self.cart_item_name = ".inventory_item_name"

    def add_backpack_to_cart(self):
        self.page.click(self.add_backpack_btn)

    def open_cart(self):
        self.page.click(self.cart_icon)

    def get_cart_item_name(self):
        return self.page.inner_text(self.cart_item_name)
