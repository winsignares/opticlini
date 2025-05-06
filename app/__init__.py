from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

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