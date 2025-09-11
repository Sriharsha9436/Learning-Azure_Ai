# Azure AI Document Intelligence: Automated Invoice Data Extractor 🤖

## Project Overview

This project showcases a complete, end-to-end solution for automating invoice data extraction with Azure AI services. The system processes unstructured PDF documents, identifies key fields like invoice numbers, dates, and total amounts, and extracts them with high accuracy. The solution leverages a combination of Azure's machine learning and storage services to build a robust and scalable pipeline, transforming a manual, error-prone process into an efficient, automated workflow.

---

## 🛠️ Key Azure Services Utilized

- **Azure AI Document Intelligence:** The core AI service used to build and train a custom model.
- **Azure Blob Storage:** The central data store for all documents.
- **Python SDK for Document Intelligence:** The programmatic interface to connect application logic to the trained AI model.

---

## 1️⃣ Azure Resource Setup (The Click-by-Click Guide)

This section guides you through the process of setting up the necessary Azure resources and training your AI model from scratch.

### Step 1: Create a Storage Account and Upload Invoices

1. Log in to the [Azure Portal](https://portal.azure.com/).
2. In the search bar, type **Storage account** and click **Create**.
3. Fill in the details for your new account (Resource Group, name, region). Click **Review + Create**, then **Create**.
4. Once deployed, navigate to the new Storage Account.
5. In the left navigation menu, under **Data storage**, click **Containers**.
6. Click the **+ Container** button, give it a name like `invoices-to-train`, and click **Create**.
7. Open the container, click the **Upload** button, and upload 5 sample invoice PDF files.

### Step 2: Create a Document Intelligence Resource

1. In the Azure Portal search bar, type **Document Intelligence** and click **Create**.
2. Fill in the details for the resource, using a unique name (e.g., `invoice-reader-ai-service`).
3. Click **Review + Create**, then **Create**.

### Step 3: Train Your Custom Model

1. Go to the Document Intelligence resource.
2. In the left navigation menu, click on **Document Intelligence Studio** (opens a new tab).
3. In the Studio, select the **Custom models** tile.
4. Click **+ Create a project**.
5. Give the project a name (e.g., `invoice-extractor-project`).
6. For the Storage Account, select the one from Step 1, then select your `invoices-to-train` container.
7. Click **Create Project**. The Studio will now show the 5 documents you uploaded.

### Step 4: Label Your Documents

1. On the right-hand panel, click **+ Add** under the **Fields** section.
2. Create three fields with these names: `invoice_number`, `invoice_date`, and `total_amount`.
3. Click on the first invoice in the left-hand panel to open it.
4. Use the mouse to select the text of the invoice number on the document. A pop-up menu will appear.
5. Click on the `invoice_number` field. The text will now be highlighted.
6. Repeat the process for the `invoice_date` and `total_amount` on this first document.
7. Click on the next document in the left panel and repeat the labeling process for all three fields. Continue until all 5 documents are fully labeled.

> **Note:** Careful and accurate labeling is crucial for optimal model performance.

### Step 5: Train and Test Your Model

1. Once all documents are labeled, click the **Train** button in the top-right corner.
2. Give the model a name (e.g., `invoice-reader-model`).
3. In the **Build mode** dropdown, select **Template** and click **Train**.
4. Once training is complete, the Studio will take you to the new model's page.
5. Click the **Test** tab, upload a new invoice file, and click **Run analysis** to see the model in action!

---

## 2️⃣ Project Integration and Execution

This section details how to programmatically connect to your trained model.

### Step 1: Get Your Credentials

1. Go back to the Azure Portal and navigate to the Document Intelligence resource.
2. In the left navigation menu, click **Keys and Endpoint**. Copy the Endpoint URL and one of the Keys.
3. In the Studio, go to the **Models** section, select your trained model, and copy the **Model ID**.

### Step 2: Set Up Your Project

Create a project folder with the following structure:

```
/InvoiceExtractor
|-- .env
|-- .gitignore
|-- requirements.txt
|-- extract_data.py
|-- /sample_invoices
|   |-- (place your test invoice file here)
```

- Populate your `.env` file with your credentials:
  ```
  AZURE_DI_ENDPOINT=<your-endpoint-url>
  AZURE_DI_API_KEY=<your-api-key>
  AZURE_MODEL_ID=<your-model-id>
  ```
- Add `.env` to your `.gitignore` file.
- Add the following content to your `requirements.txt` file:
  ```
  azure-ai-documentintelligence
  python-dotenv
  ```

### Step 3: Run the Code

1. Open the terminal and ensure it's in the project folder.
2. Install the required libraries:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the script by executing your Python code to analyze your test invoice file.

---

## 📢 Need Help?

- [Azure Document Intelligence Documentation](https://learn.microsoft.com/en-us/azure/ai-services/document-intelligence/)
- [Azure Python SDK Reference](https://pypi.org/project/azure-ai-documentintelligence/)
- For support, open an issue in this repository.

---

## 📝 License

MIT © [Sriharsha9436](https://github.com/Sriharsha9436)
