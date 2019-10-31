from pyecharts.charts import Bar,Line,Gauge
from pyecharts import options as opts


def gauge_color(x) -> Gauge:
    c = (
        Gauge()
        .add(
            "",
            [("高峰概率", x)],
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(
                    color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                )
            ),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(title="警告：预计下周香港出现自杀高峰现象概率"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )
    c.render('warning.html')
    return c

gauge_color(45)