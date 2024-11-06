import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# Sample car data and user storage
users = {}
cars = {
    1: {"name": "Sedan", "price": 20000, "specs": "4 seats, Automatic", "ratings": [], "purchases": []},
    2: {"name": "SUV", "price": 35000, "specs": "7 seats, 4x4", "ratings": [], "purchases": []},
    3: {"name": "Hatchback", "price": 15000, "specs": "5 seats, Manual", "ratings": [], "purchases": []}
}

# Sample discount offers
discount_offers = {
    "Summer Sale": {"threshold": 25000, "percentage": 10},
    "Sedan Special": {"car_id": 1, "fixed_discount": 2000},
    "New Year Discount": {"percentage": 15}
}

current_user = None
current_otp = None

# Signup functionality
def signup():
    username = entry_signup_username.get()
    password = entry_signup_password.get()
    if username in users:
        messagebox.showerror("Error", "Username already exists!")
    else:
        users[username] = {"password": password, "purchases": []}
        messagebox.showinfo("Success", f"Signup successful! Welcome, {username}")
        entry_signup_username.delete(0, tk.END)
        entry_signup_password.delete(0, tk.END)

# Signin functionality
def signin():
    global current_user
    username = entry_signin_username.get()
    password = entry_signin_password.get()
    if username in users and users[username]["password"] == password:
        current_user = username
        messagebox.showinfo("Success", f"Signin successful! Welcome back, {username}")
        show_home_page()
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# Show the list of available cars
def show_cars():
    car_list = "\n".join([f"{car_id}: {car['name']} - ${car['price']} | Specs: {car['specs']}" for car_id, car in cars.items()])
    messagebox.showinfo("Available Cars", car_list)

# Purchase a car functionality with OTP verification
def purchase_car():
    global current_otp
    if current_user is None:
        messagebox.showerror("Error", "Please sign in first.")
        return

    try:
        car_id = int(entry_car_id.get())
        payment_method = entry_payment_method.get()
        phone_number = entry_phone_number.get()

        if car_id in cars:
            send_otp()
            otp_input = simpledialog.askinteger("OTP Verification", "Enter the OTP sent to your phone:")

            if otp_input == current_otp:
                purchase_result = (
                    f"🎉 Purchase Confirmed! 🎉\n\n"
                    f"Thank you for your purchase, {current_user}!"
                )
                messagebox.showinfo("Purchase Result", purchase_result)
                entry_car_id.delete(0, tk.END)
                entry_payment_method.delete(0, tk.END)
                entry_phone_number.delete(0, tk.END)
                current_otp = None
            else:
                messagebox.showerror("Error", "Invalid OTP. Purchase canceled.")
        else:
            messagebox.showerror("Error", "Invalid car ID.")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid car ID.")

# Logout functionality
def logout():
    global current_user
    current_user = None
    messagebox.showinfo("Logout", "You have been logged out.")
    show_signin_page()

# Show the signin page
def show_signin_page():
    switch_frame(signin_frame)

# Home page after signin
def show_home_page():
    for widget in root.winfo_children():
        widget.pack_forget()
    home_frame.pack()

# Tkinter GUI setup
root = tk.Tk()
root.title("Car Showroom System")
root.configure(bg="lightblue")

# Frames with background color
main_menu_frame = tk.Frame(root, bg="lightblue")
signup_frame = tk.Frame(root, bg="lightblue")
signin_frame = tk.Frame(root, bg="lightblue")
home_frame = tk.Frame(root, bg="lightblue")

# Main Menu
label_main = tk.Label(main_menu_frame, text="Welcome to the Car Showroom System", font=("Arial", 18, "bold"), bg="lightblue")
button_signup = tk.Button(main_menu_frame, text="Signup", command=lambda: switch_frame(signup_frame))
button_signin = tk.Button(main_menu_frame, text="Signin", command=lambda: switch_frame(signin_frame))

label_main.pack(pady=20)
button_signup.pack(pady=10, ipadx=20, ipady=5)
button_signin.pack(pady=10, ipadx=20, ipady=5)
main_menu_frame.pack()

# Signup Frame
label_signup = tk.Label(signup_frame, text="Signup", font=("Arial", 16, "bold"), bg="lightblue")
label_signup_username = tk.Label(signup_frame, text="Username:", bg="lightblue")
entry_signup_username = tk.Entry(signup_frame, justify="center")
label_signup_password = tk.Label(signup_frame, text="Password:", bg="lightblue")
entry_signup_password = tk.Entry(signup_frame, show="*", justify="center")
button_signup_confirm = tk.Button(signup_frame, text="Signup", command=signup)
button_back_signup = tk.Button(signup_frame, text="Back", command=lambda: switch_frame(main_menu_frame))

label_signup.pack(pady=10)
label_signup_username.pack(pady=5)
entry_signup_username.pack(pady=5, ipadx=20, ipady=5)
label_signup_password.pack(pady=5)
entry_signup_password.pack(pady=5, ipadx=20, ipady=5)
button_signup_confirm.pack(pady=10, ipadx=20, ipady=5)
button_back_signup.pack(pady=5)

# Signin Frame
label_signin = tk.Label(signin_frame, text="Signin", font=("Arial", 16, "bold"), bg="lightblue")
label_signin_username = tk.Label(signin_frame, text="Username:", bg="lightblue")
entry_signin_username = tk.Entry(signin_frame, justify="center")
label_signin_password = tk.Label(signin_frame, text="Password:", bg="lightblue")
entry_signin_password = tk.Entry(signin_frame, show="*", justify="center")
button_signin_confirm = tk.Button(signin_frame, text="Signin", command=signin)
button_back_signin = tk.Button(signin_frame, text="Back", command=lambda: switch_frame(main_menu_frame))

label_signin.pack(pady=10)
label_signin_username.pack(pady=5)
entry_signin_username.pack(pady=5, ipadx=20, ipady=5)
label_signin_password.pack(pady=5)
entry_signin_password.pack(pady=5, ipadx=20, ipady=5)
button_signin_confirm.pack(pady=10, ipadx=20, ipady=5)
button_back_signin.pack(pady=5)

# Home Frame
label_home = tk.Label(home_frame, text="Home Page", font=("Arial", 18, "bold"), bg="lightblue")
button_view_cars = tk.Button(home_frame, text="View Cars", command=show_cars)
button_purchase_car = tk.Button(home_frame, text="Purchase Car", command=purchase_car)
button_logout = tk.Button(home_frame, text="Logout", command=logout)

label_home.pack(pady=20)
button_view_cars.pack(pady=10, ipadx=20, ipady=5)
button_purchase_car.pack(pady=10, ipadx=20, ipady=5)
button_logout.pack(pady=10, ipadx=20, ipady=5)

# Function to switch frames
def switch_frame(frame):
    for widget in root.winfo_children():
        widget.pack_forget()
    frame.pack(anchor="center")

# Show main menu initially
main_menu_frame.pack()
root.mainloop()
