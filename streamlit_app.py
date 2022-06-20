import streamlit
import snowflake.connector
import pandas

streamlit.title('Zena\'s Athleisure Catalog')

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()

# put your sql query here
my_cur.execute("select top 5 * from sweatsuits;")
my_catalog = my_cur.fetchall()



#streamlit.text(my_data_row)
streamlit.dataframe(my_catalog)


streamlit.image(
            'https://uni-klaus.s3.us-west-2.amazonaws.com/clothing/orange_sweatsuit.png',
            width=400,
            caption="Buy this wonderful product"
        )

DataFrame.to_html(buf=None
                  , columns=None
                  , col_space=None
                  , header=True
                  , index=True
                  , na_rep='NaN'
                  , formatters=None
                  , float_format=None
                  , sparsify=None
                  , index_names=True
                  , justify=None
                  , max_rows=None
                  , max_cols=None
                  , show_dimensions=False
                  , decimal='.'
                  , bold_rows=True
                  , classes=None
                  , escape=True
                  , notebook=False
                  , border=None
                  , table_id=None
                  , render_links=False
                  , encoding=None)



