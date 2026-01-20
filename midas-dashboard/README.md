# Midas Dashboard

Streamlit 기반 대시보드 UI - Quant Agent 시스템

## 기술 스택

- Python 3.12
- Streamlit
- Plotly (차트)
- httpx (API 클라이언트)
- uv (패키지 관리)

## 설치

```bash
# uv 설치 (없는 경우)
pip install uv

# 의존성 설치
uv sync
```

## 실행

```bash
# 환경변수 설정
cp .env.example .env
# .env 파일 수정

# 대시보드 실행
uv run streamlit run app/main.py
```

## 프로젝트 구조

```
midas-dashboard/
├── app/
│   ├── __init__.py
│   ├── main.py              # Streamlit 엔트리포인트
│   ├── pages/               # 멀티페이지
│   │   ├── 1_dashboard.py
│   │   ├── 2_analysis.py
│   │   └── 3_settings.py
│   ├── components/          # UI 컴포넌트
│   ├── services/            # API 클라이언트
│   └── core/                # 설정
├── .streamlit/
│   └── config.toml
├── scripts/
├── tests/
├── .env.example
├── pyproject.toml
└── README.md
```

## 페이지 구성

| 페이지 | 설명 |
|--------|------|
| Home | 메인 화면, 요약 정보 |
| Dashboard | 포트폴리오 현황 |
| Analysis | 시장 분석, 차트 |
| Settings | 설정 관리 |
