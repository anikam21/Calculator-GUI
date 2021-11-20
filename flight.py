from tkinter import * 
import json 
import requests
import os 

url = requests.get('http://universities.hipolabs.com/search?country=United+Kingdom')
# root = Tk()

# frame1 = Frame(root)
# frame2 = Frame(root)
# root.title("University Info")

# Label(frame1, text = 'Search the name of University').pack(side=LEFT)
# modify = Entry(frame1)
# modify.pack(side=LEFT, fil=BOTH, expand=1)

# modify.focus_set()

# button = Button(frame1, text='Find')
# button.pack(side=RIGHT)
# frame1.pack(side=TOP)

# text = Text(root)
# text.insert('1.0', '''Enter here''') 
# text.pack(side=BOTTOM)

# def find(button):
#     text.tag_remove('found','1.0', END)
#     search = modify.get()
#     if search: 
#         index = '1.0'
#         while 1: 
#             index =text.search(search, index, nocase=1, stopindex=END)
#             if not index:
#                 break 
#             lastIndex = "%s+%dc" % (index, lastIndex)
#             text.tag_Add('found, index', lastIndex)
#             index = lastIndex 
#         text.tag_config('found', foreground='blue')
#     modify.focus_set()
# button.config(command=find)

# root.mainloop()

#json content 
json_data = url.json()
# json_formatted = json.dumps(json_data, indent=2)
data =  json.loads(json_data)
print(data['alpha_two_code'])
# print(json_formatted)

