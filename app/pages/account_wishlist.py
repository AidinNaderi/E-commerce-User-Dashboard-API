import reflex as rx
from app.components.dashboard_sidebar import dashboard_sidebar
from app.states.user_state import UserState
from app.states.product_state import Product
from app.states.cart_state import CartState


def wishlist_item(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=product["images"][0],
                class_name="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-500",
            ),
            rx.el.button(
                rx.icon("x", class_name="w-4 h-4"),
                on_click=lambda: UserState.remove_from_wishlist(product["id"]),
                class_name="absolute top-2 right-2 bg-white/90 p-1.5 rounded-full shadow-sm text-gray-500 hover:text-red-500 transition-colors",
            ),
            class_name="relative overflow-hidden bg-gray-100 aspect-[4/3]",
        ),
        rx.el.div(
            rx.el.a(
                rx.el.h3(
                    product["name"],
                    class_name="font-semibold text-gray-900 mb-1 truncate",
                ),
                href=f"/product/{product['id']}",
                class_name="hover:text-sky-600 transition-colors block",
            ),
            rx.el.p(
                f"{product['price']:,.0f} تومان",
                class_name="text-lg font-bold text-gray-900 mb-3",
            ),
            rx.el.button(
                rx.icon("shopping-bag", class_name="w-4 h-4 mr-2"),
                "افزودن به سبد",
                on_click=lambda: CartState.add_to_cart(product),
                class_name="w-full flex items-center justify-center bg-sky-50 text-sky-600 hover:bg-sky-100 py-2 rounded-lg font-medium transition-colors",
            ),
            class_name="p-4",
        ),
        class_name="bg-white rounded-xl border border-gray-100 shadow-sm overflow-hidden group",
    )


def wishlist_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1(
            "لیست علاقه\u200cمندی\u200cها",
            class_name="text-2xl font-bold text-gray-900 mb-6",
        ),
        rx.cond(
            UserState.wishlist.length() > 0,
            rx.el.div(
                rx.foreach(UserState.wishlist, wishlist_item),
                class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6",
            ),
            rx.el.div(
                rx.icon("heart", class_name="w-16 h-16 text-gray-200 mb-4"),
                rx.el.p(
                    "لیست علاقه\u200cمندی شما خالی است", class_name="text-gray-500 mb-4"
                ),
                rx.el.a(
                    "مشاهده محصولات",
                    href="/",
                    class_name="text-sky-600 font-semibold hover:underline",
                ),
                class_name="flex flex-col items-center justify-center py-16 bg-white rounded-2xl border border-gray-100 border-dashed",
            ),
        ),
        class_name="flex-1",
    )


def account_wishlist_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            dashboard_sidebar("/account/wishlist"),
            wishlist_page(),
            class_name="flex flex-col md:flex-row gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-gray-50/50 min-h-screen",
    )