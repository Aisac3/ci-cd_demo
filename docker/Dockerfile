# ---- Base image (pinned, not latest) ----
    FROM python:3.11-slim

    # ---- Build-time arguments (from CI) ----
    ARG APP_VERSION
    ARG GIT_COMMIT
    
    # ---- Runtime environment variables ----
    ENV APP_VERSION=${APP_VERSION}
    ENV GIT_COMMIT=${GIT_COMMIT}
    ENV ENVIRONMENT=dev
    ENV PYTHONDONTWRITEBYTECODE=1
    ENV PYTHONUNBUFFERED=1
    
    # ---- Create non-root user ----
    RUN addgroup --system appgroup && \
        adduser --system --ingroup appgroup appuser
    
    # ---- Working directory ----
    WORKDIR /app
    
    # ---- Install dependencies ----
    COPY requirements.txt .
    RUN pip install --no-cache-dir -r requirements.txt
    
    # ---- Copy application code ----
    COPY app/ .
    
    # ---- Change ownership & switch user ----
    RUN chown -R appuser:appgroup /app
    USER appuser
    
    # ---- Expose application port ----
    EXPOSE 8080
    
    # ---- Run the application ----
    CMD ["python", "app.py"]
    