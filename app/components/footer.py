import reflex as rx


def footer() -> rx.Component:
    return rx.el.footer(
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.el.div(
                        rx.icon("gamepad-2", class_name="text-sky-500 w-8 h-8"),
                        rx.el.span(
                            "اسکای\u200cگیم",
                            class_name="text-xl font-bold text-gray-900",
                        ),
                        class_name="flex items-center gap-2 mb-4",
                    ),
                    rx.el.p(
                        "تجربه خریدی امن و سریع از بهترین اکانت\u200cهای بازی. تضمین کیفیت و پشتیبانی ۲۴ ساعته.",
                        class_name="text-gray-500 text-sm leading-relaxed max-w-xs",
                    ),
                    class_name="col-span-1 md:col-span-2",
                ),
                rx.el.div(
                    rx.el.h3("فروشگاه", class_name="font-semibold text-gray-900 mb-4"),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "جدیدترین\u200cها",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "پرفروش\u200cترین\u200cها",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "پیشنهادات ویژه",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        class_name="space-y-2 text-sm",
                    ),
                ),
                rx.el.div(
                    rx.el.h3("پشتیبانی", class_name="font-semibold text-gray-900 mb-4"),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "مرکز راهنما",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "شرایط تحویل",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "قوانین بازگشت",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        class_name="space-y-2 text-sm",
                    ),
                ),
                rx.el.div(
                    rx.el.h3("شرکت", class_name="font-semibold text-gray-900 mb-4"),
                    rx.el.ul(
                        rx.el.li(
                            rx.el.a(
                                "درباره ما",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "فرصت\u200cهای شغلی",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "حریم خصوصی",
                                href="#",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors",
                            )
                        ),
                        rx.el.li(
                            rx.el.a(
                                "مستندات API",
                                href="/developers/api",
                                class_name="text-gray-500 hover:text-sky-600 transition-colors font-medium",
                            )
                        ),
                        class_name="space-y-2 text-sm",
                    ),
                ),
                class_name="grid grid-cols-1 md:grid-cols-5 gap-8 py-12 border-b border-gray-100",
            ),
            rx.el.div(
                rx.el.p(
                    "© ۱۴۰۲ اسکای\u200cگیم. تمامی حقوق محفوظ است.",
                    class_name="text-gray-400 text-sm",
                ),
                rx.el.div(
                    rx.icon(
                        "twitter",
                        class_name="w-5 h-5 text-gray-400 hover:text-sky-500 cursor-pointer",
                    ),
                    rx.icon(
                        "instagram",
                        class_name="w-5 h-5 text-gray-400 hover:text-pink-500 cursor-pointer",
                    ),
                    rx.icon(
                        "linkedin",
                        class_name="w-5 h-5 text-gray-400 hover:text-blue-700 cursor-pointer",
                    ),
                    class_name="flex items-center gap-4",
                ),
                class_name="flex flex-col md:flex-row justify-between items-center py-8",
            ),
            class_name="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8",
        ),
        class_name="bg-gray-50 border-t border-gray-100 mt-auto",
    )