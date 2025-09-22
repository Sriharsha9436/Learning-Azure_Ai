# Evaluate Generative AI Model Performance with Azure AI Foundry

This repository documents my experience evaluating the performance of a generative AI model using **Azure AI Foundry**. The process is inspired by the official Microsoft Learn exercise:  
*Evaluate a Generative AI Model with Prompt Flow.*

---

## 📝 What’s in This Project?

- Used Azure AI Foundry’s built-in evaluation tools  
- Imported sample data to test my deployed generative AI model  
- Configured key evaluation metrics (relevance, groundedness, fluency)  
- Ran an evaluation job and explored the results using the dashboard  
- Captured my own screenshots—check out the `Screenshots/` folder for visual highlights!

---

## 🚦 Prerequisites

Before starting, make sure you have:

- An **active Azure subscription**
- **Access to Azure AI Foundry**
- A **deployed generative AI model** (for example, a GPT-based model)

---

## 🛠️ Steps I Followed

### 1. Open the Azure AI Project

- Signed into [Azure AI Foundry](https://azure.microsoft.com/en-us/products/ai-services/ai-foundry/)
- Selected the project where my model is deployed

### 2. Navigate to **Evaluation**

- Used the left menu to head to **Evaluate**
- Picked my deployed generative AI model for analysis

### 3. Import Evaluation Data

- Grabbed the dataset from the `Sample Test Evaluation Data/` folder
- Uploaded it as the input for evaluation

### 4. Configure Metrics

Chose several metrics to assess model quality:
- **Relevance**: How well do the responses match the expected outputs?
- **Groundedness**: Are answers based on the provided information?
- **Fluency**: Is the language clear and correct?

### 5. Run the Evaluation

- Kicked off the evaluation job
- Azure AI Foundry automatically put my model to the test using the uploaded dataset

### 6. Review Results

- Checked out the evaluation dashboard for performance insights
- Compared scores across relevance, groundedness, and fluency
- Saved screenshots of the results (see `Screenshots/`)

---

## 📁 Repository Structure

```
Sample Test Evaluation Data/   # Dataset used for evaluation  
Screenshots/                   # Screenshots of setup & results  
README.md                      # Project documentation  
```

---

## 💡 Key Learnings

- Discovered how to set up and run structured evaluations on generative AI models in Azure AI Foundry
- Gained a better understanding of built-in metrics for measuring response quality
- Practiced interpreting results to find areas for model improvement

---

## 📚 Attribution

This project is based on the Microsoft Learn module:  
*Evaluate a Generative AI Model with Prompt Flow.*

I followed Microsoft’s guidance, implemented each step in my own Azure environment, and documented the results with screenshots.

---

> **If you’re exploring generative AI in Azure, I hope this project helps you get started with model evaluation! Questions or ideas? Feel free to reach out.**
