import os
import numpy as np
import pandas as pd

from argparse import ArgumentParser
from pprint import pprint
from tokenize import String
from typing import List, Dict
from utils.get_all_event import condition_option, get_all_events
from math import pi
from bokeh.io import show, output_file
from bokeh.models import ColumnDataSource, FactorRange, HoverTool
from bokeh.plotting import figure
from bokeh.transform import factor_cmap
from bokeh.palettes import viridis
from utils.convert_cycles_to_seconds import cpu_processing_time
from utils.color_dict import gen_color_dict


FREQ = 1.3 * 1000
COLUMN_DICT = {"MIN_CYCLES": 2, "MAX_CYCLES": 3, "AVG_CYCLES": 4, "NUM_TIMES": 6}


def readProfileFile(fileName: String):
    with open(fileName, "r", encoding="utf-8") as fp:
        lines = fp.readlines()
    return lines


def genTaskDict(event_names: List):
    return dict([(event_name, list()) for event_name in event_names])


def statsEvent(
    event_list: List, record_list: List, event_dict: Dict, column_name: String
):
    execution_times_dict = dict([(k, 0) for k, v in event_dict.items()])
    index = COLUMN_DICT.get(column_name)
    temp_event_list = list()
    for event in record_list:
        if event == "##########":
            for element in event_list:
                if element not in temp_event_list:
                    event_dict[element].append(0)
            temp_event_list = list()
        else:
            # index 對應項目
            # index = 2 -> MIN_CYCLES
            # index = 3 -> MAX_CYCLES
            # index = 4 -> AVG_CYCLES
            # index = 6 -> NUM TIMES
            temp_event_list.append(event[1])
            if index != 6:
                event_dict[event[1]].append(
                    cpu_processing_time(float(event[index]), FREQ)
                )
            else:
                event_dict[event[1]].append(
                    int(event[index]) - execution_times_dict[event[1]]
                )
                execution_times_dict[event[1]] = int(event[index])
    return event_dict


def save_path(column_name: String):
    save_root_dir = "analysis_result_"
    if column_name == "NUM_TIMES":
        save_root_dir += "for_execution_times"
    else:
        save_root_dir = f"{column_name.lower()}"

    if not os.path.isdir(save_root_dir):
        os.mkdir(save_root_dir)
    return save_root_dir


def plot_bar(
    data: Dict,
    color_dict: Dict,
    fileName: String,
    option: String,
    column_name_option: String,
):
    # print(fileName)
    def gen_chart_title(file_name: String, option: String):
        file_name_list = file_name.split("/")
        file_name = file_name_list[-1]
        cup_core, ue_per_tti, ue_nums = file_name.replace(".txt", "").split("-")[0:3]

        if "queue" in option:
            if "nrt" in option:
                return f"Non Real Time Task   |   In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}"
            else:
                return f"Real Time Task   |   In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}"
        else:
            if "nrt" in option:
                return f"Non Real Time Task   |   Not In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}"
            else:
                return f"Real Time Task   |   Not In Queue   |   CPU核心數: {cup_core}   |   UE/TTI: {ue_per_tti}   |   UE個數: {ue_nums}"

    title = gen_chart_title(file_name=fileName, option=option)

    colors = viridis(len(data[list(data.keys())[0]]))
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
        title=title,
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
    # UE_NUMS, POOL_NUMS, UR_PER_TTI
    # --------------------------------------- 參數設置 ---------------------------------------
    parser = ArgumentParser()
    parser.add_argument(
        "--option",
        default="queue_profile_info_ss_rt_task",
        help="Search Task Profile Info Content or Queue Profile Info",
    )
    parser.add_argument("--f", default="20220324/2-4-32.txt", help="file name")
    parser.add_argument(
        "--column_name",
        default="AVG_CYCLES",
        help="MIN_CYCLES, MAX_CYCLES, AVG_CYCLES, NUM_TIMES",
    )
    args = parser.parse_args()

    file_name = args.f
    option = args.option
    column_name = args.column_name

    # --------------------------------------- 分析log ---------------------------------------
    condition_list = condition_option(option)
    record_list, event_list = get_all_events(file_name, condition_list)
    event_dict = genTaskDict(event_list)
    event_dict = statsEvent(event_list, record_list, event_dict, column_name)
    # pprint(event_dict)

    # --------------------------------------- 畫圖表 ---------------------------------------
    color_dict = gen_color_dict()
    plot_bar(event_dict, color_dict, file_name, option, column_name)

    # --------------------------------------- 儲存圖表 ---------------------------------------
