import reflex as rx
from app.components.dashboard_sidebar import dashboard_sidebar
from app.states.user_state import UserState


def profile_field(
    label: str, value: str, field_key: str, type_: str = "text"
) -> rx.Component:
    return rx.el.div(
        rx.el.label(label, class_name="block text-sm font-medium text-gray-700 mb-1.5"),
        rx.el.input(
            type=type_,
            on_change=lambda v: UserState.update_profile(field_key, v),
            class_name="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20 outline-none transition-all bg-gray-50 focus:bg-white",
            default_value=value,
        ),
        class_name="",
    )


def profile_page() -> rx.Component:
    return rx.el.div(
        rx.el.h1("پروفایل من", class_name="text-2xl font-bold text-gray-900 mb-6"),
        rx.el.div(
            rx.el.div(
                rx.el.div(
                    rx.image(
                        src=UserState.profile["avatar"],
                        class_name="w-24 h-24 rounded-full object-cover border-4 border-white shadow-lg",
                    ),
                    rx.el.button(
                        rx.icon("camera", class_name="w-4 h-4 text-white"),
                        class_name="absolute bottom-0 right-0 bg-sky-500 p-2 rounded-full shadow-md hover:bg-sky-600 transition-colors cursor-pointer",
                    ),
                    class_name="relative inline-block",
                ),
                rx.el.div(
                    rx.el.h2(
                        UserState.profile["name"],
                        class_name="text-lg font-bold text-gray-900",
                    ),
                    rx.el.p(
                        UserState.profile["role"],
                        class_name="text-sm text-sky-600 font-medium",
                    ),
                    class_name="mt-4 text-center",
                ),
                class_name="flex flex-col items-center p-8 bg-white rounded-2xl border border-gray-100 shadow-sm",
            ),
            rx.el.div(
                rx.el.div(
                    rx.el.h3(
                        "اطلاعات شخصی",
                        class_name="text-lg font-semibold text-gray-900 mb-4",
                    ),
                    rx.el.div(
                        profile_field(
                            "نام و نام خانوادگی", UserState.profile["name"], "name"
                        ),
                        profile_field(
                            "آدرس ایمیل", UserState.profile["email"], "email", "email"
                        ),
                        profile_field(
                            "شماره موبایل", UserState.profile["phone"], "phone", "tel"
                        ),
                        rx.el.div(
                            rx.el.label(
                                "بیوگرافی",
                                class_name="block text-sm font-medium text-gray-700 mb-1.5",
                            ),
                            rx.el.textarea(
                                on_change=lambda v: UserState.update_profile("bio", v),
                                class_name="w-full px-4 py-2.5 rounded-xl border border-gray-200 focus:border-sky-500 focus:ring-2 focus:ring-sky-500/20 outline-none transition-all bg-gray-50 focus:bg-white min-h-[100px] resize-y",
                                default_value=UserState.profile["bio"],
                            ),
                        ),
                        class_name="grid gap-6",
                    ),
                    rx.el.div(
                        rx.el.button(
                            "ذخیره تغییرات",
                            class_name="bg-sky-500 hover:bg-sky-600 text-white px-6 py-2.5 rounded-lg font-semibold shadow-lg shadow-sky-200 transition-all active:scale-95",
                        ),
                        class_name="mt-8 flex justify-end",
                    ),
                    class_name="p-8 bg-white rounded-2xl border border-gray-100 shadow-sm h-full",
                ),
                class_name="md:col-span-2",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-8",
        ),
        class_name="flex-1",
    )


def account_profile_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            dashboard_sidebar("/account/profile"),
            profile_page(),
            class_name="flex flex-col md:flex-row gap-8 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12",
        ),
        class_name="bg-gray-50/50 min-h-screen",
    )