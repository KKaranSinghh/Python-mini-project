# Terminal -> cd Dashboard -> Enter
# streamlit run Home.py -> Enter

import streamlit as st
import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Load the dataset
df= pd.read_csv('Housing_Price_Data.csv')

#st.title('Housing Price Dataset Analysis')
st.markdown("<h1 style='color: black; font-weight: bold; background-color: lightpink; border: 2px solid black; text-align: center; padding: 10px;'>Housing Price Dataset Analysis</h1>",unsafe_allow_html=True)

#display dataset
st.dataframe(df)

# Header title
st.sidebar.header('Filter')

# side Logo
st.sidebar.image('Assets\Black Gold Elegant Simple Real Estate Logo (1) (1).jpg')



# Filter functions


# Price filter
min_price, max_price= st.sidebar.slider('Price',
                                        min_value= int(df['price'].min()),
                                        max_value= int(df['price'].max()),
                                        value= (int(df['price'].min()), int(df['price'].max())))

# Area filter
min_sqft_living, max_sqft_living= st.sidebar.slider('Area',
                                                    min_value= int(df['area'].min()),
                                                    max_value= int(df['area'].max()),
                                                    value= (int(df['area'].min()), int(df['area'].max())))
# Airconditioning filter
Aircondition= st.sidebar.multiselect('Airconditioning',
                                     options= df['airconditioning'].unique(),
                                     default= df['airconditioning'].unique())

# Mainroad filter
Mainroad= st.sidebar.multiselect('Mainroad',
                                     options= df['mainroad'].unique(),
                                     default= df['mainroad'].unique())

# Furnishing status filter
Furnishing= st.sidebar.multiselect('Furnishing status',
                                     options= df['furnishingstatus'].unique(),
                                     default= df['furnishingstatus'].unique())



# Filter the data based on user selection
filtered_df= df[
    (df['price']>=min_price)&
    (df['price']<=max_price)&
    (df['area']>=min_sqft_living)&
    (df['area']<=max_sqft_living)&
    (df['airconditioning'].isin(Aircondition))&
    (df['mainroad'].isin(Mainroad))&
    (df['furnishingstatus'].isin(Furnishing))
]
st.dataframe(filtered_df)



# Create Graphs


# pie chart Distribution of Furnishingstatus between houses 

st.markdown('# **Distribution of Furnishing status between houses**')

fig = plt.figure(figsize= (8, 6))
df['furnishingstatus'].value_counts().plot(kind='pie', autopct='%1.1f%%', colors=['skyblue', 'lightblue', 'pink'])  ###
plt.title('Distribution of furnishing status of houses')
st.pyplot(fig)

st.markdown('The pie chart titled "Distribution of Furnishing Status between Houses" provides a visual representation of the furnishing status of houses within a specific market. The chart is divided into three categories: semi-furnished, unfurnished, and furnished.')
st.markdown('* Semi-Furnished Houses (41.7%) :- The majority of the houses fall into this category, indicating that a significant portion of homeowners or landlords provide some basic furnishings. This trend could be driven by a demand for partially furnished homes that offer convenience without the commitment or cost associated with fully furnished properties.')
st.markdown('* Unfurnished Houses (32.7%) :- The second largest segment consists of unfurnished houses, reflecting a notable demand for completely bare homes. This may be appealing to individuals who prefer to customize their living spaces according to personal tastes and requirements, or to those who already possess the necessary furnishings.')
st.markdown('* Furnished Houses (25.7%) :- This segment represents the fully furnished homes, which cater to renters or buyers seeking a move-in ready option. Such properties are often favored by professionals on temporary assignments, expatriates, or those looking for a hassle-free living solution.')
st.markdown('# **Conclusion**')
st.markdown('Understanding the distribution of furnishing statuses in the housing market is crucial for various stakeholders, including real estate agents, property developers, and prospective buyers or renters. The data presented in the chart can aid in decision-making, market analysis, and the development of targeted marketing strategies.')





# Box plot for price distribution by number of bedrooms

st.markdown('# **Price distribution by number of bedrooms**')

fig= plt.figure(figsize=(10, 6))
sns.boxplot(x='bedrooms', y='price', data= df)
plt.title('Price Distribution by Number of Bedrooms')
plt.xlabel('Number of Bedrooms')
plt.ylabel('Price')
st.pyplot(fig)

st.markdown('The box plot titled "Price distribution by number of bedrooms" provides a comprehensive visual representation of the house prices across different bedroom configurations. The y-axis denotes the price (in units of 1e7), while the x-axis represents the number of bedrooms, ranging from 1 to 6.')
st.markdown('* Bedroom Houses :- Prices for 1-bedroom houses are relatively concentrated, ranging from approximately 0.2 to 0.3.')
st.markdown('* Bedroom Houses :- The price distribution broadens for 2-bedroom houses, with prices spanning from around 0.2 to 0.6, with notable outliers above 0.6.')
st.markdown('* Bedroom Houses :- For 3-bedroom houses, prices further expand, ranging between 0.2 to 0.8, and several outliers exceeding 0.8.')
st.markdown('* Bedroom Houses :- Similar to 3-bedroom houses, 4-bedroom houses have prices ranging from approximately 0.3 to 0.8, with a few outliers above this range.')
st.markdown('* Bedroom Houses :- The price distribution is widest for 5-bedroom houses, spanning from about 0.3 to 1.0, with multiple outliers surpassing 1.0.')
st.markdown('* Bedroom Houses :- For 6-bedroom houses, prices narrow down again, ranging from approximately 0.3 to 0.6.')
st.markdown('# **Conclusion**')
st.markdown('The box plot reveals that the number of bedrooms significantly influences house prices, with greater variability observed as the number of bedrooms increases. This analysis is crucial for potential buyers and sellers, real estate agents, and market analysts. It provides clear insights into how house prices fluctuate based on the number of bedrooms, assisting in making informed real estate decisions.')





# Relationship between area and house price

st.markdown('# **Relationship between area and house price**')

fig = plt.figure(figsize= (10, 6))
plt.scatter(df['area'], df['price'], color= 'lightblue', edgecolors= 'black') ###
plt.title('Relationship between area and house price')
plt.xlabel('Area')
plt.ylabel('House price')
st.pyplot(fig)

st.markdown('The scatter plot "Relationship between Area and House Price" provides a visual representation of how the area of a house influences its market value.')
st.markdown('# **Key Observations:**')
st.markdown('* Positive Correlation :- The graph shows a general trend where an increase in the area tends to correspond to an increase in house prices. This positive correlation is crucial for both buyers and sellers in the real estate market.')
st.markdown('* Variability in Data :- Despite the overall upward trend, there is significant variability in the data points. This suggests that while larger areas typically result in higher prices, other factors such as location, house condition, and market conditions also play significant roles.')
st.markdown('* High-Value Outliers :- Some houses with larger areas show exceptionally high prices, possibly indicating premium properties or luxury estates that command higher market values.')
st.markdown('# **Conclusion:**')
st.markdown('Understanding the relationship between house area and price is essential for making informed decisions in real estate. Buyers can use this information to gauge potential investment values, while sellers can better price their properties. Real estate agents and market analysts can also leverage this data to provide more accurate property evaluations and market forecasts.')






# Plot the bar chart on Average house price based on main road access

st.markdown('# **Average house price based on main road access**')

# Group the data by mainroad
grouped= df.groupby('mainroad')['price']

fig, ax = plt.subplots()
grouped.plot(kind='bar', color=['lightblue', 'red'], ax=ax)
ax.set_title('Average house price based on main road access')
ax.set_xlabel('Main road access')
ax.set_ylabel('Average house price')
ax.set_xticks([0, 1])
ax.set_xticklabels(['No', 'Yes'], rotation=0)
st.pyplot(fig)

st.markdown('The bar graph titled "Average House Price Based on Main Road Access" provides a visual comparison of the average house prices with respect to their proximity to main roads.')
st.markdown('# **Key Observations:**')
st.markdown('* Higher Prices for Accessible Houses :- The bar for houses with main road access indicates significantly higher average prices compared to those without. This trend underscores the premium placed on properties that offer better accessibility and convenience.')
st.markdown('* Main Road Access Advantage :- Homes with main road access are likely more attractive to buyers due to easier commutes, better connectivity, and proximity to essential services and amenities.')
st.markdown('* Impact on Investment Decisions :- For real estate investors, this data highlights the importance of location and accessibility in determining property value. Investing in properties with main road access can potentially yield higher returns due to their market desirability.')
st.markdown('# **Conclusion**')
st.markdown('The bar graph clearly illustrates the financial impact of main road access on house prices. Properties with main road access command higher prices, reflecting the value buyers place on accessibility and convenience. This information is vital for real estate agents, investors, and homebuyers as they make informed decisions regarding property purchases and investments.')






# Bar Graph of Average house price by hot water heating and air conditioning

st.markdown('# **Average house price by hot water heating and air conditioning**')

# Group by hotwaterheating and airconditioning and calculate the average price
grouped_data= df.groupby(['hotwaterheating','airconditioning'])['price'].mean()

# Create a bar chart

fig, ax = plt.subplots(figsize=(10, 6))
grouped_data.unstack().plot(kind='bar', color=['skyblue', 'pink'], ax=ax)
ax.set_title('Average house price by hot water heating and air conditioning')
ax.set_xlabel('Hot water heating / Air conditioning')
ax.set_ylabel('Average price')
ax.legend(title='Air conditioning', labels=['No', 'Yes'])
plt.xticks(rotation=0)
st.pyplot(fig)

st.markdown('The bar chart "Average house price by hot water heating and air conditioning" provides a visual representation of the average house prices in relation to the presence of hot water heating and air conditioning systems.')
st.markdown('# **Key Observations:**')
st.markdown(' **Houses Without Hot Water Heating:**')
st.markdown('* With Air Conditioning :- These houses have a significantly higher average price, around 6 million, compared to those without air conditioning.')
st.markdown('* Without Air Conditioning :- The average price is lower, around 4 million, indicating that the presence of air conditioning adds considerable value.')
st.markdown(' **Houses With Hot Water Heating:**')
st.markdown('* With Air Conditioning :- Surprisingly, these houses have a lower average price, around 3 million, suggesting that while air conditioning is generally valued, it might not always complement houses with hot water heating.')
st.markdown('* Without Air Conditioning :- These houses have a higher average price, around 5 million, which could indicate that buyers might prioritize hot water heating over air conditioning in certain markets.')
st.markdown('# **Conclusion:**')
st.markdown('The chart provides valuable insights into how different heating and cooling features affect house prices. While air conditioning significantly increases the average price of houses without hot water heating, its presence in houses with hot water heating seems to reduce the average price. This information is essential for real estate agents, property developers, and potential buyers to understand market trends and make informed decisions.')






# Avg price of the house based on the number of rooms

st.markdown('# **Number of rooms and average price of house**')

# new column of Total rooms
df['Total rooms']= df['bedrooms'] + df['bathrooms']
avg_price= df.groupby("Total rooms") ['price'].mean()

fig, ax= plt.subplots() 
avg_price.plot(kind= 'bar', color= ['lightblue'],ax=ax)
ax.set_title('Number of rooms and average price of house')
ax.set_xlabel('Total rooms')
ax.set_ylabel('Average price of the house')
st.pyplot(fig)

st.markdown('The bar graph titled "Number of rooms and average price of house" illustrates the correlation between the total number of rooms in a house and its average price. This visual representation helps in understanding how the size of a house, in terms of the number of rooms, affects its market value.')
st.markdown('# **Key Observations:**')
st.markdown('* 2 Rooms :- Houses with 2 rooms have an average price of approximately 2 million. These houses are generally more affordable and may appeal to small families or individuals.')
st.markdown('* 3 Rooms :- The average price increases to around 3 million for houses with 3 rooms, indicating a higher value for slightly larger homes.')
st.markdown('* 4 Rooms :- With 4 rooms, the average price reaches about 4 million, showing a consistent trend of increasing prices with more rooms.')
st.markdown('* 5 Rooms :- There is a noticeable jump to an average price of 6 million for 5-room houses, reflecting the higher market demand and value for larger properties.')
st.markdown('* 6 Rooms :- Houses with 6 rooms have an average price of approximately 7 million, continuing the upward trend.')
st.markdown('* 7 Rooms :- Interestingly, the average price slightly drops to around 6.5 million for 7-room houses, which could indicate market variability or other influencing factors.')
st.markdown('* 8 Rooms :- The highest average price, about 8 million, is seen for houses with 8 rooms, indicating that the largest homes command the highest prices.')
st.markdown('# **Conclusion**')
st.markdown('The bar graph clearly demonstrates that the average price of a house generally increases with the number of rooms. This information is valuable for buyers, sellers, and real estate agents to understand market trends and make informed decisions. Larger houses with more rooms tend to have higher market values, making them more desirable for buyers looking for spacious living spaces.')





# Correlation matrix Heatmap

st.markdown('# **Correlation matrix heatmap**')

# New column of total numbers of rooms in house
df['Total rooms']= df['bedrooms'] + df['bathrooms']
df

# Correlation
correlation= df[['price', 'area', 'Total rooms', 'stories', 'parking']].corr()
correlation

fig= plt.figure(figsize=(10,8))
sns.heatmap(correlation, annot= True, cmap= 'coolwarm', fmt= '.2f')
plt.title('Correlation Matrix Heatmap')
st.pyplot(fig)

st.markdown('The heatmap titled "Correlation Matrix" visually represents the relationships between various features of real estate properties, such as price, area, total rooms, stories, and parking. Each cell in the matrix indicates the correlation coefficient between the variables, ranging from -1 to 1, with red showing strong positive correlations and blue representing weaker or negative correlations.')
st.markdown('# **Key Observations:**')
st.markdown(' **Price:**')
st.markdown('* Moderate positive correlation with area (0.54) :- This suggests that larger properties tend to have higher prices.')
st.markdown('* Moderate positive correlation with total rooms (0.51) :- More rooms in a house often contribute to a higher market value.')
st.markdown('* Moderate positive correlation with stories (0.42) :- Houses with more stories are typically priced higher.')
st.markdown('* Weak positive correlation with parking (0.38) :- Availability of parking space slightly boosts the property value.')
st.markdown(' **Area:**')
st.markdown('* Moderate positive correlation with price (0.54) :- Larger properties are generally more expensive.')
st.markdown('* Weak positive correlation with total rooms (0.20) and parking (0.35) :- Larger areas often accommodate more rooms and parking facilities.')
st.markdown(' **Total Rooms:**')
st.markdown('* Moderate positive correlation with price (0.51) :- A higher number of rooms can increase the propertys price.')
st.markdown('* Moderate positive correlation with stories (0.45) :- Houses with more stories tend to have more rooms.')
st.markdown('* Weak positive correlation with area (0.20) and parking (0.19) :- More rooms are often found in larger properties with parking spaces.')
st.markdown(' **Stories:**')
st.markdown('* Moderate positive correlation with total rooms (0.45) and price (0.42) :- Houses with multiple stories generally have more rooms and higher prices.')
st.markdown('* Very weak correlation with area (0.08) and parking (0.05) :- The number of stories has a minimal impact on property area and parking.')
st.markdown(' **Parking:**')
st.markdown('* Weak positive correlations with all other variables :- Availability of parking has slight positive effects on all other aspects, particularly with price (0.38) and area (0.35).')
st.markdown('# **Conclusion:**')
st.markdown('Understanding these correlations is crucial for real estate stakeholders. It helps in making informed decisions regarding property valuation, investment, and development. The heatmap provides valuable insights into how different features are interrelated, aiding in strategic planning and market analysis.')





# line chart ( Average price by furnishing status)

st.markdown('# **Average price by furnishing status**')

fig= plt.figure(figsize= (10,6))
sns.lineplot(x='furnishingstatus', y= 'price',
             data=df,
             marker='o',
             markersize= 10,
             color= 'red',
             linewidth= 2)
plt.title('Average price by furniture status')
plt.xlabel('Furniture status', fontsize= 14)
plt.ylabel('Average price', fontsize= 14)
plt.xticks(fontsize= 12)
plt.yticks(fontsize= 12)
plt.grid(axis='y', linestyle= '--', alpha= 0.7)
st.pyplot(fig)

st.markdown('The line graph titled "Average Price by Furnishing Status" provides a visual representation of the average prices of properties based on their furnishing status. The x-axis categorizes the properties as "furnished," "semi-furnished," and "unfurnished," while the y-axis shows the average price in millions.')
st.markdown('# **Key Observations:**')
st.markdown('* Furnished Properties :- The average price for furnished properties is the highest, around 5.5 million. This reflects the added value and convenience of move-in-ready homes, which are often more appealing to buyers who prefer minimal setup time.')
st.markdown('* Semi-Furnished Properties :- These properties have an average price of approximately 5.0 million. They offer a balance between cost and convenience, providing some essential furnishings while allowing for personalization.')
st.markdown('* Unfurnished Properties :- The average price drops to around 4.0 million for unfurnished properties. This category appeals to buyers looking to customize their living spaces completely and who may already own the necessary furnishings.')
st.markdown('# **Conclusion:**')
st.markdown('The graph clearly indicates that furnishing status significantly impacts property prices. Furnished homes command the highest prices due to their ready-to-live status, while unfurnished homes, being the least expensive, offer opportunities for customization. This information is valuable for real estate professionals, buyers, and sellers to understand market trends and make informed decisions based on the furnishing status of properties.')





# Relation between mainroad, parking and basement

st.markdown('# **Relation between mainroad, parking and basement**')

fig= sns.catplot(data=df, kind="violin", x="mainroad", y="parking",hue= 'basement', split=True)
st.pyplot(fig)

st.markdown('The violin plot titled "Relation between mainroad, parking, and basement" provides an insightful visual representation of how parking availability varies based on whether a property is located on a main road and the presence of a basement. The plot helps in understanding the density and distribution of parking availability under these different conditions.')
st.markdown('# **Key Observations:**')
st.markdown(' **Main Road Presence:**')
st.markdown('* Properties on a main road (labeled "yes" on the x-axis) show varied parking availability. The width of the violin plot at different y-values indicates the density of properties with that specific parking availability.')
st.markdown('* For properties without a basement (blue color), the distribution is broad, suggesting a wide range of parking availability.')
st.markdown('* For properties with a basement (orange color), the distribution is slightly narrower, indicating more consistent parking availability levels.')
st.markdown(' **Off the Main Road:**')
st.markdown('* Properties not on a main road (labeled "no" on the x-axis) display a different pattern.')
st.markdown('* For properties without a basement (blue color), the distribution is similar to those on a main road, but with a slight shift in density, suggesting different factors influencing parking availability.')
st.markdown('* For properties with a basement (orange color), the distribution is more concentrated, implying a tendency toward specific parking availability levels.')
st.markdown(' **Basement Presence:**')
st.markdown('* The presence of a basement (orange color) appears to influence parking availability, as seen in both on and off main road categories.')
st.markdown('* The box plot within each violin provides additional insights into the median, quartiles, and potential outliers, highlighting how basement presence affects parking.')
st.markdown('# **Conclusion**')
st.markdown('This violin plot effectively illustrates the relationship between main road presence, parking availability, and the presence of a basement. Such visualizations are crucial for urban planners, real estate developers, and property buyers, offering a deeper understanding of how these factors interact and influence parking availability.')





# Relation between basement and price of house

st.markdown('# **house price distribution by basement availability**')

fig, ax= plt.subplots()
sns.boxenplot(data= df, x='basement', y= 'price',color='pink', width_method= 'linear', ax=ax)
ax.set_title('House price Distribution by basement availability')
st.pyplot(fig)

st.markdown('The provided plot visually compares house prices based on the presence or absence of a basement. The y-axis represents the house prices, ranging from approximately 0.2 million to 1.2 million, while the x-axis distinguishes between houses with basements ("yes") and without basements ("no"). Each mirrored bar indicates the distribution of house prices within specific price ranges, with wider bars signifying a higher frequency of houses.')
st.markdown('# **Key Observations:**')
st.markdown(' **Houses Without Basements:**')
st.markdown('* The distribution shows a broader spread of house prices, with the majority falling between 0.3 million and 0.6 million.')
st.markdown('* There are fewer outliers, indicating that house prices are relatively consistent within this category.')
st.markdown('* The data suggests that a significant portion of the market consists of houses without basements priced within this range.')
st.markdown(' **Houses With Basements:**')
st.markdown('* The price distribution is more concentrated, particularly between 0.4 million and 0.7 million.')
st.markdown('* There are more outliers in this category, with some houses priced above 1.0 million, indicating a higher variability and potential for higher-value properties.')
st.markdown('* This concentration suggests that basements are a desirable feature that can lead to higher property values.')
st.markdown('# **Conclusion:**')
st.markdown('The comparative plot reveals that the presence of a basement generally correlates with higher house prices and a greater variability in price distribution. This information is valuable for prospective buyers, sellers, and real estate professionals, as it highlights the impact of basement availability on property value. Homes with basements are often priced higher and may offer a more significant return on investment.')
