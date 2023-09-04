from tkinter import *

root=Tk()

root.title("Fibonacci")
root.geometry("400x400")

label_series = Label(root, text="Fibonacci Series:  ")
label2 = Label(root)
input = Entry(root)

def Fibonacci():
    
    input_no =int(input.get())
    first_no = 0
    second_no = 1
    sum = 0
    sum2=0
    counter = 1
    while (counter <= input_no):
        label_series["text"] += str(sum) + " "
        label2 ["text"] = "Fibanocci sum:  " + str(sum2)
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no +second_no
        sum2 = sum2 + sum
    
btn = Button(root, text="SHow Fibonacci Series", command=Fibonacci)
input.pack()
btn.pack()
label_series.pack()
label2.pack()

root.mainloop() 