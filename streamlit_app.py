import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Athleisure Catalog')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# put your sql query here
my_cur.execute("select top 5 * from catalog;")
my_catalog = my_cur.fetchall()
#my_data_row = my_cur.fetchone()


#streamlit.text(my_data_row)
streamlit.dataframe(my_catalog)


streamlit.image(
            'https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png',
            width=400,
            caption="Buy this wonderful product"
        )





