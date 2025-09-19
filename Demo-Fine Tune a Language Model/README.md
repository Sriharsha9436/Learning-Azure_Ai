# 🎓 Fine-Tuning a Language Model with Azure OpenAI (Microsoft Learn Lab)

Welcome to this hands-on repository showcasing how to fine-tune a language model using **Azure OpenAI Service**! This project follows the official Microsoft Learn lab and is designed to help you understand, visualize, and demo the entire fine-tuning workflow.

> **Reference Tutorial:**  
> [Fine-tune a model in Azure AI Studio — Microsoft Learn](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/05-Finetune-model.html)

---

## 🗂️ Repository Overview

```shell
├── training_data.jsonl      # Training dataset (JSONL format; provided by Microsoft Learn)
├── sample_output.txt        # Example prompts & simulated outputs
├── finetune_logs.txt        # Mock logs showing fine-tuning workflow and statuses
└── README.md                # This documentation
```

---

## 🚀 Fine-Tuning Workflow (Step-by-Step)

### 1️⃣ **Prepare Training Data**
- Formatted conversational examples in `.jsonl` (JSON Lines) as required by Azure OpenAI.
- Each row includes roles: `system`, `user`, and `assistant`.
- Used Microsoft’s sample travel assistant dataset.

### 2️⃣ **Upload Data to Azure AI Studio**
- Navigated to **Fine-tuning** in Azure AI Studio.
- Picked a base model (e.g., `gpt-35-turbo`).
- Uploaded `training_data.jsonl`.

### 3️⃣ **Start Fine-Tuning Job**
- Configured defaults and launched the job.
- Job status transitions:
  - **Enqueued → Preprocessing → Fine-tuning started → Data import started**
- Typical duration: *5–30 minutes*.

### 4️⃣ **Monitor Progress**
- Tracked status and logs in the Azure AI Studio dashboard.
- Status moved from *Fine-tuning* to *Completed*.
- See [`finetune_logs.txt`](./finetune_logs.txt) for a mock log of all steps.

### 5️⃣ **Deploy Fine-Tuned Model**
- Upon completion, the fine-tuned model appeared in **Deployments**.
- Ready to use via:
  - Prompt Flow
  - REST API
  - Playground in Azure AI Studio

---

## 📋 Example Logs

Curious about what the workflow looks like?  
Check [`finetune_logs.txt`](./finetune_logs.txt) for a step-by-step simulated log:

- Job enqueued
- Preprocessing completed
- Fine-tuning started
- Data import started
- Fine-tuning completed successfully

---

## ⚠️ Disclaimer

- **No actual fine-tuning costs incurred** — all results are simulated for educational purposes.
- The training dataset (`training_data.jsonl`) is directly sourced from Microsoft Learn.
- This repository is **for learning, demo, and portfolio use only**.

---

## 🙏 Credits

- **Microsoft Learn** for all training data & lab instructions.
- [Official Fine-tune Tutorial](https://microsoftlearning.github.io/mslearn-ai-studio/Instructions/05-Finetune-model.html)

---

## ⭐ Why Star This Repo?

- Step-by-step educational guide for Azure OpenAI fine-tuning
- Ready-to-use sample data, logs.
- Perfect for students, professionals, and anyone building an AI portfolio

---

> **Ready to fine-tune your skills? Explore the code, follow the steps, and make AI work for you!**
