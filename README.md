

# 🚀 FastAPI CRUD Project

This is a simple FastAPI project that performs basic **CRUD operations** (Create, Read, Update, Delete) on a dictionary of names and ages. Perfect for beginners learning FastAPI! 💡

---

## 📦 Features

- 🔍 **GET** - View all names and their ages  
- ➕ **POST** - Add a new name with age  
- 🗑️ **DELETE** - Remove a name from the list  
- ♻️ **PUT** - Update an existing name and age  
- 🧭 **Swagger UI** - Interactive API docs

---

## 🛠️ Requirements

- Python 3.7+
- FastAPI
- Uvicorn

---


## 🧭 Swagger UI – Interactive API Docs

FastAPI automatically generates interactive API documentation! 🧪  

Once your server is running, go to:

🔗 **[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**  
👉 Here you can test all endpoints directly!

> Bonus: You can also check the raw OpenAPI schema at `/openapi.json`

---

## 📬 API Endpoints

### 1. **GET /**  
🔹 Returns all names and their ages  
🔹 Response:
```json
["Samreen having age 22", "Muhammad having age 87", ...]
```

---

### 2. **POST /**  
🔹 Add a new person  
🔹 Body:
```json
{
  "name": "Ali",
  "age": 30
}
```

---

### 3. **DELETE /{name}**  
🔹 Delete a person by name  
🔹 Example: `DELETE /Muhammad`  
🔹 Response:
```json
{
  "message": "Muhammad having age 87 is deleted successfully!!! 👌"
}
```

---

### 4. **PUT /{name}**  
🔹 Update a name and age  
🔹 Example URL: `PUT /Rahul`  
🔹 Body:
```json
{
  "name": "Ravi",
  "age": 28
}
```

🔹 Response:
```json
{
  "message": "Rahul updated to name Ravi and age 28 successfully! ✅"
}
```

---

## 🧪 Testing Tools

- 🔹 [Swagger UI (Docs)](http://127.0.0.1:8000/docs)  
- 🔹 [Postman](https://www.postman.com/)  
- 🔹 [Hoppscotch](https://hoppscotch.io/)  
- 🔹 cURL or any REST client

---

## 🙌 Final Notes

This project is a great starter for diving into FastAPI. You can later enhance it by:

- 💾 Connecting to a database
- 🔐 Adding authentication
- 🔄 Using background tasks or middleware

Happy coding! 💻✨

---

Let me know if you want me to save this as a file or help deploy the app!