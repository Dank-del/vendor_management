# Vendor Management System

This is a Django-based Vendor Management System. It provides APIs for managing vendors and purchase orders, and it includes performance metrics for vendors.

## Features

- Vendor management: Create, update, and delete vendors.
- Purchase order management: Create, update, and delete purchase orders.
- Vendor performance metrics: Calculate and display metrics such as on-time delivery rate, average quality rating, average response time, and fulfillment rate.

## Setup Instructions

1. Clone the repository:

```sh
git clone https://github.com/Dank-del/vendor_management
cd vendor_management
```

2. Set up a virtual environment and activate it:

```sh
python3 -m venv venv
source venv/bin/activate
```

3. Install the required packages:

```sh
pip install -r requirements.txt
```

4. Apply the migrations:

```sh
python manage.py migrate
```

5. Run the server:

```sh
python manage.py runserver
```

Now, you can access the application at `http://localhost:8000`.

## Testing

To run the tests, use the following command:

```sh
python manage.py test vendors
```