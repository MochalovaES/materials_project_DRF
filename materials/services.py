import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def get_url_payment(course):
    responce_price = stripe.Price.create(
        currency="usd",
        unit_amount=course.price * 100,
        product_data={"name": course.name},
    )
    responce_url = stripe.checkout.Session.create(
        success_url="https://example.com/success",
        line_items=[{"price": responce_price["id"], "quantity": 1}],
        mode="payment",
    )
    return responce_url["url"]
