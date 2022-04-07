from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange, HoverTool
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from pprint import pprint

output_file("bars.html")

LOCATIONS = ['CPC', 'OG2', 'HS82-83', 'IG6', 'IG4', 'IG10']
CHECKS = ['AID CHECKS', 'ITEMS SCREENED', 'PERSONS SCREENED']
palette = ["#c9d9d3", "#718dbf", "#e84d60"]
data = {'LOCATIONS': LOCATIONS,
        'AID CHECKS': [208, 622, 140, 1842, 127, 1304],
        'PERSONS SCREENED': [201, 484, 126, 1073, 81, 676],
        'ITEMS SCREENED': [28, 71, 31, 394, 32, 207]}

x = [(location, check) for location in LOCATIONS for check in CHECKS]

counts = sum(zip(data['AID CHECKS'], data['PERSONS SCREENED'], data['ITEMS SCREENED']), ())  # like an hstack
pprint(counts)

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=600, plot_width=2000, title="NPS Locations by Security Checks",
           tools="pan,wheel_zoom,box_zoom,reset, save")

p.xaxis.axis_label_text_font_size = "5pt"
p.xaxis.axis_label_text_font_style = 'bold'

p.vbar(x='x', top='counts', width=0.9, source=source,
       fill_color=factor_cmap('x', palette=palette, factors=CHECKS, start=0, end=2))
# fill_color=factor_cmap('x', palette=palette, factors=years, start=1, end=2)
p.add_tools(HoverTool(tooltips=[("LOCATION", "@x"), ("TOTAL", "@counts")]))

p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

show(p)
