from pprint import pprint
from math import pi
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange, HoverTool
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.palettes import viridis


def plot_by_bokeh(data: dict):
    colors = viridis(2)
    output_file("bars.html")
    PERIODS = [f"Period {i + 1}" for i, item in enumerate(data[list(data.keys())[0]])]
    data["PERIODS"] = PERIODS
    EVENTS = list(data.keys())
    EVENTS.remove("PERIODS")
    palette = list(colors)

    x = [(period, event) for period in PERIODS for event in EVENTS]
    counts_dict = dict([(k, v) for k, v in data.items() if k != "PERIODS"])

    counts = tuple(sub_ele for ele in zip(*counts_dict.values()) for sub_ele in ele)
    source = ColumnDataSource(data=dict(x=x, counts=counts))

    p = figure(
        x_range=FactorRange(*x),
        plot_height=800,
        plot_width=1920,
        title="TEST",
        tools="pan,wheel_zoom,box_zoom,reset, save",
    )
    p.xaxis.axis_label_text_font_size = "3pt"

    p.vbar(
        x="x",
        top="counts",
        width=0.5,
        source=source,
        fill_color=factor_cmap("x", palette=palette, factors=EVENTS, start=1, end=22),
    )
    p.add_tools(HoverTool(tooltips=[("PERIOD", "@x"), ("SEC", "@counts")]))
    p.y_range.start = 0
    p.x_range.range_padding = 0
    p.xaxis.major_label_orientation = pi / 2
    p.xgrid.grid_line_color = None

    show(p)


if __name__ == "__main__":
    data = {
        "EVT_TFU_RA_REQUEST_INDICATION": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
            0.017306153846153846,
        ],
        "EVT_TFU_CRC_INDICATION": [
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0.0015209000000000002,
            0.0015613076923076924,
            0.0015601999999999999,
            0.001557246153846154,
            0.0015510307692307693,
            0.0015499615384615385,
            0.001548323076923077,
            0.0015480769230769233,
            0.0015480692307692308,
            0.0015457538461538462,
            0.001544,
            0.0015427846153846152,
            0.0015413692307692309,
            0.0015412923076923077,
            0.0015414384615384615,
        ],
    }

    plot_by_bokeh(data)
