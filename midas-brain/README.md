# Midas Brain

AI Agent 서비스 - Quant Agent 시스템의 두뇌

## 기술 스택

- Python 3.13
- FastAPI
- LangChain / LangGraph
- uv (패키지 관리)

## 설치

```bash
# uv 설치 (없는 경우)
pip install uv

# 의존성 설치
uv sync

# 개발 의존성 포함
uv sync --dev
```

## 실행

```bash
# 환경변수 설정
cp .env.example .env
# .env 파일 수정

# 서버 실행
uv run uvicorn app.main:app --reload
```

## API 엔드포인트

| Method | Endpoint | 설명 |
|--------|----------|------|
| GET | `/` | 서비스 상태 |
| GET | `/api/v1/health` | 헬스체크 |
| POST | `/api/v1/chat` | 에이전트 대화 |

## 프로젝트 구조

```
midas-brain/
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI 엔트리포인트
│   ├── agents/          # LangGraph 멀티에이전트
│   ├── api/             # API 라우트
│   └── core/            # 설정
├── tests/
├── .env.example
├── pyproject.toml
└── README.md
```
