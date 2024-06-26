from typing import List


class Product:
    def __init__(self, name: str, seller: str, price: float, rating: float, buyers: List[str], images: List[str], tags: List[str], reviews: int) -> None:
        self.name = name
        self.seller = seller
        self.price = price
        self.rating = rating
        self.buyers = buyers
        self.images = images
        self.tags = tags
        self.reviews = reviews

        # default value. we will fill this up when we calculate scores.
        self.scores = {}

    def __repr__(self) -> str:
        return f"{self.name}, by {self.seller}"


p1 = Product(
    name="Shoes",
    seller="Nike",
    price=39.95,
    rating=4.73,
    buyers=["John", "Sam"],
    images=["./images/pic-1.jpeg", "./images/pic-2.jpeg"],
    tags=["shoes", "nike", "durable", "comfy"],
    reviews=16
)
p2 = Product(
    name="T-Shirt",
    seller="Levi's",
    price=42.95,
    rating=4.73,
    buyers=["Adam", "Sam"],
    images=["./images/pic-1.jpeg", "./images/pic-2.jpeg"],
    tags=["shirts", "levis", "durable", "comfy"],
    reviews=54
)
p3 = Product(
    name="Black pants",
    seller="New seller",
    price=12.24,
    rating=2.25,
    buyers=["Jane", "Tom"],
    images=["./images/pic-1.jpeg", "./images/pic-2.jpeg"],
    tags=["clothes", "pants", "durable", "comfy", "black"],
    reviews=21
)
p4 = Product(
    name="Blue Jacket",
    seller="New seller",
    price=16.75,
    rating=3.98,
    buyers=["Adam", "Isabelle"],
    images=["./images/pic-1.jpeg", "./images/pic-2.jpeg"],
    tags=["jackets", "warm", "durable", "comfy"],
    reviews=6
)

products = [p1, p2, p3, p4]

class RankFactor:
    name = None
    max_score = 0

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        raise NotImplementedError()
    

class SellerRankFactor(RankFactor):
    name = "seller_score"
    max_score = 10

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        top_sellers = ["Nike", "Adidas", "Zara"]
        for product in products:
            if product.seller in top_sellers:
                product.scores[cls.name] = cls.max_score
            else:
                product.scores[cls.name] = 0
    

class PriceRankFactor(RankFactor):
    name = "price_score"
    max_score = 10

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        for product in products:
            if 1 <= product.price <= 10:
                product.scores[cls.name] = 2
            elif 10 <= product.price <= 20:
                product.scores[cls.name] = 4
            elif 20 <= product.price <= 30:
                product.scores[cls.name] = 6
            elif 30 <= product.price <= 40:
                product.scores[cls.name] = 8
            elif 40 <= product.price <= 50:
                product.scores[cls.name] = 10
            else:
                product.scores[cls.name] = 0


class ProductTagsRankFactor(RankFactor):
    name = "product_tags_score"
    max_score = 10

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        most_popular_tags = ["durable", "cheap", "free_shipping"]
        for product in products:
            if set(product.tags).intersection(set(most_popular_tags)):
                product.scores[cls.name] = cls.max_score
            else:
                product.scores[cls.name] = 0


class ProductImagesRankFactor(RankFactor):
    name = "product_images_score"
    max_score = 10

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        for product in products:
            if len(product.images) > 0:
                product.scores[cls.name] = cls.max_score
            else:
                product.scores[cls.name] = 0


class RatingsRankFactor(RankFactor):
    name = "ratings_score"
    max_score = 10

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        for product in products:
            if product.rating >= 4.0:
                product.scores[cls.name] = cls.max_score
            else:
                product.scores[cls.name] = 0


class BuyersRankFactor(RankFactor):
    name = "buyers_score"
    max_score = 10

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        for product in products:
            if len(product.buyers) >= 10:
                product.scores[cls.name] = cls.max_score
            else:
                product.scores[cls.name] = 0


class ProductReviewsRankFactor(RankFactor):
    name = "product_reviews_score"
    max_score = 10

    @classmethod
    def calculate(cls, products: List[Product]) -> None:
        for product in products:
            if product.reviews >= 15:
                product.scores[cls.name] = cls.max_score
            else:
                product.scores[cls.name] = 0


def calculate_total_score(products: List[Product]) -> List[Product]:
    # calculate all individual scores
    SellerRankFactor.calculate(products)
    PriceRankFactor.calculate(products)
    ProductTagsRankFactor.calculate(products)
    ProductImagesRankFactor.calculate(products)
    RatingsRankFactor.calculate(products)
    BuyersRankFactor.calculate(products)
    ProductReviewsRankFactor.calculate(products)

    # sum up all individual scores and get total score.
    for product in products:
        total_score = sum(product.scores.values())
        product.scores["total_score"] = total_score

calculate_total_score(products)

for product in products:
    print(product.scores["total_score"])
