# AI Tech Question Reply Assistant 🤖

## 📌 Overview
This project is a **System-Message–Driven AI Assistant** built using **LangChain**.  
The assistant behaves like a **professional AI & technology professor** and provides **clear, concise, and core-focused explanations** for user queries related to **AI and technology**.

If a user asks questions **outside the AI or tech domain**, the assistant politely refuses and redirects the conversation back to technology topics.

---

## 🎯 Purpose
The goal of this project is to:
- Enforce **domain-specific responses** (AI & technology only)
- Maintain a **professional teaching tone**
- Deliver **simple, short, and clear explanations**
- Demonstrate proper use of **system messages in LangChain**

This project is ideal for learning:
- Prompt engineering
- System message control
- LangChain `ChatPromptTemplate`
- AI behavior restriction

---

## 🧠 Assistant Behavior Rules

### ✅ Allowed
- AI concepts
- Machine Learning
- Deep Learning
- Programming
- Software development
- Emerging technologies
- Backend, frontend, cloud, data science, etc.

### ❌ Not Allowed
- Non-technical topics
- General chit-chat
- Personal advice
- Entertainment, sports, politics, etc.

### 🚫 Restriction Response
If the user asks a non-tech-related question, the assistant responds with:

