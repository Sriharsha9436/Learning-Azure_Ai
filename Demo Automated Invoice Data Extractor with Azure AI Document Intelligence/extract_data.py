import os
from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Get the credentials and endpoint from the loaded environment variables
try:
    endpoint = os.getenv("AZURE_DI_ENDPOINT")
    key = os.getenv("AZURE_DI_API_KEY")
    model_id = os.getenv("AZURE_MODEL_ID")

    if not all([endpoint, key, model_id]):
        raise ValueError("Missing one or more environment variables. Please check your .env file.")

except Exception as e:
    print(f"Error loading environment variables: {e}")
    exit()

# Define the path to your test invoice file
# Make sure you have a 'sample_invoices' folder with a test file inside.
invoice_path = "sample_invoices/invoice_test.pdf"

# Initialize the Document Intelligence client
document_intelligence_client = DocumentIntelligenceClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

print(f"✅ Analyzing document: {invoice_path}")

try:
    with open(invoice_path, "rb") as document_file:
        # Begin the analysis operation using your custom model ID
        poller = document_intelligence_client.begin_analyze_document(
            model_id=model_id, document=document_file
        )
        
        # Wait for the analysis to complete and get the results
        result = poller.result()

    # Process and print the extracted data
    if result.documents:
        for doc in result.documents:
            print("\n--- Document Analysis Results ---")
            print(f"Document type: {doc.doc_type}")
            
            # Iterate through the fields you labeled
            for name, field in doc.fields.items():
                print(f"  Field: {name}")
                print(f"  Extracted Value: {field.content}")
                print(f"  Confidence Score: {field.confidence:.2f}")

    print("\n🎉 Analysis completed successfully!")

except FileNotFoundError:
    print(f"Error: The file at {invoice_path} was not found. Please check the path.")
except Exception as e:
    print(f"An error occurred during analysis: {e}")