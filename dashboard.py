"""
ArchLumeX Dashboard v1.0
실행: streamlit run dashboard.py

건축/인테리어 AI 이미지 프롬프트 엔진
대상: 집주인/일반인 (리모델링 참고용)
"""

import sys
import random
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

sys.path.insert(0, str(Path(__file__).parent))

import streamlit as st
from core.builders import build_gemini_prompt, build_chatgpt_prompt, build_midjourney_prompt
from core.data import (
    ASPECT_RATIOS,
    # 실외
    BUILDING_TYPES, ARCHITECTURAL_STYLES, EXTERIOR_MATERIALS,
    ROOF_STYLES, LANDSCAPING, EXTERIOR_VIEWPOINTS,
    # 실내
    SPACE_TYPES, INTERIOR_STYLES, INTERIOR_MATERIALS,
    FURNITURE_STYLES, COLOR_PALETTE, INTERIOR_VIEWPOINTS,
    # 공통
    LIGHTING, TIME_OF_DAY, WEATHER,
    CAMERA_ANGLES, COLOR_GRADES, MOOD,
    SPECIAL_FEATURES, CAMERAS, RENDER_STYLES,
)

st.set_page_config(
    page_title="ArchLumeX",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─── 다크 테마 CSS ────────────────────────────────────────
BG       = "#1a1a1a"
BG_SIDE  = "#212121"
BG_INPUT = "#2a2a2a"
BG_CARD  = "#252525"
GOLD     = "#b8966e"
GOLD_DIM = "#7a6045"
BORDER   = "#383838"
TEXT     = "#d0d0d0"
TEXT_DIM = "#808080"

st.markdown(f"""
<style>
.stApp, [data-testid="stAppViewContainer"] {{ background-color: {BG} !important; }}
[data-testid="stHeader"] {{ background-color: {BG} !important; }}
[data-testid="stSidebar"] {{ background-color: {BG_SIDE} !important; border-right: 1px solid {BORDER} !important; }}
[data-testid="stSidebar"] .stMarkdown p,
[data-testid="stSidebar"] label {{ color: {TEXT_DIM} !important; font-size: 0.78rem !important; }}
[data-testid="stSidebar"] h3 {{ color: {GOLD_DIM} !important; font-size: 0.65rem !important; letter-spacing: 2.5px !important; text-transform: uppercase !important; }}
h1, h2, h3, h4, h5 {{ color: {GOLD} !important; letter-spacing: 1.5px !important; }}
.stTabs [data-baseweb="tab-list"] {{ background-color: transparent !important; border-bottom: 1px solid {BORDER} !important; gap: 0 !important; }}
.stTabs [data-baseweb="tab"] {{ background-color: transparent !important; color: {TEXT_DIM} !important; font-size: 0.78rem !important; padding: 10px 20px !important; border-bottom: 2px solid transparent !important; }}
.stTabs [aria-selected="true"] {{ color: {GOLD} !important; border-bottom: 2px solid {GOLD} !important; background-color: transparent !important; }}
.stTabs [data-baseweb="tab-highlight"], .stTabs [data-baseweb="tab-border"] {{ display: none !important; }}
.stSelectbox > div > div {{ background-color: {BG_INPUT} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; color: {TEXT} !important; font-size: 0.8rem !important; }}
.stSelectbox > div > div:hover {{ border-color: rgba(184,150,110,0.4) !important; }}
.stSelectbox label {{ color: {GOLD} !important; font-size: 0.68rem !important; letter-spacing: 1.2px !important; text-transform: uppercase !important; font-weight: 600 !important; }}
.stButton > button {{ border-radius: 6px !important; font-size: 0.75rem !important; letter-spacing: 1.5px !important; text-transform: uppercase !important; font-weight: 700 !important; transition: all 0.2s !important; height: 42px !important; }}
.stButton > button[kind="primary"] {{ background: linear-gradient(135deg, {GOLD}, {GOLD_DIM}) !important; border: none !important; color: #111 !important; }}
.stButton > button[kind="primary"]:hover {{ background: linear-gradient(135deg, #d4a97e, {GOLD}) !important; transform: translateY(-1px) !important; }}
.stButton > button[kind="secondary"] {{ background: transparent !important; border: 1px solid rgba(184,150,110,0.4) !important; color: {GOLD} !important; }}
.stTextArea textarea {{ background-color: {BG_INPUT} !important; color: {TEXT} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; font-size: 0.78rem !important; line-height: 1.8 !important; }}
.stCode {{ background-color: {BG_INPUT} !important; border: 1px solid rgba(184,150,110,0.25) !important; border-radius: 6px !important; }}
.stCode code {{ color: #ce9178 !important; font-size: 0.75rem !important; line-height: 1.8 !important; }}
.stAlert {{ background-color: {BG_CARD} !important; border: 1px solid {BORDER} !important; border-radius: 6px !important; color: {TEXT_DIM} !important; font-size: 0.78rem !important; }}
hr {{ border-color: {BORDER} !important; margin: 12px 0 !important; }}
p, li, .stMarkdown {{ color: {TEXT} !important; font-size: 0.82rem !important; }}
::-webkit-scrollbar {{ width: 4px; }}
::-webkit-scrollbar-track {{ background: {BG}; }}
::-webkit-scrollbar-thumb {{ background: {BORDER}; border-radius: 2px; }}
</style>
""", unsafe_allow_html=True)

# ─── 헤더 ─────────────────────────────────────────────────
st.markdown('''
<div style="padding:8px 0 20px;">
  <div style="font-size:1.6rem;font-weight:700;letter-spacing:8px;color:#b8966e;">🏛️ ArchLumeX</div>
  <div style="font-size:0.65rem;letter-spacing:3px;color:#555;margin-top:4px;text-transform:uppercase;">AI Architecture & Interior Image Engine · v1.0</div>
</div>
''', unsafe_allow_html=True)

# ─── 사이드바 ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### ⚙️ 전역 설정")
    st.markdown("---")
    global_platform = st.radio(
        "🖥️ 출력 플랫폼",
        options=["Gemini", "ChatGPT (DALL-E)", "Midjourney"],
        index=0
    )
    global_aspect = st.selectbox(
        "📐 이미지 비율",
        options=list(ASPECT_RATIOS.keys()),
        index=0,
        help="★ = 기본값 권장"
    )
    st.markdown("---")
    platform_colors = {"Gemini": "🔵", "ChatGPT (DALL-E)": "🟢", "Midjourney": "🟣"}
    st.markdown(f"**플랫폼:** {platform_colors[global_platform]} `{global_platform}`")
    st.markdown(f"**비율:** `{global_aspect.split('—')[0].strip()}`")
    st.markdown("---")
    st.markdown("### 📌 사용법")
    st.markdown("1. 플랫폼/비율 선택\n2. 실외 또는 실내 탭 선택\n3. 원하는 스타일 선택\n4. **프롬프트 생성** 클릭\n5. 코드박스 복사 후 붙여넣기")
    st.markdown("---")
    st.markdown("### 💡 팁")
    if global_platform == "Gemini":
        st.info("자연어 서술형. 길고 상세할수록 좋아요.")
    elif global_platform == "ChatGPT (DALL-E)":
        st.success("키워드 중심. 짧고 강렬하게!")
    else:
        st.warning("태그 나열 + --파라미터 방식.")
    st.markdown("---")
    st.markdown("### 🏗️ 엔진 정보")
    st.markdown(f"**실외 스타일:** `{len(ARCHITECTURAL_STYLES)}종`")
    st.markdown(f"**실내 스타일:** `{len(INTERIOR_STYLES)}종`")
    st.markdown(f"**건물 유형:** `{len(BUILDING_TYPES)}종`")
    st.markdown(f"**공간 유형:** `{len(SPACE_TYPES)}종`")


def get_prompt(data: dict, mode: str) -> str:
    if global_platform == "Gemini":
        return build_gemini_prompt(data, global_aspect, mode)
    elif global_platform == "ChatGPT (DALL-E)":
        return build_chatgpt_prompt(data, global_aspect, mode)
    else:
        return build_midjourney_prompt(data, global_aspect, mode)


# ─── 탭 ──────────────────────────────────────────────────
tab_ext, tab_int, tab_rand = st.tabs(["🏠 실외 (Exterior)", "🛋️ 실내 (Interior)", "🎲 랜덤"])

# ══════════════════════════════════════════════════════════
# 탭 1: 실외
# ══════════════════════════════════════════════════════════
with tab_ext:
    st.markdown("### 🏠 실외 건축 이미지 생성")
    st.caption("건물 외관, 정원, 파사드 디자인을 시각화해보세요.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("##### 🏗️ 건물")
        ext_building   = st.selectbox("🏠 건물 유형",      list(BUILDING_TYPES.keys()),        key="ext_building")
        ext_arch_style = st.selectbox("🎨 건축 양식",      list(ARCHITECTURAL_STYLES.keys()),   key="ext_arch_style")
        ext_material   = st.selectbox("🧱 외장 소재",      list(EXTERIOR_MATERIALS.keys()),     key="ext_material")
        ext_roof       = st.selectbox("🏚️ 지붕 스타일",    list(ROOF_STYLES.keys()),            key="ext_roof")
        ext_landscape  = st.selectbox("🌿 조경/정원",      list(LANDSCAPING.keys()),            key="ext_landscape")

    with col2:
        st.markdown("##### 📸 촬영")
        ext_viewpoint  = st.selectbox("👁️ 시점/앵글",      list(EXTERIOR_VIEWPOINTS.keys()),    key="ext_viewpoint")
        ext_lighting   = st.selectbox("💡 조명",           list(LIGHTING.keys()),               key="ext_lighting")
        ext_time       = st.selectbox("🕐 시간대",         list(TIME_OF_DAY.keys()),            key="ext_time")
        ext_weather    = st.selectbox("🌦️ 날씨",           list(WEATHER.keys()),                key="ext_weather")
        ext_camera     = st.selectbox("📷 카메라",         list(CAMERAS.keys()),                key="ext_camera")

    with col3:
        st.markdown("##### 🎬 스타일")
        ext_angle      = st.selectbox("🔭 카메라 앵글",    list(CAMERA_ANGLES.keys()),          key="ext_angle")
        ext_color      = st.selectbox("🖼️ 색감",           list(COLOR_GRADES.keys()),           key="ext_color")
        ext_mood       = st.selectbox("🎭 무드",           list(MOOD.keys()),                   key="ext_mood")
        ext_render     = st.selectbox("✨ 렌더 스타일",    list(RENDER_STYLES.keys()),          key="ext_render")

    st.markdown("")
    col_a, col_b, _ = st.columns([1, 1, 2])
    with col_a:
        btn_ext = st.button("✨ 프롬프트 생성", type="primary", use_container_width=True, key="btn_ext")
    with col_b:
        btn_ext_rand = st.button("🎲 랜덤 생성", use_container_width=True, key="btn_ext_rand")

    if "ext_prompt" not in st.session_state:
        st.session_state.ext_prompt = ""

    if btn_ext:
        data = {
            "building_type":  BUILDING_TYPES[ext_building],
            "arch_style":     ARCHITECTURAL_STYLES[ext_arch_style],
            "ext_material":   EXTERIOR_MATERIALS[ext_material],
            "roof_style":     ROOF_STYLES[ext_roof],
            "landscaping":    LANDSCAPING[ext_landscape],
            "ext_viewpoint":  EXTERIOR_VIEWPOINTS[ext_viewpoint],
            "lighting":       LIGHTING[ext_lighting],
            "time_of_day":    TIME_OF_DAY[ext_time],
            "weather":        WEATHER[ext_weather],
            "camera":         CAMERAS[ext_camera],
            "camera_angle":   CAMERA_ANGLES[ext_angle],
            "color_grade":    COLOR_GRADES[ext_color],
            "mood":           MOOD[ext_mood],
            "render_style":   RENDER_STYLES[ext_render],
        }
        st.session_state.ext_prompt = get_prompt(data, "exterior")

    if btn_ext_rand:
        def rnd(d): return random.choice(list(d.keys()))
        data = {
            "building_type":  BUILDING_TYPES[rnd(BUILDING_TYPES)],
            "arch_style":     ARCHITECTURAL_STYLES[rnd(ARCHITECTURAL_STYLES)],
            "ext_material":   EXTERIOR_MATERIALS[rnd(EXTERIOR_MATERIALS)],
            "roof_style":     ROOF_STYLES[rnd(ROOF_STYLES)],
            "landscaping":    LANDSCAPING[rnd(LANDSCAPING)],
            "ext_viewpoint":  EXTERIOR_VIEWPOINTS[rnd(EXTERIOR_VIEWPOINTS)],
            "lighting":       LIGHTING[rnd(LIGHTING)],
            "time_of_day":    TIME_OF_DAY[rnd(TIME_OF_DAY)],
            "weather":        WEATHER[rnd(WEATHER)],
            "camera":         CAMERAS[rnd(CAMERAS)],
            "camera_angle":   CAMERA_ANGLES[rnd(CAMERA_ANGLES)],
            "color_grade":    COLOR_GRADES[rnd(COLOR_GRADES)],
            "mood":           MOOD[rnd(MOOD)],
            "render_style":   RENDER_STYLES[rnd(RENDER_STYLES)],
        }
        st.session_state.ext_prompt = get_prompt(data, "exterior")

    if st.session_state.ext_prompt:
        st.markdown("---")
        st.text_area("생성된 프롬프트", value=st.session_state.ext_prompt, height=160, key="ext_ta")
        st.code(st.session_state.ext_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")


# ══════════════════════════════════════════════════════════
# 탭 2: 실내
# ══════════════════════════════════════════════════════════
with tab_int:
    st.markdown("### 🛋️ 실내 인테리어 이미지 생성")
    st.caption("거실, 주방, 침실 등 실내 공간을 시각화해보세요.")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("##### 🏠 공간")
        int_space     = st.selectbox("🚪 공간 유형",      list(SPACE_TYPES.keys()),          key="int_space")
        int_style     = st.selectbox("🎨 인테리어 스타일", list(INTERIOR_STYLES.keys()),      key="int_style")
        int_material  = st.selectbox("🧱 소재/마감",      list(INTERIOR_MATERIALS.keys()),   key="int_material")
        int_furniture = st.selectbox("🛋️ 가구 스타일",    list(FURNITURE_STYLES.keys()),     key="int_furniture")
        int_palette   = st.selectbox("🎨 컬러 팔레트",    list(COLOR_PALETTE.keys()),        key="int_palette")
        int_features  = st.selectbox("⭐ 특별 요소",      list(SPECIAL_FEATURES.keys()),     key="int_features")

    with col2:
        st.markdown("##### 📸 촬영")
        int_viewpoint = st.selectbox("👁️ 시점/앵글",      list(INTERIOR_VIEWPOINTS.keys()),  key="int_viewpoint")
        int_lighting  = st.selectbox("💡 조명",           list(LIGHTING.keys()),             key="int_lighting")
        int_time      = st.selectbox("🕐 시간대",         list(TIME_OF_DAY.keys()),          key="int_time")
        int_camera    = st.selectbox("📷 카메라",         list(CAMERAS.keys()),              key="int_camera")

    with col3:
        st.markdown("##### 🎬 스타일")
        int_angle     = st.selectbox("🔭 카메라 앵글",    list(CAMERA_ANGLES.keys()),        key="int_angle")
        int_color     = st.selectbox("🖼️ 색감",           list(COLOR_GRADES.keys()),         key="int_color")
        int_mood      = st.selectbox("🎭 무드",           list(MOOD.keys()),                 key="int_mood")
        int_render    = st.selectbox("✨ 렌더 스타일",    list(RENDER_STYLES.keys()),        key="int_render")

    st.markdown("")
    col_a, col_b, _ = st.columns([1, 1, 2])
    with col_a:
        btn_int = st.button("✨ 프롬프트 생성", type="primary", use_container_width=True, key="btn_int")
    with col_b:
        btn_int_rand = st.button("🎲 랜덤 생성", use_container_width=True, key="btn_int_rand")

    if "int_prompt" not in st.session_state:
        st.session_state.int_prompt = ""

    if btn_int:
        data = {
            "space_type":      SPACE_TYPES[int_space],
            "int_style":       INTERIOR_STYLES[int_style],
            "int_material":    INTERIOR_MATERIALS[int_material],
            "furniture_style": FURNITURE_STYLES[int_furniture],
            "color_palette":   COLOR_PALETTE[int_palette],
            "special_features": SPECIAL_FEATURES[int_features],
            "int_viewpoint":   INTERIOR_VIEWPOINTS[int_viewpoint],
            "lighting":        LIGHTING[int_lighting],
            "time_of_day":     TIME_OF_DAY[int_time],
            "camera":          CAMERAS[int_camera],
            "camera_angle":    CAMERA_ANGLES[int_angle],
            "color_grade":     COLOR_GRADES[int_color],
            "mood":            MOOD[int_mood],
            "render_style":    RENDER_STYLES[int_render],
        }
        st.session_state.int_prompt = get_prompt(data, "interior")

    if btn_int_rand:
        def rnd(d): return random.choice(list(d.keys()))
        data = {
            "space_type":      SPACE_TYPES[rnd(SPACE_TYPES)],
            "int_style":       INTERIOR_STYLES[rnd(INTERIOR_STYLES)],
            "int_material":    INTERIOR_MATERIALS[rnd(INTERIOR_MATERIALS)],
            "furniture_style": FURNITURE_STYLES[rnd(FURNITURE_STYLES)],
            "color_palette":   COLOR_PALETTE[rnd(COLOR_PALETTE)],
            "special_features": SPECIAL_FEATURES[rnd(SPECIAL_FEATURES)],
            "int_viewpoint":   INTERIOR_VIEWPOINTS[rnd(INTERIOR_VIEWPOINTS)],
            "lighting":        LIGHTING[rnd(LIGHTING)],
            "time_of_day":     TIME_OF_DAY[rnd(TIME_OF_DAY)],
            "camera":          CAMERAS[rnd(CAMERAS)],
            "camera_angle":    CAMERA_ANGLES[rnd(CAMERA_ANGLES)],
            "color_grade":     COLOR_GRADES[rnd(COLOR_GRADES)],
            "mood":            MOOD[rnd(MOOD)],
            "render_style":    RENDER_STYLES[rnd(RENDER_STYLES)],
        }
        st.session_state.int_prompt = get_prompt(data, "interior")

    if st.session_state.int_prompt:
        st.markdown("---")
        st.text_area("생성된 프롬프트", value=st.session_state.int_prompt, height=160, key="int_ta")
        st.code(st.session_state.int_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")


# ══════════════════════════════════════════════════════════
# 탭 3: 랜덤
# ══════════════════════════════════════════════════════════
with tab_rand:
    st.markdown("### 🎲 완전 랜덤 생성")
    st.caption("실외/실내를 랜덤으로 골라 프롬프트를 생성합니다.")

    col1, col2, _ = st.columns([1, 1, 2])
    with col1:
        btn_rand_ext = st.button("🏠 실외 랜덤", type="primary", use_container_width=True, key="btn_rand_ext")
    with col2:
        btn_rand_int = st.button("🛋️ 실내 랜덤", use_container_width=True, key="btn_rand_int")

    if "rand_prompt" not in st.session_state:
        st.session_state.rand_prompt = ""
    if "rand_mode" not in st.session_state:
        st.session_state.rand_mode = ""

    def rnd(d): return random.choice(list(d.keys()))

    if btn_rand_ext:
        data = {
            "building_type":  BUILDING_TYPES[rnd(BUILDING_TYPES)],
            "arch_style":     ARCHITECTURAL_STYLES[rnd(ARCHITECTURAL_STYLES)],
            "ext_material":   EXTERIOR_MATERIALS[rnd(EXTERIOR_MATERIALS)],
            "roof_style":     ROOF_STYLES[rnd(ROOF_STYLES)],
            "landscaping":    LANDSCAPING[rnd(LANDSCAPING)],
            "ext_viewpoint":  EXTERIOR_VIEWPOINTS[rnd(EXTERIOR_VIEWPOINTS)],
            "lighting":       LIGHTING[rnd(LIGHTING)],
            "time_of_day":    TIME_OF_DAY[rnd(TIME_OF_DAY)],
            "weather":        WEATHER[rnd(WEATHER)],
            "camera":         CAMERAS[rnd(CAMERAS)],
            "camera_angle":   CAMERA_ANGLES[rnd(CAMERA_ANGLES)],
            "color_grade":    COLOR_GRADES[rnd(COLOR_GRADES)],
            "mood":           MOOD[rnd(MOOD)],
            "render_style":   RENDER_STYLES[rnd(RENDER_STYLES)],
        }
        st.session_state.rand_prompt = get_prompt(data, "exterior")
        st.session_state.rand_mode = "🏠 실외"

    if btn_rand_int:
        data = {
            "space_type":       SPACE_TYPES[rnd(SPACE_TYPES)],
            "int_style":        INTERIOR_STYLES[rnd(INTERIOR_STYLES)],
            "int_material":     INTERIOR_MATERIALS[rnd(INTERIOR_MATERIALS)],
            "furniture_style":  FURNITURE_STYLES[rnd(FURNITURE_STYLES)],
            "color_palette":    COLOR_PALETTE[rnd(COLOR_PALETTE)],
            "special_features": SPECIAL_FEATURES[rnd(SPECIAL_FEATURES)],
            "int_viewpoint":    INTERIOR_VIEWPOINTS[rnd(INTERIOR_VIEWPOINTS)],
            "lighting":         LIGHTING[rnd(LIGHTING)],
            "time_of_day":      TIME_OF_DAY[rnd(TIME_OF_DAY)],
            "camera":           CAMERAS[rnd(CAMERAS)],
            "camera_angle":     CAMERA_ANGLES[rnd(CAMERA_ANGLES)],
            "color_grade":      COLOR_GRADES[rnd(COLOR_GRADES)],
            "mood":             MOOD[rnd(MOOD)],
            "render_style":     RENDER_STYLES[rnd(RENDER_STYLES)],
        }
        st.session_state.rand_prompt = get_prompt(data, "interior")
        st.session_state.rand_mode = "🛋️ 실내"

    if st.session_state.rand_prompt:
        st.caption(f"생성 모드: {st.session_state.rand_mode}")
        st.text_area("랜덤 프롬프트", value=st.session_state.rand_prompt, height=160, key="rand_ta")
        st.code(st.session_state.rand_prompt, language=None)
        st.caption(f"👆 복사 후 {global_platform}에 붙여넣으세요!")

st.markdown("---")
st.markdown(f'<div style="text-align:center;color:#444;font-size:0.75rem;">🏛️ ArchLumeX v1.0 — AI Architecture & Interior Image Engine</div>', unsafe_allow_html=True)