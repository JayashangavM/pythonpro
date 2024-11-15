import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk
import random

# Sample Data with Indian Cars
cars = {
    "BMW Series 3": 4500000,
    "BMW X5": 6000000,
    "BMW Z4": 5000000,
    "Audi A4": 5500000,
    "Hyundai Creta": 1350000,
    "Ford Figo": 600000,
    "Maruti Suzuki Swift": 600000,
    "Tata Nexon": 800000,
}

users = {
    "admin": "password123"
}

bookings = {
    "admin": []
}

dealers = {
    "BMW": {
        "Delhi": ["BMW Delhi South", "BMW Delhi West"],
        "Mumbai": ["BMW Mumbai Central", "BMW Navi Mumbai"],
    }
}


class CarSalesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JD Car Sales")
        self.root.geometry("1800x800")
        self.otp = None  # Placeholder for OTP
        self.logged_in_user = None

        # Image Slider
        self.slider_images = [ImageTk.PhotoImage(Image.open(f"image{i}.png").resize((1800, 400), Image.LANCZOS)) for i in range(1, 4)]
        self.background_canvas = tk.Canvas(self.root, width=1800, height=400)
        self.background_canvas.pack(fill=tk.BOTH, expand=False)
        self.current_image_index = 0
        self.image_item = self.background_canvas.create_image(0, 0, anchor="nw", image=self.slider_images[self.current_image_index])
        self.update_image_slider()

        # Navbar
        self.navbar_frame = tk.Frame(self.root, bg="#003DA5")
        self.navbar_frame.pack(fill=tk.X)
        tk.Button(self.navbar_frame, text="Home", command=self.create_home_page, bg="#003DA5", fg="white", font=("Helvetica", 12), width=20).pack(side=tk.LEFT, padx=2)
        tk.Button(self.navbar_frame, text="Book Cars", command=self.create_booking_page, bg="#003DA5", fg="white", font=("Helvetica", 12), width=20).pack(side=tk.LEFT, padx=2)
        tk.Button(self.navbar_frame, text="Login", command=self.create_login_page, bg="#003DA5", fg="white", font=("Helvetica", 12), width=20).pack(side=tk.LEFT, padx=2)
        tk.Button(self.navbar_frame, text="Dealers", command=self.create_dealer_page, bg="#003DA5", fg="white", font=("Helvetica", 12), width=20).pack(side=tk.LEFT, padx=2)

        # Content Frame
        self.content_frame = tk.Frame(self.root, bg="#f5f5f5")
        self.content_frame.pack(fill=tk.BOTH, expand=True)
        self.create_home_page()

    def update_image_slider(self):
        self.current_image_index = (self.current_image_index + 1) % len(self.slider_images)
        self.background_canvas.itemconfig(self.image_item, image=self.slider_images[self.current_image_index])
        self.root.after(4000, self.update_image_slider)

    def create_home_page(self):
        self.clear_frame()
        tk.Label(self.content_frame, text="𝙹𝘿 𝘾𝙖𝙧 𝙨𝙖𝙡𝙚𝙨🏎️", font=("Helvetica", 24, "bold"), bg="#003DA5", fg="white").pack(pady=20, fill=tk.X)
        tk.Label(self.content_frame, text="Available Cars and Prices:", font=("Helvetica", 18), bg="#f5f5f5", fg="#333").pack(pady=10)

        car_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
        car_frame.pack(pady=20)
        for car, price in cars.items():
            car_item = tk.Frame(car_frame, bg="#e0e0e0", padx=20, pady=10)
            car_item.pack(side=tk.LEFT, padx=10)
            tk.Label(car_item, text=car, font=("Helvetica", 16, "bold"), bg="#e0e0e0").pack()
            tk.Label(car_item, text=f"₹{price:,}", font=("Helvetica", 14), bg="#e0e0e0", fg="#555").pack()

    def create_booking_page(self):
        self.clear_frame()
        tk.Label(self.content_frame, text="Booking Section", font=("Helvetica", 24, "bold"), bg="#003DA5", fg="white").pack(pady=20, fill=tk.X)
        booking_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
        booking_frame.pack(pady=20)

        tk.Label(booking_frame, text="Name", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.name_entry = tk.Entry(booking_frame, width=30, font=("Helvetica", 14))
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(booking_frame, text="Mobile Number", bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.mobile_entry = tk.Entry(booking_frame, width=30, font=("Helvetica", 14))
        self.mobile_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(booking_frame, text="Select Car", bg="#f5f5f5").grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.car_combobox = ttk.Combobox(booking_frame, values=list(cars.keys()), width=30, font=("Helvetica", 14))
        self.car_combobox.grid(row=2, column=1, padx=10, pady=5)

        tk.Label(booking_frame, text="Enter OTP", bg="#f5f5f5").grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.otp_entry = tk.Entry(booking_frame, width=30, font=("Helvetica", 14))
        self.otp_entry.grid(row=3, column=1, padx=10, pady=5)

        tk.Button(booking_frame, text="Generate OTP", command=self.generate_otp, bg="#003DA5", fg="white", font=("Helvetica", 14), width=20).grid(row=4, column=0, pady=10, sticky="e")
        tk.Button(booking_frame, text="Book Now", command=self.verify_otp_and_book, bg="#003DA5", fg="white", font=("Helvetica", 14), width=20).grid(row=4, column=1, pady=10, sticky="w")

    def generate_otp(self):
        self.otp = str(random.randint(1000, 9999))
        messagebox.showinfo("OTP Generated", f"Your OTP is: {self.otp}")

    def verify_otp_and_book(self):
        entered_otp = self.otp_entry.get()
        if entered_otp == self.otp:
            self.book_car()
        else:
            messagebox.showerror("Invalid OTP", "The OTP entered is incorrect.")

    def book_car(self):
        name = self.name_entry.get()
        mobile = self.mobile_entry.get()
        car = self.car_combobox.get()
        if name and mobile and car:
            bookings["admin"].append({"name": name, "mobile": mobile, "car": car})
            messagebox.showinfo("Success", f"Booking Successful for {car}")
            self.create_home_page()
        else:
            messagebox.showwarning("Incomplete Information", "Please fill in all the details.")

    def create_login_page(self):
        self.clear_frame()
        tk.Label(self.content_frame, text="Login Page", font=("Helvetica", 24, "bold"), bg="#003DA5", fg="white").pack(pady=20, fill=tk.X)

        login_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
        login_frame.pack(pady=20)

        tk.Label(login_frame, text="Username", bg="#f5f5f5").grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.username_entry = tk.Entry(login_frame, width=30, font=("Helvetica", 14))
        self.username_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(login_frame, text="Password", bg="#f5f5f5").grid(row=1, column=0, padx=10, pady=5, sticky="e")
        self.password_entry = tk.Entry(login_frame, width=30, font=("Helvetica", 14), show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Button(login_frame, text="Login", command=self.login, bg="#003DA5", fg="white", font=("Helvetica", 14), width=20).grid(row=2, column=0, columnspan=2, pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if username in users and users[username] == password:
            self.logged_in_user = username
            self.display_booking_details()
        else:
            messagebox.showerror("Login Failed", "Invalid Username or Password")

    def display_booking_details(self):
        self.clear_frame()
        tk.Label(self.content_frame, text="Booking Details", font=("Helvetica", 24, "bold"), bg="#003DA5", fg="white").pack(pady=20, fill=tk.X)

        if self.logged_in_user in bookings and bookings[self.logged_in_user]:
            for booking in bookings[self.logged_in_user]:
                tk.Label(self.content_frame, text=f"Name: {booking['name']}", font=("Helvetica", 14), bg="#f5f5f5").pack(anchor="w", padx=10)
                tk.Label(self.content_frame, text=f"Mobile: {booking['mobile']}", font=("Helvetica", 14), bg="#f5f5f5").pack(anchor="w", padx=10)
                tk.Label(self.content_frame, text=f"Car: {booking['car']}", font=("Helvetica", 14), bg="#f5f5f5").pack(anchor="w", padx=10)
                tk.Label(self.content_frame, text="-" * 50, bg="#f5f5f5").pack(fill=tk.X, pady=5)
        else:
            tk.Label(self.content_frame, text="No bookings found.", font=("Helvetica", 14), bg="#f5f5f5").pack()

    def create_dealer_page(self):
        self.clear_frame()
        tk.Label(self.content_frame, text="Dealer Information", font=("Helvetica", 24, "bold"), bg="#003DA5", fg="white").pack(pady=20, fill=tk.X)

        dealer_frame = tk.Frame(self.content_frame, bg="#f5f5f5")
        dealer_frame.pack(pady=20)

        for city, locations in dealers["BMW"].items():
            city_frame = tk.Frame(dealer_frame, bg="#f5f5f5")
            city_frame.pack(pady=10, fill=tk.X)
            tk.Label(city_frame, text=city, font=("Helvetica", 16, "bold"), bg="#f5f5f5").pack(anchor="w")
            for location in locations:
                tk.Label(city_frame, text=location, font=("Helvetica", 14), bg="#f5f5f5").pack(anchor="w")

    def clear_frame(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = CarSalesApp(root)
    root.mainloop()
