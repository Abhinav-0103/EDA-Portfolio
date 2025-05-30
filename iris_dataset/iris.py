import streamlit as st

def iris(results_path) :
    st.title("🌸 Iris Dataset")

    # Introduction section
    st.header("📘 Introduction")
    st.markdown("""
    The **Iris dataset** was used in R.A. Fisher's classic 1936 paper *"The Use of Multiple Measurements in Taxonomic Problems"*, and is available via the [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/iris).

    It includes **three iris species** with **50 samples each**, and four features:
    - Sepal Length (cm)
    - Sepal Width (cm)
    - Petal Length (cm)
    - Petal Width (cm)

    🔍 One of the species is linearly separable from the other two, which overlap significantly.

    **Dataset Columns:**
    - `Id`
    - `SepalLengthCm`
    - `SepalWidthCm`
    - `PetalLengthCm`
    - `PetalWidthCm`
    - `Species`
    """)

    st.header("📉 Visualizations")

    with st.expander("🔲 Box Plots"):
        st.image(f"{results_path}/BoxPlots.jpg", use_container_width=True)

    with st.expander("📊 Histograms"):
        st.image(f"{results_path}/HistPlots.jpg", use_container_width=True)

    with st.expander("🔢 Count Plot (Species Distribution)"):
        st.image(f"{results_path}/CountPlot.jpg", use_container_width=True)

    with st.expander("🧠 Correlation Heatmap"):
        st.image(f"{results_path}/CorrelationHeatmap.jpg", use_container_width=True)

    with st.expander("🎻 Violin Plots"):
        st.image(f"{results_path}/ViolinPlots.jpg", use_container_width=True)

    with st.expander("🎯 Strip Plots"):
        st.image(f"{results_path}/StripPlots.jpg", use_container_width=True)

    with st.expander("🧩 Pair Plot"):   
        st.image(f"{results_path}/PairPlot.jpg", use_container_width="auto")

    with st.expander("📏 Size Comparison Plot"):
        st.image(f"{results_path}/HowLargePlot.jpg", use_container_width=True)

    with st.expander("📈 Area Plot"):
        st.image(f"{results_path}/AreaPlot.jpg", use_container_width=True)

    # Closing message
    st.markdown("---")
    st.success("✅ EDA complete! These visualizations give a comprehensive look at how each feature behaves across iris species.")

if __name__ == "__main__" :
    iris()