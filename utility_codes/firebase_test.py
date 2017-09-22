import pyrebase

config = {
  "apiKey": " AIzaSyBHCAsvRwt-NMLsv4F1222SNXoQeyNQbzE ",
  "authDomain": "tweets11596.firebaseapp.com",
  "databaseURL": "https://tweets11596.firebaseio.com",
  "storageBucket": "tweets11596.appspot.com"
}

firebase = pyrebase.initialize_app(config)
firebase.auth()
# Get a reference to the database service
db = firebase.database()
# data to save
users = ["@sardesairajdeep","@BDUTT","@sagarikaghose","@vikramchandra","@asharma","@SachinKalbag","@madversity","@cricketwallah","@Kanchangupta","@rahulkanwal","@timesofindia","@ndtv","@IndiaToday","@IndianExpress","@the_hindu","@CNNnews18","@firstpost","@bsindia","@dna","@DeccanChronicle","@Oneindia","@FinancialXpress","@BreakingNews","@BBCBreaking","@cnnbrk","@WSJbreakingnews","@CBSNews"]
data = {}
blank = []
for name in users:
    data["users/" + name + "/"] = {"0" : 0}
print data
print type(data)
db.update({"users" : 0})
