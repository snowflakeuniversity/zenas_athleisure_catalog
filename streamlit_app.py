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

# Using Series.values.tolist()
color_list = dataframe[0].values.tolist()
print(color_list)

# Using Series.values.tolist()
#col_list = df["Courses"].values.tolist()
#print(col_list)



# Let's put a pick list here so they can pick the color 
streamlit.multiselect("Pick a color:", list(color_list))

# Display the table on the page.




streamlit.image(
            'https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png',
            width=400,
            caption="Buy this wonderful product"
        )





