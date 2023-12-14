import anvil.server

# Get live fraud detection data
@anvil.server.callable
def get_fraud_data():
  # Retrieve and return fraud stats
  return {
    "transactions" : 10000,
    "fraud_transactions" : 203,
    "fraud_rate" : "2.03%"    
  }

# Client side Form code
class HomeForm(HomeFormTemplate):

  def __init__(self, **properties):
    # Set init properties from server function
    self.init_components(**properties)

    # Attach server function to button
    self.get_data_button.set_event_handler("click", self.get_data)

  # Retrieve fraud data  
  def get_data(self, **event_args):
    self.report_panel.visible = False
    fraud_data = anvil.server.call('get_fraud_data')
    
    self.transactions_label.text = "Total Transactions: " + str(fraud_data["transactions"])
    self.fraud_transactions_label.text ="Fraud Transactions: " + str(fra
