import tkinter as tk
from tkinter.ttk import *
import mysql.connector
import sqlalchemy
import pandas as pd
from fpdf import FPDF
# setting the windows size
root=tk.Tk()
root.geometry("700x500")
mysql_ = mysql.connector.connect(host = 'localhost', user='root', passwd='root')
mycursor = mysql_.cursor()
mycursor.execute("use new1")
engine = sqlalchemy.create_engine('mysql+pymysql://root:root@localhost:3306/new1')
dataframe = pd.read_sql_table("pet",engine)
# declaring string variable
# for storing name and password
appno_var=tk.StringVar()
height_var=tk.StringVar()
htconfirm_var=tk.StringVar()
def submit():
	app_no=appno_var.get()
	appno = str(float(app_no))
	results=[]
	results.append(dataframe.loc[dataframe.ctrlno1==appno,'Name'])
	s1=str(results[0][0])
	print('Name :- ',s1)
	results=[]
	results.append(dataframe.loc[dataframe.ctrlno1==appno,'f_name'])
	s2=str(results[0][0])
	print('f_name is :- ',s2)
	results=[]
	results.append(dataframe.loc[dataframe.ctrlno1==appno,'petdate'])
	s3=str(results[0][0])
	print('PET Date :- ',s3)
	results=[]
	results.append(dataframe.loc[dataframe.ctrlno1==appno,'rollno'])
	s4=str(results[0][0])
	print('Roll Number :- ',s4)
	#s2=results[0]['rollno']
	#s3=results[0]['f_name']
	#s4=results[0]['petdate']

	#print(type(s2))
	#print(type(s3))
	#print(type(s4))
	res=[]
	res.append(dataframe.loc[dataframe.ctrlno1 == appno,'duplicate'])
	st=res[0][0]
	height_real = float(st)
	height= height_var.get()
	htconfirm=htconfirm_var.get()
	if height == htconfirm:
		if height < st:
			text='FAILED'
			details_label = tk.Label(root, text= text,font=('calibre',30,'bold'),fg='#f00')
			pdfwriter(appno,height,s1,s2,s3,s4)
		else:
			text='PASSED'
			details_label = tk.Label(root, text= text,font=('calibre',30,'bold'),fg='#008000')
		details_label.grid(row=16,column=1)
	else:
		print("Re-enter your height")
def pdfwriter(appno,height,name,F_name,PETDate,Roll):
	pdf = FPDF()
	pdf.add_page()
	pdf.set_font("Arial",size = 15)
	pdf.cell(5, 6, txt = "F/H Name :- "+F_name, ln = 1, align = 'L')
	pdf.cell(5, 6, txt = "PET Date :- "+PETDate, ln = 1, align = 'L')
	pdf.cell(5, 6, txt = "DOC Verification Date:-", ln = 1, align = 'L')
	text= 'Height: FAILED('+str(height)+')'
	pdf.cell(5, 6, txt = text, ln = 8, align = 'L')
	pdf.image('C://Users//RAJAT//Desktop//line.png',12, 34, 253)
	pdf.cell(200, 14, txt = "Note: This a Computer Based Test", ln = 1, align = 'C')
	pdf.cell(200, 10, txt = "Candidate Copy", ln = 1, align = 'C')
	pdf.image('C://Users//RAJAT//Desktop//bihar-police.png',12,54,20)
	pdf.set_font("Arial","B",size=20)
	pdf.cell(200, 10, txt = "Central Selection Board of Constable", ln = 1, align = 'C')
	pdf.set_font("Arial",size = 15)
	pdf.cell(200, 6, txt = "Driver Constable Recruitment-2016", ln = 1, align = 'C')
	pdf.cell(200, 6, txt = "DOCUMENT VERIFICATION ENTRY PASS", ln = 1, align = 'C')
	pdf.image('C://Users//RAJAT//Desktop//qrcode.png',100,80,30)
	pdf.cell(210, 33, txt = Roll, ln = 1, align = 'C')
	pdf.set_font("Arial",size = 18)
	pdf.cell(175, 10, txt = "Roll Number:- "+Roll, ln = 1, align = 'L')
	pdf.cell(175, 10, txt = "Name:- "+name, ln = 1, align = 'L')
	pdf.cell(175, 10, txt = "F/H Name :- "+F_name, ln = 1, align = 'L')
	pdf.cell(175, 10, txt = "PET Date :- "+PETDate, ln = 1, align = 'L')
	pdf.cell(175, 10, txt = "DOC Verification Date:-", ln = 1, align = 'L')
	text= 'Height: FAILED('+str(height)+')'
	pdf.cell(175, 10, txt = text, ln = 1, align = 'L')
	pdf.image('C://Users//RAJAT//footer.png',10,185,196)
	#pdf.set_font("Arial","BU",size=18)
	#pdf.cell(385, 100, txt = "Signature of Student", align = 'L')
	#pdf.cell(5, 10, txt = "Signature of Invigilator", ln = 1, align = 'R')
	pdf.output("C://Users//RAJAT//Desktop//report.pdf")
appno_label = tk.Label(root, text = 'Application Number :', font=('calibre',15,'bold'))
appno_entry = tk.Entry(root,textvariable = appno_var, font=('calibre',20,'normal'))
height_label = tk.Label(root, text = 'Enter the height of candidate:', font=('calibre',15,'bold'))
height_entry = tk.Entry(root,textvariable = height_var, font=('calibre',20,'normal'))
htconfirm_label = tk.Label(root, text = 'Re-enter the height of candidate:', font=('calibre',15,'bold'))
htconfirm_entry = tk.Entry(root,textvariable = htconfirm_var, font=('calibre',20,'normal'))
sub_btn=tk.Button(root,text = 'Submit', command = submit)
exit_btn=tk.Button(root,text = 'Exit',command=root.quit)
appno_label.grid(row=1,column=0)
appno_entry.grid(row=1,column=1)
height_label.grid(row=6,column=0,pady=20)
height_entry.grid(row=6,column=1,pady=20)
htconfirm_label.grid(row=9,column=0,pady=20)
htconfirm_entry.grid(row=9,column=1,pady=20)
#frwd_btn.grid(row=14, column=0,columnspan=3,pady=10)
sub_btn.grid(row=14, column=1,columnspan=3,pady=10)
exit_btn.grid(row=74,column=0,columnspan=3,pady=10)
p1 = tk.PhotoImage(file = 'C://Users//RAJAT//icon.png')
# Setting icon of master window
root.iconphoto(False, p1)
root.title("Aplication")
# performing an infinite loop
# for the window to display
root.mainloop()
