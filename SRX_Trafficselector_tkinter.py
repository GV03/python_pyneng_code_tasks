from Tkinter import *

### Create window to popup
window = Tk()
window.title("Configuration Generation")
window.geometry('1500x1500')


##Set label in open window and it's size and it's place in window
Title = Label(window, text="IPSEC Configuration Template", font=("Arial Bold", 15))
Title.grid(column=3, row=0)

labl_interface = Label(window, text="Enter interface")
labl_interface.grid(column=0, row=1)

labl_unit = Label(window, text = "Unit Number")
labl_unit.grid(column= 2, row=1)

lbl1 = Label(window, text="Add Local IP", font=("Arial Bold", 10))
lbl1.grid(column=0, row=5)

lbl2 = Label(window, text="Add Remote IP", font=("Arial Bold", 10))
lbl2.grid(column=0, row=6)


lbl3 = Label(window, text="Enter VPN Name", font=("Arial Bold", 10))
lbl3.grid(column=0, row=7)


## Add Entry function for getting input from users
interface = Entry(window,width=13)
interface.grid(column=1, row=1)

unit = Entry(window, width=6)
unit.grid(column=3, row=1)


Local = Entry(window,width=50)
Local.grid(column=1, row=5)

Remote = Entry(window, width=50)
Remote.grid(column=1, row=6)

VPN = Entry(window, width=50)
VPN.grid(column=1, row=7)

### define Function which need to execute after clicking button
def submit():

	c = interface.get().replace("'", "")
	u = int(unit.get())
	
	L = Local.get()
	patt1  = re.compile(r'\d+\.\d+\.\d+\.\d+\/\d+',re.I|re.M)
	LIP = patt1.findall(L)##### List format of Local IP
	LC = len(LIP)
	###3lbl.configure(text=input)
	
	
	R = Remote.get()
	patt2 = re.compile(r'\d+\.\d+\.\d+\.\d+\/\d+',re.I|re.M)
	RIP = patt2.findall(R)##### List format of Remote IP
	RC = len(RIP)
	
	TC = LC*RC
	#print TC
	#print LIP
	#print RIP
	V = VPN.get()
	
	m=0
	i=0
	j=0
	result_display = Text(master=window, height=20, width=110)
	result_display.grid(column=4)
	result_display.insert(END, "set interfaces %s unit %d description XYZ\n\n" %(c, u))
	
	while i < len(LIP):
		while j < len(RIP):
			while m <= TC:
				result_display.insert(END, "set security ipsec vpn %s traffic-selector %s_Proxy%d local-ip %s\n" %(V, V, m, LIP[i]))
				result_display.insert(END, "set security ipsec vpn %s traffic-selector %s_Proxy%d remote-ip %s\n" %(V, V, m, RIP[j]))
				m = m+1
				break
			j = j+1
		j=0
		i = i+1
		#break
		

	
	

###set button with color and it's action when press
btn = Button(window, text="submit", bg="yellow", fg="red", command=submit)
##set position of label in window
btn.grid(column=1, row=9)


window.mainloop()