from flask import Flask, jsonify

app = Flask(__name__)

def change(amount):
    res = []
    coins = [25, 10, 5, 1]  # value of quarters, dimes, nickels, pennies
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    for coin in coins:
        num, amount = divmod(int(amount * 100), coin)
        if num > 0:
            res.append({coin_lookup[coin]: num})

    return res

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return 'Hello World! I can make change at route: /change'

@app.route('/change/<int:dollar>/<int:cents>')
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = dollar + cents / 100
    result = change(amount)
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
