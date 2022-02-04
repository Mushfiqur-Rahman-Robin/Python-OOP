try:
    f = open(r"C:\Users\USER\Desktop\Project\Python+OOP\Corey Schafer's Python in-depth tutorial\Functions.py")
    #var = bad_var
    # if f.name == 'Dictionaries.py':
    #     raise Exception  # manually raising exception

except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:  # executes if only there is no exception
    print(f.read())
    f.close()
finally:
    print("Finally executing!")