# ✦ LumineX — AI Fashion Image Generation Engine

Gemini 기반 패션/에디토리얼 여성 이미지 생성 엔진.
프리셋 JSON 파일만 추가하면 무한 확장 가능.

---

## 🚀 빠른 시작

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. API 키 설정
```bash
cp .env.example .env
# .env 파일 열고 GEMINI_API_KEY 입력
```

### 3. 실행
```bash
# 프리셋으로 생성
python main.py --preset editorial_glam

# 완전 랜덤 생성
python main.py --random

# 프리셋 기반 랜덤 믹스
python main.py --mixed runway_power

# 배치 생성 (4장)
python main.py --preset neon_noir --batch 4

# 직접 프롬프트 입력
python main.py --prompt "Professional fashion photograph of..."

# 프리셋 목록 확인
python main.py --list
```

---

## 📁 프로젝트 구조

```
LumineX/
├── main.py              # CLI 진입점
├── config.py            # 설정 (API 키, 프로바이더 선택)
├── requirements.txt
├── .env                 # API 키 (git 제외)
├── .env.example
│
├── core/
│   ├── engine.py        # 프롬프트 조립 엔진
│   └── randomizer.py    # 랜덤 조합 로직
│
├── providers/
│   ├── base.py          # 추상 클래스
│   ├── gemini.py        # Gemini 구현체
│   └── __init__.py      # 프로바이더 팩토리
│
├── presets/             # JSON 프리셋 (무한 추가 가능)
│   ├── editorial_glam.json
│   ├── runway_power.json
│   ├── neon_noir.json
│   ├── chrome_vixen.json
│   ├── fitness_power.json
│   └── aqua_bikini.json
│
└── output/              # 생성된 이미지 저장
```

---

## ➕ 새 프리셋 추가 방법

`presets/` 폴더에 JSON 파일 하나만 추가하면 끝.

```json
{
  "tag": "My Custom Preset",
  "subject": "a professional model",
  "body": "athletic toned physique, confident stance",
  "outfit": "designer fashion ensemble",
  "material": "luxury fabric",
  "environment": "location description",
  "lighting": "lighting description",
  "style": "photography style reference",
  "quality": "shot on Hasselblad, ultra-sharp, 8K"
}
```

---

## 🔄 프로바이더 교체

`config.py`에서 한 줄만 바꾸면 됨:
```python
ACTIVE_PROVIDER = "gemini"      # gemini | stability | midjourney
```

새 프로바이더 추가 시 `providers/base.py`의 `ImageProvider`를 상속 구현.

---

## 📦 현재 프리셋 목록

| 프리셋 | 스타일 |
|--------|--------|
| `editorial_glam` | Vogue 에디토리얼, 스튜디오 |
| `runway_power` | 파리 패션위크 런웨이 |
| `neon_noir` | 사이버펑크, 도쿄 거리 |
| `chrome_vixen` | SF 미래주의, 크롬 |
| `fitness_power` | 피트니스 매거진 에디토리얼 |
| `aqua_bikini` | Sports Illustrated, 리조트 |