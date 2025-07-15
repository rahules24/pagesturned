# 📖 PagesTurned — A Full-Stack Poetry Blog & Storefront
```🧠 Designed for creative writers, poets, and indie sellers to showcase and monetize their art.```


PagesTurned is a personal poetry publishing platform fused with a merchandise storefront, designed to let creativity meet commerce. Built using **Django**, **React**, and **SQLite3**, this project merges expressive writing with modern web development and showcases a complete suite of e-commerce functionality — from blogging to integrated payments.

> 🚀 “Where verses turn into value — and stories are sold.”

---

<img width="1889" height="877" alt="image" src="https://github.com/user-attachments/assets/b03edff7-2947-4e9a-a6a5-cef13cea84fb" />


## 🌟 Features

### ✒️ Poetry Blog
- Beautifully templated blog section for publishing poems and prose
- Markdown support and auto-rendering
- Date-based sorting and tagging for categories

### 🛍️ Merchandise Storefront
- Browse and purchase poetry-themed merchandise
- Dynamic product listings with descriptions and prices
- Integrated cart and checkout functionality

### 🔐 Secure Payment Gateway
- Seamless integration with **Paytm**
- Checksum verification for transaction integrity
- Secure and reliable payment handling

### ⚙️ Admin Dashboard
- Add/Edit/Delete products and blog posts
- Real-time order tracking
- Streamlined content management for site owners

---

## 🛠️ Tech Stack

| Frontend | Backend | Payments | Database |
|----------|---------|----------|----------|
| React    | Django  | Paytm    | SQLite3  |

- REST API integration for dynamic content rendering
- Django ORM for database operations
- Admin dashboard powered by Django Admin

---

## 📂 Project Structure

```
pagesturned-master/
├── blog/ → Blog logic & templates
├── shop/ → E-commerce & product views
├── Paytm/ → Payment processing with checksum verification
├── pagesturned/ → Main project configuration
└── manage.py → Django management script
```

---

## ✍️ About the Poet/Developer

**Rahul** — Full-stack developer & software engineer and part-time poet <3
📍 Chandigarh, India | 🌍 Currently @ Tarragona, Spain  
🔗 [Portfolio](https://rahules24.github.io/sirenscripts) | [GitHub](https://github.com/rahules24) | [LinkedIn](https://linkedin.com/in/rahules24)

---

## 💡 Future Scope

- Add JWT authentication and user accounts
- Migrate to PostgreSQL for production-readiness
- Add Stripe & Razorpay as alternate payment gateways
- Implement real-time comment system via WebSockets
