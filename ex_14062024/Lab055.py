def allowed_to_attain_class(name):
    match name:

        case "Dell":
            print("Dell is allowed")
        case "Shubham":
            print("Shubham is allowed")
        case "Pallavi":
            print("Pallavi is allowed")
        case _:
            print("Not allowed")


allowed_to_attain_class("Shubham")
