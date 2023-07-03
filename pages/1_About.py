import streamlit as st

st.set_page_config(
    page_title="PerformanceMeasures",
    page_icon='📈'
)

st.title('About the method')
cont = st.container()
cont2 = st.container()


cont.markdown('<div style="text-align: justify;">The DP2 distance is a synthetic indicator developed by Trapero (1977) with the purpose of comparing variables inter-spatially and/or intertemporally. There are two inherent advantages to this method: The first advantage is the assignment of scores to each element involved in the analysis, forming a ranking of the elements based on what reality allows. In other words, the method works with hierarchically constructed reference points. The second advantage is the possibility of measuring disparities among the entities involved. The method requires a matrix, where the rows represent the companies being analyzed (in the case of the thesis) and the columns represent the variables to be synthesized. Each element xij of the matrix represents the associated value of company i in variable j. Regarding the algorithm, it can be formulated as follows: Establish the matrix of component values for the m companies involved. Verify the behavior criteria for the n variables involved, i.e., classify the variables according to their objective: "the higher, the better" or "the lower, the better." Select a reference base for each variable, determining its theoretical ideal. Calculate the Frechet distances. Order the components from highest to lowest to create a hierarchy for the model. Obtain the DP2 for each company by incorporating the components according to the defined hierarchy. Repeat iterations until all variables have been incorporated into the model.</div>', unsafe_allow_html=True)

url = "http://www.jcyl.es/jcyl/cee/dgeae/congresos_ecoreg/CERCL/12339.PDF"
cont2.write("[Un indicador sintético para el reparto de fondos de compensación](%s)" % url)
