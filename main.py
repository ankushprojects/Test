from fastapi import FastAPI, Response
import uvicorn
import os
import google.generativeai as genai
from dotenv import load_dotenv
from pydantic import BaseModel
# Used to securely store your API key

load_dotenv()
GOOGLE_API_KEY = os.environ.get('GOOGLE_API_KEY')

app = FastAPI()

class LLMQuery(BaseModel):
    query: str

@app.post("/call_api")
async def call_api(llmquery:LLMQuery):
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(llmquery.query)
    return Response(content=response.text,media_type="application/text")

if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.3",port=4444,reload=True)