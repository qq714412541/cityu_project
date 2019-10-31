from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.faker import Faker
from pandas import Timestamp

y = [14.86719396958091, 13.510266072720729, 12.709436780114725, 19.120341825456464, 17.565343810061957, 11.068799731987731, 18.290293753851763, 10.144566306698927, 8.728851702925777, 17.62287816655381, 11.199669748997099]
x = [ '1周', '2周', '3周', '4周', '5周', '6周', '7周', '8周', '9周', '10周','11周']
x_new = [Timestamp('2005-01-02 00:00:00'), Timestamp('2005-01-09 00:00:00'), Timestamp('2005-01-16 00:00:00'), Timestamp('2005-01-23 00:00:00'), Timestamp('2005-01-30 00:00:00'), Timestamp('2005-02-06 00:00:00'), Timestamp('2005-02-13 00:00:00'), Timestamp('2005-02-20 00:00:00')]
#y_detail = ['week_1','week_2','week_3','week_4','week_5','week_6','week_6','week_8','week_9','week_10','week_11']
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
    print(Faker.days_attrs)
    print(Faker.days_values)
    print(type(Faker.days_attrs),len(Faker.days_values))
    c.render('suicide_predict.html')
    return c

bar_datazoom_slider(x,y)