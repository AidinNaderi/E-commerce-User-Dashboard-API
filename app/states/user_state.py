import reflex as rx
from typing import TypedDict, Optional
from .product_state import Product


class UserProfile(TypedDict):
    name: str
    email: str
    phone: str
    bio: str
    avatar: str
    role: str


class OrderItem(TypedDict):
    name: str
    price: float
    quantity: int
    image: str


class Order(TypedDict):
    id: str
    date: str
    status: str
    total: float
    items: list[OrderItem]
    tracking_number: str


class Address(TypedDict):
    id: str
    label: str
    street: str
    city: str
    state: str
    zip_code: str
    country: str
    is_default: bool


class UserSettings(TypedDict):
    notifications_email: bool
    notifications_sms: bool
    dark_mode: bool
    language: str


class UserState(rx.State):
    profile: UserProfile = {
        "name": "علی محمدی",
        "email": "ali.mohammadi@example.com",
        "phone": "۰۹۱۲۳۴۵۶۷۸۹",
        "bio": "عاشق بازی\u200cهای آنلاین و رقابتی. همیشه دنبال اکانت\u200cهای خاص و کمیاب هستم.",
        "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=Ali",
        "role": "کاربر ویژه",
    }
    orders: list[Order] = [
        {
            "id": "ORD-1402-001",
            "date": "۲۴ مهر ۱۴۰۲",
            "status": "تکمیل شده",
            "total": 3500000.0,
            "tracking_number": "TRK99283711",
            "items": [
                {
                    "name": "اکانت لول ۷۰ پابجی",
                    "price": 3500000.0,
                    "quantity": 1,
                    "image": "/placeholder.svg",
                }
            ],
        },
        {
            "id": "ORD-1402-089",
            "date": "۱۵ شهریور ۱۴۰۲",
            "status": "در حال بررسی",
            "total": 2100000.0,
            "tracking_number": "در انتظار",
            "items": [
                {
                    "name": "اکانت کلش آف کلنز",
                    "price": 2100000.0,
                    "quantity": 1,
                    "image": "/placeholder.svg",
                }
            ],
        },
    ]
    addresses: list[Address] = [
        {
            "id": "1",
            "label": "خانه",
            "street": "خیابان آزادی، کوچه گل\u200cها",
            "city": "تهران",
            "state": "تهران",
            "zip_code": "1234567890",
            "country": "ایران",
            "is_default": True,
        },
        {
            "id": "2",
            "label": "محل کار",
            "street": "میدان ونک، برج فناوری",
            "city": "تهران",
            "state": "تهران",
            "zip_code": "0987654321",
            "country": "ایران",
            "is_default": False,
        },
    ]
    wishlist: list[Product] = [
        {
            "id": "2",
            "name": "اکانت کال آف دیوتی موبایل",
            "price": 8900000.0,
            "original_price": 9500000.0,
            "description": "اکانت ریجن هند تک سیو.",
            "category": "کال آف دیوتی",
            "images": ["/placeholder.svg"],
            "rating": 4.9,
            "review_count": 89,
            "specs": {"لول": "150 Max"},
            "reviews": [],
            "is_featured": True,
        }
    ]
    settings: UserSettings = {
        "notifications_email": True,
        "notifications_sms": False,
        "dark_mode": False,
        "language": "فارسی",
    }
    active_tab: str = "Profile"
    selected_order_id: str = ""

    @rx.var
    def selected_order(self) -> Optional[Order]:
        for order in self.orders:
            if order["id"] == self.selected_order_id:
                return order
        return None

    @rx.event
    def set_active_tab(self, tab: str):
        self.active_tab = tab

    @rx.event
    def update_profile(self, field: str, value: str):
        self.profile[field] = value

    @rx.event
    def toggle_setting(self, setting: str):
        if setting in self.settings:
            self.settings[setting] = not self.settings[setting]

    @rx.event
    def remove_address(self, address_id: str):
        self.addresses = [a for a in self.addresses if a["id"] != address_id]

    @rx.event
    def set_default_address(self, address_id: str):
        new_addresses = []
        for a in self.addresses:
            a["is_default"] = a["id"] == address_id
            new_addresses.append(a)
        self.addresses = new_addresses

    @rx.event
    def remove_from_wishlist(self, product_id: str):
        self.wishlist = [p for p in self.wishlist if p["id"] != product_id]

    @rx.event
    def select_order(self, order_id: str):
        self.selected_order_id = order_id

    @rx.event
    def close_order_modal(self):
        self.selected_order_id = ""