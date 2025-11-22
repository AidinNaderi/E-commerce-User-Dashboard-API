import reflex as rx
from typing import TypedDict
from .product_state import Product


class CartItem(TypedDict):
    product: Product
    quantity: int


class CartState(rx.State):
    items: list[CartItem] = []
    is_open: bool = False

    @rx.var
    def total_items(self) -> int:
        return sum((item["quantity"] for item in self.items))

    @rx.var
    def subtotal(self) -> float:
        return sum((item["product"]["price"] * item["quantity"] for item in self.items))

    @rx.event
    def toggle_cart(self):
        self.is_open = not self.is_open

    @rx.event
    def add_to_cart(self, product: Product):
        found = False
        new_items = []
        for item in self.items:
            if item["product"]["id"] == product["id"]:
                item["quantity"] += 1
                found = True
            new_items.append(item)
        if not found:
            new_items.append({"product": product, "quantity": 1})
        self.items = new_items
        self.is_open = True

    @rx.event
    def remove_from_cart(self, product_id: str):
        self.items = [
            item for item in self.items if item["product"]["id"] != product_id
        ]

    @rx.event
    def increment_quantity(self, product_id: str):
        new_items = []
        for item in self.items:
            if item["product"]["id"] == product_id:
                item["quantity"] += 1
            new_items.append(item)
        self.items = new_items

    @rx.event
    def decrement_quantity(self, product_id: str):
        new_items = []
        for item in self.items:
            if item["product"]["id"] == product_id:
                if item["quantity"] > 1:
                    item["quantity"] -= 1
                    new_items.append(item)
                else:
                    pass
            else:
                new_items.append(item)
        self.items = new_items