import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select color_or_style, direct_url from sweatsuits;")
my_catalog = my_cur.fetchall()

# put the data into a dataframe
df = pandas.DataFrame(my_catalog)

# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)

# Let's put a pick list here so they can pick the color 
option = 'orange'
option = streamlit.selectbox('Pick a sweatsuit color:', list(color_list))

streamlit.write('You selected:', option)

# trying to drive the image from data table
my_cur.execute("select direct_url from sweatsuits where color_or_style = 'Pink';")
image_url = my_cur.fetchone()[0]
streamlit.write(image_url)

streamlit.image(
            image_url,
            width=400,
            caption="Buy this wonderful product"
        )





