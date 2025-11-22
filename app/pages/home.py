import reflex as rx
from app.states.product_state import ProductState, Category
from app.components.product_card import product_card


def category_card(category: Category) -> rx.Component:
    return rx.el.a(
        rx.el.div(
            rx.icon(category["icon"], class_name="w-8 h-8 text-sky-500 mb-3"),
            rx.el.h3(category["name"], class_name="font-semibold text-gray-900"),
            rx.el.p(
                f"{category['count']} محصول", class_name="text-sm text-gray-500 mt-1"
            ),
            class_name="bg-white p-6 rounded-xl border border-gray-100 hover:border-sky-200 hover:shadow-lg hover:shadow-sky-50/50 transition-all duration-300 group cursor-pointer h-full",
        ),
        href="#",
        class_name="block",
    )


def hero_section() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(
                    "جدیدترین اکانت\u200cهای گیمینگ",
                    class_name="text-sky-600 font-bold tracking-wider text-sm uppercase mb-4 block",
                ),
                rx.el.h1(
                    "تجربه حرفه\u200cای بازی با اکانت\u200cهای سطح بالا",
                    class_name="text-4xl md:text-6xl font-extrabold text-gray-900 leading-tight mb-6",
                ),
                rx.el.p(
                    "مجموعه\u200cای بی\u200cنظیر از اکانت\u200cهای بازی\u200cهای محبوب. از پابجی موبایل و کال آف دیوتی تا فورتنایت و کلش آف کلنز، با تضمین امنیت و بهترین قیمت.",
                    class_name="text-lg text-gray-600 mb-8 max-w-lg",
                ),
                rx.el.div(
                    rx.el.button(
                        "مشاهده فروشگاه",
                        class_name="bg-sky-500 hover:bg-sky-600 text-white px-8 py-3.5 rounded-full font-semibold transition-all shadow-lg shadow-sky-200 hover:shadow-sky-300 transform hover:-translate-y-0.5",
                    ),
                    rx.el.button(
                        "ارتباط با پشتیبانی",
                        class_name="bg-white text-gray-700 border border-gray-200 hover:border-gray-300 px-8 py-3.5 rounded-full font-semibold transition-all hover:bg-gray-50",
                    ),
                    class_name="flex flex-wrap gap-4",
                ),
                class_name="flex-1 z-10",
            ),
            rx.el.div(
                rx.image(
                    src="/placeholder.svg",
                    class_name="w-full h-auto object-cover rounded-3xl shadow-2xl transform md:rotate-2 hover:rotate-0 transition-transform duration-500",
                ),
                class_name="flex-1 max-w-lg relative",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-24 flex flex-col md:flex-row items-center gap-12 md:gap-20",
        ),
        class_name="bg-gradient-to-b from-sky-50/50 to-white",
    )


def home_page() -> rx.Component:
    return rx.el.div(
        hero_section(),
        rx.el.div(
            rx.el.div(
                rx.el.h2(
                    "دسته\u200cبندی بازی\u200cها",
                    class_name="text-2xl font-bold text-gray-900 mb-8",
                ),
                rx.el.div(
                    rx.foreach(ProductState.categories, category_card),
                    class_name="grid grid-cols-2 md:grid-cols-4 gap-6",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
            )
        ),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.h2(
                        "محصولات ویژه", class_name="text-2xl font-bold text-gray-900"
                    ),
                    rx.el.a(
                        "مشاهده همه",
                        href="#",
                        class_name="text-sky-600 font-semibold hover:text-sky-700 flex items-center gap-1",
                    ),
                    class_name="flex justify-between items-end mb-8",
                ),
                rx.el.div(
                    rx.foreach(ProductState.filtered_products, product_card),
                    class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-8",
                ),
                class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16",
            ),
            class_name="bg-gray-50/50",
        ),
    )