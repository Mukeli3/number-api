#!/usr/bin/python3
import requests

# non-fun_fact responses from Numbers API
UNINTERESTING_RESPONSES = [
    "is a number for which we're missing a fact",
    "is an uninteresting number",
    "is a boring number"
    "is an unremarkable number"
]

def is_prime(n):
    """Check if a number is prime (negative numbers are NOT prime)"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    """Check if a number is a perfect number (only positive numbers apply)"""
    if n < 1:
        return False
    return sum([i for i in range(1, n) if n % i == 0]) == n

def is_armstrong(n):
    """Check if a number is an Armstrong number (only positive numbers apply)"""
    if n < 0:
        return False
    return sum(int(digit) ** len(str(n)) for digit in str(abs(n))) == abs(n)

def digit_sum(n):
    """Calculate the sum of digits (for both positive and negative numbers)"""
    return sum(int(digit) for digit in str(abs(n)))

def fetch_fun_fact(n):
    """Fetch fun fact from Numbers API, or provide a custom one if unavailable"""
    if n < 0:
        return f"Negative numbers like {n} don't have traditional mathematical classifications, but they are crucial in fields like physics and finance!"
    
    try:
        response = requests.get(f"http://numbersapi.com/{n}")
        if response.status_code == 200:
            fact = response.text.strip()
            if not any(phrase in fact for phrase in UNINTERESTING_RESPONSES):
                return fact
    except requests.RequestException:
        pass  # If API request fails, proceed to custom facts

    # Use custom facts if the Numbers API fails or gives an uninteresting response
    custom_facts = []
    
    if is_armstrong(n):
        custom_facts.append(f"{n} is an Armstrong number because {' + '.join([f'{digit}^{len(str(n))}' for digit in str(abs(n))])} = {n}")
    
    if is_perfect(n):
        custom_facts.append(f"{n} is a perfect number because its divisors sum to {n}")

    if is_prime(n):
        custom_facts.append(f"{n} is a prime number")

    return ' '.join(custom_facts) if custom_facts else f"No fun fact available for {n}."

def classify_number(n):
    """Classify the number and return its properties"""
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