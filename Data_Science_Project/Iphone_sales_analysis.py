# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# import plotly.io as pio

# pio.renderers.default = 'browser'  # 👈 Add this line

# df = pd.read_csv('apple_products.csv')

# high_rating = df.sort_values(by=['Star Rating'], ascending=False)
# high_rating = high_rating.head(10)

# figure = px.bar(
#     high_rating,
#     y='Number Of Ratings',
#     x='Product Name',
#     title='Number of Ratings for Top 10 iPhones by Star Rating',
#     orientation='h'
# )
# figure.show()


import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.renderers.default = 'browser'

pio.renderers.default = 'browser'
df = pd.read_csv('apple_products.csv')
# print(df.head())
# print(df.describe())
print(df.isnull().sum())

#data sorting
# high_rating = df.sort_values(by=['Star Rating'], ascending=False)
# high_rating = high_rating.head(10)
# iphone = high_rating['Product Name'].value_counts()
# label = iphone.index
# count = high_rating['Number Of Ratings']
# figure = px.bar(high_rating ,x=label,y=count, title='Number of the Rating of Iphone')
# figure.show()

#Scatter Plot
# figure =px.scatter(data_frame=df, x = 'Number Of Ratings', y = 'Sale Price',
#                    size='Discount Percentage',trendline='ols',title="Highest Sales number of rating")
# figure.show()

figure =px.scatter(data_frame=df, x = 'Number Of Ratings', y = 'Discount Percentage',
                   size='Sale Price',trendline='ols',title="Relation Ship between Number of Rating and Discount Percentage")
figure.show()