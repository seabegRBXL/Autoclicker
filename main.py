import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.toast import ToastNotification
from ttkbootstrap.validation import add_regex_validation

option_keybind = "."
global packed
packed = 0

class main(ttk.Frame):

    def __init__(self, master_window):
        super().__init__(master_window, padding=(20,10))
        self.pack(fill=BOTH, expand=YES)
        self.name = ttk.StringVar(value="")
        self.student_id = ttk.StringVar(value="")
        self.course_name = ttk.StringVar(value="")
        self.final_score = ttk.DoubleVar(value=0)
        self.data = []
        self.colors = master_window.style.colors
        global warning_notif
        global instruction_master
        global instruction
        global adv_option_button

        instruction_master = ttk.Frame(self)
        instruction_master.pack(fill=X, expand=YES, pady=5)

        instruction_text = "Created by @seabeg!" 
        instruction = ttk.Label(instruction_master, text=instruction_text)
        instruction.pack(side=LEFT)

        adv_option_txt = "Settings"

        adv_option_button = ttk.Button(
            instruction_master,
            text=adv_option_txt,
            command=self.on_page
        )

        adv_option_button.pack(side=RIGHT)

        global final_score_input
        final_score_input = self.create_form_entry("CPS:", self.final_score)
        final_score_input.pack()
        self.create_meter()
        self.create_buttonbox()

        self.table = self.create_table()

    
    def create_form_entry(self, label, variable):
        global form_field_label
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X, expand=YES, pady=5)

        form_field_label = ttk.Label(master=form_field_container, text=label, width=15)
        form_field_label.pack(side=LEFT, padx=12)

        form_input = ttk.Entry(master=form_field_container, textvariable=variable, validate="key", validatecommand=(self.register(self.validate_int), "%P"))
        form_input.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return form_input

    def validate_int(self, value):
        try:
            # Try converting the input to an integer
            int(value)
            return True
        except ValueError:
            # If the conversion fails, it's not a valid integer
            return False
    
    def create_buttonbox(self):
        global cancel_btn
        global submit_btn
        global keybind_instruction

        button_container = ttk.Frame(self)
        button_container.pack(fill=X, expand=YES, pady=(15, 10))

        keybind_instruction_text = "You can use the keybind \"" + option_keybind + "\" instead of the buttons" 
        keybind_instruction = ttk.Label(
            master=button_container, 
            text=keybind_instruction_text, 
            width=50
            )
        keybind_instruction.pack(side=LEFT, padx=10)

        cancel_btn = ttk.Button(
            master=button_container,
            text="Disable",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
            state=DISABLED
        )

        cancel_btn.pack(side=RIGHT, padx=5)

        submit_btn = ttk.Button(
            master=button_container,
            text="Enable",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )

        

        submit_btn.pack(side=RIGHT, padx=5)

    def create_meter(self):
        global packed
        global meter
        packed = 0
        meter = ttk.Meter(
            master=self,
            metersize=150,
            padding=5,
            amounttotal=20,
            amountused=10,
            metertype="discrete",
            subtext="CPS",
            interactive=True,
        )

        meter.pack()

        def check_meter():
            global packed
            try:
                print("CHECKING METER")
                zv = float(meter.amountusedvar.get())
                if 1 <= zv <= 20:
                    zv = int(round(zv))  # Round to the nearest integer to remove decimal places
                elif zv < 1:
                    zv = 1
                elif zv > 20:
                    zv = 20
                if zv >= 15:
                    if packed == 0:
                        warning_txt = "⚠️ High Cps - Autoclicker Prevention and/or Alternating Clicks May Occur"
                        global warning_notif
                        warning_notif = ttk.Label(text=warning_txt, foreground="yellow")
                        warning_notif.pack()
                        packed = 1 
                else:
                    #remove an element
                    if packed == 1:
                        warning_notif.destroy()
                        packed = 0
            except TimeoutError:
                randomvar = 1
            else:
                randomvar = 1
    
            
            meter.amountusedvar.set(zv)
            self.after(10, check_meter)  # Check meter every 10 milliseconds

        # Initial check and configuration
        check_meter()

        self.final_score.set(meter.amountusedvar)
        final_score_input.configure(textvariable=meter.amountusedvar)


    
    def create_table(self):
        coldata = [
            {"text": "Option Name"},
            {"text": "Type", "stretch": False},
            {"text": "Description"},
            {"text": "Value", "stretch": False}
        ]

        print(self.data)
    
    def on_page(self):
        cancel_btn.destroy()
        submit_btn.destroy()
        meter.destroy()
        keybind_instruction.destroy()
        instruction.destroy()
        instruction_master.destroy()
        adv_option_button.destroy()
        final_score_input.destroy()
        form_field_label.destroy()
        try:
            warning_notif.destroy()
        except NameError:
            print("No Warning_Notif found, THIS IS NOT AN ERROR")
        else:
            print("No Warning_Notif found, THIS IS NOT AN ERROR")
        settings(self)

    def on_submit(self):
        global cancel_btn
        global submit_btn
        cancel_btn['state'] = NORMAL
        submit_btn['state'] = DISABLED

    def on_cancel(self):
        global cancel_btn
        global submit_btn
        cancel_btn['state'] = DISABLED
        submit_btn['state'] = NORMAL

class settings(ttk.Frame):

    def __init__(self, master_window):
        super().__init__(master_window, padding=(20,10))
        self.pack(fill=BOTH, expand=YES)
        self.name = ttk.StringVar(value="")
        self.student_id = ttk.StringVar(value="")
        self.course_name = ttk.StringVar(value="")
        self.final_score = ttk.DoubleVar(value=0)
        self.data = []
        self.colors = master_window.style.colors
        global warning_notif
        global instruction_master
        global instruction
        global adv_option_button

        instruction_master = ttk.Frame(self)
        instruction_master.pack(fill=X, expand=YES, pady=5)

        instruction_text = "Created by @seabeg!" 
        instruction = ttk.Label(instruction_master, text=instruction_text)
        instruction.pack(side=LEFT)

        adv_option_txt = "Back"

        adv_option_button = ttk.Button(
            instruction_master,
            text=adv_option_txt
        )

        adv_option_button.pack(side=RIGHT)

        global final_score_input
        final_score_input = self.create_form_entry("CPS:", self.final_score)
        final_score_input.pack()


        self.create_buttonbox()

    
    def create_form_entry(self, label, variable):
        form_field_container = ttk.Frame(self)
        form_field_container.pack(fill=X, expand=YES, pady=5)

        form_field_label = ttk.Label(master=form_field_container, text=label, width=15)
        form_field_label.pack(side=LEFT, padx=12)

        form_input = ttk.Entry(master=form_field_container, textvariable=variable, validate="key")
        form_input.pack(side=LEFT, padx=5, fill=X, expand=YES)

        return form_input

    
    def create_buttonbox(self):

        global keybind_instruction

        button_container = ttk.Frame(self)
        button_container.pack(fill=X, expand=YES, pady=(15, 10))

        keybind_instruction_text = "You can use the keybind \"" + option_keybind + "\" instead of the buttons" 
        keybind_instruction = ttk.Label(
            master=button_container, 
            text=keybind_instruction_text, 
            width=50
            )
        keybind_instruction.pack(side=LEFT, padx=10)

        cancel_btn = ttk.Button(
            master=button_container,
            text="Disable",
            command=self.on_cancel,
            bootstyle=DANGER,
            width=6,
        )

        cancel_btn.pack(side=RIGHT, padx=5)

        submit_btn = ttk.Button(
            master=button_container,
            text="Enable",
            command=self.on_submit,
            bootstyle=SUCCESS,
            width=6,
        )
        
        submit_btn.pack(side=RIGHT, padx=5)

    def on_cancel():
        toast_update = ToastNotification(
        title="Option update successful!",
        message="Your data has been successfully updated.",
        duration=3000,
        )

        toast_update.show_toast()

    def on_submit():
        toast_update = ToastNotification(
        title="Option update successful!",
        message="Your data has been successfully updated.",
        duration=3000,
        )

        toast_update.show_toast()

if __name__ == "__main__":

    app = ttk.Window("ClickQuick AutoClicker", "superhero", resizable=(False, False))
    main(app)
    app.mainloop()
else:
    print("if __name__ == '__main__' Check failed. Plese obtain a legal copy of this program. \n If this was a mistake, please restart the program. \n #stopPirating")