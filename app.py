from flask import Flask, render_template

app = Flask(__name__)

cars = [
    {
        "name": "BMW 3 Series",
        "brand": "BMW",
        "price": "₹72 Lakh",
        "year": 2025,
        "fuel": "Petrol",
        "image": "https://images.unsplash.com/photo-1555215695-3004980ad54e?w=900"
    },
    {
        "name": "Mercedes-Benz C-Class",
        "brand": "Mercedes",
        "price": "₹61 Lakh",
        "year": 2025,
        "fuel": "Petrol",
        "image": "https://images.unsplash.com/photo-1618843479313-40f8afb4b4d8?w=900"
    },
    {
        "name": "Audi A5",
        "brand": "Audi",
        "price": "₹50 Lakh",
        "year": 2025,
        "fuel": "Petrol",
        "image": "https://images.unsplash.com/photo-1606664515524-ed2f786a0bd6?w=900"
    },
    {
        "name": "Porsche 911",
        "brand": "Porsche",
        "price": "₹2 Crore",
        "year": 2025,
        "fuel": "Petrol",
        "image": "https://images.unsplash.com/photo-1503376780353-7e6692767b70?w=900"
    }
]


@app.route("/")
def home():
    return render_template("index.html", cars=cars)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5004, debug=True)
