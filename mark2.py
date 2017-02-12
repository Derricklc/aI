from tkinter import *

master = Tk()


tp = [(0, 0), (1, 2), (2, 5), (3, 1), (4, 0), (5, 2), (6, 4), (7, 0), (8, 4), (9, 7), (10, 9), (11, 3)]

b1 = tp[0]
b2 = tp[1]
b3 = tp[2]
b4 = tp[3]
b5 = tp[4]
b6 = tp[5]
b7 = tp[6]
b8 = tp[7]
b9 = tp[8]
b10 = tp[9]
b11 = tp[10]
b12 = tp[11]

L1 = Label(master, text=" ")
L1.pack()
E1 = Entry(master, bd =5)
E1.insert(0, 'Value #1')
E1.pack()

L2 = Label(master, text=" ")
L2.pack()
E2 = Entry(master, bd =5)
E2.insert(0, 'Value #2')
E2.pack()

L3 = Label(master, text=" ")
L3.pack()
E3 = Entry(master, bd =5)
E3.insert(0, 'Value #3')
E3.pack()





w = Canvas(master, width=1000, height=500)
w.pack()



#____________________________________________________________________________________________

def plot():
        #____________HISTOGRAM PLOTTING ALGORITHM_____________________________________________________________________________________________________________________________________________________________________

        #ENTRY VERIABLES
        en1 = E1.get()
        en2 = E2.get()
        en3 = E3.get()
        median = 0
        print (en1)

        num = [ int(en1), int(en2), int(en3)] #turns the entry strings into integers then arranges them into a list

        #mean equation
        mean = (int(en1) + int(en2) + int(en3)) / 3 #9

        # median finding algorythm______________________

        if num[0] > num[1] and num[0] < num[2]  or num[0] > num[2] and num[0] < num[1] : #Checks if value number 1 is the mrdian
                median = num[0]
        elif num[1] > num[0] and num[1] < num[2] or num[1] > num[2] and num[1] < num[0] : #Checks if value number 2 is the mrdian
                median = num[1]
        elif num[2] > num[0] and num[2] < num[1] or num[2] > num[1] and num[2] < num[0] : #Checks if value number 3 is the mrdian
                median = num[2]
        elif num[0] == num[1] and num[1] == num[2] : #looks to see if all values are equal
                median = num[0]
        else:
                #displays an error if a median is mot found
                print ("ERROR!!!!")
        # end of median finding algorythm_______________

        max_height = 200 / mean
        max_height = max_height * mean
        max_height = max_height - 200


        med_height = 200 / mean
        med_height = med_height * median
        med_height = med_height - 200
        med_height = med_height * (-1)


        sec_height = median / 2
        sec_height = (200 / mean) * sec_height
        sec_height = sec_height - 200
        sec_height = sec_height * (-1)


        thir_height = median / 3
        thir_height = (200 / mean) * thir_height
        thir_height = thir_height - 200
        thir_height = thir_height * (-1)


        frth_height = median / 5
        frth_height = (200 / mean) * frth_height
        frth_height = frth_height - 200
        frth_height = frth_height * (-1)


        fith_height = median / 8
        fith_height = (200 / mean) * fith_height
        fith_height = fith_height - 200
        fith_height = fith_height * (-1)


        six_height = median / 12
        six_height = (200 / mean) * six_height
        six_height = six_height - 200
        six_height = six_height * (-1)


        svth_height = median / 17
        svth_height = (200 / mean) * svth_height
        svth_height = svth_height - 200
        svth_height = svth_height * (-1)


        lst_height = mean - median
        lst_height = (200 / mean) * lst_height
        lst_height = lst_height - 200
        lst_height = lst_height * (-1)

        print (max_height)
        print (med_height)

        #end of median equation
        print (median)



        print (mean)
        #stdev = 2
        #Y = { 1/[ σ * sqrt(2π) ] } * e-(x - μ)2/2σ2





        #____________HISTOGRAM_____________________________________________________________________________


        #VIRTICAL LINES
        w.create_line(15, 0, 15, 205, fill = "#000000", dash=(4, 4),tags = "line") # This makes the Y-axis
        w.create_line(340, 0, 340, 205, fill = "#000000", dash=(4, 4),tags = "line")

        #HORIZONTAL LINES # Horizontal line in 10 point increments
        w.create_line(15, 0, 340, 0, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 20, 340, 20, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 40, 340, 40, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 60, 340, 60, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 80, 340, 80, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 100, 340, 100, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 120, 340, 120, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 140, 340, 140, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 160, 340, 160, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(15, 180, 340, 180, fill = "#000000", dash=(4, 4),tags = "line") # Horizontal line in 10 point increments
        w.create_line(0, 200, 340, 200, fill = "#000000", dash=(4, 4),tags = "line") # this makes the X-axis

        #BARS
        #notes bareley show a value for 12
        w.create_rectangle(25, 200, 55, lst_height, fill="#bfff00")      #This makes bar #1 on the graph (25, 200, 55, 0) == ( 25=Xposition-1, 200=Maximum height of the bar, 55=Xposition-2, 0=makes the bar 200px-55px tall,)
        w.create_rectangle(55, 200, 80, svth_height, fill="#bfff00")    #This makes bar #2 on the graph
        w.create_rectangle(80, 200, 105, six_height, fill="#bfff00")    #This makes bar #3 on the graph
        w.create_rectangle(105, 200, 130, fith_height, fill="#bfff00")   #This makes bar #4 on the graph
        w.create_rectangle(130, 200, 155, frth_height, fill="#bfff00")   #This makes bar #5 on the graph
        w.create_rectangle(155, 200, 180, thir_height, fill="#bfff00")   #This makes bar #6 on the graph
        w.create_rectangle(180, 200, 205, sec_height, fill="#bfff00")   #This makes bar #7 on the graph
        w.create_rectangle(205, 200, 230, med_height, fill="#bfff00")  #This makes bar #8 on the graph
        w.create_rectangle(230, 200, 255, max_height, fill="#bfff00")   #This makes bar #9 on the graph
        w.create_rectangle(255, 200, 280, med_height, fill="#bfff00")   #This makes bar #10 on the graph
        w.create_rectangle(280, 200, 305, sec_height, fill="#bfff00")  #This makes bar #11 on the graph
        w.create_rectangle(305, 200, 330, thir_height, fill="#bfff00")   #This makes bar #12 on the graph
        #__________________________END OF HISTOGRAM__________________________________________________________



        #____________END OF HISTOGRAM PLOTTING ALGORITHM______________________________________________________________________________________________________________________________________________________________



        #____________________________________________________________________________________________





b = Button(master, text="Enter", command = plot)
b.pack()




mainloop()
