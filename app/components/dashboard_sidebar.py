import reflex as rx


def sidebar_item(text: str, icon_name: str, url: str, is_active: bool) -> rx.Component:
    return rx.el.a(
        rx.icon(
            icon_name,
            class_name=rx.cond(
                is_active,
                "w-5 h-5 text-sky-600",
                "w-5 h-5 text-gray-400 group-hover:text-gray-600",
            ),
        ),
        rx.el.span(text, class_name="font-medium"),
        href=url,
        class_name=rx.cond(
            is_active,
            "flex items-center gap-3 px-4 py-3 bg-sky-50 text-sky-700 rounded-xl border border-sky-100 transition-all",
            "flex items-center gap-3 px-4 py-3 text-gray-600 hover:bg-gray-50 hover:text-gray-900 rounded-xl transition-all group",
        ),
    )


def dashboard_sidebar(current_path: str) -> rx.Component:
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "حساب کاربری",
                    class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4 px-4",
                ),
                rx.el.nav(
                    sidebar_item(
                        "پروفایل",
                        "user",
                        "/account/profile",
                        current_path == "/account/profile",
                    ),
                    sidebar_item(
                        "سفارش\u200cها",
                        "package",
                        "/account/orders",
                        current_path == "/account/orders",
                    ),
                    sidebar_item(
                        "آدرس\u200cها",
                        "map-pin",
                        "/account/addresses",
                        current_path == "/account/addresses",
                    ),
                    sidebar_item(
                        "علاقه\u200cمندی\u200cها",
                        "heart",
                        "/account/wishlist",
                        current_path == "/account/wishlist",
                    ),
                    sidebar_item(
                        "تنظیمات",
                        "settings",
                        "/account/settings",
                        current_path == "/account/settings",
                    ),
                    class_name="space-y-1",
                ),
                class_name="mb-8",
            ),
            rx.el.div(
                rx.el.h3(
                    "پشتیبانی",
                    class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4 px-4",
                ),
                rx.el.nav(
                    sidebar_item("مرکز راهنما", "circle_plus", "#", False),
                    sidebar_item("خروج", "log-out", "/", False),
                    class_name="space-y-1",
                ),
            ),
            class_name="flex flex-col h-full",
        ),
        class_name="w-full md:w-64 shrink-0 md:min-h-[600px]",
    )