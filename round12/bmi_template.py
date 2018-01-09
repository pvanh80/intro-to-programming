# TIE-02100 Johdatus ohjelmointiin
# TIE-02106 Introduction to Programming
# BMI

from tkinter import *


class Userinterface:

    def __init__(self):
        self.__mainwindow = Tk()
        # TODO: Change the title of the main window to be "BMI calculator"
        self.__mainwindow.title("BMI calculator")
        self.__mainwindow.geometry("500x130")
        self.__mainwindow.resizable(width=False, height=False)
        # TODO: Add GUI components to make the GUI understandable for the
        # user, for example labels to indicate what the user should write
        # in the Entry-components.
        self.__bmi_value = StringVar()
        self.__explanation = StringVar()
        self.__label_weight = Label(self.__mainwindow, text="Enter your weight (kg):")
        self.__label_height = Label(self.__mainwindow, text="Enter your height (m):")
        self.__label_bmi = Label(self.__mainwindow, text="Your BMI:")
        self.__reset_h_value = StringVar()
        self.__reset_w_value = StringVar()
        # TODO: Create an Entry-component for the weight.
        self.__weight_value = Entry(self.__mainwindow, width=40, textvariable=self.__reset_w_value)
        # TODO: Create an Entry-component for the height.
        self.__height_value = Entry(self.__mainwindow, width=40, textvariable=self.__reset_h_value)

        # TODO: Create a Button that will call the calculate_BMI-method.
        # TODO: Change the colour of the Button to something else than
        # the default colour.
        self.__calculate_button = Button(self.__mainwindow,text="Calculate",bg="red",command=self.calculate_BMI)
        # TODO: Create a Label that will show the decimal value of the BMI 
        # after it has been calculated.
        self.__result_text = Label(self.__mainwindow,textvariable=self.__bmi_value)
        # TODO: Create a Label that will show a verbal description of the BMI
        # after the BMI has been calculated.
        self.__explanation_text = Label(self.__mainwindow,textvariable=self.__explanation)
        # TODO: Create a button that will call the stop-method.
        self.__stop_button = Button(self.__mainwindow,bg="red", text='Quit', command=self.stop)

        #TODO: Create a reset button that will ease the fields
        self.__reset_button = Button(self.__mainwindow, bg="red", text='Reset', command=self.reset_fields)
        # TODO: Place the components in the GUI as you wish.
        # If you read the Gaddis book, you can use pack here instead of grid!
        self.__label_height.grid(row=1,column=1)
        self.__label_weight.grid(row=2,column=1)
        self.__weight_value.grid(row=2,column=2)
        self.__height_value.grid(row=1,column=2)
        self.__calculate_button.grid(row=5,column=1)
        self.__stop_button.grid(row=5,column=3)
        self.__reset_button.grid(row=5,column=2)
        self.__result_text.grid(row=3,column=2)
        self.__label_bmi.grid(row=3, column=1)
        self.__explanation_text.grid(row=4,column=1)

    # TODO: Implement this method.
    def calculate_BMI(self):
        """ Section b) This method calculates the BMI of the user and
            displays it. First the method will get the values of
            height and weight from the GUI components
            self.__height_value and self.__weight_value.  Then the
            method will calculate the value of the BMI and show it in
            the element self.__result_text. 
            
            Section e) Last, the method will display a verbal
            description of the BMI in the element
            self.__explanation_text. 
        """ 
        pass
        try:
            weight = float(self.__weight_value.get())
            height = float(self.__height_value.get())
            if weight <= 0 or height <= 0 :
                self.__bmi_value.set("Error: height and weight must be positive.")
            else:
                bmi = float(weight/(height*height))
                self.__bmi_value.set("BMI: " + format(bmi,'.2f'))
                if bmi <= 25 and bmi >= 18.5:
                    self.__explanation.set("Your weight is normal.")
                elif bmi >= 25:
                    self.__explanation.set("You are overweight.")
                elif bmi <= 18.5:
                    self.__explanation.set("You are underweight.")
                else:
                    self.__explanation.set("You are underweight.")
        except:
            self.__bmi_value.set("Error: height and weight must be numbers.")


    # TODO: Implement this method.
    def reset_fields(self):
        """ In error situations this method will zeroize the elements
            self.__result_text, self.__height_value, and self.__weight_value.
        """
        pass
        weight = 0
        height = 0
        result = 0
        self.__weight_value.delete(0, END)
        self.__weight_value.insert(0, "")
        self.__height_value.delete(0, END)
        self.__height_value.insert(0, "")

    def stop(self):
        """ Ends the execution of the program.
        """
        self.__mainwindow.destroy()

    def start(self):
        """ Starts the mainloop. 
        """
        self.__mainwindow.mainloop()


def main():
    ui = Userinterface()
    ui.start()


main()
