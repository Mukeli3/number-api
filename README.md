# Number Classification API 🚀

An API that takes a number and returns interesting mathematical properties about it, along with a fun fact.

## Project Structure

```
number-api/
│── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── utils.py
│── requirements.txt
│── run.py
│── README.md
```

## Features 🌟
- 📌 Identifies if a number is Prime, Perfect, Armstrong, Even, or Odd.
- 🧮 Computes the sum of its digits.
- 🎉 Retrieves a fun fact about the number.
- 🔄 Handles invalid inputs with proper error responses.
- 🌍 Supports CORS (Cross-Origin Resource Sharing).
### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Mukeli3/public-api.git
   cd public_api
   ```
2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt

   ```
4. Run the API:
   ```sh
   python run.py
   ```
   
## API Documentation 📖

### Endpoint
**GET** `/api/classify-number?number=<integer>`
 
### Responses

#### ✅ 200 OK (Valid Number)
```json
{
    "number": 28,
    "is_prime": false,
    "is_perfect": true,
    "properties": ["perfect", "even"],
    "digit_sum": 11,
    "fun_fact": "28 is the number of days the curing time of concrete is classically considered to be."
}
