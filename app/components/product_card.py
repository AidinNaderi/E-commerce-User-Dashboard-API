import reflex as rx
from app.states.product_state import Product
from app.states.cart_state import CartState


def product_card(product: Product) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=product["images"][0],
                class_name="w-full h-64 object-cover transform hover:scale-105 transition-transform duration-500",
            ),
            rx.cond(
                product["original_price"] > 0,
                rx.el.span(
                    "فروش ویژه",
                    class_name="absolute top-3 left-3 bg-red-500 text-white text-xs font-bold px-2 py-1 rounded shadow-sm",
                ),
            ),
            rx.el.button(
                rx.icon("shopping-bag", class_name="w-5 h-5"),
                on_click=lambda: CartState.add_to_cart(product),
                class_name="absolute bottom-3 right-3 bg-white text-gray-800 p-2.5 rounded-full shadow-lg hover:bg-sky-500 hover:text-white transition-all opacity-0 group-hover:opacity-100 translate-y-2 group-hover:translate-y-0",
            ),
            class_name="relative overflow-hidden bg-gray-100 aspect-square",
        ),
        rx.el.a(
            rx.el.div(
                rx.el.div(
                    rx.el.span(
                        product["category"],
                        class_name="text-xs font-medium text-sky-600 uppercase tracking-wider",
                    ),
                    rx.el.div(
                        rx.icon(
                            "star",
                            class_name="w-3.5 h-3.5 text-yellow-400 fill-yellow-400",
                        ),
                        rx.el.span(
                            product["rating"],
                            class_name="text-xs font-medium text-gray-500 ml-1",
                        ),
                        class_name="flex items-center",
                    ),
                    class_name="flex justify-between items-center mb-2",
                ),
                rx.el.h3(
                    product["name"],
                    class_name="text-gray-900 font-semibold text-lg mb-1 truncate group-hover:text-sky-600 transition-colors",
                ),
                rx.el.div(
                    rx.el.span(
                        f"{product['price']:,.0f} تومان",
                        class_name="text-gray-900 font-bold",
                    ),
                    rx.cond(
                        product["original_price"] > 0,
                        rx.el.span(
                            f"{product['original_price']:,.0f} تومان",
                            class_name="text-gray-400 text-sm line-through ml-2",
                        ),
                    ),
                    class_name="flex items-baseline",
                ),
                class_name="p-5",
            ),
            href=f"/product/{product['id']}",
            class_name="block",
        ),
        class_name="group bg-white rounded-2xl overflow-hidden border border-gray-100 hover:shadow-xl hover:shadow-sky-100/50 transition-all duration-300",
    )