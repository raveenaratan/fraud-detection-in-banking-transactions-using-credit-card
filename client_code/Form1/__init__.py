from ._anvil_designer import Form1Template

from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class Form1(Form1Template):

  def __init__(self, **properties):

    # Set Form properties and Data Bindings.

    self.init_components(**properties)
    




    # Any code you write here will run before the form opens.

  def text_box_1_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    pass

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def form_show(self, **event_args):
    """This method is called when the form is shown on the page"""
    pass

  def button_1_click(self, **event_args):
    # Display a popup that says 'You clicked the button'
    alert("You clicked the button")



  def button_1_click(self, **event_args):
    # Set 'Name' to the text in the 'name_box'
    Name = self.name_box.text
    # Set 'Email' to the text in the 'email_box'
    Email = self.email_box.text
    # Set 'Phone' to the text in the 'phone_box'
    Phone = self.phone_box.text
    # Set 'Password' to the text in the 'password_box'
    Password = self.password_box.text
    # Set 'Enter your Password' to the text in the 'repswd_box'
    PasswordAgain = self.repswd_box.text


  def  button_1_click(self, **event_args):
    Name = self.name_box.text
    Email = self.email_box.text
    Phone = self.phone_box.text
    # Call your 'add_feedback' server function
    # pass in name, email and phone as arguments
    anvil.server.call('add_Signup', Name, Email, Phone)


  def button_1_click(self, **event_args):
    Name = self.name_box.text
    Email = self.email_box.text
    Phone = self.phone_box.text
    anvil.server.call('add_Signup', Name, Email, Phone)
    # Show a popup that says 'Feedback submitted!'
    Notification("Signed In!").show()

  def clear_inputs(self):
    # Clear our three text boxes
    self.name_box.text = ""
    self.email_box.text = ""
    self.phone_box.text = ""

  def button_1_click(self, **event_args):
    Name = self.name_box.text
    Email = self.email_box.text
    Phone = self.phone_box.text
    anvil.server.call('add_Signup', Name, Email, Phone)
    Notification("submitted!").show()
    # Call your 'clear_inputs' method to clear the boxes
    self.clear_inputs()