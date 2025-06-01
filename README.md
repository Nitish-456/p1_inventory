
# 🧾 Product Inventory Manager (Python CLI App)

This is a **simple command-line based Inventory Management System** developed in Python. It allows you to manage product records in a CSV file, including the ability to add, view, update, delete, and search for products. It also logs all actions for auditing.

---

## 📁 Features

- ✅ Add new products with price and quantity
- 📋 View the current product inventory
- ✏️ Update existing product details
- 🗑️ Delete a product by name
- 🔍 Search products by name, price range, or quantity
- 📜 Action logs stored in a `log.txt` file
- 💾 All data stored persistently in `Inventory.csv`

---

## 🛠️ File Structure

- `Inventory.csv`: Stores product data (created automatically)
- `log.txt`: Logs all add/update/delete/search actions with timestamps

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then run:

```bash
python inventory_manager.py
```

You'll see a menu like:

```
------ Product Inventory Manager ------
1. Add Product
2. View Products
3. Update Product
4. Delete Product
5. Search Product
6. Exit
```

---

## 🔍 Search Options

- **By Product Name**: Finds exact or partial matches
- **By Price Range**: Finds products within min–max price
- **By Quantity**: Finds products above a certain quantity

---

## 🧠 Code Highlights & Comments

- Uses Python's `csv` module for persistent file operations.
- Adds error-handling (e.g., for invalid input or negative numbers).
- Uses `datetime.now()` to timestamp all logged actions.

Key functions:
- `add_product()` – Adds new item to inventory.
- `view_products()` – Displays all records from CSV.
- `update_product()` – Updates product info by name.
- `delete_product()` – Removes a product entry.
- `search_product()` – Advanced search options.
- `log_action()` – Records all key actions in `log.txt`.

---

## 📝 Example CSV Structure

```csv
Product,Price,Quantity
Notebook,45.5,10
Pen,10,50
```

---

## 📌 Future Improvements (Ideas)
- Add GUI (Tkinter or PyQt)
- Use JSON or SQLite instead of CSV
- Add category field or product ID
- Export search results to a file

---

## 👨‍💻 Author

Built with ❤️ by Nitish (Chat GPT guidance)

