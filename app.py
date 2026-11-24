import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Directorio Jalisco ODS 5",
    page_icon="",
    layout="wide"
)

# --- 1. DATOS OFICIALES DE JALISCO EN SESSION_STATE (CON LIGA A FUENTE) ---
DATOS_INICIALES = [
    {
        "nombre": "Emergencias Jalisco (Código Violeta)",
        "municipio": "Estatal (Todo Jalisco)",
        "tipo": "Emergencia 24/7",
        "telefono": "911",
        "horario": "24 horas, los 365 días",
        "accesibilidad": "Atención telefónica inmediata y canalización C5 Jalisco",
        "descripcion": "Línea de emergencia estatal. Si eres víctima de una agresión o delito, marca 911 e indica 'Código Violeta' para atención prioritaria.",
        "fuente_url": "https://redcjm.jalisco.gob.mx/"
    },
    {
        "nombre": "Chatbot #Violeta (WhatsApp C5 Jalisco)",
        "municipio": "Estatal (Todo Jalisco)",
        "tipo": "Emergencia y Orientación",
        "telefono": "33 1415 1002",
        "horario": "24 horas, los 365 días",
        "accesibilidad": "Mensajería de texto silenciosa por WhatsApp con envío de ubicación GPS",
        "descripcion": "Canal de contacto confidencial por WhatsApp operado por la Red CJM y C5 Jalisco para orientación informativa o alerta en situación de riesgo.",
        "fuente_url": "https://redcjm.jalisco.gob.mx/"
    },
    {
        "nombre": "Secretaría de Igualdad Sustantiva entre Mujeres y Hombres (SISEMH)",
        "municipio": "Guadalajara",
        "tipo": "Igualdad Sustantiva y Orientación",
        "telefono": "33 3679 2470",
        "horario": "Lunes a Viernes 09:00 - 17:00",
        "accesibilidad": "Atención presencial en Francisco de Quevedo #169, Col. Arcos Vallarta",
        "descripcion": "Dependencia estatal rectora de políticas de igualdad de género, prevención de violencias y vinculación institucional en Jalisco.",
        "fuente_url": "https://igualdad.jalisco.gob.mx/contacto/"
    },
    {
        "nombre": "Unidad Metropolitana de Atención Integral a Mujeres y Niñez (SISEMH)",
        "municipio": "Guadalajara (AMG)",
        "tipo": "Psicología, Legal y Trabajo Social",
        "telefono": "33 3586 6150",
        "horario": "Lunes a Viernes 09:00 - 17:00",
        "accesibilidad": "Atención presencial en Miguel Blanco #883, Zona Centro, Guadalajara",
        "descripcion": "Servicios gratuitos de prevención, orientación jurídica, atención psicológica y acompañamiento integral para mujeres y niñez en el Área Metropolitana.",
        "fuente_url": "https://igualdad.jalisco.gob.mx/contacto/"
    },
    {
        "nombre": "Unidad Metropolitana de Atención a Violencia Sexual (SISEMH)",
        "municipio": "Guadalajara",
        "tipo": "Atención Especializada y Salud",
        "telefono": "33 2200 6117",
        "horario": "Lunes a Viernes 09:00 - 17:00",
        "accesibilidad": "Atención presencial especializada en Miguel Blanco #883, Zona Centro",
        "descripcion": "Atención integral especializada a mujeres, adolescentes y niñez víctimas de violencia sexual que habitan o transitan por Jalisco.",
        "fuente_url": "https://igualdad.jalisco.gob.mx/contacto/"
    },
    {
        "nombre": "Centro de Justicia para las Mujeres (CJM) - Sede Guadalajara",
        "municipio": "Guadalajara",
        "tipo": "Refugio, Legal y Salud 24/7",
        "telefono": "33 3668 1880",
        "horario": "24 horas, los 365 días (Ext. 2)",
        "accesibilidad": "Área lúdica infantil, atención médica, pericial y estancia temporal en Álvaro Alcázar #5869, Jardines Alcalde",
        "descripcion": "Concentra en un mismo espacio recepción de denuncias, órdenes de protección, asesoría penal/familiar, atención médica y empoderamiento.",
        "fuente_url": "https://redcjm.jalisco.gob.mx/paginared_sedes"
    },
    {
        "nombre": "Centro de Justicia para las Mujeres (CJM) - Sede Tlaquepaque",
        "municipio": "San Pedro Tlaquepaque",
        "tipo": "Refugio, Legal y Salud 24/7",
        "telefono": "33 3668 1880",
        "horario": "24 horas, los 365 días (Ext. 6)",
        "accesibilidad": "Atención integral en Calle Benjamín Cerda #778, San Pedro Tlaquepaque",
        "descripcion": "Atención interinstitucional gratuita para mujeres víctimas de violencia y sus hijas e hijos: orientación jurídica, psicológica, médica y medidas de protección.",
        "fuente_url": "https://redcjm.jalisco.gob.mx/paginared_sedes"
    },
    {
        "nombre": "Centro de Justicia para las Mujeres (CJM) - Sede Tlajomulco",
        "municipio": "Tlajomulco de Zúñiga",
        "tipo": "Refugio, Legal y Salud 24/7",
        "telefono": "33 3668 1880",
        "horario": "24 horas, los 365 días (Ext. 5)",
        "accesibilidad": "Atención integral en Blvd. Distrito Federal #175, Fracc. Chulavista",
        "descripcion": "Servicios especializados de acceso a la justicia, consejería psicológica, trabajo social, atención médica y vinculación a refugio.",
        "fuente_url": "https://redcjm.jalisco.gob.mx/paginared_sedes"
    },
    {
        "nombre": "Centro de Justicia para las Mujeres (CJM) - Sede Puerto Vallarta",
        "municipio": "Puerto Vallarta",
        "tipo": "Refugio, Legal y Salud 24/7",
        "telefono": "33 3668 1880",
        "horario": "24 horas, los 365 días (Ext. 3)",
        "accesibilidad": "Atención integral en Av. Las Palmas #315, Col. Parque Las Palmas",
        "descripcion": "Atención especializada con perspectiva de género en la región Costa Norte: denuncias, medidas de protección, terapia y bolsa de trabajo.",
        "fuente_url": "https://redcjm.jalisco.gob.mx/paginared_sedes"
    },
    {
        "nombre": "Centro de Justicia para las Mujeres (CJM) - Sede Colotlán",
        "municipio": "Colotlán",
        "tipo": "Refugio, Legal y Salud 24/7",
        "telefono": "33 3668 1880",
        "horario": "24 horas, los 365 días (Ext. 4)",
        "accesibilidad": "Atención integral en Blvd. Salvador Lutteroth González #215, Col. Colotlán",
        "descripcion": "Sede regional en la Zona Norte de Jalisco con servicios gratuitos de acompañamiento legal, psicológico, médico y resguardo temporal.",
        "fuente_url": "https://redcjm.jalisco.gob.mx/paginared_sedes"
    },
    {
        "nombre": "Instituto Municipal de la Mujer para la Igualdad Sustantiva en Tonalá (IMMIST)",
        "municipio": "Tonalá",
        "tipo": "Igualdad Sustantiva y Prevención",
        "telefono": "33 3792 6626",
        "horario": "Lunes a Viernes 09:00 - 17:00",
        "accesibilidad": "Atención presencial en Calle Pedro Moreno #85, Col. Centro, Tonalá",
        "descripcion": "Instancia municipal dedicada a la igualdad sustantiva, diversidad e inclusión, y prevención y atención de la violencia de género en Tonalá.",
        "fuente_url": "https://mujer.tonala.gob.mx/contacto/"
    },
    {
        "nombre": "Instituto Municipal de las Mujeres de Guadalajara (InMujeresGDL)",
        "municipio": "Guadalajara",
        "tipo": "Psicología, Legal y Prevención",
        "telefono": "33 3638 5287",
        "horario": "Lunes a Viernes 09:00 - 17:00",
        "accesibilidad": "Atención presencial en Calle Mitla #386, Col. Monumental, Guadalajara",
        "descripcion": "Atención psicológica, asesoría jurídica gratuita y programas de prevención de violencia y autonomía económica para mujeres en Guadalajara.",
        "fuente_url": "https://inmujeresgdl.gob.mx/directorio.php"
    }
]

if "servicios" not in st.session_state:
    st.session_state.servicios = DATOS_INICIALES.copy()

# --- 2. BARRA LATERAL: ACCESIBILIDAD VISUAL Y FILTROS ---
with st.sidebar:
    st.header("Accesibilidad Visual")
    texto_grande = st.toggle("Texto grande (30 px)", value=False)
    espaciado_amplio = st.toggle("Mayor espaciado entre letras y líneas", value=False)

    st.divider()
    st.header("Filtros")
    df_base = pd.DataFrame(st.session_state.servicios)
    municipio_sel = st.selectbox("Municipio / Cobertura", ["Todos"] + sorted(df_base["municipio"].unique().tolist()))
    tipo_sel = st.selectbox("Tipo de apoyo", ["Todos"] + sorted(df_base["tipo"].unique().tolist()))
    busqueda = st.text_input("Buscar recurso", placeholder="Ej. Tonalá, CJM, 24 horas, legal...")

# --- 3. PALETA ÚNICA DE ALTO CONTRASTE PARA BAJA VISIÓN (WCAG AAA) ---
bg_app = "#000000"
fg_app = "#FFFFFF"
sidebar_bg = "#0D061A"
surface_bg = "#0A0414"
pill_bg = "#2E1065"
pill_fg = "#FDE047"
border_main = "#FDE047"
btn_bg = "#E9D5FF"
btn_fg = "#000000"
btn_hover = "#FDE047"
input_bg = "#120824"
info_bg = "#1E0B3B"
focus_ring = "#FDE047"

root_size = "30px" if texto_grande else "17px"
h1_size = "46px" if texto_grande else "34px"
h2_size = "38px" if texto_grande else "26px"
h3_size = "34px" if texto_grande else "22px"
pill_size = "24px" if texto_grande else "15px"

line_height = "1.8" if espaciado_amplio else "1.6"
letter_spacing = "0.04em" if espaciado_amplio else "0.01em"
word_spacing = "0.08em" if espaciado_amplio else "normal"

st.markdown(
    f"""
    <style>
        html {{
            font-size: {root_size} !important;
        }}
        .stApp {{
            background-color: {bg_app};
            color: {fg_app};
            font-size: {root_size} !important;
            line-height: {line_height};
            letter-spacing: {letter_spacing};
            word-spacing: {word_spacing};
        }}
        [data-testid="stSidebar"] {{
            background-color: {sidebar_bg} !important;
            border-right: 3px solid {border_main} !important;
        }}
        p, label, span, div, input, textarea, .stMarkdown,
        [data-testid="stMetricValue"], [data-testid="stMetricLabel"] {{
            color: {fg_app} !important;
            font-size: {root_size} !important;
            line-height: {line_height} !important;
            letter-spacing: {letter_spacing};
            word-spacing: {word_spacing};
        }}
        h1 {{
            color: {fg_app} !important;
            font-size: {h1_size} !important;
            font-weight: 800 !important;
            line-height: 1.3 !important;
        }}
        h2 {{
            color: {fg_app} !important;
            font-size: {h2_size} !important;
            font-weight: 700 !important;
            line-height: 1.35 !important;
        }}
        h3 {{
            color: {fg_app} !important;
            font-size: {h3_size} !important;
            font-weight: 700 !important;
            line-height: 1.4 !important;
        }}
        button:focus-visible, input:focus-visible, textarea:focus-visible,
        select:focus-visible, a:focus-visible, [tabindex]:focus-visible {{
            outline: 4px solid {focus_ring} !important;
            outline-offset: 3px !important;
        }}
        input, textarea, [data-baseweb="select"] > div {{
            background-color: {input_bg} !important;
            color: {fg_app} !important;
            border: 2.5px solid {border_main} !important;
            border-radius: 8px !important;
        }}
        [data-testid="stVerticalBlockBorderWrapper"] {{
            background-color: {surface_bg} !important;
            border: 3px solid {border_main} !important;
            border-radius: 14px;
            padding: 0.9rem 1.1rem;
        }}
        [data-testid="stAlert"] {{
            background-color: {info_bg} !important;
            color: {fg_app} !important;
            border: 2px solid {border_main} !important;
            border-left: 8px solid {border_main} !important;
            border-radius: 8px !important;
        }}
        .care-pill {{
            display: inline-block;
            background-color: {pill_bg};
            color: {pill_fg} !important;
            border: 2px solid {border_main};
            border-radius: 8px;
            padding: 0.25rem 0.75rem;
            font-size: {pill_size} !important;
            font-weight: 700;
            margin-right: 0.45rem;
            margin-bottom: 0.45rem;
        }}
        .stButton > button, .stLinkButton > a {{
            background-color: {btn_bg} !important;
            color: {btn_fg} !important;
            border: 3px solid {border_main} !important;
            border-radius: 10px !important;
            min-height: 54px !important;
            font-size: {root_size} !important;
            font-weight: 800 !important;
            text-decoration: underline !important;
            text-underline-offset: 4px;
        }}
        .stButton > button *, .stLinkButton > a * {{
            color: {btn_fg} !important;
            font-size: {root_size} !important;
        }}
        .stButton > button:hover, .stLinkButton > a:hover {{
            background-color: {btn_hover} !important;
        }}
        hr {{
            border-top: 2px solid {border_main} !important;
            opacity: 1 !important;
        }}
        .block-container {{
            max-width: 1180px;
            padding-top: 1.5rem;
            padding-bottom: 2.5rem;
        }}
    </style>
    """,
    unsafe_allow_html=True
)

# --- 4. ENCABEZADO PRINCIPAL Y SALIDA RÁPIDA ---
col_head, col_exit = st.columns([4, 1], vertical_alignment="center")
with col_head:
    st.markdown('<span class="care-pill">Violeta Care Compass · Jalisco · ODS 5</span>', unsafe_allow_html=True)
    st.title("Atención e Igualdad de Género")
    st.write("Directorio público, gratuito y confidencial de instituciones en Jalisco para la igualdad sustantiva y atención a violencias.")

with col_exit:
    st.link_button(
        "Salida rápida",
        "https://www.google.com/search?q=",
        use_container_width=True,
        help="Sale rápidamente a una búsqueda neutra"
    )

st.divider()

# --- 5. FORMULARIO PARA AÑADIR NUEVOS REGISTROS ---
with st.expander("Agregar nuevo recurso o institución al directorio", expanded=False):
    st.write("Completa los campos obligatorios (*). Si falta algún dato, se conserva lo que ya ingresaste.")
    with st.form("form_care_compass", clear_on_submit=True):
        c1, c2 = st.columns(2)
        with c1:
            nombre_nuevo = st.text_input("Nombre de la institución o servicio *", placeholder="Ej. Instituto Municipal de las Mujeres de Zapopan")
            municipio_nuevo = st.text_input("Municipio o cobertura *", placeholder="Ej. Zapopan, Tonalá, Estatal")
            tipo_nuevo = st.text_input("Tipo de apoyo *", placeholder="Ej. Igualdad Sustantiva, Psicología y Legal")
        with c2:
            telefono_nuevo = st.text_input("Teléfono *", placeholder="Ej. 33 3818 2200")
            horario_nuevo = st.text_input("Horario", value="Lunes a Viernes 09:00 - 17:00")
            accesibilidad_nuevo = st.text_input(
                "Dirección y accesibilidad",
                value="Atención presencial y telefónica",
                placeholder="Ej. Dirección, rampa, Lengua de Señas, lectura fácil"
            )

        fuente_nueva = st.text_input(
            "Liga de la fuente de información (URL)",
            value="https://igualdad.jalisco.gob.mx/contacto/",
            placeholder="Ej. https://..."
        )
        descripcion_nueva = st.text_area(
            "Descripción *",
            placeholder="Describe qué servicios brinda la institución y cómo acceder..."
        )
        guardar = st.form_submit_button("Guardar recurso")

        if guardar:
            errores = []
            if not nombre_nuevo.strip():
                errores.append("Indica el **Nombre de la institución o servicio**.")
            if not municipio_nuevo.strip():
                errores.append("Indica el **Municipio o cobertura**.")
            if not tipo_nuevo.strip():
                errores.append("Indica el **Tipo de apoyo**.")
            if not telefono_nuevo.strip():
                errores.append("Indica un **Teléfono** de contacto.")
            if not descripcion_nueva.strip():
                errores.append("Escribe una **Descripción** breve del servicio.")

            if errores:
                st.error("Revisa los siguientes campos:\n- " + "\n- ".join(errores))
            else:
                url_limpia = fuente_nueva.strip()
                if url_limpia and not url_limpia.startswith(("http://", "https://")):
                    url_limpia = "https://" + url_limpia
                st.session_state.servicios.append({
                    "nombre": nombre_nuevo.strip(),
                    "municipio": municipio_nuevo.strip(),
                    "tipo": tipo_nuevo.strip(),
                    "telefono": telefono_nuevo.strip(),
                    "horario": horario_nuevo.strip() or "No especificado",
                    "accesibilidad": accesibilidad_nuevo.strip() or "No especificado",
                    "descripcion": descripcion_nueva.strip(),
                    "fuente_url": url_limpia or "https://igualdad.jalisco.gob.mx/contacto/"
                })
                st.success(f"Se añadió **{nombre_nuevo.strip()}** al directorio.")
                st.rerun()

# --- 6. FILTRADO Y VISUALIZACIÓN DE TARJETAS ---
df_actual = pd.DataFrame(st.session_state.servicios)
df_filtrado = df_actual.copy()

if municipio_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["municipio"] == municipio_sel]
if tipo_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo"] == tipo_sel]
if busqueda.strip():
    termino = busqueda.strip().lower()
    df_filtrado = df_filtrado[
        df_filtrado.apply(lambda r: termino in str(r.values).lower(), axis=1)
    ]

st.subheader(f"Instituciones y recursos disponibles ({len(df_filtrado)})")

if df_filtrado.empty:
    st.warning("No hay recursos que coincidan con los filtros actuales. Ajusta los criterios en la barra lateral.")
else:
    cols = st.columns(2)
    for idx, (_, row) in enumerate(df_filtrado.iterrows()):
        with cols[idx % 2]:
            with st.container(border=True):
                st.markdown(
                    f'<span class="care-pill">Apoyo: {row["tipo"]}</span>'
                    f'<span class="care-pill">Lugar: {row["municipio"]}</span>'
                    f'<span class="care-pill">Horario: {row["horario"]}</span>',
                    unsafe_allow_html=True
                )
                st.markdown(f"### {row['nombre']}")
                st.write(row["descripcion"])
                st.info(f"**Ubicación y accesibilidad:** {row['accesibilidad']}")
                st.metric("Teléfono de contacto", row["telefono"])
                tel_limpio = "".join(ch for ch in str(row["telefono"]) if ch.isdigit() or ch == "+")
                st.link_button(
                    f"Llamar a {row['nombre']}",
                    f"tel:{tel_limpio}",
                    use_container_width=True
                )
                fuente_row = str(row.get("fuente_url", "")).strip()
                if fuente_row:
                    st.link_button(
                        "Fuente oficial",
                        fuente_row,
                        use_container_width=True,
                        help=f"Abre la fuente oficial: {fuente_row}"
                    )

st.divider()
st.caption("Fuentes oficiales: Secretaría de Igualdad Sustantiva entre Mujeres y Hombres (SISEMH Jalisco), Red de Centros de Justicia para las Mujeres (REDCJM) e Institutos Municipales de las Mujeres. Emergencias: 911.")