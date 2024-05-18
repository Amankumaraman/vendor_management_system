
Welcome to the Vendor Management System API documentation.

## API Endpoints

### Vendors

- **GET /api/vendors/**: Retrieve a list of all vendors.
- **POST /api/vendors/**: Create a new vendor.
- **GET /api/vendors/{vendor_id}/**: Retrieve details of a specific vendor.
- **PUT /api/vendors/{vendor_id}/**: Update details of a specific vendor.
- **DELETE /api/vendors/{vendor_id}/**: Delete a specific vendor.

### Purchase Orders

- **GET /api/purchase_orders/**: Retrieve a list of all purchase orders.
- **POST /api/purchase_orders/**: Create a new purchase order.
- **GET /api/purchase_orders/{po_id}/**: Retrieve details of a specific purchase order.
- **PUT /api/purchase_orders/{po_id}/**: Update details of a specific purchase order.
- **DELETE /api/purchase_orders/{po_id}/**: Delete a specific purchase order.

### Authentication

- **POST /api/token/**: Obtain an authentication token by providing username and password.
- **POST /api/register/generic/**: Register a new user.

## Authentication

To access protected endpoints, include the token obtained from `/api/token/` in the `Authorization` header of your requests.

### Create a Vendor

```bash
curl -X POST -H "Content-Type: application/json" -H "Authorization: Token <your_token>" -d '{"name": "Vendor Name", "contact_details": "Contact Details", "address": "Vendor Address", "vendor_code": "VENDOR001"}' http://127.0.0.1:8000/api/vendors/
```

### Retrieve All Purchase Orders

```bash
curl -X GET -H "Authorization: Token <your_token>" http://127.0.0.1:8000/api/purchase_orders/
```

## Running the Test Suite

To run the test suite, execute the following command in the project directory:

```bash
python manage.py test
```

---
