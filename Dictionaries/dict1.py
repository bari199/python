frontend = {
    "name":"anil",
    "version":"1.0.3",
    "dependencies":"10.2.3",
    "tailwind":"1.0.6",
    "magic-ui":"1.2.6",
    "material-ui":"4.1.0",
    "react":"3.4.5",
    "react-router-dom":"4.5.2",
    "react-create":"4.4.9",
    "bootstrap5":"2.4.3",
    "motion-ui":"1.19.0",
    "toast":"8.2.0"
}

backend ={
     "name":"rajib",
     "version":"2.3.4",
     "dependencies":"12.3.4",
     "mongodb":"13.6.3",
     "cors":"2.8.5",
     "jsonwebtoken":"8.5.1",
     "redux":"3.6.5",
     "express":"4.17.1",
     "nodemon":"2.0.7",
     "bcryptjs":"2.4.3",
     "body-parser":"1.19.0",
     "dotenv":"10.0.0",
     "nodemailer":"6.4.18",
     "twilo":"4.5.1",
}
for key, value in frontend.items():
        if key=="react":
            print(key,":", value)
for key, value in backend.items():
    if key == "mongodb" and value == "1.0.6":
        print("Matched →", key, value)

formulaz = frontend

frontend.clear()
print("After clearing frontend:", frontend)
