ollama run llama3

pip install -r requirements.txt

uvicorn app.main:app --reload

streamlit run ui/app.py
