import pandas as pd
from pyecharts.charts import Bar, Line, Gauge, Page
from pyecharts import options as opts
import time
from pandas import DataFrame
class MyGraph:
    def myg(self):
        df = pd.read_csv('../file/All2.csv')
        mycount = df['week_count'].to_list()[:-1]
        pre_date = df['week_date'].to_list()
        pre_count = df['pre'].to_list()
        mydate = df['week_date'].to_list()[:-1]
        suicide1_list = df['sui1'].to_list()[:-1]
        suicide2_list = df['sui2'].to_list()[:-1]
        suicide3_list = df['sui3'].to_list()[:-1]
        pos = df['pos'].to_list()[:-1]
        neg = df['neg'].to_list()[:-1]
        x = pre_count[-1]/(max(mycount)-min(mycount)) * 98



        start = (1 - 30 / len(mycount)) * 100

        b = (
            Gauge()
                .add(
                "",
                [("Peak probability", round(x,0))],
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(
                        color=[(0.3, "#67e0e3"), (0.7, "#37a2da"), (1, "#fd666d")], width=30
                    )
                ),
            )
                .set_global_opts(
                title_opts=opts.TitleOpts(title="Warning! The probability of peak suicide next week In HongKong:"),
                legend_opts=opts.LegendOpts(is_show=False),
            )
        )



        c = (
            Line()
                .add_xaxis(pre_date)

                .add_yaxis("Weekly Suicide(Prediction)", pre_count, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False), )
                .add_yaxis("Weekly Suicide(Reality)", mycount, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False), )

                .set_global_opts(title_opts=opts.TitleOpts(title="Weekly Suicide In HongKong"),
                                 # tooltip_opts=opts.TooltipOpts(is_show=False),

                                 # legend_opts=opts.LegendOpts(textstyle_opts={"fontSize": 20}),
                                 # graphic_textstyle_opts = opts.GraphicTextStyleOpts(font='2em "STHeiti", sans-serif'),
                                 datazoom_opts=opts.DataZoomOpts(range_start=start, range_end=100))
            # .set_global_opts()

            # .render("China_1_Daily_C_vs_P.html")
        )

        d = (
            Line()
                .add_xaxis(mydate)
                .add_yaxis("(suicide)", suicide1_list, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False), )
                .add_yaxis("(自杀)", suicide2_list, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False), )
                .add_yaxis("(自殺)", suicide3_list, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False), )

                .set_global_opts(title_opts=opts.TitleOpts(title="Weekly Google Trends In HongKong"),
                                 # tooltip_opts=opts.TooltipOpts(is_show=False),

                                 # legend_opts=opts.LegendOpts(textstyle_opts={"fontSize": 20}),
                                 # graphic_textstyle_opts = opts.GraphicTextStyleOpts(font='2em "STHeiti", sans-serif'),
                                 datazoom_opts=opts.DataZoomOpts(range_start=start, range_end=100))
            # .set_global_opts()

            # .render("China_1_Daily_C_vs_P.html")
        )

        e = (
            Line()
                .add_xaxis(mydate)
                .add_yaxis("Positive", pos, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False), )
                .add_yaxis("Negative", neg, is_symbol_show=True,
                           label_opts=opts.LabelOpts(is_show=False), )

                .set_global_opts(title_opts=opts.TitleOpts(title="Weekly Media Effect In HongKong"),
                                 # tooltip_opts=opts.TooltipOpts(is_show=False),

                                 # legend_opts=opts.LegendOpts(textstyle_opts={"fontSize": 20}),
                                 # graphic_textstyle_opts = opts.GraphicTextStyleOpts(font='2em "STHeiti", sans-serif'),
                                 datazoom_opts=opts.DataZoomOpts(range_start=start, range_end=100))
            # .set_global_opts()

            # .render("China_1_Daily_C_vs_P.html")
        )
        page = Page(layout=Page.SimplePageLayout)
        page.add(b,c, d, e)
        path = str(time.time())+'result.html'

        df3 = pd.read_csv('../file/All2.csv')
        df3['path'].iloc[-1]=path
        df3.to_csv('../file/All2.csv',index = None)


        res = '../route/static/templates/'+path
        page.render(res)
        return path


su = MyGraph()
su.myg()