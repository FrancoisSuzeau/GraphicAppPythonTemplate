from packages import application, functions

if __name__ == "__main__":
    MyApp = application.App()

    MyApp.create_canva()
    MyApp.mainloop()