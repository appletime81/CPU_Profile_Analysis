import altair as alt
from vega_datasets import data

source = data.barley()
print(source)

alt.Chart(source).mark_bar().encode(
    x='year:O',
    y='sum(yield):Q',
    color='year:N',
    column='site:N'
)