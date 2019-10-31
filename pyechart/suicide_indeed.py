


y = [11, 21, 14, 15, 13, 10, 19, 13, 13, 15, 18, 8, 22, 19, 20, 21, 22, 22, 29, 27, 27, 19, 18, 15, 13, 18, 23, 19, 16, 20, 19, 14, 8, 12, 19, 16, 18, 15, 8, 21, 19, 16, 19, 27, 17, 11, 18, 20, 15, 14, 25, 16]
leng = len(y)
x = []
for i in range(1,leng+1):
    #print(i)
    string = str(i) + '周'
    #print(string)

    x = x + [string]
print(x)
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker

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
    print(Faker.days_attrs)
    print(Faker.days_values)
    print(type(Faker.days_attrs),len(Faker.days_values))
    c.render('suicide_indeed.html')
    return c

bar_datazoom_slider(x,y)