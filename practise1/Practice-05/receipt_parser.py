import re

def extract_prices(text):
    prices = re.findall(r'\d+\.\d+', text)
    return prices

def extract_products(text):
    products = re.findall(r'[A-Za-z ]+(?= \d+\.\d+)', text)
    return products

def extract_date(text):
    date = re.search(r'\d{4}-\d{2}-\d{2}', text)
    if date:
        return date.group()

def extract_payment(text):
    payment = re.search(r'Payment: (\w+)', text)
    if payment:
        return payment.group(1)

def calculate_total(prices):
    prices = [float(p) for p in prices]
    return sum(prices)