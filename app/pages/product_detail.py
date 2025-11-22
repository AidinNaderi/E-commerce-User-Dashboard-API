import reflex as rx
from app.states.product_state import ProductState
from app.states.cart_state import CartState


def spec_row(key: str, value: str) -> rx.Component:
    return rx.el.div(
        rx.el.span(key, class_name="text-gray-500 font-medium w-1/3"),
        rx.el.span(value, class_name="text-gray-900 font-medium"),
        class_name="flex py-3 border-b border-gray-100 last:border-0",
    )


def review_card(review: dict) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.span(review["user"][0], class_name="text-white font-bold"),
                    class_name="w-10 h-10 rounded-full bg-sky-400 flex items-center justify-center",
                ),
                rx.el.div(
                    rx.el.h4(
                        review["user"], class_name="font-semibold text-gray-900 text-sm"
                    ),
                    rx.el.span(review["date"], class_name="text-gray-400 text-xs"),
                    class_name="ml-3",
                ),
                class_name="flex items-center",
            ),
            rx.el.div(
                rx.foreach(
                    rx.Var.range(review["rating"]),
                    lambda _: rx.icon(
                        "star", class_name="w-4 h-4 text-yellow-400 fill-yellow-400"
                    ),
                ),
                class_name="flex gap-0.5",
            ),
            class_name="flex justify-between items-center mb-3",
        ),
        rx.el.p(review["comment"], class_name="text-gray-600 text-sm leading-relaxed"),
        class_name="bg-gray-50 p-5 rounded-xl",
    )


def product_detail_page() -> rx.Component:
    product = ProductState.current_product
    return rx.cond(
        product,
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.a("خانه", href="/", class_name="hover:text-sky-600"),
                    rx.el.span("/", class_name="mx-2 text-gray-300"),
                    rx.el.a("محصولات", href="#", class_name="hover:text-sky-600"),
                    rx.el.span("/", class_name="mx-2 text-gray-300"),
                    rx.el.span(product["name"], class_name="text-gray-900"),
                    class_name="text-sm text-gray-500 flex items-center mb-8",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.image(
                            src=product["images"][0],
                            class_name="w-full aspect-square object-cover rounded-2xl border border-gray-100 shadow-sm bg-white",
                        ),
                        rx.el.div(
                            rx.foreach(
                                product["images"],
                                lambda img: rx.image(
                                    src=img,
                                    class_name="w-20 h-20 rounded-lg border border-gray-200 cursor-pointer hover:border-sky-500",
                                ),
                            ),
                            class_name="flex gap-4 mt-4 overflow-x-auto py-2",
                        ),
                        class_name="flex-1",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                product["category"],
                                class_name="text-sky-600 font-bold uppercase tracking-wider text-sm",
                            ),
                            rx.el.h1(
                                product["name"],
                                class_name="text-3xl md:text-4xl font-extrabold text-gray-900 mt-2 mb-4",
                            ),
                            rx.el.div(
                                rx.el.span(
                                    f"{product['price']:,.0f} تومان",
                                    class_name="text-3xl font-bold text-gray-900",
                                ),
                                rx.cond(
                                    product["original_price"] > 0,
                                    rx.el.span(
                                        f"{product['original_price']:,.0f} تومان",
                                        class_name="text-xl text-gray-400 line-through ml-3",
                                    ),
                                ),
                                class_name="flex items-baseline mb-6",
                            ),
                            rx.el.div(
                                rx.icon(
                                    "star",
                                    class_name="w-5 h-5 text-yellow-400 fill-yellow-400",
                                ),
                                rx.el.span(
                                    f"{product['rating']} ({product['review_count']} نظر)",
                                    class_name="text-sm font-medium text-gray-600 ml-2",
                                ),
                                class_name="flex items-center mb-6",
                            ),
                            rx.el.p(
                                product["description"],
                                class_name="text-gray-600 leading-relaxed mb-8",
                            ),
                            rx.el.div(
                                rx.el.button(
                                    "افزودن به سبد خرید",
                                    on_click=lambda: CartState.add_to_cart(product),
                                    class_name="flex-1 bg-sky-500 hover:bg-sky-600 text-white py-4 rounded-xl font-bold shadow-lg shadow-sky-200 hover:shadow-sky-300 transition-all",
                                ),
                                rx.el.button(
                                    rx.icon("heart", class_name="w-6 h-6"),
                                    class_name="p-4 border border-gray-200 rounded-xl hover:bg-gray-50 text-gray-400 hover:text-red-500 transition-colors",
                                ),
                                class_name="flex gap-4 mb-8",
                            ),
                            rx.el.div(
                                rx.el.h3(
                                    "مشخصات اکانت",
                                    class_name="font-bold text-gray-900 mb-4",
                                ),
                                rx.el.div(
                                    rx.foreach(
                                        product["specs"].entries(),
                                        lambda item: spec_row(item[0], item[1]),
                                    ),
                                    class_name="bg-gray-50 rounded-xl p-6",
                                ),
                            ),
                        ),
                        class_name="flex-1 lg:max-w-lg",
                    ),
                    class_name="flex flex-col lg:flex-row gap-12",
                ),
                rx.el.div(
                    rx.el.h3(
                        "نظرات مشتریان",
                        class_name="text-2xl font-bold text-gray-900 mb-6",
                    ),
                    rx.cond(
                        product["reviews"].length() > 0,
                        rx.el.div(
                            rx.foreach(product["reviews"], review_card),
                            class_name="grid grid-cols-1 md:grid-cols-2 gap-6",
                        ),
                        rx.el.p(
                            "هنوز نظری ثبت نشده است.", class_name="text-gray-500 italic"
                        ),
                    ),
                    class_name="mt-20 pt-12 border-t border-gray-100",
                ),
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        rx.el.div(
            rx.spinner(class_name="text-sky-500"),
            class_name="flex items-center justify-center min-h-[60vh]",
        ),
    )