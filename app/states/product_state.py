import reflex as rx
from typing import TypedDict, Any


class Review(TypedDict):
    user: str
    rating: int
    comment: str
    date: str


class Product(TypedDict):
    id: str
    name: str
    price: float
    original_price: float
    description: str
    category: str
    images: list[str]
    rating: float
    review_count: int
    specs: dict[str, str]
    reviews: list[Review]
    is_featured: bool


class Category(TypedDict):
    id: str
    name: str
    icon: str
    count: int


class ProductState(rx.State):
    categories: list[Category] = [
        {"id": "pubg", "name": "پابجی موبایل", "icon": "crosshair", "count": 120},
        {"id": "cod", "name": "کال آف دیوتی", "icon": "swords", "count": 85},
        {"id": "fortnite", "name": "فورتنایت", "icon": "gamepad-2", "count": 45},
        {"id": "clash", "name": "کلش آف کلنز", "icon": "shield", "count": 30},
        {"id": "steam", "name": "استیم", "icon": "monitor", "count": 60},
    ]
    products: list[Product] = [
        {
            "id": "1",
            "name": "اکانت لول ۷۰ پابجی - کانکرر سیزن ۱۲",
            "price": 3500000.0,
            "original_price": 4200000.0,
            "description": "اکانت فوق\u200cالعاده پابجی موبایل با اسکین\u200cهای کمیاب ام فور یخی لول ۵ و ست کامل فرعون. دارای تایتل کانکرر سیزن ۱۲ و ۱۹. تحویل فوری با گارانتی مادام\u200cالعمر.",
            "category": "پابجی موبایل",
            "images": ["/placeholder.svg"],
            "rating": 4.8,
            "review_count": 124,
            "specs": {
                "لول": "70",
                "رنک": "Conqueror",
                "تعداد یوسی": "350",
                "ریجن": "گلوبال",
                "نوع تحویل": "فوری",
                "گارانتی": "دارد",
            },
            "reviews": [
                {
                    "user": "علی",
                    "rating": 5,
                    "comment": "اکانت عالی بود، تحویل سریع!",
                    "date": "۱۴۰۲/۰۷/۱۰",
                }
            ],
            "is_featured": True,
        },
        {
            "id": "2",
            "name": "اکانت کال آف دیوتی موبایل - ۳ گان متیک",
            "price": 8900000.0,
            "original_price": 9500000.0,
            "description": "اکانت ریجن هند تک سیو. دارای ۳ گان متیک فول آپگرید و ۵ گان لجندری. بتل پس سیزن\u200cهای اخیر کامل. مناسب برای استریمرها.",
            "category": "کال آف دیوتی",
            "images": ["/placeholder.svg"],
            "rating": 4.9,
            "review_count": 89,
            "specs": {
                "لول": "150 Max",
                "ریجن": "هند",
                "تعداد گان متیک": "3",
                "لینک": "اکتیویژن",
                "نوع تحویل": "۲۴ ساعته",
                "گارانتی": "۴۸ ساعت مهلت تست",
            },
            "reviews": [],
            "is_featured": True,
        },
        {
            "id": "3",
            "name": "اکانت فورتنایت - بلک نایت سیزن ۱",
            "price": 6200000.0,
            "original_price": 0,
            "description": "اکانت قدیمی و کمیاب فورتنایت شامل اسکین بلک نایت، ماکو گلایدر و دنس\u200cهای سیزن ۱. سیو د ورلد قدیمی (ویباکس دار).",
            "category": "فورتنایت",
            "images": ["/placeholder.svg"],
            "rating": 4.6,
            "review_count": 56,
            "specs": {
                "تعداد اسکین": "120+",
                "پلتفرم": "همه",
                "ویباکس": "1500",
                "نوع تحویل": "فوری",
                "گارانتی": "ندارد",
            },
            "reviews": [],
            "is_featured": True,
        },
        {
            "id": "4",
            "name": "اکانت کلش آف کلنز - تان هال ۱۵ مکس",
            "price": 2100000.0,
            "original_price": 2500000.0,
            "description": "دهکده قدرتمند تان هال ۱۵ با دیوارها و هیروهای مکس. آماده برای وار و لیگ. دارای جم بالا برای تغییر نام.",
            "category": "کلش آف کلنز",
            "images": ["/placeholder.svg"],
            "rating": 4.7,
            "review_count": 210,
            "specs": {
                "تان هال": "15",
                "لول هیروها": "Max",
                "جم": "2500",
                "کارگر": "6",
                "نوع تحویل": "فوری",
            },
            "reviews": [],
            "is_featured": True,
        },
        {
            "id": "5",
            "name": "اکانت استیم - ۲۵۰۰ بازی",
            "price": 4500000.0,
            "original_price": 0,
            "description": "اکانت استیم با آرشیو کامل بازی\u200cهای روز دنیا. بدون بن و محدودیت. ریجن آرژانتین. مناسب برای کلکسیونرها.",
            "category": "استیم",
            "images": ["/placeholder.svg"],
            "rating": 4.5,
            "review_count": 78,
            "specs": {
                "لول استیم": "50",
                "تعداد بازی": "2500+",
                "ریجن": "آرژانتین",
                "سال ساخت": "2015",
                "نوع تحویل": "فوری",
            },
            "reviews": [],
            "is_featured": False,
        },
    ]
    search_query: str = ""
    current_product_id: str = ""

    @rx.var
    def featured_products(self) -> list[Product]:
        return [p for p in self.products if p["is_featured"]]

    @rx.var
    def filtered_products(self) -> list[Product]:
        if not self.search_query:
            return self.products
        q = self.search_query.lower()
        return [
            p
            for p in self.products
            if q in p["name"].lower() or q in p["category"].lower()
        ]

    @rx.var
    def current_product(self) -> Product | None:
        for p in self.products:
            if p["id"] == self.current_product_id:
                return p
        return None

    @rx.event
    def set_search_query(self, query: str):
        self.search_query = query

    @rx.event
    def set_current_product(self, p_id: str):
        self.current_product_id = p_id

    @rx.event
    def load_product_detail(self):
        p_id = self.router.page.params.get("id")
        if p_id:
            self.current_product_id = p_id