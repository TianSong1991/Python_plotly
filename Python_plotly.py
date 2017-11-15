import plotly 
plotly.tools.set_credentials_file(username='templarz', api_key='PtKMjV9gAzINZqmQRU4T')

import plotly.offline as pltoff
'''
绘制普通线图
'''
#数据，x为横坐标，y,z为纵坐标的两项指标，三个array长度相同
dataset = {'x':[1,2,3,4,5,6,7,8,9,10,11,12],
           'y':[0.05,0.04,0.01,0.03,0.011,0.02,0.06,0.07,0.019,0.020,0.025,0.08],
           'z':[0.012,0.09,0.02,0.06,0.03,0.025,0.08,0.017,0.022,0.05,0.06,0.07]}
data_g = []
#分别插入 y, z
tr_x = go.Scatter(
    x = dataset['x'],
    y = dataset['y'],
    name = '兴业回收率' 
)
data_g.append(tr_x)
tr_z = go.Scatter(
    x = dataset['x'],
    y = dataset['z'],
    name = '广发回收率' 
)
data_g.append(tr_z)
#设置layout,指定图表title,x轴和y轴名称
layout = go.Layout(title="客户月回收率统计", xaxis={'title':'x'}, yaxis={'title':'value'})
#将layout设置到图表
fig = go.Figure(data=data_g, layout=layout)
#绘图,输出路径为name参数指定
pltoff.plot(fig)


'''
绘制柱状图
'''
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as pltoff
dataset = {'x':['Windows', 'Linux', 'Unix', 'MacOS'],
           'y1':[45, 26, 37, 13],
           'y2':[19, 27, 33, 21]}
data_g = []
tr_y1 = go.Bar(
    x = dataset['x'],
    y = dataset['y1'],
    name = 'v1'
)
data_g.append(tr_y1)


tr_y2 = go.Bar(
    x = dataset['x'],
    y = dataset['y2'],
    name = 'v2'
)
data_g.append(tr_y2)
layout = go.Layout(title="bar charts", xaxis={'title':'x'}, yaxis={'title':'value'})
fig = go.Figure(data=data_g, layout=layout)
pltoff.plot(fig)



'''
绘制堆叠填充的线图
'''
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import plotly.offline as pltoff
dataset = {'x':[1,2,3,4,5,6,7,8,9,10,11,12],
           'y1':[5,4,1,3,11,2,6,7,19,20,22,12],
           'y2':[12,9,0,0,3,25,8,17,22,5,5,9],
           'y3':[13,22,46,1,15,4,18,11,17,20,23,18]}


#计算y1,y2,y3的堆叠占比
dataset['y1_stack'] = dataset['y1']
dataset['y2_stack'] = [y1+y2 for y1, y2 in zip(dataset['y1'], dataset['y2'])]
dataset['y3_stack'] = [y1+y2+y3 for y1, y2, y3 in zip(dataset['y1'], dataset['y2'], dataset['y3'])]


dataset['y1_text'] = ['%s(%s%%)'%(y1, y1*100/y3_s) for y1, y3_s in zip(dataset['y1'], dataset['y3_stack'])]
dataset['y2_text'] = ['%s(%s%%)'%(y2, y2*100/y3_s) for y2, y3_s in zip(dataset['y2'], dataset['y3_stack'])]
dataset['y3_text'] = ['%s(%s%%)'%(y3, y3*100/y3_s) for y3, y3_s in zip(dataset['y3'], dataset['y3_stack'])]


data_g = []
tr_1 = go.Scatter(
    x = dataset['x'],
    y = dataset['y1_stack'],
    text = dataset['y1_text'],
    hoverinfo = 'x+text',
    mode = 'lines',
    name = 'y1', 
    fill = 'tozeroy' #填充方式: 到x轴
)
data_g.append(tr_1)


tr_2 = go.Scatter(
    x = dataset['x'],
    y = dataset['y2_stack'],
    text = dataset['y2_text'],
    hoverinfo = 'x+text',
    mode = 'lines',
    name = 'y2', 
    fill = 'tonexty' #填充方式:到下方的另一条线
)
data_g.append(tr_2)


tr_3 = go.Scatter(
    x = dataset['x'],
    y = dataset['y3_stack'],
    text = dataset['y3_text'],
    hoverinfo = 'x+text',
    mode = 'lines',
    name = 'y3',
    fill = 'tonexty'
)
data_g.append(tr_3)


layout = go.Layout(title="field area plots", xaxis={'title':'x'}, yaxis={'title':'value'})
fig = go.Figure(data=data_g, layout=layout)
pltoff.plot(fig)


'''
绘制散点图
'''
import plotly.plotly as py
import plotly.graph_objs as go
import plotly
import plotly.offline as pltoff
dataset = {'x':[0,1,2,3,4,5,6,7,8,9],
           'y':[5,4,1,3,11,2,6,7,19,20],
           'text':['5_txt','4_txt','1_txt','3_txt','11_txt','2_txt','6_txt','7_txt','19_txt','20_txt']}


data_g = []


tr_x = go.Scatter(
    x = dataset['x'],
    y = dataset['y'],
    text = dataset['text'],
    textposition='top center',
    mode='markers+text',
    name = 'y' 
)
data_g.append(tr_x)


layout = go.Layout(title="scatter plots", xaxis={'title':'x'}, yaxis={'title':'value'})
fig = go.Figure(data=data_g, layout=layout)
pltoff.plot(fig)