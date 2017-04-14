def convertString(string):

    if type(string) is str:
        try:
            int(string)
            print("String is now int")
            return string

        except:

            try:
                float(string)
                print("String is now float")
                return string

            except:
                print("Cannot convert.")
                return string
    else:
        print("Input is not a string")
        return
