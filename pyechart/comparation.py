from pyecharts.charts import Bar,Line
from pyecharts import options as opts
from pyecharts.faker import Faker

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
    c.render('comparation.html')
    return c



line_smooth(x,y,y_pred)