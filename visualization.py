import streamlit as st
from PIL import Image


# Page config
st.set_page_config(page_title="Likelihood of South African Load Shedding", layout="wide")

WIDTH = 1000
DEMAND = int(WIDTH * 1.25)

# Main Title
st.markdown("<h1 style='text-align: center;'>Likelihood of South African Load Shedding</h1>", unsafe_allow_html=True)
st.markdown("---")

# Two main columns
col_left, col_right = st.columns([1.2, 1])

# =======================
# LEFT COLUMN
# =======================
with col_left:
    # Create two subcolumns inside col_left
    base_col, interest_col = st.columns(2)

    with base_col:
        st.markdown("<h3 style='text-align: center;'>Base Scenarios</h3>", unsafe_allow_html=True)

        st.button("Eskom TDP", use_container_width=True)
        st.button("NECOM Expected", use_container_width=True)
        st.button("Delayed Roll-out", use_container_width=True)

    with interest_col:
        st.markdown(
            "<h3 style='text-align: center;'>Scenarios of Interest</h3>",
            unsafe_allow_html=True,
        )


        st.button("Scenario A", use_container_width=True)
        st.button("Scenario B", use_container_width=True)
        st.button("Documentation", use_container_width=True)

    # Build-out section
    st.markdown(
        "<h3 style='text-align: center;'>Build-out trajectories: Eskom TDP 2025</h3>",
        unsafe_allow_html=True,
    )
    demand = Image.open("images/NECOM base demand.drawio(1).png")
    st.image(demand, caption="Annual System Peak Demand (GW)", width=DEMAND)

    years = list(range(2025, 2031))

    demand_options = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5, 2.0, 2.5]
    runtime_options = [0, 5, 6, 10, 15, 20, 25]

    st.markdown("### Demand growth adjustment (GW):")

    # Create columns for demand growth, one column per year
    demand_cols = st.columns(len(years))
    demand_growth = {}
    for i, year in enumerate(years):
        default_index = demand_options.index(0.0)  # default 0.0 for all
        demand_growth[year] = demand_cols[i].selectbox(
            f"{year}", demand_options, index=default_index, key=f"demand_{year}"
        )

    st.markdown("### OCGT max annual runtime (%):")

    # Create columns for OCGT runtime, one column per year
    runtime_cols = st.columns(len(years))
    ocgt_runtime = {}
    for i, year in enumerate(years):
        # set default based on your original values
        if year == 2025:
            default_index = runtime_options.index(6)
        elif year in [2026, 2027]:
            default_index = runtime_options.index(10)
        else:
            default_index = runtime_options.index(15)

        ocgt_runtime[year] = runtime_cols[i].selectbox(
            f"{year}", runtime_options, index=default_index, key=f"runtime_{year}"
        )

    # # Optional: display selected values
    # st.write("### Selected Demand Growth:")
    # st.write(demand_growth)
    #
    # st.write("### Selected OCGT Runtime:")
    # st.write(ocgt_runtime)

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
        print(i)
        image_25 = Image.open("images/Bx Dxx Oxx 20xx.png")


        image_25 = image_25.convert("RGBA")

        size = int(background.size[0] * 3 / 4 / 5)
        new_size = (int(size), int(size))
        image_25 = image_25.resize(new_size)

        overlay_fullsize = Image.new("RGBA", background.size, (0, 0, 0, 0))

        print(int(background.size[0] * 3 / 4))

        paste_pos = (
            (background.size[0] - new_size[0]) // 2 - int(background.size[0] / 2 * 3 / 4) + size * i,
            (background.size[1] - new_size[1]) // 2 - 8,
        )

        overlay_fullsize.paste(image_25, paste_pos)

        background = Image.alpha_composite(background, overlay_fullsize)

    st.image(background, caption="Load Shedding Forecast by Year", width=WIDTH)


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
    st.image(combined, caption="EAF vs Month Heatmap", width=WIDTH)


    # =======================
    # Legend
    # =======================
    legend = Image.open("images/NECOM Key.drawio(3).png")
    st.image(legend, caption="Legend for the EAF vs Month Heatmap",width=WIDTH)
