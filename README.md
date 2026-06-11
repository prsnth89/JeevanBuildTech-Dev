Step 1: Install Ollama
ollama run llama3

Step 2: Install dependencies
pip install -r requirements.txt

Step 3: Start backend
uvicorn app.main:app --reload

Step 4: Start UI
streamlit run ui/app.py
