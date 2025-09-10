# Langfuse Infrastructure
Observability Infrastructure for LLM/Agent:
- Tracing (user_id, session_id, environment, ....)
- Prompt Management
- ...

![Langfuse Dashboard](images/langfuse.png)


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

## 4. Architecture

The following diagram shows the Langfuse self-hosted architecture:

```mermaid
flowchart TB
    subgraph VPC
        A[Web Server<br>langfuse-langfuse]
        B[Redis<br>Cache, Queue]
        C[Async Worker<br>langfuse-worker]
        D[(Postgres<br>OLTP - Transactional Data)]
        E[(ClickHouse<br>OLAP - Observability Data)]
        F[(S3 / Blob Storage<br>Raw events, multimodal attachments)]
    end

    UI[UI, API, SDKs] --> A
    A --> B
    B --> C
    C --> D
    C --> E
    C --> F

    subgraph Optional
        LLM[LLM API/Gateway<br>Optional]
    end

    A -->|Optional| LLM
    C -->|Optional| LLM
```
