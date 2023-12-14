import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

@anvil.server.callable
def add_signup(Name, Email, Phone):
  app_tables.signup.add_row(
    Name=Name, 
    Email=Email, 
    Phone=Phone, 
    # Date_and_Time=Date_and_Time.now()
  )

# @anvil.server.callable
# def add_feedback(name, email, feedback):
#   app_tables.signup.add_row(
#     Name=Name, 
#     Email=Email, 
#     Phone=Phone, 
#     Date_and_Time=Date_and_Time.now()
#   )
  # Send yourself an email each time feedback is submitted
  anvil.email.send(#to="noreply@anvil.works", # Change this to your email address!
                   subject=f"Sign up from {Name}",
                   text=f""" A new person has Signed up! Name: {Name} Email address: {Email} Phone: {Phone} """)


# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
