import streamlit
import snowflake.connector

streamlit.title('Zena\'s Athleisure Catalog')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# put your sql query here
my_cur.execute("select top 1 direct_url from catalog;")
my_data_row = my_cur.fetchone()

streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

streamlit.image(
            'https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png',
            width=400,
            caption="Buy this wonderful product"
        )





