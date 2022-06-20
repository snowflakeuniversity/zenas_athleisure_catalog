import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# put your sql query here
my_cur.execute("select color_or_style, direct_url, price from sweatsuits;")
my_catalog = my_cur.fetchall()



#streamlit.text(my_data_row)
streamlit.dataframe(my_catalog)


streamlit.image(
            'https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png',
            width=400,
            caption="Buy this wonderful product"
        )





