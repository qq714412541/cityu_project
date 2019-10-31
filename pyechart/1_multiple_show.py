from pyecharts.charts import Bar,Line,Gauge,Page
from pyecharts import options as opts

#######warning
def gauge_color(x) -> Gauge:

    c1 = (
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
            title_opts=opts.TitleOpts(title="警告：预计下周香港出现高峰自杀行为的概率"),
            legend_opts=opts.LegendOpts(is_show=False),
        )
    )

    #c.render('warning.html')
    return c1

a = gauge_color(45)

#######comparation
y = [11, 21, 14, 15, 13, 10, 19, 13, 13, 15, 18]
y_pred  = [14.86719396958091, 13.510266072720729, 12.709436780114725, 19.120341825456464, 17.565343810061957, 11.068799731987731, 18.290293753851763, 10.144566306698927, 8.728851702925777, 17.62287816655381, 11.199669748997099]

leng = len(y)
x = []
for i in range(1,leng+1):
    #print(i)
    string = str(i) + '周'
    #print(string)

    x = x + [string]

def line_smooth(x,y,y_pred) -> Line:
    c = (
        Line()
        .add_xaxis(x)
        .add_yaxis("预测", y_pred, is_smooth=True)
        .add_yaxis("实际", y, is_smooth=True)
        .set_global_opts(title_opts=opts.TitleOpts(title="预测与实际比较"))
    )
    #c.render('comparation.html')
    return c

b = line_smooth(x,y,y_pred)


#####prediction
y = [14.86719396958091, 13.510266072720729, 12.709436780114725, 19.120341825456464, 17.565343810061957, 11.068799731987731, 18.290293753851763, 10.144566306698927, 8.728851702925777, 17.62287816655381, 11.199669748997099]
x = [ '1周', '2周', '3周', '4周', '5周', '6周', '7周', '8周', '9周', '10周','11周']

def bar_datazoom_slider(x,y) -> Bar:
    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis('预测自杀人数', y)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="自杀人数调研/Hong Kong"),
            datazoom_opts=opts.DataZoomOpts(),

        )
    )


    return c

c = bar_datazoom_slider(x,y)


#####indeed

y_indeed = [11, 21, 14, 15, 13, 10, 19, 13, 13, 15, 18, 8, 22, 19, 20, 21, 22, 22, 29, 27, 27, 19, 18, 15, 13, 18, 23, 19, 16, 20, 19, 14, 8, 12, 19, 16, 18, 15, 8, 21, 19, 16, 19, 27, 17, 11, 18, 20, 15, 14, 25, 16]
leng = len(y_indeed)
x_indeed = []
for i in range(1,leng+1):
    #print(i)
    string = str(i) + '周'
    #print(string)

    x_indeed = x_indeed + [string]
print(x_indeed)

def bar_datazoom_slider(x,y) -> Bar:
    c = (
        Bar()
        .add_xaxis(x)
        .add_yaxis('实际自杀人数', y)
        .set_global_opts(
            title_opts=opts.TitleOpts(title="自杀人数调研/Hong Kong"),
            datazoom_opts=opts.DataZoomOpts(),

        )
    )
    return c

d = bar_datazoom_slider(x_indeed,y_indeed)

page = Page(layout=Page.SimplePageLayout)
page.add(a,b,c,d)
page.render('multiple_test.html')