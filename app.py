import streamlit as st
import duckdb


con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

#solution = duckdb.sql(answer).df()

with st.sidebar:
    theme = st.selectbox(
        "What would you like to review?",
        ("cross_joins","GroupBy", "windows Functions"),
        index=None,
        placeholder="Select a theme...",

    )
    st.write('You selected:', theme)

    exercise = con.execute(f"SELECT * FROM memory_state WHERE theme = '{theme}'").df()
    st.write(exercise)

st.header("enter your code:")
query = st.text_area(label="votre code sql ici", key="user_input")
# if query:
#     result = duckdb.sql(query).df()
#     st.dataframe(result)
#
# tab2, tab3 = st.tabs(["Tables", "Solution"])
#
# with tab2:
#     st.write("table: beverages")
#     st.dataframe(beverages)
#     st.write("table: food_items")
#     st.dataframe(food_items)
#     st.write("expected:")
#     st.dataframe(solution)
#
# with tab3:
#     st.write(answer)