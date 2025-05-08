from flask import Flask, render_template
from app.controllers import (
    users,
    products,
    services,
    schedules,
    carts,
    cart_detail,
    orders,
    order_details,
    payment_methods,
    contact_info
)
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.register_blueprint(users.bp)
    app.register_blueprint(products.bp)
    app.register_blueprint(services.bp)
    app.register_blueprint(schedules.bp)
    app.register_blueprint(carts.bp)
    app.register_blueprint(cart_detail.bp)
    app.register_blueprint(orders.bp)
    app.register_blueprint(order_details.bp)
    app.register_blueprint(payment_methods.bp)
    app.register_blueprint(contact_info.bp)

    @app.route('/')
    def index():
        return render_template("index.html")

    @app.route('/cart')
    def cart():
        return render_template("cart.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    @app.route('/pay-cart')
    def pay_cart():
        return render_template("pay-cart.html")

    return app