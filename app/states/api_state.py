import reflex as rx
from typing import TypedDict, Any, Optional
import json
import random
import asyncio
import logging


class ApiParam(TypedDict):
    name: str
    type: str
    required: bool
    description: str


class ApiEndpoint(TypedDict):
    id: str
    method: str
    path: str
    summary: str
    description: str
    tags: list[str]
    params: list[ApiParam]


class ApiState(rx.State):
    selected_tag: str = "All"
    selected_endpoint_id: str = "get_products"
    response_status: int = 200
    response_time: str = "0ms"
    response_body: str = "برای مشاهده نتیجه، روی دکمه 'اجرای درخواست' کلیک کنید."
    is_loading: bool = False
    param_inputs: dict[str, str] = {}
    endpoints: list[ApiEndpoint] = [
        {
            "id": "get_products",
            "method": "GET",
            "path": "/api/products",
            "summary": "لیست تمام محصولات",
            "description": "دریافت لیست کامل محصولات موجود با قابلیت فیلتر کردن.",
            "tags": ["محصولات"],
            "params": [
                {
                    "name": "search",
                    "type": "string",
                    "required": False,
                    "description": "عبارت جستجو برای فیلتر محصولات",
                },
                {
                    "name": "limit",
                    "type": "integer",
                    "required": False,
                    "description": "حداکثر تعداد آیتم\u200cهای بازگشتی",
                },
            ],
        },
        {
            "id": "get_product_detail",
            "method": "GET",
            "path": "/api/products/{id}",
            "summary": "دریافت جزئیات محصول",
            "description": "دریافت اطلاعات کامل درباره یک محصول خاص.",
            "tags": ["محصولات"],
            "params": [
                {
                    "name": "id",
                    "type": "string",
                    "required": True,
                    "description": "شناسه یکتای محصول",
                }
            ],
        },
        {
            "id": "get_user_profile",
            "method": "GET",
            "path": "/api/user/profile",
            "summary": "دریافت پروفایل کاربر",
            "description": "دریافت اطلاعات پروفایل کاربر احراز هویت شده فعلی.",
            "tags": ["کاربر"],
            "params": [],
        },
        {
            "id": "get_user_orders",
            "method": "GET",
            "path": "/api/user/orders",
            "summary": "دریافت تاریخچه سفارشات",
            "description": "دریافت لیست سفارش\u200cهای قبلی کاربر.",
            "tags": ["کاربر"],
            "params": [],
        },
        {
            "id": "get_cart",
            "method": "GET",
            "path": "/api/cart",
            "summary": "دریافت آیتم\u200cهای سبد خرید",
            "description": "دریافت محتویات فعلی سبد خرید.",
            "tags": ["سبد خرید"],
            "params": [],
        },
        {
            "id": "add_to_cart",
            "method": "POST",
            "path": "/api/cart/add",
            "summary": "افزودن به سبد خرید",
            "description": "افزودن یک محصول به سبد خرید کاربر.",
            "tags": ["سبد خرید"],
            "params": [
                {
                    "name": "product_id",
                    "type": "string",
                    "required": True,
                    "description": "شناسه محصول برای افزودن",
                },
                {
                    "name": "quantity",
                    "type": "integer",
                    "required": True,
                    "description": "تعداد محصول",
                },
            ],
        },
        {
            "id": "get_addresses",
            "method": "GET",
            "path": "/api/addresses",
            "summary": "دریافت آدرس\u200cهای ذخیره شده",
            "description": "دریافت لیست آدرس\u200cهای ارسال ذخیره شده.",
            "tags": ["آدرس"],
            "params": [],
        },
        {
            "id": "get_wishlist",
            "method": "GET",
            "path": "/api/wishlist",
            "summary": "دریافت لیست علاقه\u200cمندی\u200cها",
            "description": "دریافت آیتم\u200cهای موجود در لیست علاقه\u200cمندی کاربر.",
            "tags": ["علاقه\u200cمندی\u200cها"],
            "params": [],
        },
    ]

    @rx.var
    def current_endpoint(self) -> Optional[ApiEndpoint]:
        for ep in self.endpoints:
            if ep["id"] == self.selected_endpoint_id:
                return ep
        return self.endpoints[0]

    @rx.var
    def available_tags(self) -> list[str]:
        tags = set()
        for ep in self.endpoints:
            for tag in ep["tags"]:
                tags.add(tag)
        return sorted(list(tags))

    @rx.var
    def filtered_endpoints(self) -> list[ApiEndpoint]:
        if self.selected_tag == "All":
            return self.endpoints
        return [ep for ep in self.endpoints if self.selected_tag in ep["tags"]]

    @rx.event
    def set_endpoint(self, ep_id: str):
        self.selected_endpoint_id = ep_id
        self.response_body = "برای مشاهده نتیجه، روی دکمه 'اجرای درخواست' کلیک کنید."
        self.response_status = 200
        self.response_time = "0ms"
        self.param_inputs = {}

    @rx.event
    def update_param(self, param: str, value: str):
        self.param_inputs[param] = value

    @rx.event
    async def execute_request(self):
        self.is_loading = True
        self.response_body = "در حال پردازش..."
        await asyncio.sleep(0.5)
        try:
            endpoint_id = self.selected_endpoint_id
            result = {}
            from .product_state import ProductState
            from .user_state import UserState
            from .cart_state import CartState

            product_state = await self.get_state(ProductState)
            user_state = await self.get_state(UserState)
            cart_state = await self.get_state(CartState)
            if endpoint_id == "get_products":
                search = self.param_inputs.get("search", "")
                result = {
                    "count": len(product_state.products),
                    "results": product_state.products[:5],
                }
            elif endpoint_id == "get_product_detail":
                pid = self.param_inputs.get("id", "1")
                product = next(
                    (p for p in product_state.products if p["id"] == pid), None
                )
                if product:
                    result = product
                else:
                    self.response_status = 404
                    result = {"error": "محصول یافت نشد", "code": 404}
            elif endpoint_id == "get_user_profile":
                result = user_state.profile
            elif endpoint_id == "get_user_orders":
                result = {"orders": user_state.orders}
            elif endpoint_id == "get_cart":
                result = {
                    "items": cart_state.items,
                    "total_items": cart_state.total_items,
                    "subtotal": cart_state.subtotal,
                }
            elif endpoint_id == "add_to_cart":
                pid = self.param_inputs.get("product_id", "1")
                qty = self.param_inputs.get("quantity", "1")
                product = next(
                    (p for p in product_state.products if p["id"] == pid), None
                )
                if product:
                    result = {
                        "success": True,
                        "message": f"{qty} عدد {product['name']} به سبد خرید اضافه شد",
                        "cart_updated": True,
                    }
                else:
                    self.response_status = 404
                    result = {"error": "محصول یافت نشد"}
            elif endpoint_id == "get_addresses":
                result = {"addresses": user_state.addresses}
            elif endpoint_id == "get_wishlist":
                result = {"wishlist": user_state.wishlist}
            else:
                result = {"message": "منطق این اندپوینت هنوز پیاده\u200cسازی نشده است"}
            self.response_body = json.dumps(result, indent=2)
            if self.response_status != 404:
                self.response_status = 200
            self.response_time = f"{random.randint(20, 150)}ms"
        except Exception as e:
            logging.exception(f"Error: {e}")
            self.response_status = 500
            self.response_body = json.dumps({"error": str(e)}, indent=2)
        finally:
            self.is_loading = False