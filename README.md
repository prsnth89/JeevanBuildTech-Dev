Step 1: Install Ollama
Shellollama run llama3Show more lines

Step 2: Install dependencies
Shellpip install -r requirements.txtShow more lines

Step 3: Start backend
Shelluvicorn app.main:app --reloadShow more lines

Step 4: Start UI
Shellstreamlit run ui/app.pyShow more lines
