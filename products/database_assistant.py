from langchain_community.utilities import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain
from langchain_google_genai import GoogleGenerativeAI
from langchain.prompts import PromptTemplate
import os

def query_my_database(user_question):
    # 1. Secure Connection (Read-Only Mode)
    db_uri = "sqlite:///db.sqlite3?mode=ro"

    # 2. Privacy: ONLY include non-encrypted, readable fields
    # We EXCLUDE 'supplier_cost_encrypted' and 'internal_notes_encrypted'
    db = SQLDatabase.from_uri(
        db_uri,
        include_tables=['products_product'], # Django prefixes table names
        sample_rows_in_table_info=2
    )

    llm = GoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GEMINI_API_KEY"))

    # 3. Custom Prompt: Tell the AI what it CAN and CANNOT see
    custom_prompt = PromptTemplate(
        input_variables=["input", "table_info", "dialect"],
        template="""You are a data assistant for a Product Management System. 
        Given an input question, create a syntactically correct {dialect} query to run.
        
        CRITICAL INSTRUCTIONS:
        - Return ONLY the raw SQL query. 
        - DO NOT use markdown code blocks. 
        - DO NOT use backticks (```).
        - DO NOT include the word 'sqlite' in the output.
        
        IMPORTANT:
        - Use ONLY the following tables: {table_info}
        - You ONLY have access to product_id, product_category, product_price, product_manufacturing_date, and product_expiry_date.
        - DO NOT attempt to query fields ending in '_encrypted'.
        
        Question: {input}"""
    )
    # 4. Create the Chain
    db_chain = SQLDatabaseChain.from_llm(
        llm, 
        db, 
        prompt=custom_prompt,
        verbose=True, 
        return_direct=False
    )

    try:
        return db_chain.run(user_question)
    except Exception as e:
        return f"I encountered an error processing your request: {str(e)}"