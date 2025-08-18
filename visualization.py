import streamlit as st
from PIL import Image

from utils import *


st.markdown(
    """
    <style>
    :root {
        --primary-control-color: #d3d3d3; /* Light grey */
    }

    /* Main app background */
    .stApp {
        background-color: black !important;
        color: white !important;
    }

    /* Style buttons */
    .stButton > button {
        background-color: var(--primary-control-color) !important;
        color: black !important;
        border: none;
    }
    .stButton > button span {
        color: black !important;
    }
    .stButton > button:hover {
        background-color: #bbbbbb !important;
        color: black !important;
    }
    .stButton > button:hover span {
        color: black !important;
    }

    /* Style selectboxes (dropdowns) */
    div[data-baseweb="select"] > div {
        background-color: var(--primary-control-color) !important;
        color: black !important;
        transition: background-color 0.2s ease;
    }
    div[data-baseweb="select"] svg {
        fill: black !important;
    }
    div[data-baseweb="select"] span {
        color: black !important;
    }

    /* Explicitly style dropdown labels */
    label[data-baseweb="select"] {
        color: white !important;
    }
    .stSelectbox label {
        color: white !important;
    }

    /* Hover effect for dropdowns */
    div[data-baseweb="select"] > div:hover {
        background-color: #bbbbbb !important; /* Slightly darker grey */
        color: black !important;
    }
    div[data-baseweb="select"] > div:hover span {
        color: black !important;
    }
    div[data-baseweb="select"] > div:hover svg {
        fill: black !important;
    }

    img {
        border-radius: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Page config
st.set_page_config(page_title="Likelihood of South African Load Shedding", layout="wide")

# Main Title
st.markdown("<h1 style='text-align: center;'>Likelihood of South African Load Shedding</h1>", unsafe_allow_html=True)
st.markdown("---")

# Two main columns
col_left, col_right = st.columns([1, 1])

# =======================
# LEFT COLUMN
# =======================
for btn_key in [
    "eskom_tdp_clicked", "necom_expected_clicked", "delayed_rollout_clicked",
    "scenario_a_clicked", "scenario_b_clicked", "documentation_clicked"
]:
    if btn_key not in st.session_state:
        st.session_state[btn_key] = False

with col_left:
    # Create two subcolumns inside col_left
    base_col, interest_col = st.columns(2)

    default_build_out = 0
    default_demand = {2025: 0.5, 2026: 1, 2027: 1.5, 2028: 0, 2029: 2, 2030: -0.5}
    default_runtime = {2025: 6, 2026: 10, 2027: 15, 2028: 30, 2029: 6, 2030: 10}

    # =======================
    # BASE AND INTEREST COLUMNS
    # =======================

    flag = False

    with base_col:
        st.markdown("<h3 style='text-align: center;'>Base Scenarios</h3>", unsafe_allow_html=True)

        if st.button("Eskom TDP", use_container_width=True):
            default_build_out, default_demand, default_runtime = eskom_tdp_preset()
            flag = True
        if st.button("NECOM Expected", use_container_width=True):
            default_build_out, default_demand, default_runtime = necom_expected_preset()
            flag = True
        if st.button("Delayed Roll-out", use_container_width=True):
            default_build_out, default_demand, default_runtime = delayed_roll_out_preset()
            flag = True

    with interest_col:
        st.markdown(
            "<h3 style='text-align: center;'>Scenarios of Interest</h3>",
            unsafe_allow_html=True,
        )

        if st.button("Scenario A", use_container_width=True):
            default_build_out, default_demand, default_runtime = scenario_A()
            flag = True
        if st.button("Scenario B", use_container_width=True):
            default_build_out, default_demand, default_runtime = scenario_B()
            flag = True
        if st.button("Documentation", use_container_width=True):
            documentation()

    # Build-out section
    label_col, dropdown_col = st.columns([1, 2])

    with label_col:
        st.markdown(
            "<h3 style='margin: 0;'>Build-out Trajectory:</h3>", unsafe_allow_html=True
        )

    with dropdown_col:
        trajectory_option = st.selectbox(
            "Select Trajectory",
            options=["Eskom TDP 2025",
                     "NECOM Expected",
                     "Delayed roll-out"],
            index=default_build_out,
            key="build_out_trajectory",
        )

    demand = Image.open("images/NECOM base demand.drawio(1).png")
    st.image(demand, caption="Annual System Peak Demand (GW)", use_container_width=True)

    years = list(range(2025, 2031))
    print(default_build_out, default_demand, default_runtime)

    runtime_options = [6, 10, 15, 30]

    st.markdown("### Demand growth adjustment (GW):")

    # Create columns for demand growth, one column per year
    yearly_demand_options = {
        2025: [0, 0.5],
        2026: [-0.5, 0, 0.5, 1],
        2027: [-0.5, 0, 0.5, 1, 1.5, 2],
        2028: [-0.5, 0, 0.5, 1, 1.5, 2, 2.5],
        2029: [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5],
        2030: [-1, -0.5, 0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4],
    }

    label_to_code = {
        -1.0: "D01",
        -0.5: "D02",
        0.0: "D03",
        0.5: "D04",
        1.0: "D05",
        1.5: "D06",
        2.0: "D07",
        2.5: "D08",
        3.0: "D09",
        3.5: "D10",
        4.0: "D11",
    }

    for year in years:
        if f"demand_{year}" not in st.session_state:
            st.session_state[f"demand_{year}"] = default_demand.get(year, 0)

        if f"runtime_{year}" not in st.session_state:
            st.session_state[f"runtime_{year}"] = default_runtime.get(year, 6)

        if flag:
            st.session_state[f"demand_{year}"] = default_demand.get(year, 0)
            st.session_state[f"runtime_{year}"] = default_runtime.get(year, 6)

    demand_cols = st.columns(len(years))
    demand_growth_labels, demand_growth_codes = {}, {}
    for i, year in enumerate(years):
        options = yearly_demand_options[year]
        selected_label = demand_cols[i].selectbox(
            f"{year}",
            options,
            index=options.index(st.session_state[f"demand_{year}"]),
            key=f"demand_{year}",
        )
        demand_growth_labels[year] = selected_label
        demand_growth_codes[year] = label_to_code[selected_label]

    st.markdown("### OCGT max annual runtime (%):")

    # Create columns for OCGT runtime, one column per year
    label_to_ocgt = {
        6: "06",
        10: "10",
        15: "15",
        30: "30",
    }

    runtime_options = list(label_to_ocgt.keys())

    runtime_cols = st.columns(len(years))
    ocgt_runtime_labels = {}  # selected hours
    ocgt_runtime_codes = {}  # mapped codes

    for i, year in enumerate(years):
        selected_label = runtime_cols[i].selectbox(
            f"{year}",
            runtime_options,
            index=runtime_options.index(st.session_state[f"runtime_{year}"]),
            key=f"runtime_{year}",
        )
        ocgt_runtime_labels[year] = selected_label
        ocgt_runtime_codes[year] = label_to_ocgt[selected_label]

    filenames = all_drop_downs(trajectory_option, demand_growth_codes, ocgt_runtime_codes)

    for name in filenames:
        print(name)


    # =======================
    # Legend
    # =======================
    legend = Image.open("images/NECOM Key.drawio(3).png")
    st.image(legend, caption="Legend for the EAF vs Month Heatmap",use_container_width=True)



# =======================
# RIGHT COLUMN
# =======================
with col_right:
    # =======================
    # YEARS
    # =======================
    background = Image.open("images/NECOM chart background top.drawio.png")
    background = background.convert("RGBA")

    for i in range(6):

        image_25 = Image.open("images/Bx Dxx Oxx 20xx.png")


        image_25 = image_25.convert("RGBA")

        size = int(background.size[0] * 3 / 4 / 5)
        new_size = (int(size), int(size))
        image_25 = image_25.resize(new_size)

        overlay_fullsize = Image.new("RGBA", background.size, (0, 0, 0, 0))

        paste_pos = (
            (background.size[0] - new_size[0]) // 2 - int(background.size[0] / 2 * 3 / 4) + size * i,
            (background.size[1] - new_size[1]) // 2 - 8,
        )

        overlay_fullsize.paste(image_25, paste_pos)

        background = Image.alpha_composite(background, overlay_fullsize)

    st.image(background, caption="Load Shedding Forecast by Year", use_container_width=True)


    year = st.selectbox("Select Year to display in detail:", options=["2025", "2026", "2027", "2028", "2029", "2030"])


    # =======================
    # EAF Detailed View
    # =======================
    background = Image.open(
        "images/NECOM chart background mid 2025.drawio.png"
    ).convert("RGBA")
    overlay = Image.open("images/Bx Dxx Oxx 20xx.png")

    background = background.convert("RGBA")
    overlay = overlay.convert("RGBA")


    size = 0.84
    new_size = (int(background.size[0] * size), int(background.size[1] * size))
    overlay_resized = overlay.resize(new_size)


    overlay_fullsize = Image.new("RGBA", background.size, (0, 0, 0, 0))


    paste_pos = (
        (background.size[0] - new_size[0]) // 2 + 30,
        (background.size[1] - new_size[1]) // 2 - 8,
    )


    overlay_fullsize.paste(overlay_resized, paste_pos)


    combined = Image.alpha_composite(background, overlay_fullsize)
    st.image(combined, caption="EAF vs Month Heatmap", use_container_width=True)


