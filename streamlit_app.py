import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Amazing Athleisure Catalog')


my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# run a snowflake query and put it all in a var called my_catalog
my_cur.execute("select distinct color_or_style, price, direct_url, image_last_modified from catalog")
my_catalog = my_cur.fetchall()

# put the data into a dataframe
df = pandas.DataFrame(my_catalog)
#ss_price = df.loc['price']
streamlit.write(df)

# put the first column into a list
color_list = df[0].values.tolist()
# print(color_list)

# Let's put a pick list here so they can pick the color 
option = 'orange'
option = streamlit.selectbox('Pick a sweatsuit color or style:', list(color_list))

#streamlit.write('You selected:', option)

# trying to drive the image from data table
my_cur.execute("select direct_url, price, image_last_modified from catalog where color_or_style = '" + option + "';")
image_url = my_cur.fetchone()[0]
product_desc = 'Our warm, comfortable, ' + option + ' sweatsuit!' #my_cur.fetchone()[1]


# streamlit.write(image_url)

streamlit.image(
            image_url,
            width=400,
            caption= product_desc
        )





