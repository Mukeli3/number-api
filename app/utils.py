#!/usr/bin/python3
import requests


def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_perfect(n):
    "check for perfect numbers"
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    "check if a number is an Armstrong number"
    # str - convert number to string for iteration thru the digits
    digits = [int(d) for d in str(n)]
    power = len(digits)
    return sum(d ** power for d in digits) == n

def digit_sum(n):
    "calculate digits sum"
    # str - convert the number to str for iteration over each digit
    return sum(int(digit) for digit in str(abs(n)))

def fetch_fun_fact(n):
    "fetch fun fact from numbers API"
    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        if response.status_code == 200:
            return response.text

    except requests.RequestException:
        pass
    return f"Couldn't fetch a fun fact for {n}!"

def classify_number(n):
    "classify the number and return it's properties"
    props = []
    if is_prime(n):
        props.append("prime")
    if is_perfect(n):
        props.append("perfect")
    if is_armstrong(n):
        props.append("armstrong")
    props.append("even" if n % 2 == 0 else "odd")

    return {
            "number": n,
            "is_prime": is_prime(n),
            "is_perfect": is_perfect(n),
            "properties": props,
            "digit_sum": digit_sum(n),
            "fun_fact": fetch_fun_fact(n),
            }
