import streamlit as st

st.set_page_config(
    page_title="ApoioDecisao",
    page_icon='📈'
)

st.title('Sobre o método')
cont = st.container()
cont2 = st.container()

cont3 = st.container()



cont.markdown('<div style="text-align: justify;">A distância DP2 é um indicador sintético elaborado por Trapero (1977) que tem por finalidade a comparação interespacial e/ou intertemporal de variáveis. Há duas vantagens inerentes ao método: </div>', unsafe_allow_html=True)
cont.markdown('<div style="text-align: justify;">o primeiro é a atribuição de pontuação a cada elemento envolvido na análise, formando um ranking dos elementos envolvidos frente o que a realidade permite, ou seja, o método trabalha com pontos de referência hierarquicamente construídos. A segunda vantagem é a possibilidade da mensuração de disparidades entre os envolvidos</div>', unsafe_allow_html=True)
cont.markdown('<div style="text-align: justify;">O método necessita de uma matriz, cujos elementos em linha são no caso da tese as empresas em análise e as colunas as variáveis a serem sintetizadas. </div>', unsafe_allow_html=True)
cont.markdown('<div style="text-align: justify;">Cada elemento  xij da matriz representa o valor associado da empresa i na variável j. </div>', unsafe_allow_html=True)

cont.markdown('<div style="text-align: justify;">Sobre o Algoritmo </div>', unsafe_allow_html=True)

cont.markdown('<div style="text-align: justify;">pode-se formular o algoritmo para o cálculo do DP2 é dado como segue:</div>', unsafe_allow_html=True)

cont.markdown('<div style="text-align: justify;">Estabelecimento da matriz de valores das componentes das m empresas envolvidas.</div>', unsafe_allow_html=True)

cont.markdown('<div style="text-align: justify;">Verificar os critérios das n variáveis envolvidas quanto a sua conduta, ou seja, classificar as variáveis quanto a seu objetivo: “quanto maior, melhor” ou “quanto menor, melhor”;</div>', unsafe_allow_html=True)

cont.markdown('<div style="text-align: justify;">Eleição da base de referência em cada variável, determinando seu ideal teórico;</div>', unsafe_allow_html=True)
cont.markdown('<div style="text-align: justify;">Calcular as distâncias de Frechet;</div>', unsafe_allow_html=True)
cont.markdown('<div style="text-align: justify;">Ordenação das componentes de maior para menor à hierarquização do modelo;</div>', unsafe_allow_html=True)
cont.markdown('<div style="text-align: justify;">Obtenção do DP2 de cada empresa fazendo entrar as componentes segundo a hierarquia definida em (v);</div>', unsafe_allow_html=True)
cont.markdown('<div style="text-align: justify;">Iterações consecutivas até que todas a variáveis tenham sido incorporadas ao modelo.</div>', unsafe_allow_html=True)
