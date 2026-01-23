# Midas Agent

Quant Agent 시스템

## 프로젝트 구조

```
midas_agent/
├── midas-dashboard/    # UI 서비스
│   ├── app/
│   │   ├── components/ # 차트, 사이드바 컴포넌트
│   │   ├── core/       # 설정
│   │   ├── pages/      # 페이지
│   │   ├── services/   # API 클라이언트
│   │   └── main.py     # 메인 앱
│   ├── scripts/        # 실행 스크립트
│   └── tests/          # 테스트
├── midas-brain/        # AI Agent 서비스
│   ├── app/
│   │   └── main.py     # FastAPI 앱
│   └── tests/          # 테스트
├── docs/               # 문서
├── .gitignore
└── README.md
```

## 서비스 구성

| 서비스 | 설명 | 기술 스택 |
|--------|------|-----------|
| midas-dashboard | 대시보드/시각화 UI | Python, Streamlit, Plotly |
| midas-brain | AI 두뇌/의사결정 엔진 | Python, FastAPI, LangChain, LangGraph |

## 실행 방법

### midas-dashboard

```bash
cd midas-dashboard
uv sync
uv run streamlit run app/main.py
```

### midas-brain

```bash
cd midas-brain
uv sync
uv run uvicorn app.main:app --reload
```

## 요구사항

- Python >= 3.12
- uv (패키지 매니저)
