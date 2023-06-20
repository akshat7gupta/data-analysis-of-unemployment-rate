import pandas as pandu
from matplotlib import pyplot as plt
import turtle
from turtle import Turtle,Screen
import tkinter as tk
from tkinter import *
from sys import argv
from datetime import datetime

#Screen 2nd
def forward1():
    global root1
    root.destroy()
    root1 = tk.Tk()
    root1.geometry("1200x720")
    root1.resizable(width=False, height=False)
    root1.title("Data Analysis--India's Unemployement")
    photo1 = PhotoImage(file="picnew.png")                      #Background image
    panel = tk.Label(root1, image=photo1)
    panel.pack(side="bottom", fill="both", expand="yes")
    label = tk.Label(root1, bg="white")
    sliding_effect3_label(label)                                #call of Sliding effect function
    label1 = tk.Label(root1, bg="white")
    sliding_effect2_label(label1)
    label2 = tk.Button(root1, bg="white",command=forward2)      #Shift to screen 3rd
    sliding_effect1_label(label2)                               #call of Sliding effect function
    root1.mainloop()

#screen 3rd
def forward2():
    global root1
    global root2
    global root3
    try:
        root1.destroy()                                         # if called from 2nd window
    except:
        root3.destroy()                                         # if called from 4th window
    root2 = tk.Tk()
    root2.geometry("1200x720")
    root2.resizable(width=False, height=False)
    root2.title("Data Analysis--India's Unemployement")
    photo = tk.PhotoImage(file="pic_facts.png")                 #Background image
    panel1 = tk.Label(root2, compound= CENTER, image=photo , font=('arial', 20, 'bold'), bd=4,bg="white", fg="white")
    sliding_effect4_label(panel1)                               #call of Sliding effect function
    Button = tk.Button(root2,text="Next",font=('Cooper Black', 20, 'italic'), bg="gray60",fg="black",bd=20,command=forward3)
    Button.place(relx=0.85, rely=0.82, anchor=CENTER)            #Shift to screen 4th
    root2.mainloop()

#screen 4th
def forward3():
    global root2
    global root3
    global root4
    try:
        root2.destroy()                                         # if called from 3rd window
    except:
        root4.destroy()                                         # if called from 5th window
    root3 = tk.Tk()
    root3.geometry("1200x720")
    root3.resizable(width=False, height=False)
    root3.title("Data Analysis--India's Unemployement")
    photo2 = tk.PhotoImage(file="pic_screen.png")               #Background image
    panel = tk.Label(root3, compound= CENTER, image=photo2 )
    panel.pack(side="bottom", fill="both", expand="yes")
    b3 = tk.Button(root3, bg="white" ,command=forward4)         #quick access commands
    sliding_effect6_label(b3)                                   #call of Sliding effect functions
    b4 = tk.Button(root3, bg="white" ,command=forward5)
    sliding_effect7_label(b4)
    b5 = tk.Button(root3, bg="white",command=forward6)
    sliding_effect8_label(b5)
    b6 = tk.Button(root3, bg="white",command=forward7)
    sliding_effect9_label(b6)
    b7 = tk.Label(root3, bg="white")
    sliding_effect10_label(b7)
    b8 = tk.Label(root3, bg="white")
    sliding_effect11_label(b8)
    B9 = tk.Button(root3, text=u"Next \u27A4", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60", fg="black",
                   bd=10, command=forward4)                     #Shift to screen 5th
    B9.place(relx=0.94, rely=0.82, anchor=CENTER)
    B10 = tk.Button(root3, text=u"\u00AB Previous", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60",
                    fg="black", bd=10, command=forward2)
    B10.place(relx=0.82, rely=0.82, anchor=CENTER)              #Shift to screen 3rd
    root3.mainloop()

#screen 5th
def forward4():
    global root3
    global root4
    global root5
    try:
        root3.destroy()                                         # if called from 4th window
    except:
        root5.destroy()                                         # if called from 6th window
    root4 = tk.Tk()
    root4.geometry("1200x720")
    root4.resizable(width=False, height=False)
    root4.title("Data Analysis--India's Unemployement")
    data = pandu.read_csv(r'Excel_data1.csv')
    df = pandu.DataFrame(data, columns=['Date:-', ' Unemployment Rate ', 'Annual change'])      #Slicing of columns
    df = df.set_index('Date:-')
    photo = tk.PhotoImage(file="pic_screen.PNG")                #Background image
    panel1 = tk.Label(root4, compound=CENTER, image=photo, bg="white", fg="black")
    panel1.pack(side="bottom", fill="both", expand="yes")
    l1 = tk.Label(root4, text=df, font=('Segoe UI Black', 10, 'italic'), bg="deep sky blue", fg="black",borderwidth = 8,width = 40,relief="sunken")
    l1.place(relx=0.169, rely=0.5, anchor=CENTER)
    photo5 = tk.PhotoImage(file="g7.png")                       #graph button image
    panel2 = tk.Button(root4, image=photo5, bg="white", fg="white", bd=10, command=graph_7)
    panel2.place(relx=0.84, rely=0.25, anchor=CENTER)
    photo6 = tk.PhotoImage(file="g8.png")                       #graph button image
    panel3 = tk.Button(root4, image=photo6, bg="white", fg="white", bd=10, command=graph_8)
    panel3.place(relx=0.84, rely=0.55, anchor=CENTER)
    t1 = "So,here we have a dataset of overall" \
         "\nunemployment rate of India and their " \
         "\ncorresponding graphs depicting " \
         "\nunemployment and the annual changes too" \
         "\n\nNow we can see that there is drastic change" \
         "\n between year 2019 and 2020" \
         "\n just because of the pandemic \"Covid-19\""         #analysation of the graphs
    t2 = "\u21C7Dataset  \t  Graphs\u21C9"
    panel8 = tk.Label(root4, text=t1, bg="white", fg="black", font=('Segoe UI Black', 14, 'italic'))
    panel8.place(relx=0.53, rely=0.4, anchor=CENTER)
    panel9 = tk.Label(root4, text=t2, bg="white", fg="black", font=('Segoe UI Black', 18, 'bold', 'italic'))
    panel9.place(relx=0.53, rely=0.65, anchor=CENTER)
    b1 = tk.Button(root4, text=u"Next \u27A4", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60", fg="black",
                   bd=10,command=forward5)
    b1.place(relx=0.94, rely=0.82, anchor=CENTER)               #Shift to screen 6th
    b2 = tk.Button(root4, text=u"\u00AB Previous", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60",
                    fg="black", bd=10,command=forward3)
    b2.place(relx=0.82, rely=0.82, anchor=CENTER)               #Shift to screen 4th
    root4.mainloop()

#screen 6th
def forward5():
    global root5
    global root4
    global root3
    global root6
    try:
        root3.destroy()                                         # if called from 4th window
    except:
        pass
    try:
        root4.destroy()                                         # if called from 5th window
    except:
        pass
    try:
        root6.destroy()                                         # if called from 7th window
    except:
        pass
    root5 = tk.Tk()
    root5.geometry("1200x720")
    root5.resizable(width=False, height=False)
    root5.title("Data Analysis--India's Unemployement")
    data = pandu.read_csv(r'Excel_data1.csv')
    df = pandu.DataFrame(data, columns=['Date:-', 'Youth Unemployment Rate ', 'Annual Change'])     #Slicing of columns
    df = df.set_index('Date:-')
    photo = tk.PhotoImage(file="pic_screen.PNG")                #Background image
    panel1 = tk.Label(root5, compound=CENTER, image=photo, bg="white", fg="black")
    panel1.pack(side="bottom", fill="both", expand="yes")
    l1 = tk.Label(root5, text=df, font=('Segoe UI Black', 9, 'italic'), bg="deep sky blue", fg="black",borderwidth = 8,width = 40,relief="sunken")
    l1.place(relx=0.165, rely=0.48, anchor=CENTER)
    photo5 = tk.PhotoImage(file="g5.png")                       #graph button image
    panel2 = tk.Button(root5, image=photo5, bg="white", fg="white", bd=10, command=graph_5)
    panel2.place(relx=0.84, rely=0.25, anchor=CENTER)
    photo6 = tk.PhotoImage(file="g6.png")                       #graph button image
    panel3 = tk.Button(root5, image=photo6, bg="white", fg="white", bd=10, command=graph_6)
    panel3.place(relx=0.84, rely=0.55, anchor=CENTER)
    t1 = "So,now we come to a dataset of Youth" \
         "\nunemployment rate of India which effects" \
         "\n India's unemployment directly " \
         "\n\nNow we can again see that there is also a " \
         "\n drastic change between year 2019 and 2020" \
         "\n just because of the pandemic \"Covid-19\"" \
         "\nDue to this most of youth lost their jobs and " \
         "\nIndia felt a huge loss..!!"                         #analysation of the graphs
    t2 = "\u21C7Dataset  \t  Graphs\u21C9"
    panel8 = tk.Label(root5, text=t1, bg="white", fg="black", font=('Segoe UI Black', 14, 'italic'))
    panel8.place(relx=0.53, rely=0.4, anchor=CENTER)
    panel9 = tk.Label(root5, text=t2, bg="white", fg="black", font=('Segoe UI Black', 18, 'bold', 'italic'))
    panel9.place(relx=0.53, rely=0.6, anchor=CENTER)
    B9 = tk.Button(root5, text=u"Next \u27A4", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60", fg="black",
                   bd=10,command=forward6)
    B9.place(relx=0.94, rely=0.82, anchor=CENTER)                #Shift to 7th window
    B10 = tk.Button(root5, text=u"\u00AB Previous", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60",
                    fg="black", bd=10,command=forward4)
    B10.place(relx=0.82, rely=0.82, anchor=CENTER)               #Shift to 5th window
    root5.mainloop()

#screen 7th
def forward6():
    global root5
    global root6
    global root3
    global root7
    try:
        root3.destroy()                                         # if called from 4th window
    except:
        pass
    try:
        root5.destroy()                                         # if called from 6th window
    except:
        pass
    try:
        root7.destroy()                                         # if called from 8th window
    except:
        pass
    root6 = tk.Tk()
    root6.geometry("1200x720")
    root6.resizable(width=False, height=False)
    root6.title("Data Analysis--India's Unemployement")
    data = pandu.read_csv(r'Excel_data1.csv')
    df = pandu.DataFrame(data, columns=['Date:', ' Literacy Rate', ' Annual Change(%)'])        #Slicing of columns
    df = df.set_index('Date:')
    photo = tk.PhotoImage(file="pic_screen.PNG")                #Background image
    panel1 = tk.Label(root6, compound=CENTER, image=photo, bg="white", fg="black")
    panel1.pack(side="bottom", fill="both", expand="yes")
    l1 = tk.Label(root6, text=df[0:7], font=('Segoe UI Black', 12, 'italic'), bg="deep sky blue", fg="black",borderwidth = 8,width = 40,relief="sunken")
    l1.place(relx=0.185, rely=0.3, anchor=CENTER)
    photo4 = tk.PhotoImage(file="pic_screen.PNG")
    panel3 = tk.Label(root6, compound=CENTER, image=photo4, bg="white", fg="white")
    panel3.pack(side="bottom", fill="both", expand="yes")
    photo5 = tk.PhotoImage(file="g3.png")                       #graph button image
    panel2 = tk.Button(root6, image=photo5, bg="white", fg="white", bd=10, command=graph_3)
    panel2.place(relx=0.84, rely=0.25, anchor=CENTER)
    photo6 = tk.PhotoImage(file="g4.png")                       #graph button image
    panel3 = tk.Button(root6, image=photo6, bg="white", fg="white", bd=10, command=graph_4)
    panel3.place(relx=0.84, rely=0.55, anchor=CENTER)
    t1 = "\nWe all know the fact that" \
         "\n\"An educated country is " \
         "\n a developed country\" and also" \
         "\nfrom the graph we can see that" \
         "\n\n Nature of graph is linear ,which" \
         "\nimplies that people are getting " \
         "\neducated  and employed."                            #analysation of the graphs
    t2 = "\u21C7Dataset  \t  Graphs\u21C9"
    panel8 = tk.Label(root6, text=t1, bg="white", fg="black", font=('Segoe UI Black', 14, 'italic'))
    panel8.place(relx=0.54, rely=0.38, anchor=CENTER)
    panel9 = tk.Label(root6, text=t2, bg="white", fg="black", font=('Segoe UI Black', 18, 'bold', 'italic'))
    panel9.place(relx=0.54, rely=0.6, anchor=CENTER)
    B9 = tk.Button(root6, text=u"Next \u27A4", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60", fg="black",
                   bd=10,command=forward7)
    B9.place(relx=0.94, rely=0.82, anchor=CENTER)               #Shift to 8th window
    B10 = tk.Button(root6, text=u"\u00AB Previous", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60",
                    fg="black", bd=10,command=forward5)
    B10.place(relx=0.82, rely=0.82, anchor=CENTER)              #Shift to 6th window
    root6.mainloop()

#screen 8th
def forward7():
    global root6
    global root7
    global root8
    try:
        root3.destroy()                                         # if called from 4th window
    except:
        pass
    try:
        root6.destroy()                                         # if called from 7th window
    except:
        pass
    try:
        root8.destroy()                                         # if called from 9th window
    except:
        pass
    root7 = tk.Tk()
    root7.geometry("1200x720")
    root7.resizable(width=False, height=False)
    root7.title("Data Analysis--India's Unemployement")
    data = pandu.read_csv(r'Excel_data1.csv')
    df = pandu.DataFrame(data, columns=['Date-',' % Under US $5.50 Per Day','Change'])      #Slicing of columns
    df = df.set_index('Date-')
    photo = tk.PhotoImage(file="pic_screen.PNG")                 #Background image
    panel1 = tk.Label(root7, compound=CENTER, image=photo, bg="white", fg="black")
    panel1.pack(side="bottom", fill="both", expand="yes")
    l1 = tk.Label(root7, text=df[0:8], font=('Segoe UI Black', 12, 'italic'), bg="deep sky blue", fg="black",borderwidth = 8,width = 40,relief="sunken")
    l1.place(relx=0.185, rely=0.33, anchor=CENTER)
    photo5 = tk.PhotoImage(file="g1.png")                       #graph button image
    panel2 = tk.Button(root7, image=photo5, bg="white", fg="white", bd=10, command=graph_1)
    panel2.place(relx=0.84, rely=0.25, anchor=CENTER)
    photo6 = tk.PhotoImage(file="g2.png")                       #graph button image
    panel3 = tk.Button(root7, image=photo6, bg="white", fg="white", bd=10, command=graph_2)
    panel3.place(relx=0.84, rely=0.55, anchor=CENTER)
    t1 = "But getting educated and employed to " \
         "\na low payble salary doesn't imply " \
         "\n that individual is fully settled with " \
         "\nhis/her occupation ,so here is a dataset of" \
         "\n\n% of individuals getting Under US $5.50 " \
         "\nper Day and are considered " \
         "\nto be under poverty "                               #analysation of the graphs
    t2 = "\u21C7Dataset  \t  Graphs\u21C9"
    panel8 = tk.Label(root7, text=t1, bg="white", fg="black", font=('Segoe UI Black', 14, 'italic'))
    panel8.place(relx=0.54, rely=0.38, anchor=CENTER)
    panel9 = tk.Label(root7, text=t2, bg="white", fg="black", font=('Segoe UI Black', 18, 'bold', 'italic'))
    panel9.place(relx=0.54, rely=0.6, anchor=CENTER)
    B9 = tk.Button(root7, text=u"Finish \u27A4", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60", fg="black",
                   bd=10,command=forward8)                      #Shift to 9th window
    B9.place(relx=0.94, rely=0.82, anchor=CENTER)
    B10 = tk.Button(root7, text=u"\u00AB Previous", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60",
                    fg="black", bd=10,command=forward6)         #Shift to 7th window
    B10.place(relx=0.82, rely=0.82, anchor=CENTER)
    root7.mainloop()

#screen 9th
def forward8():
    global root7
    global root8
    root7.destroy()                                             #called from 8th window
    root8 = tk.Tk()
    root8.geometry("1200x720")
    root8.resizable(width=False, height=False)
    root8.title("Data Analysis--India's Unemployement")
    photo = tk.PhotoImage(file="thank_you.PNG")                 #Background image
    panel1 = tk.Label(root8, compound=CENTER, image=photo)
    panel1.pack(side="bottom", fill="both", expand="yes")
    B10 = tk.Button(root8, text=u"\u00AB Previous", font=('Cooper Black', 15, 'italic', 'bold'), bg="gray60",
                    fg="black", bd=10, command=forward7)        # Shift to 8th window
    B10.place(relx=0.82, rely=0.82, anchor=CENTER)
    root8.mainloop()

i,c,l,d,e,g,j,w = 0,0,0,0,0,0,0,0
p = -0.1
q,m = 0.8,0.8
b=-0.4
s,n,f,h,k,y=0.9,0.9,0.9,0.9,0.9,0.9
t11="Overall Unemployment rate"
t22="YOUTH unemployment rate"
t3="Literacy rate"
t4="Poverty rate"
t5="\"From Facts and figures we can see that" \
   "\n\n(India's Unemployment rate) \u221D (Youth employment rate)" \
   "\n\nand Literacy rate,poverty rate etc. are its relative factors " \
   "\n if one get disturbed then other also changes due to " \
   "\n correlation between them, we will analyse their \"Data\"  " \
   "\none by one according to the given dataset of past 20 years\" " \
   "\n \n Or you can quickly access any factor directly also" \
   "\n\u27FD From there"
text1 = "Project Name:"
text2 = "\"India\'s  Unemployment rate\" \nThe relative factors:-" \
            "\n\t          *Overall Unemployment rate\n \t   *Youth employment rate\n*Literacy rate" \
            "\n*Poverty rate"
text3 = "But before proceeding to data analysis " \
            "\nlet\'s see the facts and figures " \
            "\nTo proceed--click here"

# 8 graphs from fraph_1 to graph_8
def graph_1():
    global df
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:8]
    df['Date-'] = df['Date-'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))     #stripping year out of full date
    x = df['Date-']
    y = df[' % Under US $5.50 Per Day']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=3,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=12, markevery=1)

    plt.title('--Poverty rate--', fontdict=font)
    plt.ylabel(' % Under US $5.50 Per Day', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

def graph_2():
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:8]
    df['Date-'] = df['Date-'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))     #stripping year out of full date
    x = df['Date-']
    y = df['Change']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=3,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=12, markevery=1)
    plt.title('--Annual Change--', fontdict=font)
    plt.ylabel('Change', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

def graph_3():
    global df
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:7]
    df['Date:'] = df['Date:'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))     #stripping year out of full date
    x = df['Date:']
    y = df[' Literacy Rate']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=3,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=12, markevery=1)

    plt.title('--Literacy Rate--', fontdict=font)
    plt.ylabel(' % of people Educated', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

def graph_4():
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:7]
    df['Date:'] = df['Date:'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))     #stripping year out of full date
    x = df['Date:']
    y = df[' Annual Change(%)']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=3,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=12, markevery=1)
    plt.title('--Annual Change--', fontdict=font)
    plt.ylabel('Change', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

def graph_5():
    global df
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:30]
    #df=data
    df['Date:-'] = df['Date:-'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))   #stripping year out of full date
    x = df['Date:-']
    y = df['Youth Unemployment Rate ']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=2,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=6, markevery=1)

    plt.title('--Youth Unemployment Rate--', fontdict=font)
    plt.ylabel(' % of Youth unemployed', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

def graph_6():
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:31]
    #df = data
    df['Date:-'] = df['Date:-'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))   #stripping year out of full date
    x = df['Date:-']
    y = df['Annual Change']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=2,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=6, markevery=1)
    plt.title('--Annual Change--', fontdict=font)
    plt.ylabel('Change', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

def graph_7():
    global df
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:30]
    #df=data
    df['Date:-'] = df['Date:-'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))   #stripping year out of full date
    x = df['Date:-']
    y = df[' Unemployment Rate ']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=2,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=6, markevery=1)

    plt.title('--Unemployment Rate--', fontdict=font)
    plt.ylabel(' % of people unemployed', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

def graph_8():
    data = pandu.read_csv(r'Excel_data1.csv')
    df = data[0:31]
    #df = data
    df['Date:-'] = df['Date:-'].map(lambda x: datetime.strptime(str(x), '%m/%d/%Y'))   #stripping year out of full date
    x = df['Date:-']
    y = df['Annual change']
    font = {'family': 'Cooper Black',
            'color': 'darkblue',
            'weight': 'normal',
            'size': 14,
            }
    plt.plot(x, y, color='blue', linewidth=2,
             marker='h', markerfacecolor='lightgreen', markeredgewidth=2,
             markersize=6, markevery=1)
    plt.title('--Annual Change--', fontdict=font)
    plt.ylabel('Change', fontdict=font)
    plt.xlabel('Year', fontdict=font)
    plt.grid(color='g', linewidth=2)
    plt.legend()
    plt.show()

#all sliding effects functions
def sliding_effect3_label(label):
    def sliding_effect3():
        global i
        global p
        global text1
        if i != 121:
            label.config(text=text1, font=('Cooper Black', 30, 'italic', 'underline'), bd=6, fg="dark blue")
            label.place(relx=p, rely=0.18, anchor=CENTER)
            i += 1
            p += 0.01
            label.after(15, sliding_effect3)

    sliding_effect3()
def sliding_effect2_label(label):
    def sliding_effect2():
        global text2
        global i
        global q
        if i != 91:
            label.config(text=text2, font=('Segoe UI Black', 25, 'italic',), fg="blue")
            label.place(relx=q, rely=0.42, anchor=CENTER)
            i += 1
            q -= 0.01
            label.after(15, sliding_effect2)

    sliding_effect2()
def sliding_effect1_label(label):
    def sliding_effect1():
        global text3
        global i
        global m
        if i != 91:
            label.config(text=text3, font=('Segoe UI Black', 15, 'italic', 'underline'), fg="DodgerBlue2", bd=15)
            label.place(relx=m, rely=0.75, anchor=CENTER)
            i += 1
            m -= 0.01
            label.after(15, sliding_effect1)

    sliding_effect1()
def sliding_effect4_label(label):
    def sliding_effect4():
        global c
        global b
        if c != 91:
            #label.config(text="")
            label.place(relx=0.5, rely=b, anchor=CENTER)
            c+=1
            b+=0.01
            label.after(5, sliding_effect4)
        else:
            c=0
            b=-0.4
    sliding_effect4()
def sliding_effect6_label(label):
    def sliding_effect6():
        global t11
        global w
        global y
        if w != 71:
            label.config(text=t11, font=('Segoe UI Black', 15, 'italic', 'underline'), fg="DodgerBlue2", bd=5)
            label.place(relx=0.13, rely=y, anchor=CENTER)
            w += 1
            y -= 0.01
            label.after(15, sliding_effect6)
        else:
            w=0
            y=0.9

    sliding_effect6()
def sliding_effect7_label(label):
    def sliding_effect7():
        global t22
        global l
        global s
        if l != 61:
            label.config(text=t22, font=('Segoe UI Black', 15, 'italic', 'underline'), fg="DodgerBlue2", bd=5)
            label.place(relx=0.13, rely=s, anchor=CENTER)
            l += 1
            s -= 0.01
            label.after(15, sliding_effect7)
        else:
            l=0
            s=0.9
    sliding_effect7()
def sliding_effect8_label(label):
    def sliding_effect8():
        global t3
        global d
        global n
        if d != 51  :
            label.config(text=t3, font=('Segoe UI Black', 15, 'italic', 'underline'), fg="DodgerBlue2", bd=5)
            label.place(relx=0.07, rely=n, anchor=CENTER)
            d += 1
            n -= 0.01
            label.after(15, sliding_effect8)
        else:
            d=0
            n=0.9
    sliding_effect8()
def sliding_effect9_label(label):
    def sliding_effect9():
        global t4
        global e
        global f
        if e != 41:
            label.config(text=t4, font=('Segoe UI Black', 15, 'italic', 'underline'), fg="DodgerBlue2", bd=5)
            label.place(relx=0.07, rely=f, anchor=CENTER)
            e += 1
            f -= 0.01
            label.after(15, sliding_effect9)
        else:
            e=0
            f=0.9
    sliding_effect9()
def sliding_effect10_label(label):
    def sliding_effect10():
        global g
        global h
        if g != 29:
            label.config(text=u'\u27F0 Quick Access', font=('Segoe UI Black', 15, 'bold','underline'), fg="black", bd=5)
            label.place(relx=0.08, rely=h, anchor=CENTER)
            g += 1
            h -= 0.01
            label.after(15, sliding_effect10)
        else:
            g=0
            h=0.9

    sliding_effect10()
def sliding_effect11_label(label):
    def sliding_effect11():
        global t5
        global j
        global k
        if j != 49:
            label.config(text=t5, font=('Segoe UI Black', 20, 'bold','italic'), fg="black", bd=5)
            label.place(relx=0.63, rely=k, anchor=CENTER)
            j += 1
            k -= 0.01
            label.after(15, sliding_effect11)
        else:
            j=0
            k=0.9
    sliding_effect11()

#main window
def main_window():
    global root
    global Parent
    inputValue = textBox.get("1.0","end-1c")
    Parent.destroy()
    root = tk.Tk()
    root.geometry("1200x720")
    root.resizable(width=False, height=False)
    root.title("Data Analysis--India's Unemployement")
    photo= PhotoImage(file="Capture2.png")
    canvas = Canvas(root, width=1200, height=720)
    canvas.pack(expand=YES, fill=BOTH)
    t1 = turtle.RawTurtle(canvas)
    t2 = turtle.RawTurtle(canvas)
    canvas.create_image(0, 0, image=photo, anchor=CENTER)
    label = Label(canvas, text="Welcome  %s!!  "
                               "\nThis is my project report of data analysis,"
                               "\nwith Tkinter GUI"
                               "\nTo proceed please click on the START  button"
                               "\n\n\t\t Submitted by-"
                               "\n\t\t  Devender kumar,Bhuvnesh Kumar,Vinit Kumar"
                               "\n\t\t\t(June2021 : 4-6pm batch)"%(inputValue), fg='white', bg='black',
                  font=('Cooper Black', 15, 'italic'))
    label.place(relx=0.52, rely=0.5, anchor=CENTER)
    B1 = Button(master=root, text="START", width=6, height=0, font=('Cooper Black', 15, 'italic'), bd=10, bg="gray60",
                command=forward1)
    B1.place(relx=0.5, rely=0.72, anchor=CENTER)
    t1.pencolor("#ff0000")  # Red
    t2.pencolor("#ff0000")  # Red
    colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
    t1.penup()
    t1.setposition(-320, -200)
    t1.speed(0)
    t2.penup()
    t2.setposition(320, 200)
    t2.speed(0)
    #to operate multiple turtles at same time
    for x in range(120):
        t1.pendown()
        t2.pendown()
        t1.pencolor(colors[x % 6])
        t2.pencolor(colors[x % 6])
        t1.width(x / 100 + 1)
        t2.width(x / 100 + 1)
        t1.forward(x)
        t2.forward(x)
        t1.left(59)
        t2.left(59)
    root.mainloop()

#asking name window
Parent=tk.Tk()
Parent.geometry("500x450")
Parent.title("Tell me your Name")
canvas =Canvas( Parent ,width = 500, height = 450,bg="white")
canvas.pack(expand= YES,fill=BOTH)
photo5 = tk.PhotoImage(file="ask_name.png")
panel2 = tk.Label(canvas, image=photo5, bg="white", fg="white")
panel2.place(relx=0.5, rely=0.75, anchor=CENTER)
l1 = tk.Label(Parent, text="Before getting started, \n Can i know your good name please? ", font=('Segoe UI Black', 12, 'italic'), bg="black", fg="white",
                  borderwidth=8, width=40, relief="ridge")              #taking name as entry
l1.place(relx=0.5,rely=0.15,anchor=CENTER)
textBox=Text(canvas, height=1, width=20,bd=10)
textBox.place(relx=0.5,rely=0.32,anchor=CENTER)
buttonCommit=Button(canvas, height=1, width=10, text="Begin",bd=5, font=('Segoe UI Black', 10, 'italic'), bg="black", fg="white",
                    command=main_window)

buttonCommit.place(relx=0.5,rely=0.44,anchor=CENTER)

Parent.mainloop()