import pandas as pd 


##https://plotly.com/python/line-charts/
import plotly.express as px 


data = pd.read_csv('videos_export.csv')
data['uploaded_at'] = pd.to_datetime(data['uploaded_at'])


#Calculate aggregation by codec 

plot_df = []

for codec in data['codec'].unique():
    temp = data[data.codec == codec]
    temp = temp.groupby(['uploaded_at']).count()

    temp = pd.DataFrame({"Date":temp.index, "Codec": codec, "Count" : temp.codec})
    temp = pd.concat([temp, totals], axis=1)
    temp['Count_Percentage'] = 100*temp.Count/temp.Total_Counts
    temp['Aggregation'] = temp.Count.cumsum()
    temp['Aggregation_Percentage'] = 100*temp.Aggregation/temp.Total_Aggregation

    plot_df.append(temp)

# Turn list back into one dataframe

plot_df = pd.concat(plot_df)
plot_df = plot_df.sort_values(by=['Date'])

# Original plot just by counts

temp = plot_df.dropna(subset=['Aggregation_Percentage'])

fig = px.line(temp, x = "Date", y = "Aggregation_Percentage", color='Codec')
fig.show()

#https://plotly.com/python/static-image-export/ might need this
#https://github.com/plotly/orca
#https://github.com/plotly/orca/releases

fig.write_image("counts.png")

