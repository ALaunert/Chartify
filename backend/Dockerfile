FROM python:3.13
LABEL authors="alaunert"

WORKDIR /app

RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv "$HOME/.local/bin/uv" /usr/local/bin/

COPY pyproject.toml uv.lock ./
RUN uv pip install --system --no-deps --requirement uv.lock

COPY . .


CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]