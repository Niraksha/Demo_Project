# Demo E-Commerce App

A simple e-commerce backend built with Flask.
This project is used to test the PR Review Agent.

## Structure

```
demo-ecommerce/
├── main.py                        # App entry point
├── app/
│   ├── models/
│   │   ├── user.py                # User model
│   │   ├── product.py             # Product model
│   │   └── order.py               # Order model
│   ├── routes/
│   │   ├── user_routes.py         # Login, register, get user
│   │   ├── product_routes.py      # Product CRUD
│   │   └── order_routes.py        # Order management
│   ├── services/
│   │   └── payment_service.py     # Payment processing
│   └── utils/
│       └── helpers.py             # Utility functions
└── tests/                         # No tests yet
```

## Endpoints

- POST /users/login
- POST /users/register
- GET  /users/<id>
- GET  /products/
- POST /products/
- POST /products/<id>/discount
- POST /orders/
- GET  /orders/<id>
- POST /orders/<id>/cancel
