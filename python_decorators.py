def main(func):
    def sun():
        print("inside sub func")
        func()
    print("inside main func")
    return sun

@main
def call_sun():
    print("inside call_sun func")

call_sun()