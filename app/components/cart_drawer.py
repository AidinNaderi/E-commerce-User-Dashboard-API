import reflex as rx
from app.states.cart_state import CartState, CartItem


def cart_item_view(item: CartItem) -> rx.Component:
    product = item["product"]
    return rx.el.div(
        rx.image(
            src=product["images"][0],
            class_name="w-20 h-20 object-cover rounded-lg border border-gray-100 bg-gray-50",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h4(
                    product["name"],
                    class_name="text-sm font-semibold text-gray-900 line-clamp-2",
                ),
                rx.el.button(
                    rx.icon("x", class_name="w-4 h-4 text-gray-400 hover:text-red-500"),
                    on_click=lambda: CartState.remove_from_cart(product["id"]),
                ),
                class_name="flex justify-between items-start gap-2",
            ),
            rx.el.p(
                f"{product['price']:,.0f} تومان",
                class_name="text-sky-600 font-medium text-sm mt-1",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.button(
                        "-",
                        on_click=lambda: CartState.decrement_quantity(product["id"]),
                        class_name="w-6 h-6 flex items-center justify-center text-gray-500 hover:bg-gray-100 rounded",
                    ),
                    rx.el.span(
                        item["quantity"],
                        class_name="text-sm font-medium w-6 text-center",
                    ),
                    rx.el.button(
                        "+",
                        on_click=lambda: CartState.increment_quantity(product["id"]),
                        class_name="w-6 h-6 flex items-center justify-center text-gray-500 hover:bg-gray-100 rounded",
                    ),
                    class_name="flex items-center border border-gray-200 rounded-md",
                ),
                class_name="flex justify-between items-center mt-3",
            ),
            class_name="flex-1 ml-4",
        ),
        class_name="flex p-4 border-b border-gray-100 last:border-0 animate-fade-in",
    )


def cart_drawer() -> rx.Component:
    return rx.el.div(
        rx.cond(
            CartState.is_open,
            rx.el.div(
                on_click=CartState.toggle_cart,
                class_name="fixed inset-0 bg-black/30 backdrop-blur-sm z-50 transition-opacity duration-300",
            ),
        ),
        rx.el.div(
            rx.el.div(
                rx.el.h2("سبد خرید", class_name="text-xl font-bold text-gray-900"),
                rx.el.button(
                    rx.icon("x", class_name="w-6 h-6"),
                    on_click=CartState.toggle_cart,
                    class_name="p-2 hover:bg-gray-100 rounded-full transition-colors",
                ),
                class_name="flex items-center justify-between p-5 border-b border-gray-100",
            ),
            rx.el.div(
                rx.cond(
                    CartState.items.length() > 0,
                    rx.el.div(
                        rx.foreach(CartState.items, cart_item_view),
                        class_name="flex flex-col",
                    ),
                    rx.el.div(
                        rx.icon(
                            "shopping-bag", class_name="w-16 h-16 text-gray-200 mb-4"
                        ),
                        rx.el.p(
                            "سبد خرید شما خالی است",
                            class_name="text-gray-500 font-medium",
                        ),
                        rx.el.button(
                            "شروع خرید",
                            on_click=CartState.toggle_cart,
                            class_name="mt-4 text-sky-600 font-medium hover:underline",
                        ),
                        class_name="flex flex-col items-center justify-center h-64",
                    ),
                ),
                class_name="flex-1 overflow-y-auto",
            ),
            rx.cond(
                CartState.items.length() > 0,
                rx.el.div(
                    rx.el.div(
                        rx.el.span("جمع کل", class_name="text-gray-600 font-medium"),
                        rx.el.span(
                            f"{CartState.subtotal:,.0f} تومان",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        class_name="flex justify-between items-center mb-4",
                    ),
                    rx.el.button(
                        "تسویه حساب",
                        class_name="w-full py-3.5 bg-sky-500 hover:bg-sky-600 text-white font-semibold rounded-xl shadow-lg shadow-sky-200 transition-all transform active:scale-95",
                    ),
                    rx.el.p(
                        "محاسبه هزینه ارسال و مالیات در مرحله بعد.",
                        class_name="text-center text-xs text-gray-400 mt-3",
                    ),
                    class_name="p-5 border-t border-gray-100 bg-gray-50",
                ),
            ),
            class_name=rx.cond(
                CartState.is_open,
                "fixed inset-y-0 left-0 w-full sm:w-[400px] bg-white shadow-2xl z-50 flex flex-col transition-transform duration-300 translate-x-0",
                "fixed inset-y-0 left-0 w-full sm:w-[400px] bg-white shadow-2xl z-50 flex flex-col transition-transform duration-300 -translate-x-full",
            ),
        ),
    )