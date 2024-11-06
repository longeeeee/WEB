import streamlit as st
import pandas as pd
import pyodbc
import streamlit as st
import pandas as pd
import pyodbc
from graphviz import Digraph
#streamlit run c:/Users/52980/Desktop/stream_正式.py
#绘制Chart图
def draw_chart(df):
    BD_POL_PID = new_df[['BOND_PROD', 'POL_PROD']].drop_duplicates(subset=['BOND_PROD', 'POL_PROD'])
    if 'BOND_PROD' in BD_POL_PID.columns and 'POL_PROD' in BD_POL_PID.columns:
        # 使用 groupby 将 BOND_PROD 作为键，POL_PROD 作为列表值
        bond_prod_dict = BD_POL_PID.groupby('BOND_PROD')['POL_PROD'].apply(list).to_dict()
    POL_CUT_PID = new_df[['POL_PROD', 'CUT_PANEL_PROD']].drop_duplicates(subset=['POL_PROD', 'CUT_PANEL_PROD'])
    if 'POL_PROD' in POL_CUT_PID.columns and 'CUT_PANEL_PROD' in POL_CUT_PID.columns:
        # 使用 groupby 将 POL_PROD 作为键，CUT_PANEL_PROD 作为列表值
        pol_cut_dict = POL_CUT_PID.groupby('POL_PROD')['CUT_PANEL_PROD'].apply(list).to_dict()
    CUT_FSA_PID = new_df[['CUT_PANEL_PROD', 'FSA_PROD']].drop_duplicates(subset=['CUT_PANEL_PROD', 'FSA_PROD'])
    if 'CUT_PANEL_PROD' in CUT_FSA_PID.columns and 'FSA_PROD' in CUT_FSA_PID.columns:
        # 使用 groupby 将 CUT_PANEL_PROD 作为键，FSA_PROD 作为列表值
        cut_fsa_dict = CUT_FSA_PID.groupby('CUT_PANEL_PROD')['FSA_PROD'].apply(list).to_dict()
    FSA_PICF_PID = new_df[['FSA_PROD', 'PICF_PROD']].drop_duplicates(subset=['FSA_PROD', 'PICF_PROD'])
    if 'FSA_PROD' in FSA_PICF_PID.columns and 'PICF_PROD' in FSA_PICF_PID.columns:
        # 使用 groupby 将 FSA_PROD 作为键，PICF_PROD 作为列表值
        fsa_picf_dict = FSA_PICF_PID.groupby('FSA_PROD')['PICF_PROD'].apply(list).to_dict()
    FSA_PITFT_PID = new_df[['FSA_PROD', 'PITFT_PROD']].drop_duplicates(subset=['FSA_PROD', 'PITFT_PROD'])
    if 'FSA_PROD' in FSA_PITFT_PID.columns and 'PITFT_PROD' in FSA_PITFT_PID.columns:
        # 使用 groupby 将 FSA_PROD 作为键，PITFT_PROD 作为列表值
        fsa_pitft_dict = FSA_PITFT_PID.groupby('FSA_PROD')['PITFT_PROD'].apply(list).to_dict()
    PITFT_ARY_PID = new_df[['PITFT_PROD', 'ARY_PROD']].drop_duplicates(subset=['PITFT_PROD', 'ARY_PROD'])
    if 'PITFT_PROD' in PITFT_ARY_PID.columns and 'ARY_PROD' in PITFT_ARY_PID.columns:
        # 使用 groupby 将 PITFT_PROD 作为键，ARY_PROD 作为列表值
        pitft_ary_dict = PITFT_ARY_PID.groupby('PITFT_PROD')['ARY_PROD'].apply(list).to_dict()
    PICF_CF_PID = new_df[['PICF_PROD', 'CF_PROD']].drop_duplicates(subset=['PICF_PROD', 'CF_PROD'])
    if 'PICF_PROD' in PICF_CF_PID.columns and 'CF_PROD' in PICF_CF_PID.columns:
        # 使用 groupby 将 PITFT_PROD 作为键，CF_PROD 作为列表值
        picf_cf_dict = PICF_CF_PID.groupby('PICF_PROD')['CF_PROD'].apply(list).to_dict()
    dot = Digraph(comment='PID-Tree')
    dot.attr(rankdir='LR', size='10,10', ratio='fill')  # 设置大小和比例为正方形
    # 为不同节点设置形状的示例
    bond_shape = 'box'   # 例：Bond节点使用椭圆形
    pol_shape = 'box'       # 例：Policy节点使用方形
    cut_shape = 'box'   # 例：Cut节点使用菱形
    fsa_shape = 'box'     # 例：FSA节点使用椭圆
    picf_shape = 'box'   # 例：PICF节点使用圆形
    cf_shape = 'box'    # 例：CF节点使用六边形
    pitft_shape = 'box'   # 例：PITFT节点使用梯形
    ary_shape = 'box'   # 例：ARY节点使用纯文本形状
    for i, bond_prod in enumerate(bond_prod_dict.keys()):
        dot.node(f'BD{i}', label=f'{bond_prod}\nBD_PID', shape=bond_shape)  # 添加注释
        for j, pol_item in enumerate(bond_prod_dict[bond_prod]):
            dot.node(f'POL{i}_{j}', label=f'{pol_item}\nPOL_PID', shape=pol_shape)  # 添加注释
            dot.edge(f'POL{i}_{j}', f'BD{i}')  # 反向连线POL到BD
            if pol_item in pol_cut_dict.keys():
                for k, cut_item in enumerate(pol_cut_dict[pol_item]):
                    dot.node(f'CUT{i}_{j}_{k}', label=f'{cut_item}\nCut_PID', shape=cut_shape)  # 添加注释
                    dot.edge(f'CUT{i}_{j}_{k}', f'POL{i}_{j}')  # 反向连线CUT到POL
                    if cut_item in cut_fsa_dict.keys():
                        for l, fsa_item in enumerate(cut_fsa_dict[cut_item]):
                            dot.node(f'FSA{i}_{j}_{k}_{l}', label=f'{fsa_item}\nFSA_PID', shape=fsa_shape)  # 添加注释
                            dot.edge(f'FSA{i}_{j}_{k}_{l}', f'CUT{i}_{j}_{k}')  # 反向连线FSA到CUT
                            if fsa_item in fsa_picf_dict.keys():
                                for m, picf_item in enumerate(fsa_picf_dict[fsa_item]):
                                    dot.node(f'PICF{i}_{j}_{k}_{l}_{m}', label=f'{picf_item}\nPI-CF_PID', shape=picf_shape)  # 添加注释
                                    dot.edge(f'PICF{i}_{j}_{k}_{l}_{m}', f'FSA{i}_{j}_{k}_{l}')  # 反向连线PICF到FSA
                                    print(dot.source)  # 打印DOT源代码
                                    if picf_item in picf_cf_dict.keys():
                                        for n, cf_item in enumerate(picf_cf_dict[picf_item]):
                                            dot.node(f'CF{i}_{j}_{k}_{l}_{m}_{n}', label=f'{cf_item}\nCF_PID', shape=cf_shape)  # 添加注释
                                            dot.edge(f'CF{i}_{j}_{k}_{l}_{m}_{n}', f'PICF{i}_{j}_{k}_{l}_{m}')  # 反向连线CF到PICF
                                    if fsa_item in fsa_pitft_dict.keys():
                                        for m, pitft_item in enumerate(fsa_pitft_dict[fsa_item]):
                                            dot.node(f'PITFT{i}_{j}_{k}_{l}_{m}', label=f'{pitft_item}\nPI-TFT_PID', shape=pitft_shape)  # 添加注释
                                            dot.edge(f'PITFT{i}_{j}_{k}_{l}_{m}', f'FSA{i}_{j}_{k}_{l}')  # 反向连线PITFT到FSA
                                            if pitft_item in pitft_ary_dict.keys():
                                                for n, ary_item in enumerate(pitft_ary_dict[pitft_item]):
                                                    dot.node(f'ARY{i}_{j}_{k}_{l}_{m}_{n}', label=f'{ary_item}\nARRAY', shape=ary_shape)  # 添加注释
                                                    dot.edge(f'ARY{i}_{j}_{k}_{l}_{m}_{n}', f'PITFT{i}_{j}_{k}_{l}_{m}')  # 反向连线ARY到PITFT
    # 绘制图形
        # 将 Graphviz 图转换为字符串
    graphviz_source = dot.source
    # 在 Streamlit 应用中显示 Graphviz 图
    st.title("PID-Tree图片")
    st.graphviz_chart(graphviz_source)

# 数据库连接设置
def get_connection():
    conn_str = (
    "DRIVER={IBM DB2 ODBC DRIVER - DB2COPY1};"
    "DATABASE=FP2CPPT;"
    "HOSTNAME=10.6.151.84;"
    "PORT=50201;"  # 根据实际端口修改
    "PROTOCOL=TCPIP;"
    "UID=fp2cppta1;"
    "PWD=f2cppt400;"
    )
    return pyodbc.connect(conn_str)
def get_EDA():
    conn_str = (
    "DRIVER={IBM DB2 ODBC DRIVER - DB2COPY2};"
    "DATABASE=FP2GEDA;"
    "HOSTNAME=10.6.151.88;"
    "PORT=50401;"  # 根据实际端口修改
    "PROTOCOL=TCPIP;"
    "UID=fp2gedaa1;"
    "PWD=f2grpt4647;"
    )
    return pyodbc.connect(conn_str)
#st.image('C:/Users/52980/Desktop/22.png')
# 设置页面标题
#st.video('C:/Users/52980/Desktop/22.mp4')
st.title("数据库查询应用")
st.sidebar.title("INFORMATION")
col1,col2,col3 = st.columns(3)
#col1.image('C:/Users/52980/Desktop/2.png', width=300)
#col2.image('C:/Users/52980/Desktop/1.png', width=300)
#col3.image('C:/Users/52980/Desktop/3.png', width=300)
brm = st.sidebar.selectbox("CELL", ["Recipe", "PID-Tree", "MTRL"])
spc = st.sidebar.selectbox("SPC", ["SPC-Chart图-点值", "Char_资料", "Data_group资料","SPC-上线情况"])
tiaojian = {"array": "PID", "PID-Tree": "类别", "Code": "代码"}
if brm == "Recipe":
    coli1, coli2 = st.columns(2)
    name = coli1.text_input('输入PID查询对应Recipe',  max_chars=14, help='最大长度为14字符')
    ope=coli2.text_input('OPE-可不填',  max_chars=5, help='最大长度为100字符')
    if st.button('查询'):
        try:
            conn = get_connection()
            if name:
                if ope:
                    sql = '''
                            SELECT
                                TRIM (B.HEADER) ReleaseFlag   
                                , TRIM (B.PRODUCT_ID) Prod
                                , TRIM (B.EC_CODE) EC_CODE
                                , TRIM (B.ROUTE_ID) Route_ID
                                , TRIM (B.OPE_ID) OPER
                                , TRIM (B.OPE_VER) OPE_VER
                                , TRIM (B.EQPT_ID) EQPT_ID
                                , TRIM (B.RETICLE_SET_ID) Reticle
                                , TRIM (B.RECIPE_ID) PPID
                                , TRIM (B.ACTIVE_FLAG) ActiveFlag  
                                , TRIM(A.EQPT_ID) SUB_EQ
                                ,TRIM(A.RECIPE_ID) Recipe_id
                                ,A.RUN_FLG Run_Flag
                            FROM BRM.BBPARAM_RCP B FULL JOIN RMS.RMRCPTABLE A
                            ON (TRIM (B.EQPT_ID)||TRIM(B.RECIPE_ID)=TRIM(A.ROOT_EQPT_ID)||TRIM(A.PPID))
                            WHERE B.PRODUCT_ID like ?
                            and B.OPE_ID like ?
                            '''
                    df = pd.read_sql(sql, conn, params= ['%'+str(name)+'%', '%'+str(ope)+'%'])
                    st.dataframe(df)
                    conn.close()
                else:
                    sql = '''
                            SELECT
                                TRIM (B.HEADER) ReleaseFlag   
                                , TRIM (B.PRODUCT_ID) Prod
                                , TRIM (B.EC_CODE) EC_CODE
                                , TRIM (B.ROUTE_ID) Route_ID
                                , TRIM (B.OPE_ID) OPER
                                , TRIM (B.OPE_VER) OPE_VER
                                , TRIM (B.EQPT_ID) EQPT_ID
                                , TRIM (B.RETICLE_SET_ID) Reticle
                                , TRIM (B.RECIPE_ID) PPID
                                , TRIM (B.ACTIVE_FLAG) ActiveFlag  
                                , TRIM(A.EQPT_ID) SUB_EQ
                                ,TRIM(A.RECIPE_ID) Recipe_id
                                ,A.RUN_FLG Run_Flag
                            FROM BRM.BBPARAM_RCP B FULL JOIN RMS.RMRCPTABLE A
                            ON (TRIM (B.EQPT_ID)||TRIM(B.RECIPE_ID)=TRIM(A.ROOT_EQPT_ID)||TRIM(A.PPID))
                            WHERE B.PRODUCT_ID like ?
                            '''
                    df = pd.read_sql(sql, conn, params= '%'+str(name)+'%')
                    st.dataframe(df)
                    conn.close()
        except Exception as e:
            st.error(e)
            conn.close()
elif brm == "PID-Tree":
    pid = st.text_input('输入对应内容',  max_chars=100, help='最大长度为100字符')
    coli1, coli2, coli3,coli4 = st.columns(4)
    bt_pid = coli1.button('查询PID-Tree')
    bt_code = coli2.button('查询PID-Tree-by客户别')
    bt_all = coli3.button('查询全部PID-Tree')
    chart = coli4.checkbox('是否生成Chart图', value=False, key=None, help=None, on_change=None)

    if bt_pid:
            try:
                if pid:
                    conn = get_connection()
                    CONN_EDA = get_EDA()
                    sql_EDA = '''
                            SELECT FAB_SPFCD BOND_PROD,EXT_05 "客户别" FROM RPT.COMMON_TBL WHERE TABLENAME ='ProductID_Center'
                            '''
                    sql = '''
                            SELECT DISTINCT TRIM (C.CODE_EXT) BOND_PROD
                            , TRIM (C.SUBITEM) MODEL
                            , TRIM(C.EXT_2) XNMODEL
                            , TRIM (C.EXT_1) VER
                            , TRIM (M.MTRL_PRODUCT_ID) POL_PROD
                            , TRIM (ME.SUBITEM) POL_MODEL
                            , TRIM (D.CODE_EXT) CUT_PANEL_PROD
                            , TRIM (DE.SUBITEM) CUT_PANEL_PROD_MODEL
                            , TRIM (F.PRODUCT_ID) FSA_PROD
                            , TRIM (CB.CF_PRODUCT_ID) PICF_PROD
                            , TRIM (CB.PRODUCT_ID) PITFT_PROD
                            , TRIM (ARY.MTRL_PRODUCT_ID) ARY_PROD
                            , TRIM (CF.MTRL_PRODUCT_ID) CF_PROD
                        FROM BRM.BBCODE C
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD M ON (C.CODE_EXT = M.PRODUCT_ID AND M.MTRL_PRODUCT_ID LIKE 'C2%')
                        LEFT JOIN BRM.BBCODE ME ON (M.MTRL_PRODUCT_ID = ME.CODE_EXT AND ME.CODE_CATE = 'PDMN')        
                        LEFT JOIN BRM.BBCODE D ON (M.MTRL_PRODUCT_ID = D.SUBITEM AND D.CODE_CATE = 'PCRL' AND D.EXT_1 = 'C4000' )
                        LEFT JOIN BRM.BBCODE DE ON (D.CODE_EXT = DE.CODE_EXT AND DE.CODE_CATE = 'PDMN')
                        LEFT JOIN PPT.APRDCTCT F ON (F.AC_PRODUCT_ID = D.CODE_EXT)
                        LEFT JOIN PPT.APRDCTCM CB ON(F.PRODUCT_ID=CB.NEW_PRODUCT_ID)
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD ARY ON (CB.PRODUCT_ID = ARY.PRODUCT_ID AND ARY.MTRL_PRODUCT_ID LIKE 'AB%')
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD CF ON (CB.CF_PRODUCT_ID = CF.PRODUCT_ID AND CF.MTRL_PRODUCT_ID LIKE 'FB%')
                        WHERE C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND   C.CODE_EXT like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND   C.SUBITEM like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  C.EXT_2 like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  M.MTRL_PRODUCT_ID like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  D.CODE_EXT like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  DE.SUBITEM like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  F.PRODUCT_ID like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  CB.CF_PRODUCT_ID like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  CB.PRODUCT_ID like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  ARY.MTRL_PRODUCT_ID like ?
                        OR
                        C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                        AND  CF.MTRL_PRODUCT_ID like ? '''
                    df = pd.read_sql(sql, conn, params= ['%'+str(pid)+'%']*11)
                    df_EDA = pd.read_sql(sql_EDA, CONN_EDA)
                    new_df = pd.merge(df, df_EDA, on='BOND_PROD', how='left')
                    order =['BOND_PROD','客户别','MODEL','XNMODEL','VER','POL_PROD','POL_MODEL','CUT_PANEL_PROD','CUT_PANEL_PROD_MODEL','FSA_PROD','PICF_PROD','PITFT_PROD','ARY_PROD','CF_PROD']
                    new_df = new_df[order]
                    st.dataframe(new_df)
                    if chart:
                        draw_chart(df=new_df)
                    conn.close()
                    CONN_EDA.close()
                    
            except Exception as e:
                st.error(e)
                conn.close()
                CONN_EDA.close()
    elif bt_code:
        try:
            if pid:
                conn = get_connection()
                CONN_EDA = get_EDA()
                sql_EDA = '''
                    SELECT FAB_SPFCD BOND_PROD,EXT_05 "客户别" FROM RPT.COMMON_TBL WHERE TABLENAME ='ProductID_Center'
                    AND EXT_05 LIKE ?
                    '''
                sql = '''
                        SELECT DISTINCT TRIM (C.CODE_EXT) BOND_PROD
                        , TRIM (C.SUBITEM) MODEL
                        , TRIM(C.EXT_2) XNMODEL
                        , TRIM (C.EXT_1) VER
                        , TRIM (M.MTRL_PRODUCT_ID) POL_PROD
                        , TRIM (ME.SUBITEM) POL_MODEL
                        , TRIM (D.CODE_EXT) CUT_PANEL_PROD
                        , TRIM (DE.SUBITEM) CUT_PANEL_PROD_MODEL
                        , TRIM (F.PRODUCT_ID) FSA_PROD
                        , TRIM (CB.CF_PRODUCT_ID) PICF_PROD
                        , TRIM (CB.PRODUCT_ID) PITFT_PROD
                        , TRIM (ARY.MTRL_PRODUCT_ID) ARY_PROD
                        , TRIM (CF.MTRL_PRODUCT_ID) CF_PROD
                    FROM BRM.BBCODE C
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD M ON (C.CODE_EXT = M.PRODUCT_ID AND M.MTRL_PRODUCT_ID LIKE 'C2%')
                        LEFT JOIN BRM.BBCODE ME ON (M.MTRL_PRODUCT_ID = ME.CODE_EXT AND ME.CODE_CATE = 'PDMN')        
                        LEFT JOIN BRM.BBCODE D ON (M.MTRL_PRODUCT_ID = D.SUBITEM AND D.CODE_CATE = 'PCRL' AND D.EXT_1 = 'C4000' )
                        LEFT JOIN BRM.BBCODE DE ON (D.CODE_EXT = DE.CODE_EXT AND DE.CODE_CATE = 'PDMN')
                        LEFT JOIN PPT.APRDCTCT F ON (F.AC_PRODUCT_ID = D.CODE_EXT)
                        LEFT JOIN PPT.APRDCTCM CB ON(F.PRODUCT_ID=CB.NEW_PRODUCT_ID)
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD ARY ON (CB.PRODUCT_ID = ARY.PRODUCT_ID AND ARY.MTRL_PRODUCT_ID LIKE 'AB%')
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD CF ON (CB.CF_PRODUCT_ID = CF.PRODUCT_ID AND CF.MTRL_PRODUCT_ID LIKE 'FB%')
                    WHERE C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                    '''
                df = pd.read_sql(sql, conn)
                df_EDA = pd.read_sql(sql_EDA, CONN_EDA, params= ['%'+str(pid)+'%'])
                new_df = pd.merge(df_EDA, df, on='BOND_PROD', how='left')
                order =['BOND_PROD','客户别','MODEL','XNMODEL','VER','POL_PROD','POL_MODEL','CUT_PANEL_PROD','CUT_PANEL_PROD_MODEL','FSA_PROD','PICF_PROD','PITFT_PROD','ARY_PROD','CF_PROD']
                new_df = new_df[order]
                st.dataframe(df_EDA)
                st.dataframe(new_df)
                if chart:
                    draw_chart(df=new_df)
                conn.close()
                CONN_EDA.close()
        except Exception as e:
            st.error(e)
            conn.close()
            CONN_EDA.close()


    elif bt_all:
        try:
            conn = get_connection()
            CONN_EDA = get_EDA()
            sql_EDA = '''
                SELECT FAB_SPFCD BOND_PROD,EXT_05 "客户别" FROM RPT.COMMON_TBL WHERE TABLENAME ='ProductID_Center'
                '''
            sql = '''
                    SELECT DISTINCT TRIM (C.CODE_EXT) BOND_PROD
                    , TRIM (C.SUBITEM) MODEL
                    , TRIM(C.EXT_2) XNMODEL
                    , TRIM (C.EXT_1) VER
                    , TRIM (M.MTRL_PRODUCT_ID) POL_PROD
                    , TRIM (ME.SUBITEM) POL_MODEL
                    , TRIM (D.CODE_EXT) CUT_PANEL_PROD
                    , TRIM (DE.SUBITEM) CUT_PANEL_PROD_MODEL
                    , TRIM (F.PRODUCT_ID) FSA_PROD
                    , TRIM (CB.CF_PRODUCT_ID) PICF_PROD
                    , TRIM (CB.PRODUCT_ID) PITFT_PROD
                    , TRIM (ARY.MTRL_PRODUCT_ID) ARY_PROD
                    , TRIM (CF.MTRL_PRODUCT_ID) CF_PROD
                FROM BRM.BBCODE C
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD M ON (C.CODE_EXT = M.PRODUCT_ID AND M.MTRL_PRODUCT_ID LIKE 'C2%')
                        LEFT JOIN BRM.BBCODE ME ON (M.MTRL_PRODUCT_ID = ME.CODE_EXT AND ME.CODE_CATE = 'PDMN')        
                        LEFT JOIN BRM.BBCODE D ON (M.MTRL_PRODUCT_ID = D.SUBITEM AND D.CODE_CATE = 'PCRL' AND D.EXT_1 = 'C4000' )
                        LEFT JOIN BRM.BBCODE DE ON (D.CODE_EXT = DE.CODE_EXT AND DE.CODE_CATE = 'PDMN')
                        LEFT JOIN PPT.APRDCTCT F ON (F.AC_PRODUCT_ID = D.CODE_EXT)
                        LEFT JOIN PPT.APRDCTCM CB ON(F.PRODUCT_ID=CB.NEW_PRODUCT_ID)
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD ARY ON (CB.PRODUCT_ID = ARY.PRODUCT_ID AND ARY.MTRL_PRODUCT_ID LIKE 'AB%')
                        LEFT JOIN BRM.BBPRDCT_MTRLPRD CF ON (CB.CF_PRODUCT_ID = CF.PRODUCT_ID AND CF.MTRL_PRODUCT_ID LIKE 'FB%')
                WHERE C.CODE_CATE = 'PDMN' AND SUBSTR (C.CODE_EXT, 1, 2) IN ('CV', 'CN')
                '''
            df = pd.read_sql(sql, conn)
            df_EDA = pd.read_sql(sql_EDA, CONN_EDA)
            new_df = pd.merge(df, df_EDA, on='BOND_PROD', how='left')
            order =['BOND_PROD','客户别','MODEL','XNMODEL','VER','POL_PROD','POL_MODEL','CUT_PANEL_PROD','CUT_PANEL_PROD_MODEL','FSA_PROD','PICF_PROD','PITFT_PROD','ARY_PROD','CF_PROD']
            new_df = new_df[order]
            st.dataframe(df_EDA)
            st.dataframe(new_df)
            conn.close()
            CONN_EDA.close()
        except Exception as e:
            st.error(e)
            conn.close()
            CONN_EDA.close()

elif brm == "MTRL":
    mt = st.text_input('输入PID/物料',  max_chars=100, help='最大长度为100字符')
    if st.button('查询'):
        try:
            if mt:
                conn = get_connection()
                sql = '''
                        SELECT
                        A.MTRL_PRODUCT_CATE, A.MTRL_PRODUCT_ID,B.EXT_1 "最小包装数",B.EXT_2 "侧别", A.PRODUCT_CATE,A.PRODUCT_ID, A.OPE_ID
                        ,A.PRODUCT_TYPE 
                        FROM (
                        SELECT MTRL_PRODUCT_CATE, MTRL_PRODUCT_ID, PRODUCT_CATE,PRODUCT_ID, OPE_ID,
                            (CASE 
                                WHEN MTRL_PRODUCT_ID IN (SELECT MTRL_PRODUCT_ID FROM PPT.AMTRLPRODPEP_ATTR WHERE PRODUCT_ID = PPT.AMTRLPRODPEP_ENG.PRODUCT_ID) 
                                THEN '实验' 
                                ELSE '量产' 
                            END) AS PRODUCT_TYPE
                        FROM PPT.AMTRLPRODPEP_ENG 
                        ) A
                        LEFT JOIN 
                        (SELECT * FROM BRM.BBCODE
                        WHERE CODE_CATE = 'MTPT'
                        ) B
                        ON (A.MTRL_PRODUCT_ID = B.CODE_EXT)
                        WHERE product_id LIKE ?
                        OR mtrl_product_id LIKE ?
                        '''
                df = pd.read_sql(sql, conn, params= ['%'+str(mt)+'%']*2)
                st.dataframe(df)
                conn.close()
        except Exception as e:
            st.error(e)
            conn.close()
            

