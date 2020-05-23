import pyecharts.options as opts
from pyecharts.charts import Pie

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://echarts.baidu.com/examples/editor.html?c=pie-nest

目前无法实现的功能:

1、暂无
"""

inner_x_data = ["CryptoMarket", "ShareMarket", "Fund","cash"]
inner_y_data = [129587.51, 19158.40, 6913.08,68694.0]
inner_data_pair = [list(z) for z in zip(inner_x_data, inner_y_data)]

outer_x_data = ["Okex", "Huobi-account1", "Huobi-account2", "Huobi-account3", "Binance","OKB","创业板","信息技术","券商ETF","建信500","中证环保","中证红利","中证传媒","中证500","全指金融","恒生指数","cash"]
outer_y_data = [12116.34, 25697.99, 26827.78, 25788.1, 35161.34,3998.89,7493.6,6848.8,4816.00,1702.37,887.11,1089.51,490.84,398.53, 593.99, 597.69,68694.0]
outer_data_pair = [list(z) for z in zip(outer_x_data, outer_y_data)]

(
    Pie(init_opts=opts.InitOpts(width="1600px", height="800px"))
    .add(
        series_name="访问来源",
        data_pair=inner_data_pair,
        radius=[0, "30%"],
        label_opts=opts.LabelOpts(position="inner"),
    )
    .add(
        series_name="访问来源",
        radius=["40%", "55%"],
        data_pair=outer_data_pair,
        label_opts=opts.LabelOpts(
            position="outside",
            formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
            background_color="#eee",
            border_color="#aaa",
            border_width=1,
            border_radius=4,
            rich={
                "a": {"color": "#999", "lineHeight": 22, "align": "center"},
                "abg": {
                    "backgroundColor": "#e3e3e3",
                    "width": "100%",
                    "align": "right",
                    "height": 22,
                    "borderRadius": [4, 4, 0, 0],
                },
                "hr": {
                    "borderColor": "#aaa",
                    "width": "100%",
                    "borderWidth": 0.5,
                    "height": 0,
                },
                "b": {"fontSize": 16, "lineHeight": 33},
                "per": {
                    "color": "#eee",
                    "backgroundColor": "#334455",
                    "padding": [2, 4],
                    "borderRadius": 2,
                },
            },
        ),
    )
    .set_global_opts(legend_opts=opts.LegendOpts(pos_left="left", orient="vertical"))
    .set_series_opts(
        tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
        )
    )
    .render("nested_pies.html")
)
