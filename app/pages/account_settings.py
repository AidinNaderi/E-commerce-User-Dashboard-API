import reflex as rx
from app.components.dashboard_sidebar import dashboard_sidebar
from app.states.user_state import UserState


def setting_toggle(
    label: str, description: str, setting_key: str, is_checked: bool
) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h4(label, class_name="font-medium text-gray-900"),
            rx.el.p(description, class_name="text-sm text-gray-500 mt-0.5"),
            class_name="flex-1 mr-4",
        ),
        rx.el.button(
            rx.cond(
                is_checked,
                rx.el.div(
                    class_name="w-5 h-5 bg-white rounded-full shadow-sm transform translate-x-5 transition-transform duration-200"
                ),
                rx.el.div(
                    class_name="w-5 h-5 bg-white rounded-full shadow-sm transform translate-x-0.5 transition-transform duration-200"
                ),
            ),
            on_click=lambda: UserState.toggle_setting(setting_key),
            class_name=rx.cond(
                is_checked,
                "w-11 h-6 bg-sky-500 rounded-full transition-colors duration-200 focus:outline-none",
                "w-11 h-6 bg-gray-200 rounded-full transition-colors duration-200 focus:outline-none hover:bg-gray-300",
            ),
        ),
        class_name="flex items-center justify-between py-4 border-b border-gray-100 last:border-0",
    )


def settings_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1("تنظیمات حساب", class_name="text-2xl font-bold text-gray-900 mb-6"),
        rx.el.div(
            rx.el.div(
                rx.el.h3(
                    "اعلانات",
                    class_name="text-lg font-semibold text-gray-900 mb-4 px-6 pt-6",
                ),
                rx.el.div(
                    setting_toggle(
                        "اطلاع\u200cرسانی ایمیلی",
                        "دریافت به\u200cروزرسانی\u200cهای وضعیت سفارش و پیشنهادات ویژه",
                        "notifications_email",
                        UserState.settings["notifications_email"],
                    ),
                    setting_toggle(
                        "اطلاع\u200cرسانی پیامکی",
                        "دریافت به\u200cروزرسانی\u200cها از طریق پیامک",
                        "notifications_sms",
                        UserState.settings["notifications_sms"],
                    ),
                    class_name="px-6 pb-6",
                ),
                class_name="bg-white rounded-2xl border border-gray-100 shadow-sm mb-6",
            ),
            rx.el.div(
                rx.el.h3(
                    "شخصی\u200cسازی",
                    class_name="text-lg font-semibold text-gray-900 mb-4 px-6 pt-6",
                ),
                rx.el.div(
                    setting_toggle(
                        "حالت شب",
                        "فعال\u200cسازی حالت تیره برای تجربه بهتر در شب",
                        "dark_mode",
                        UserState.settings["dark_mode"],
                    ),
                    class_name="px-6 pb-6",
                ),
                class_name="bg-white rounded-2xl border border-gray-100 shadow-sm mb-6",
            ),
            rx.el.div(
                rx.el.h3(
                    "امنیت",
                    class_name="text-lg font-semibold text-gray-900 mb-4 px-6 pt-6",
                ),
                rx.el.div(
                    rx.el.div(
                        rx.el.button(
                            "تغییر رمز عبور",
                            class_name="text-gray-700 font-medium hover:text-sky-600 transition-colors",
                        ),
                        class_name="py-3 border-b border-gray-100",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "حذف حساب کاربری",
                            class_name="text-red-500 font-medium hover:text-red-700 transition-colors",
                        ),
                        class_name="py-3",
                    ),
                    class_name="px-6 pb-6 flex flex-col",
                ),
                class_name="bg-white rounded-2xl border border-gray-100 shadow-sm",
            ),
            class_name="max-w-3xl",
        ),
        class_name="flex-1",
    )


def account_settings_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            dashboard_sidebar("/account/settings"),
            settings_page(),
            class_name="flex flex-col md:flex-row gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-gray-50/50 min-h-screen",
    )