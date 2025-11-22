import reflex as rx
from app.states.cart_state import CartState
from app.states.product_state import ProductState


def navbar() -> rx.Component:
    return rx.el.nav(
        rx.el.div(
            rx.el.a(
                rx.el.div(
                    rx.icon("gamepad-2", class_name="text-sky-500 w-8 h-8"),
                    rx.el.span(
                        "اسکای\u200cگیم",
                        class_name="text-2xl font-bold text-gray-900 tracking-tight",
                    ),
                    class_name="flex items-center gap-2",
                ),
                href="/",
                class_name="cursor-pointer",
            ),
            rx.el.div(
                rx.icon(
                    "search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400",
                ),
                rx.el.input(
                    placeholder="جستجو در محصولات...",
                    on_change=ProductState.set_search_query.debounce(300),
                    class_name="w-full pl-10 pr-4 py-2.5 bg-gray-50 border border-gray-200 rounded-full focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent transition-all text-sm font-['Vazirmatn']",
                ),
                class_name="hidden md:block relative w-96 mx-8",
            ),
            rx.el.div(
                rx.el.a(
                    rx.icon("user", class_name="w-5 h-5"),
                    rx.el.span(
                        "حساب کاربری", class_name="hidden sm:block text-sm font-medium"
                    ),
                    href="/account/profile",
                    class_name="flex items-center gap-2 text-gray-600 hover:text-sky-600 transition-colors p-2 rounded-lg hover:bg-sky-50",
                ),
                rx.el.button(
                    rx.el.div(
                        rx.icon("shopping-cart", class_name="w-5 h-5"),
                        rx.cond(
                            CartState.total_items > 0,
                            rx.el.span(
                                CartState.total_items,
                                class_name="absolute -top-1 -right-1 bg-sky-500 text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full min-w-[18px] text-center border-2 border-white",
                            ),
                        ),
                        class_name="relative",
                    ),
                    rx.el.span(
                        "سبد خرید", class_name="hidden sm:block text-sm font-medium"
                    ),
                    on_click=CartState.toggle_cart,
                    class_name="flex items-center gap-2 text-gray-600 hover:text-sky-600 transition-colors p-2 rounded-lg hover:bg-sky-50 ml-2",
                ),
                class_name="flex items-center gap-2",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-20 flex items-center justify-between",
        ),
        class_name="sticky top-0 z-40 bg-white/80 backdrop-blur-md border-b border-gray-100",
    )