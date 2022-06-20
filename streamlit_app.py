import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# put your sql query here
my_cur.execute("select color_or_style from sweatsuits;")
my_catalog = my_cur.fetchall()
streamlit.dataframe(my_catalog)


# Let's put a pick list here so they can pick the color 
streamlit.multiselect("Pick a color:", list(my_catalog))

# Display the table on the page.




streamlit.image(
            'https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png',
            width=400,
            caption="Buy this wonderful product"
        )





