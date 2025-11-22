import reflex as rx
from app.components.navbar import navbar
from app.components.footer import footer
from app.states.api_state import ApiState, ApiEndpoint, ApiParam


def method_badge(method: str) -> rx.Component:
    color_map = {
        "GET": "bg-blue-100 text-blue-700 border-blue-200",
        "POST": "bg-green-100 text-green-700 border-green-200",
        "PUT": "bg-orange-100 text-orange-700 border-orange-200",
        "DELETE": "bg-red-100 text-red-700 border-red-200",
    }
    return rx.el.span(
        method,
        class_name=rx.match(
            method,
            (
                "GET",
                "px-2.5 py-0.5 rounded-md text-xs font-bold border bg-blue-100 text-blue-700 border-blue-200",
            ),
            (
                "POST",
                "px-2.5 py-0.5 rounded-md text-xs font-bold border bg-green-100 text-green-700 border-green-200",
            ),
            (
                "PUT",
                "px-2.5 py-0.5 rounded-md text-xs font-bold border bg-orange-100 text-orange-700 border-orange-200",
            ),
            (
                "DELETE",
                "px-2.5 py-0.5 rounded-md text-xs font-bold border bg-red-100 text-red-700 border-red-200",
            ),
            "px-2.5 py-0.5 rounded-md text-xs font-bold border bg-gray-100 text-gray-700 border-gray-200",
        ),
    )


def sidebar_endpoint_item(endpoint: ApiEndpoint) -> rx.Component:
    is_selected = ApiState.selected_endpoint_id == endpoint["id"]
    return rx.el.button(
        rx.el.div(
            method_badge(endpoint["method"]),
            rx.el.span(
                endpoint["summary"], class_name="text-sm truncate ml-2 font-medium"
            ),
            class_name="flex items-center w-full",
        ),
        on_click=lambda: ApiState.set_endpoint(endpoint["id"]),
        class_name=rx.cond(
            is_selected,
            "w-full text-left px-3 py-2.5 rounded-lg bg-sky-50 text-sky-700 border border-sky-100 transition-colors mb-1",
            "w-full text-left px-3 py-2.5 rounded-lg hover:bg-gray-50 text-gray-600 border border-transparent hover:border-gray-100 transition-colors mb-1",
        ),
    )


def param_input_row(param: ApiParam) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.span(
                param["name"],
                class_name="font-mono text-sm font-semibold text-gray-900",
            ),
            rx.cond(
                param["required"],
                rx.el.span(
                    "اجباری", class_name="text-xs text-red-500 ml-2 font-medium"
                ),
                rx.el.span("اختیاری", class_name="text-xs text-gray-400 ml-2"),
            ),
            class_name="mb-1",
        ),
        rx.el.p(param["description"], class_name="text-xs text-gray-500 mb-2"),
        rx.el.input(
            placeholder=f"مقدار {param['type']} را وارد کنید...",
            type="text",
            on_change=lambda v: ApiState.update_param(param["name"], v),
            class_name="w-full px-3 py-2 bg-white border border-gray-200 rounded-md text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-transparent",
        ),
        class_name="py-3 border-b border-gray-100 last:border-0",
    )


def api_docs_page() -> rx.Component:
    return rx.el.div(
        navbar(),
        rx.el.div(
            rx.el.aside(
                rx.el.div(
                    rx.el.h2(
                        "مستندات API", class_name="text-lg font-bold text-gray-900 mb-6"
                    ),
                    rx.el.div(
                        rx.el.h3(
                            "منابع",
                            class_name="text-xs font-bold text-gray-400 uppercase tracking-wider mb-3",
                        ),
                        rx.foreach(ApiState.filtered_endpoints, sidebar_endpoint_item),
                        class_name="space-y-1",
                    ),
                    class_name="sticky top-24",
                ),
                class_name="hidden lg:block w-72 border-r border-gray-100 min-h-[calc(100vh-80px)] p-6 bg-white",
            ),
            rx.el.main(
                rx.el.div(
                    rx.el.div(
                        rx.el.div(
                            rx.el.h1(
                                ApiState.current_endpoint["summary"],
                                class_name="text-2xl font-bold text-gray-900 mb-2",
                            ),
                            rx.el.div(
                                method_badge(ApiState.current_endpoint["method"]),
                                rx.el.span(
                                    ApiState.current_endpoint["path"],
                                    class_name="ml-3 font-mono text-sm text-gray-600",
                                ),
                                class_name="flex items-center mt-2",
                            ),
                            class_name="mb-6",
                        ),
                        rx.el.p(
                            ApiState.current_endpoint["description"],
                            class_name="text-gray-600 leading-relaxed max-w-2xl",
                        ),
                        class_name="border-b border-gray-100 pb-8 mb-8",
                    ),
                    rx.el.div(
                        rx.el.div(
                            rx.el.h3(
                                "پارامترهای درخواست",
                                class_name="text-lg font-semibold text-gray-900 mb-4",
                            ),
                            rx.cond(
                                ApiState.current_endpoint["params"].length() > 0,
                                rx.el.div(
                                    rx.foreach(
                                        ApiState.current_endpoint["params"],
                                        param_input_row,
                                    ),
                                    class_name="bg-gray-50 rounded-xl p-4 border border-gray-100",
                                ),
                                rx.el.p(
                                    "این اندپوینت نیازی به پارامتر ندارد.",
                                    class_name="text-gray-500 italic text-sm",
                                ),
                            ),
                            class_name="mb-8",
                        ),
                        rx.el.div(
                            rx.el.div(
                                rx.el.h3(
                                    "کنسول تعاملی",
                                    class_name="text-lg font-semibold text-gray-900",
                                ),
                                rx.el.button(
                                    rx.cond(
                                        ApiState.is_loading,
                                        rx.el.span(
                                            "در حال پردازش...",
                                            class_name="flex items-center gap-2",
                                        ),
                                        rx.el.span(
                                            "اجرای درخواست",
                                            class_name="flex items-center gap-2",
                                        ),
                                    ),
                                    disabled=ApiState.is_loading,
                                    on_click=ApiState.execute_request,
                                    class_name="px-4 py-2 bg-sky-600 text-white rounded-lg font-medium text-sm hover:bg-sky-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed",
                                ),
                                class_name="flex justify-between items-center mb-4",
                            ),
                            rx.el.div(
                                rx.el.div(
                                    rx.el.span(
                                        "وضعیت پاسخ",
                                        class_name="text-xs text-gray-400 uppercase tracking-wider font-bold",
                                    ),
                                    rx.el.div(
                                        rx.el.div(
                                            class_name=rx.cond(
                                                ApiState.response_status == 200,
                                                "w-2 h-2 rounded-full bg-green-500 mr-2",
                                                "w-2 h-2 rounded-full bg-red-500 mr-2",
                                            )
                                        ),
                                        rx.el.span(
                                            f"{ApiState.response_status} OK",
                                            class_name=rx.cond(
                                                ApiState.response_status == 200,
                                                "font-mono text-sm text-green-600 font-bold",
                                                "font-mono text-sm text-red-600 font-bold",
                                            ),
                                        ),
                                        class_name="flex items-center mt-1",
                                    ),
                                    class_name="mb-4",
                                ),
                                rx.el.div(
                                    rx.el.div(
                                        rx.el.span(
                                            "JSON",
                                            class_name="text-xs font-bold text-gray-500",
                                        ),
                                        rx.el.span(
                                            f"زمان: {ApiState.response_time}",
                                            class_name="text-xs font-mono text-gray-400",
                                        ),
                                        class_name="flex justify-between items-center px-4 py-2 bg-gray-800 rounded-t-lg border-b border-gray-700",
                                    ),
                                    rx.el.pre(
                                        rx.el.code(
                                            ApiState.response_body,
                                            class_name="block font-mono text-sm text-gray-300 whitespace-pre-wrap",
                                        ),
                                        class_name="p-4 bg-gray-900 rounded-b-lg overflow-x-auto min-h-[200px] max-h-[500px]",
                                    ),
                                    class_name="rounded-lg shadow-lg",
                                ),
                                class_name="bg-white p-1 rounded-xl",
                            ),
                            class_name="bg-gray-50 p-6 rounded-2xl border border-gray-100",
                        ),
                        class_name="grid grid-cols-1 gap-8",
                    ),
                    class_name="max-w-4xl mx-auto",
                ),
                class_name="flex-1 p-6 lg:p-12 bg-white",
            ),
            class_name="flex max-w-7xl mx-auto w-full",
        ),
        footer(),
        class_name="min-h-screen bg-white flex flex-col font-['Vazirmatn']",
    )