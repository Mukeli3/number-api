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
    if power == 1:
        return False

    return sum(d ** power for d in digits) == n

def digit_sum(n):
    "calculate digits sum"
    # str - convert the number to str for iteration over each digit
    return sum(int(digit) for digit in str(abs(n)))

UNINTERESTING_RESPONSES = [
    "is a number for which we're missing a fact",
    "is an uninteresting number",
    "is a boring number",
    "is an unremarkable number"
]

def fetch_fun_fact(n):
    """Fetch fun fact from Numbers API or provide a custom fact if unavailable"""
    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        if response.status_code == 200:
            fact = response.text.strip()

            # fallback to custom facts, Numbers API returns an "uninteresting" fact
            if not any(phrase in fact for phrase in UNINTERESTING_RESPONSES):
                return fact
    except requests.RequestException:
        pass  # proceed to custom facts, error occurs while fetching

    # custom facts if Numbers API fails or gives an uninteresting response
    custom_facts = []
    
    if is_armstrong(n):
        custom_facts.append(f"{n} is an Armstrong number because {' + '.join([f'{digit}^{len(str(n))}' for digit in str(n)])} = {n}")
    
    if is_perfect(n):
        custom_facts.append(f"{n} is a perfect number because its divisors sum to {n}")

    if is_prime(n):
        custom_facts.append(f"{n} is a prime number")

    return ' '.join(custom_facts) if custom_facts else f"No fun fact available for {n}."

def classify_number(n):
    """classify number and return its properties"""
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
