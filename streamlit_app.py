# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Custom Smoothe Order :cup_with_straw:")
st.write("""Orders that need to filled.""")



session = get_active_session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
editable_df = st.experimental_data_editor(my_dataframe)



# Import python packages
import streamlit as st
from snowflake.snowpark.context import get_active_session
from snowflake.snowpark.functions import col

# Write directly to the app
st.title(":cup_with_straw: Custom Smoothe Order :cup_with_straw:")
st.write("""Orders that need to filled.""")



session = get_active_session()
my_dataframe = session.table("smoothies.public.orders").filter(col("ORDER_FILLED")==0).collect()
editable_df = st.experimental_data_editor(my_dataframe)


submitted = st.button('submit')

if submitted:
    st.success("Somwone clicked the button", icon = "👍")









