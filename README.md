# Langfuse Infrastructure
Observability Infrastructure for LLM/Agent:
- Tracing
- ...

## 1. 🚀 **Deployment**
### 1.1. Install dependency
```bash
curl -fsSL https://just.systems/install.sh | bash -s -- --to /usr/local/bin
```

### 1.2. Start Server
```bash
just environment //Add your key 

just start
```

## 2. Environment
### 2.1. Login
Login with: 
```bash
LANGFUSE_INIT_USER_EMAIL=YOUR_EMAIL
LANGFUSE_INIT_USER_PASSWORD=YOUR_PASSWORD
```

### 2.2. Init Organization/Project
```bash
LANGFUSE_INIT_ORG_ID=YOUR_ORG
LANGFUSE_INIT_ORG_NAME=YOUR_ORG
LANGFUSE_INIT_PROJECT_ID=YOUR_PROJECT
LANGFUSE_INIT_PROJECT_NAME=YOUR_PROJECT
LANGFUSE_INIT_PROJECT_PUBLIC_KEY=pk-YOUR_KEY
LANGFUSE_INIT_PROJECT_SECRET_KEY=sk-YOUR_KEY
```

## 3. Application
### 3.1. Setup Environment
In application (e.g FastAPI), use add enviroment:
```bash
# Tracing
LANGFUSE_HOST=YOUR_HOST
LANGFUSE_SECRET_KEY=YOUR_KEY
LANGFUSE_PUBLIC_KEY=YOUR_KEY
```

### 3.2 Using it
- Config your tracer: `examples/config.py`
- Examples:
    - OpenAI LLM: `examples/openai.py`
    - Agno Agent: `examples/agno.py`
