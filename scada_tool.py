#coding=utf-8

import trans_qual
import trans_long
import db_trans
import wx

#id转换
def get_id(event):
    result = input_box.GetValue()
    str = ''
    try:
        str = trans_long.key_to_id(result)
    except:
        str = '输入KEY错误\ntable column record\ntable area column record\nid'
    
    output_box.SetValue(str.decode('utf-8', 'ignore'))
    
#遥测质量码
def get_yc_qual(event):
    result = input_box.GetValue()   
    str = ''
    try:
        str = trans_qual.trans_yc_qual(int(result))
    except:
        str = '输入状态错误 \n[0,3221225472]'

    output_box.SetValue(str.decode('utf-8', 'ignore'))

#遥信质量码
def get_yx_qual(event):
    result = input_box.GetValue()   
    str = ''
    try:
        str = trans_qual.trans_yx_qual(int(result))
    except:
        str = '输入状态错误 \n[0,3221225472]'
    
    output_box.SetValue(str.decode('utf-8', 'ignore'))
    
#表号查询    
def get_table_info(event):
    result = input_box.GetValue().encode('utf-8', 'ignore')
    str=''
    str = db_trans.trans_table(result)
    if(str==''):
        str='输入中文表名或表号'
    
    output_box.SetValue(str.decode('utf-8', 'ignore'))

        
#主函数        
app=wx.App()
win=wx.Frame(None,title='scada tool',size=(700,500))
bkg=wx.Panel(win)

#输入输出框
input_box = wx.TextCtrl(bkg)
output_box = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL |wx.VSCROLL)

#按钮
id_btn=wx.Button(bkg,label='ID转换'.decode('utf-8', 'ignore'))
id_btn.Bind(wx.EVT_BUTTON,get_id)

db_btn=wx.Button(bkg,label='表号查询'.decode('utf-8', 'ignore'))
db_btn.Bind(wx.EVT_BUTTON,get_table_info)

yc_btn=wx.Button(bkg,label='遥测质量码'.decode('utf-8', 'ignore'))
yc_btn.Bind(wx.EVT_BUTTON,get_yc_qual)

yx_btn=wx.Button(bkg,label='遥信质量码'.decode('utf-8', 'ignore'))
yx_btn.Bind(wx.EVT_BUTTON,get_yx_qual)



#布局
input_vbox=wx.BoxSizer(wx.VERTICAL)
input_vbox.Add(input_box,proportion=1,flag=wx.EXPAND)

btn_vbox1=wx.BoxSizer(wx.VERTICAL)
btn_vbox1.Add(yc_btn,proportion=1)
btn_vbox1.Add(yx_btn,proportion=1)

btn_vbox2=wx.BoxSizer(wx.VERTICAL)
btn_vbox2.Add(id_btn,proportion=1)
btn_vbox2.Add(db_btn,proportion=1)

hbox1 = wx.BoxSizer()
hbox1.Add(input_vbox,proportion=1,flag=wx.EXPAND)
hbox1.Add(btn_vbox1,proportion=0,flag=wx.LEFT,border=5)
hbox1.Add(btn_vbox2,proportion=0,flag=wx.LEFT,border=5)

hbox2 = wx.BoxSizer()
hbox2.Add(output_box,proportion=2,flag=wx.EXPAND)

vbox=wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox1,proportion=0,flag=wx.EXPAND|wx.ALL,border=5)
vbox.Add(hbox2,proportion=1,flag=wx.EXPAND|wx.LEFT|wx.BOTTOM|wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()