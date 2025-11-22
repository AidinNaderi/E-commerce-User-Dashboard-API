import reflex as rx
from app.components.dashboard_sidebar import dashboard_sidebar
from app.states.user_state import UserState, Address


def address_card(address: Address) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.icon("map-pin", class_name="w-5 h-5 text-sky-500"),
                rx.el.h3(address["label"], class_name="font-bold text-gray-900 ml-2"),
                rx.cond(
                    address["is_default"],
                    rx.el.span(
                        "پیش\u200cفرض",
                        class_name="ml-2 px-2 py-0.5 bg-sky-100 text-sky-700 text-[10px] uppercase font-bold rounded-full tracking-wider",
                    ),
                ),
                class_name="flex items-center mb-3",
            ),
            rx.el.button(
                rx.icon("trash-2", class_name="w-4 h-4"),
                on_click=lambda: UserState.remove_address(address["id"]),
                class_name="text-gray-400 hover:text-red-500 transition-colors p-1",
            ),
            class_name="flex justify-between items-start",
        ),
        rx.el.div(
            rx.el.p(address["street"], class_name="text-gray-600"),
            rx.el.p(
                f"{address['city']}, {address['state']} {address['zip_code']}",
                class_name="text-gray-600",
            ),
            rx.el.p(address["country"], class_name="text-gray-600"),
            class_name="text-sm leading-relaxed mb-4",
        ),
        rx.cond(
            ~address["is_default"],
            rx.el.button(
                "تنظیم به عنوان پیش\u200cفرض",
                on_click=lambda: UserState.set_default_address(address["id"]),
                class_name="text-sm text-sky-600 font-medium hover:underline",
            ),
            rx.el.span("آدرس پیش\u200cفرض", class_name="text-sm text-gray-400 italic"),
        ),
        class_name="bg-white p-6 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-all",
    )


def addresses_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h1(
                "آدرس\u200cهای ذخیره شده", class_name="text-2xl font-bold text-gray-900"
            ),
            rx.el.button(
                rx.icon("plus", class_name="w-4 h-4 mr-2"),
                "افزودن آدرس جدید",
                class_name="flex items-center bg-gray-900 hover:bg-gray-800 text-white px-4 py-2 rounded-lg text-sm font-semibold transition-colors",
            ),
            class_name="flex justify-between items-center mb-6",
        ),
        rx.el.div(
            rx.foreach(UserState.addresses, address_card),
            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
        ),
        class_name="flex-1",
    )


def account_addresses_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            dashboard_sidebar("/account/addresses"),
            addresses_page(),
            class_name="flex flex-col md:flex-row gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-gray-50/50 min-h-screen",
    )