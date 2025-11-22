import reflex as rx
from app.components.dashboard_sidebar import dashboard_sidebar
from app.states.user_state import UserState, Order, OrderItem


def order_item_preview(item: OrderItem) -> rx.Component:
    return rx.el.div(
        rx.image(
            src=item["image"],
            class_name="w-10 h-10 rounded-md object-cover border border-gray-200",
        ),
        class_name="flex -space-x-2",
    )


def order_card(order: Order) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.div(
                rx.el.span(order["id"], class_name="text-sm font-bold text-gray-900"),
                rx.el.span(order["date"], class_name="text-xs text-gray-500 ml-2"),
                class_name="flex items-center",
            ),
            rx.el.span(
                order["status"],
                class_name=rx.cond(
                    order["status"] == "تکمیل شده",
                    "px-2.5 py-1 rounded-full bg-green-100 text-green-700 text-xs font-semibold",
                    "px-2.5 py-1 rounded-full bg-yellow-100 text-yellow-700 text-xs font-semibold",
                ),
            ),
            class_name="flex justify-between items-start mb-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.foreach(order["items"], order_item_preview),
                class_name="flex items-center gap-2",
            ),
            rx.el.div(
                rx.el.span("مبلغ کل", class_name="text-xs text-gray-500 mr-2"),
                rx.el.span(
                    f"{order['total']:,.0f} تومان",
                    class_name="text-sm font-bold text-gray-900",
                ),
                class_name="flex items-center",
            ),
            class_name="flex justify-between items-center",
        ),
        rx.el.button(
            "مشاهده جزئیات",
            on_click=lambda: UserState.select_order(order["id"]),
            class_name="w-full mt-4 py-2 text-sm text-sky-600 font-medium hover:bg-sky-50 rounded-lg transition-colors border border-transparent hover:border-sky-100",
        ),
        class_name="bg-white p-5 rounded-xl border border-gray-100 shadow-sm hover:shadow-md transition-all",
    )


def order_detail_modal() -> rx.Component:
    order = UserState.selected_order
    return rx.cond(
        UserState.selected_order_id != "",
        rx.el.div(
            rx.el.div(
                on_click=UserState.close_order_modal,
                class_name="absolute inset-0 bg-black/40 backdrop-blur-sm",
            ),
            rx.cond(
                order,
                rx.el.div(
                    rx.el.div(
                        rx.el.h2(
                            "جزئیات سفارش", class_name="text-xl font-bold text-gray-900"
                        ),
                        rx.el.button(
                            rx.icon("x", class_name="w-5 h-5 text-gray-500"),
                            on_click=UserState.close_order_modal,
                            class_name="p-1 hover:bg-gray-100 rounded-full transition-colors",
                        ),
                        class_name="flex justify-between items-center mb-6 pb-4 border-b border-gray-100",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.p(
                                "شماره سفارش",
                                class_name="text-xs text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.p(
                                order["id"], class_name="font-semibold text-gray-900"
                            ),
                            class_name="mb-4",
                        ),
                        rx.el.div(
                            rx.el.p(
                                "کد رهگیری",
                                class_name="text-xs text-gray-500 uppercase tracking-wider",
                            ),
                            rx.el.p(
                                order["tracking_number"],
                                class_name="font-mono text-sm text-sky-600",
                            ),
                            class_name="mb-4",
                        ),
                        class_name="grid grid-cols-2 gap-4 mb-6",
                    ),
                    rx.el.h3(
                        "آیتم\u200cها", class_name="font-semibold text-gray-900 mb-3"
                    ),
                    rx.el.div(
                        rx.foreach(
                            order["items"],
                            lambda item: rx.el.div(
                                rx.image(
                                    src=item["image"],
                                    class_name="w-12 h-12 rounded-md object-cover border border-gray-100",
                                ),
                                rx.el.div(
                                    rx.el.p(
                                        item["name"],
                                        class_name="text-sm font-medium text-gray-900",
                                    ),
                                    rx.el.p(
                                        f"تعداد: {item['quantity']}",
                                        class_name="text-xs text-gray-500",
                                    ),
                                    class_name="flex-1 ml-3",
                                ),
                                rx.el.p(
                                    f"{item['price']:,.0f} تومان",
                                    class_name="text-sm font-semibold text-gray-900",
                                ),
                                class_name="flex items-center py-3 border-b border-gray-50 last:border-0",
                            ),
                        ),
                        class_name="mb-6",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.span(
                                "مبلغ پرداختی", class_name="font-medium text-gray-900"
                            ),
                            rx.el.span(
                                f"{order['total']:,.0f} تومان",
                                class_name="font-bold text-xl text-sky-600",
                            ),
                            class_name="flex justify-between items-center pt-4 border-t border-gray-100",
                        ),
                        class_name="mt-auto",
                    ),
                    rx.el.button(
                        rx.el.span("دانلود فاکتور", class_name="ml-2"),
                        rx.icon("download", class_name="w-4 h-4"),
                        class_name="mt-6 w-full flex items-center justify-center py-2.5 bg-gray-900 text-white rounded-lg font-medium hover:bg-gray-800 transition-colors",
                    ),
                    class_name="bg-white rounded-2xl w-full max-w-lg p-6 shadow-2xl relative z-10 animate-fade-in-up",
                ),
            ),
            class_name="fixed inset-0 z-50 flex items-center justify-center p-4",
        ),
    )


def orders_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1("تاریخچه سفارشات", class_name="text-2xl font-bold text-gray-900 mb-6"),
        rx.cond(
            UserState.orders.length() > 0,
            rx.el.div(
                rx.foreach(UserState.orders, order_card),
                class_name="grid grid-cols-1 md:grid-cols-2 gap-4",
            ),
            rx.el.div(
                rx.icon("package", class_name="w-16 h-16 text-gray-300 mb-4"),
                rx.el.p("هیچ سفارشی یافت نشد", class_name="text-gray-500"),
                class_name="flex flex-col items-center justify-center py-16 bg-white rounded-2xl border border-gray-100 border-dashed",
            ),
        ),
        order_detail_modal(),
        class_name="flex-1",
    )


def account_orders_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            dashboard_sidebar("/account/orders"),
            orders_page(),
            class_name="flex flex-col md:flex-row gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-gray-50/50 min-h-screen",
    )