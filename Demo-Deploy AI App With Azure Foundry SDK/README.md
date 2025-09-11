# 🚀 Azure AI Foundry Chatbot Demo

A hands-on demo showcasing how to build an interactive chatbot using the **Azure AI Foundry SDK** in Python.

---

## 📁 Project Structure

| File / Folder     | Purpose                                                                 |
|-------------------|-------------------------------------------------------------------------|
| `.env`            | Environment variables for Azure endpoint & Agent ID (**not included**)   |
| `requirements.txt`| Python dependencies                                                     |
| `app.py`          | Main script to interact with your Azure AI chatbot                      |

---

## 🛠️ Setup Instructions

### 1️⃣ **Create Azure AI Foundry Resource**

1. Sign in to [Azure Portal](https://portal.azure.com).
2. Click **Create a resource** → search for **Azure AI Foundry** → create a new instance.
3. Provide subscription, resource group, region & resource name.
4. Click **Review + create** → **Create**.

### 2️⃣ **Deploy a Chatbot Model**

1. Open your Azure AI Foundry resource.
2. Go to **Models** or **Agents** tab.
3. Add a new model/agent (e.g., **GPT-4.1 Mini** or custom).
4. Name & deploy your chat model.

### 3️⃣ **Get Endpoint & Agent ID**

1. Go to **Overview**/**Properties** for your resource.
2. Copy the **Project Endpoint URL**  
   (e.g., `https://<your-resource>.services.ai.azure.com/api/projects/<project-name>`)
3. Go to **Agents**, select your agent, and copy the **Agent ID**  
   (e.g., starts with `asst_`).

### 4️⃣ **Configure Your Local Project**

1. In your project root, create a `.env` file:

    ```
    PROJECT_ENDPOINT=https://your-foundry-project-endpoint
    AGENT_ID=your-agent-id
    ```

2. Install Python dependencies:

    ```
    pip install -r requirements.txt
    ```

### 5️⃣ **Run the Chatbot**

Start the chatbot:

```
python app.py
```

Interact with your deployed AI chatbot right from the terminal!

---

## ⚡ Notes

- Never commit your `.env` file to public repositories.
- You need an active Azure subscription and a deployed Foundry AI project.
- Refer to official documentation for advanced Azure AI Foundry features and SDK usage.

---

## 📚 Resources

- [Azure AI Foundry Documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/)
- [Azure AI Foundry SDK Python Samples](https://github.com/Azure/azure-sdk-for-python/tree/main/sdk/ai/azure-ai-projects/samples)

---

> **Feel free to modify and extend this project!  
> Clear, practical guidance to get you started with Azure AI Foundry and Python.**
