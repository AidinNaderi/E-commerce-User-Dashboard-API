import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.components.cart_drawer import cart_drawer
from app.pages.home import home_page
from app.pages.product_detail import product_detail_page
from app.pages.account_profile import account_profile_page
from app.pages.account_orders import account_orders_page
from app.pages.account_addresses import account_addresses_page
from app.pages.account_wishlist import account_wishlist_page
from app.pages.account_settings import account_settings_page
from app.pages.api_docs import api_docs_page
from app.states.product_state import ProductState


def layout(content: rx.Component) -> rx.Component:
    return rx.el.div(
        navbar(),
        cart_drawer(),
        rx.el.main(content, class_name="flex-1 w-full bg-white"),
        footer(),
        dir="rtl",
        class_name="min-h-screen flex flex-col font-['Vazirmatn'] antialiased text-gray-900",
    )


def index() -> rx.Component:
    return layout(home_page())


def product_page() -> rx.Component:
    return layout(product_detail_page())


def profile_page_route() -> rx.Component:
    return layout(account_profile_page())


def orders_page_route() -> rx.Component:
    return layout(account_orders_page())


def addresses_page_route() -> rx.Component:
    return layout(account_addresses_page())


def wishlist_page_route() -> rx.Component:
    return layout(account_wishlist_page())


def settings_page_route() -> rx.Component:
    return layout(account_settings_page())


app = rx.App(
    theme=rx.theme(appearance="light", accent_color="sky"),
    stylesheets=[
        "https://fonts.googleapis.com/css2?family=Vazirmatn:wght@100..900&display=swap"
    ],
)
app.add_page(index, route="/")
app.add_page(
    product_page, route="/product/[id]", on_load=ProductState.load_product_detail
)
app.add_page(profile_page_route, route="/account/profile")
app.add_page(orders_page_route, route="/account/orders")
app.add_page(addresses_page_route, route="/account/addresses")
app.add_page(wishlist_page_route, route="/account/wishlist")
app.add_page(settings_page_route, route="/account/settings")
app.add_page(api_docs_page, route="/developers/api")