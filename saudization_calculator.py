import streamlit as st

# Title
st.title("📊 Saudization Calculator")

# Inputs
expats = st.number_input("Enter current expatriates:", min_value=0, value=581)
current_saudis = st.number_input("Enter current Saudis:", min_value=0, value=113)
target_percent = st.number_input("Target Saudization % (e.g. 50)", min_value=0.0, max_value=100.0, value=50.0)

# Calculate when button is clicked
if st.button("Calculate"):
    t = target_percent / 100
    best_result = None

    for x in range(0, 101):  # Special needs
        for y in range(0, 1001):  # Normal Saudis
            effective_saudis = current_saudis + 4 * x + y
            total_headcount = current_saudis + 4 * x + y + expats
            achieved = effective_saudis / total_headcount
            total_saudis_headcount = current_saudis + x + y
            max_special = int(total_saudis_headcount * 0.10)

            if abs(achieved - t) < 0.001 and x <= max_special:
                if (
                    best_result is None
                    or x > best_result["x"]
                    or (x == best_result["x"] and x + y < best_result["x"] + best_result["y"])
                ):
                    best_result = {
                        "x": x,
                        "y": y,
                        "achieved": achieved,
                        "max_special": max_special,
                        "total_hires": x + y
                    }

    if best_result:
        st.success(f"🎯 Target Saudization of {target_percent:.1f}% Achieved!")
        st.markdown(f"✅ Hire **{best_result['y']} normal Saudis**")
        st.markdown(f"✅ Hire **{best_result['x']} special needs Saudis**")
        st.markdown(f"📊 Achieved Saudization: **{best_result['achieved']*100:.2f}%**")
        st.markdown(f"📌 Max special needs allowed: **{best_result['max_special']}**")
        st.markdown(f"👥 Total hires: **{best_result['total_hires']}**")
    else:
        st.error("❌ Could not find a valid combination. Try lowering the target.")
