from imutils import paths
import numpy as np
import argparse
import imutils
import pickle
import cv2
import os
from os import listdir
from os.path import isfile, join
from pathlib import Path
from collections import Counter
# import the necessary packages
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from imutils.video import VideoStream
from imutils.video import FPS
import time
from tkinter import *
from tkinter import messagebox
import sqlite3
import pandas as pd
from PIL import Image, ImageTk
import tkinter as tk
import pandas as pd


ARIAL = ("arial",10,"bold")

class BankUi:
    def __init__(self,root):
        self.root = root
        # Modern color scheme
        self.bg_color = "#1a237e"  # Deep blue background
        self.button_color = "#4a90e2"  # Modern blue for buttons
        self.text_color = "#ffffff"  # White text
        self.input_bg = "#f5f5f5"  # Light gray for input fields
        
        self.header = Label(self.root, text="GIET BANK OF INDIA", bg=self.bg_color, fg=self.text_color, 
                           font=("arial", 24, "bold"), pady=15)
        self.header.pack(fill=X)
        
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        root.geometry("1000x600")
        
        # Enhanced welcome button
        self.button1 = Button(self.frame, text="Click to begin", bg=self.button_color, fg=self.text_color,
                            font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                            command=self.begin_page)
        self.q = Button(self.frame, text="Quit", bg="#e57373", fg=self.text_color,
                       font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                       command=self.root.destroy)
        
        # Centered layout with proper spacing
        self.button1.place(relx=0.5, rely=0.4, width=300, height=50, anchor=CENTER)
        self.q.place(relx=0.5, rely=0.5, width=200, height=40, anchor=CENTER)
        
        self.countter = 2
        self.frame.pack(fill=BOTH, expand=True)
   
    def begin_page(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        root.geometry("1000x600")
    
        # Create a container for buttons
        button_frame = Frame(self.frame, bg=self.bg_color)
        button_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    
        # Enhanced buttons with consistent styling
        self.enroll = Button(button_frame, text="Enroll", bg=self.button_color, fg=self.text_color,
                            font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                            width=20, height=2, command=self.enroll_user)
        self.withdraw = Button(button_frame, text="Continue Banking", bg=self.button_color, fg=self.text_color,
                              font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                              width=20, height=2, command=self.withdraw_money_page)
        self.q = Button(button_frame, text="Quit", bg="#e57373", fg=self.text_color,
                       font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                       width=15, height=1, command=self.root.destroy)
    
        # Vertical layout with proper spacing
        self.enroll.pack(pady=10)
        self.withdraw.pack(pady=10)
        self.q.pack(pady=20)
        self.frame.pack(fill=BOTH, expand=True)
    
    def final_page(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a container for the main content
        main_container = Frame(self.frame, bg=self.bg_color)
        main_container.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        # Title
        title = Label(main_container, text="ATM Operations", bg=self.bg_color, fg=self.text_color,
                     font=("Helvetica", 24, "bold"))
        title.pack(pady=(0, 30))
        
        # Create a grid layout for transaction buttons
        button_frame = Frame(main_container, bg=self.bg_color)
        button_frame.pack()
        
        # Button style configuration
        button_width = 20
        button_height = 2
        button_font = ("Helvetica", 12, "bold")
        button_padding = 15
        
        # Enhanced transaction buttons with hover effect
        self.detail = Button(button_frame, text="Transfer", bg=self.button_color, fg=self.text_color,
                            font=button_font, cursor="hand2", relief=FLAT,
                            width=button_width, height=button_height,
                            command=self.user_account_transfer)
        self.enquiry = Button(button_frame, text="Balance Enquiry", bg=self.button_color, fg=self.text_color,
                             font=button_font, cursor="hand2", relief=FLAT,
                             width=button_width, height=button_height,
                             command=self.user_balance)
        self.deposit = Button(button_frame, text="Deposit Money", bg=self.button_color, fg=self.text_color,
                             font=button_font, cursor="hand2", relief=FLAT,
                             width=button_width, height=button_height,
                             command=self.user_deposit_money)
        self.withdrawl = Button(button_frame, text="Withdrawal Money", bg=self.button_color, fg=self.text_color,
                               font=button_font, cursor="hand2", relief=FLAT,
                               width=button_width, height=button_height,
                               command=self.user_withdrawl_money)
        
        # Grid layout for transaction buttons with padding
        self.detail.grid(row=0, column=0, padx=button_padding, pady=button_padding)
        self.enquiry.grid(row=0, column=1, padx=button_padding, pady=button_padding)
        self.deposit.grid(row=1, column=0, padx=button_padding, pady=button_padding)
        self.withdrawl.grid(row=1, column=1, padx=button_padding, pady=button_padding)
        
        # Logout button at the bottom
        self.q = Button(main_container, text="Log out", bg="#e57373", fg=self.text_color,
                       font=button_font, cursor="hand2", relief=FLAT,
                       width=15, height=1, command=self.begin_page)
        self.q.pack(pady=(30, 0))
        
        self.frame.pack(fill=BOTH, expand=True)

    
    def enroll_user(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a form container
        form_frame = Frame(self.frame, bg=self.bg_color)
        form_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Enhanced form components
        self.userlabel = Label(form_frame, text="Full Name", bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.uentry = Entry(form_frame, bg=self.input_bg, font=("arial", 11),
                           highlightcolor=self.button_color,
                           highlightthickness=2,
                           highlightbackground=self.text_color)
        
        self.plabel = Label(form_frame, text="Password", bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.pentry = Entry(form_frame, bg=self.input_bg, show="*", font=("arial", 11),
                           highlightcolor=self.button_color,
                           highlightthickness=2,
                           highlightbackground=self.text_color)
        
        self.button1 = Button(form_frame, text="Next", bg=self.button_color, fg=self.text_color,
                             font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                             command=self.enroll_and_move_to_next_screen)
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.begin_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.userlabel.pack(pady=(0, 5))
        self.uentry.pack(pady=(0, 15), ipadx=50, ipady=5)
        self.plabel.pack(pady=(0, 5))
        self.pentry.pack(pady=(0, 20), ipadx=50, ipady=5)
        self.button1.pack(pady=(0, 20), ipadx=40, ipady=5)
        
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.frame.pack(fill=BOTH, expand=True)

    def password_verification(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        print(self.real_user)
        
        # Create a centered container frame
        container = Frame(self.frame, bg=self.bg_color, padx=40, pady=40)
        container.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        # Title with modern styling
        title = Label(container, 
                     text="Password Verification",
                     bg=self.bg_color,
                     fg=self.text_color,
                     font=("Helvetica", 24, "bold"))
        title.pack(pady=(0, 20))
        
        # Password label with improved typography
        self.plabel = Label(container, 
                           text="Please enter your account password",
                           bg=self.bg_color,
                           fg=self.text_color,
                           font=("Helvetica", 14))
        self.plabel.pack(pady=(0, 10))
        
        # Enhanced password entry field
        self.givenpentry = Entry(container,
                                bg=self.input_bg,
                                show="•",
                                font=("Helvetica", 12),
                                width=30,
                                highlightcolor=self.button_color,
                                highlightthickness=2,
                                highlightbackground=self.text_color,
                                relief=FLAT)
        self.givenpentry.pack(pady=(0, 20))
        
        # Button container for better layout
        button_frame = Frame(container, bg=self.bg_color)
        button_frame.pack(pady=(10, 0))
        
        # Styled buttons
        self.button1 = Button(button_frame,
                            text="Verify",
                            bg=self.button_color,
                            fg=self.text_color,
                            font=("Helvetica", 12, "bold"),
                            width=10,
                            relief=FLAT,
                            cursor="hand2",
                            command=self.verify_user)
        self.button1.pack(side=LEFT, padx=5)
        
        self.b = Button(button_frame,
                       text="Back",
                       bg=self.button_color,
                       fg=self.text_color,
                       font=("Helvetica", 12),
                       width=10,
                       relief=FLAT,
                       cursor="hand2",
                       command=self.begin_page)
        self.b.pack(side=LEFT, padx=5)
        
        self.q = Button(button_frame,
                       text="Quit",
                       bg="#e57373",
                       fg=self.text_color,
                       font=("Helvetica", 12),
                       width=10,
                       relief=FLAT,
                       cursor="hand2",
                       command=self.root.destroy)
        self.q.pack(side=LEFT, padx=5)
        
        self.frame.pack(fill=BOTH, expand=True)
        
        # Create a form container
        form_frame = Frame(self.frame, bg=self.bg_color)
        form_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Enhanced verification form
        self.plabel = Label(form_frame, text="Please enter your account password",
                           bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.givenpentry = Entry(form_frame, bg=self.input_bg, show="*", font=("arial", 11),
                                highlightcolor=self.button_color,
                                highlightthickness=2,
                                highlightbackground=self.text_color)
        
        self.button1 = Button(form_frame, text="Verify", bg=self.button_color, fg=self.text_color,
                             font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                             command=self.verify_user)
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.begin_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.plabel.pack(pady=(0, 15))
        self.givenpentry.pack(pady=(0, 20), ipadx=50, ipady=5)
        self.button1.pack(pady=(0, 20), ipadx=40, ipady=5)
        
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.frame.pack(fill=BOTH, expand=True)

    def enroll_and_move_to_next_screen(self):
        name = self.uentry.get()
        password = self.pentry.get()
        if not name and not password:
            messagebox._show("Error", "You need a name to enroll an account and you need to input a password!")
            self.enroll_user()
        elif not password:
            messagebox._show("Error", "You need to input a password!")
            self.enroll_user()
        elif not name:
            messagebox._show("Error", "You need a name to enroll an account!")
            self.enroll_user()
        elif len(password) < 8:
            messagebox._show("Password Error", "Your password needs to be at least 8 digits!")
            self.enroll_user()
        else:
            self.write_to_csv()
            self.video_capture_page()

    def password_verification(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        print(self.real_user)
        
        # Create a form container
        form_frame = Frame(self.frame, bg=self.bg_color)
        form_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Enhanced verification form
        self.plabel = Label(form_frame, text="Please enter your account password",
                           bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.givenpentry = Entry(form_frame, bg=self.input_bg, show="*", font=("arial", 11),
                                highlightcolor=self.button_color,
                                highlightthickness=2,
                                highlightbackground=self.text_color)
        
        self.button1 = Button(form_frame, text="Verify", bg=self.button_color, fg=self.text_color,
                             font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                             command=self.verify_user)
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.begin_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.plabel.pack(pady=(0, 15))
        self.givenpentry.pack(pady=(0, 20), ipadx=50, ipady=5)
        self.button1.pack(pady=(0, 20), ipadx=40, ipady=5)
        
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.frame.pack(fill=BOTH, expand=True)

    def verify_user(self):
        data = pd.read_csv('bank_details.csv')
        self.gottenpassword = data[data.loc[:,'unique_id'] == self.real_user].loc[:,'password'].values[0]
        #print(str(self.givenpentry.get()))
        print(str(self.gottenpassword))
        if str(self.givenpentry.get()) == str(self.gottenpassword):
            messagebox._show("Verification Info!", "Verification Successful!")
            self.final_page()
        else:
            messagebox._show("Verification Info!", "Verification Failed")
            self.begin_page()

   
   
   
    def final_page(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a container for the main content
        main_container = Frame(self.frame, bg=self.bg_color)
        main_container.place(relx=0.5, rely=0.5, anchor=CENTER)
        
        # Title
        title = Label(main_container, text="ATM Operations", bg=self.bg_color, fg=self.text_color,
                     font=("Helvetica", 24, "bold"))
        title.pack(pady=(0, 30))
        
        # Create a grid layout for transaction buttons
        button_frame = Frame(main_container, bg=self.bg_color)
        button_frame.pack()
        
        # Button style configuration
        button_width = 20
        button_height = 2
        button_font = ("Helvetica", 12, "bold")
        button_padding = 15
        
        # Enhanced transaction buttons with hover effect
        self.detail = Button(button_frame, text="Transfer", bg=self.button_color, fg=self.text_color,
                            font=button_font, cursor="hand2", relief=FLAT,
                            width=button_width, height=button_height,
                            command=self.user_account_transfer)
        self.enquiry = Button(button_frame, text="Balance Enquiry", bg=self.button_color, fg=self.text_color,
                             font=button_font, cursor="hand2", relief=FLAT,
                             width=button_width, height=button_height,
                             command=self.user_balance)
        self.deposit = Button(button_frame, text="Deposit Money", bg=self.button_color, fg=self.text_color,
                             font=button_font, cursor="hand2", relief=FLAT,
                             width=button_width, height=button_height,
                             command=self.user_deposit_money)
        self.withdrawl = Button(button_frame, text="Withdrawal Money", bg=self.button_color, fg=self.text_color,
                               font=button_font, cursor="hand2", relief=FLAT,
                               width=button_width, height=button_height,
                               command=self.user_withdrawl_money)
        
        # Grid layout for transaction buttons with padding
        self.detail.grid(row=0, column=0, padx=button_padding, pady=button_padding)
        self.enquiry.grid(row=0, column=1, padx=button_padding, pady=button_padding)
        self.deposit.grid(row=1, column=0, padx=button_padding, pady=button_padding)
        self.withdrawl.grid(row=1, column=1, padx=button_padding, pady=button_padding)
        
        # Logout button at the bottom
        self.q = Button(main_container, text="Log out", bg="#e57373", fg=self.text_color,
                       font=button_font, cursor="hand2", relief=FLAT,
                       width=15, height=1, command=self.begin_page)
        self.q.pack(pady=(30, 0))
        
        self.frame.pack(fill=BOTH, expand=True)

    
    def user_account_transfer(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a form container
        form_frame = Frame(self.frame, bg=self.bg_color)
        form_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Enhanced transfer form
        self.label11 = Label(form_frame, text="Please enter the recipient's account number",
                           bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.entry11 = Entry(form_frame, bg=self.input_bg, font=("arial", 11),
                            highlightcolor=self.button_color,
                            highlightthickness=2,
                            highlightbackground=self.text_color)
        
        self.label21 = Label(form_frame, text="Please enter the amount to be transferred",
                           bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.entry21 = Entry(form_frame, bg=self.input_bg, font=("arial", 11),
                            highlightcolor=self.button_color,
                            highlightthickness=2,
                            highlightbackground=self.text_color)
        
        self.button1 = Button(form_frame, text="Transfer", bg=self.button_color, fg=self.text_color,
                             font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                             command=self.user_account_transfer_transc)
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.final_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.label11.pack(pady=(0, 5))
        self.entry11.pack(pady=(0, 15), ipadx=50, ipady=5)
        self.label21.pack(pady=(0, 5))
        self.entry21.pack(pady=(0, 15), ipadx=50, ipady=5)
        self.button1.pack(pady=(0, 20), ipadx=40, ipady=5)
        
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.frame.pack(fill=BOTH, expand=True)
        

    def user_account_transfer_transc(self):
        data = pd.read_csv('bank_details.csv')
        if int(self.entry11.get()) not in data['account_number'].values:
             messagebox._show("Transfer Info!", "Invalid account number") 
        elif int(self.entry11.get()) == self.real_user:
            messagebox._show("Transfer Info!", "Sorry, you cannot make a transfer to yourself")
        elif int(self.entry21.get()) >= data[data.loc[:,'unique_id'] == self.real_user].loc[:,'account_balance'].values[0]:
            messagebox._show("Transfer Info!", "Insufficient Funds") 
        else:
            data = pd.read_csv('bank_details.csv')
            update_data = data.set_index('account_number')
            update_data.loc[int(self.entry11.get()),'account_balance'] += int(self.entry21.get())
            update_data.loc[data[data.loc[:,'unique_id'] == self.real_user].loc[:,'account_number'].values[0],'account_balance'] -= int(self.entry21.get())
            update_data['account_number'] = update_data.index
            update_data.reset_index(drop = True, inplace= True)
            update_data = update_data.reindex(labels = ['unique_id','account_number','name','bank', 'password','account_balance'], axis = 1)
            update_data.to_csv('bank_details.csv',index = None)
            messagebox._show("Transfer Info!", "Successfully Transferred")

    def user_balance(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a container for balance display
        balance_frame = Frame(self.frame, bg=self.bg_color)
        balance_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Get and display balance
        data = pd.read_csv('bank_details.csv')
        text = data[data.loc[:,'unique_id'] == self.real_user].loc[:,'account_balance'].values[0]
        
        self.label = Label(balance_frame, 
                          text='Current Account Balance: ₹' + str(text),
                          bg=self.bg_color,
                          fg=self.text_color,
                          font=("arial", 16, "bold"))
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.final_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.label.pack(pady=20)
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.frame.pack(fill=BOTH, expand=True)

    def user_deposit_money(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a form container
        form_frame = Frame(self.frame, bg=self.bg_color)
        form_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Enhanced deposit form
        self.label = Label(form_frame, text="Enter amount to deposit",
                          bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.money_box = Entry(form_frame, bg=self.input_bg, font=("arial", 11),
                              highlightcolor=self.button_color,
                              highlightthickness=2,
                              highlightbackground=self.text_color)
        self.submitButton = Button(form_frame, text="Deposit",
                                  bg=self.button_color, fg=self.text_color,
                                  font=("arial", 12, "bold"), cursor="hand2", relief=FLAT)
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.final_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.label.pack(pady=(0, 15))
        self.money_box.pack(pady=(0, 20), ipadx=50, ipady=5)
        self.submitButton.pack(pady=(0, 20), ipadx=40, ipady=5)
        
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.submitButton.bind("<Button-1>", self.user_deposit_trans)
        self.frame.pack(fill=BOTH, expand=True)

    def user_deposit_trans(self,flag):
        data = pd.read_csv('bank_details.csv')
        data = pd.read_csv('bank_details.csv')
        update_data = data.set_index('unique_id')
        update_data.loc[self.real_user,'account_balance'] += int(self.money_box.get())
        update_data.reset_index(inplace=True)
        update_data.columns = ['unique_id','account_number','name','bank', 'password','account_balance']
        update_data.to_csv('bank_details.csv',index = None)
        messagebox._show("Deposit Info!", "Successfully Deposited!") 

    def withdraw_money_page(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a form container
        form_frame = Frame(self.frame, bg=self.bg_color)
        form_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Enhanced verification form
        self.plabel = Label(form_frame, text="Please enter your account number",
                           bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.account_entry = Entry(form_frame, bg=self.input_bg, font=("arial", 11),
                                highlightcolor=self.button_color,
                                highlightthickness=2,
                                highlightbackground=self.text_color)
        
        self.button1 = Button(form_frame, text="Proceed", bg=self.button_color, fg=self.text_color,
                             font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                             command=self.video_check)
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.begin_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.plabel.pack(pady=(0, 15))
        self.account_entry.pack(pady=(0, 20), ipadx=50, ipady=5)
        self.button1.pack(pady=(0, 20), ipadx=40, ipady=5)
        
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.frame.pack(fill=BOTH, expand=True)

    def user_withdrawl_money(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg=self.bg_color, width=1000, height=600)
        
        # Create a form container
        form_frame = Frame(self.frame, bg=self.bg_color)
        form_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
        
        # Enhanced withdrawal form
        self.label1 = Label(form_frame, text="Please enter the amount to withdraw",
                           bg=self.bg_color, fg=self.text_color, font=("arial", 12, "bold"))
        self.entry1 = Entry(form_frame, bg=self.input_bg, font=("arial", 11),
                           highlightcolor=self.button_color,
                           highlightthickness=2,
                           highlightbackground=self.text_color)
        self.button1 = Button(form_frame, text="Withdraw", bg=self.button_color, fg=self.text_color,
                             font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                             command=self.process_withdrawal)
        
        # Navigation buttons
        nav_frame = Frame(self.frame, bg=self.bg_color)
        nav_frame.place(relx=0.5, rely=0.8, anchor=CENTER)
        
        self.b = Button(nav_frame, text="Back", bg=self.button_color, fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.final_page)
        self.q = Button(nav_frame, text="Quit", bg="#e57373", fg=self.text_color,
                        font=("arial", 12, "bold"), cursor="hand2", relief=FLAT,
                        command=self.root.destroy)
        
        # Layout with proper spacing
        self.label1.pack(pady=(0, 15))
        self.entry1.pack(pady=(0, 20), ipadx=50, ipady=5)
        self.button1.pack(pady=(0, 20), ipadx=40, ipady=5)
        
        self.b.pack(side=LEFT, padx=10)
        self.q.pack(side=LEFT, padx=10)
        
        self.frame.pack(fill=BOTH, expand=True)
    
    def process_withdrawal(self):
        try:
            withdrawal_amount = int(self.entry1.get())
            data = pd.read_csv('bank_details.csv')
            current_balance = data[data.loc[:,'unique_id'] == self.real_user].loc[:,'account_balance'].values[0]
            
            if withdrawal_amount <= 0:
                messagebox._show("Withdrawal Info!", "Please enter a valid amount")
            elif withdrawal_amount > current_balance:
                messagebox._show("Withdrawal Info!", "Insufficient funds")
            else:
                # Update balance
                update_data = data.copy()
                update_data.loc[data['unique_id'] == self.real_user, 'account_balance'] -= withdrawal_amount
                update_data.to_csv('bank_details.csv', index=None)
                messagebox._show("Withdrawal Info!", f"Successfully withdrawn {withdrawal_amount}")
                self.final_page()
        except ValueError:
            messagebox._show("Withdrawal Info!", "Please enter a valid number")
   
   
   
    def write_to_csv(self):
        import csv
        from random import randint
        n = 10;range_start = 10**(n-1);range_end = (10**n)-1
        account_number = randint(range_start, range_end)
        n = 5;range_start = 10**(n-1);range_end = (10**n)-1
        unique_id = randint(range_start, range_end)
        bank = "GIET Bank of India"
        account_balance = "10000"
        name = self.uentry.get()
        password = self.pentry.get()
        with open(r'bank_details.csv','a',newline = '\n') as f:
            writer = csv.writer(f)
            writer.writerow([unique_id,account_number,name,bank, password, account_balance])
        messagebox._show("Enrollment Info!", "Successfully Enrolled!")    

    def video_capture_page(self):
        self.frame.destroy()
        self.frame = Frame(self.root, bg="#1a237e", width=900, height=600)
        
        # Create a header frame
        header_frame = Frame(self.frame, bg="#283593", width=900, height=60)
        header_frame.place(x=0, y=0)
        header_label = Label(header_frame, text="Face Capture", bg="#283593", fg="white", font=("Arial", 20, "bold"))
        header_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Add instructions panel
        instructions_frame = Frame(self.frame, bg="#283593", width=700, height=200)
        instructions_frame.place(x=100, y=80)
        
        instructions_text = """
        Face Capture Instructions:
        1. Position your face within the green circle
        2. Look directly at the camera
        3. Ensure good lighting
        4. Keep a neutral expression
        5. Press SPACE to capture (5 photos needed)
        Press ESC to cancel
        """
        
        instructions_label = Label(instructions_frame, 
                                 text=instructions_text,
                                 bg="#283593", 
                                 fg="white",
                                 font=("Arial", 12),
                                 justify=LEFT)
        instructions_label.place(relx=0.5, rely=0.5, anchor="center")
        
        # Modern styled capture button
        button_frame = Frame(self.frame, bg="#1a237e", width=700, height=60)
        button_frame.place(x=100, y=350)
        
        self.button = Button(button_frame, 
                            text="Start Camera", 
                            bg="#4caf50", 
                            fg="white",
                            font=("Arial", 12, "bold"), 
                            command=self.captureuser,
                            relief="flat", 
                            cursor="hand2")
        self.button.place(relx=0.5, rely=0.5, width=200, height=40, anchor="center")
        
        self.frame.pack(fill=BOTH, expand=True)

    def captureuser(self):
        data = pd.read_csv('bank_details.csv')
        name = data.loc[:,'unique_id'].values[-1]
        
        # Ensure dataset directory exists
        try:
            os.makedirs('dataset', exist_ok=True)
            os.makedirs(f'dataset/{name}', exist_ok=True)
        except Exception as e:
            messagebox.showerror("Error", f"Failed to create directories: {str(e)}")
            return

        cam = cv2.VideoCapture(0)
        if not cam.isOpened():
            messagebox.showerror("Camera Error", "Failed to open camera. Please check if camera is connected.")
            return

        cv2.namedWindow("Face Capture", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Face Capture", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        def draw_guide(frame):
            height, width = frame.shape[:2]
            center = (width // 2, height // 2)
            radius = min(width, height) // 3
            cv2.circle(frame, center, radius, (0, 255, 0), 2)
            return frame

        img_counter = 0
        while True:
            ret, frame = cam.read()
            if not ret:
                messagebox.showerror("Camera Error", "Failed to capture frame. Please check your camera.")
                break
                
            frame = draw_guide(frame)
            cv2.imshow("Face Capture", frame)
            
            if img_counter == 5:
                cv2.destroyWindow("Face Capture")
                messagebox.showinfo("Success", "Face capture completed successfully!")
                break
                
            k = cv2.waitKey(1)

            if k%256 == 27:  # ESC pressed
                print("Escape hit, closing...")
                break
            elif k%256 == 32:  # SPACE pressed
                try:
                    img_name = f"{img_counter}.jpg"
                    save_path = os.path.join('dataset', str(name), img_name)
                    cv2.imwrite(save_path, frame)
                    print(f"Saved {save_path}")
                    img_counter += 1
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to save image: {str(e)}")

        cam.release()
        cv2.destroyAllWindows()
       
        try:
            self.get_embeddings()
            self.train_model()
            messagebox.showinfo('Registration Info', 'Face ID Successfully Registered!')
        except Exception as e:
            messagebox.showerror("Error", f"Failed to process face data: {str(e)}")
            return
            
        self.begin_page()



    def get_embeddings(self):
        #summary:
        # construct the argument parser and parse the arguments
        ap = argparse.ArgumentParser()
        ap.add_argument("-i", "--dataset", required=True,
            help="path to input directory of faces + images")
        ap.add_argument("-e", "--embeddings", required=True,
            help="path to output serialized db of facial embeddings")
        ap.add_argument("-d", "--detector", required=True,
            help="path to OpenCV's deep learning face detector")
        ap.add_argument("-m", "--embedding-model", required=True,
            help="path to OpenCV's deep learning face embedding model")
        ap.add_argument("-c", "--confidence", type=float, default=0.5,
            help="minimum probability to filter weak detections")
        #args = vars(ap.parse_args())
       
        # load our serialized face detector from disk
        print("[INFO] loading face detector...")

        detector = cv2.dnn.readNetFromCaffe('face_detection_model/deploy.prototxt', 'face_detection_model/res10_300x300_ssd_iter_140000.caffemodel')
        # load our serialized face embedding model from disk
        embedder = cv2.dnn.readNetFromTorch('nn4.small2.v1.t7')
        #embedder = cv2.dnn.readNetFromTorch('openface_nn4.small2.v1.t7')

        # grab the paths to the input images in our dataset
        print("[INFO] quantifying faces...")
        imagePaths = list(paths.list_images('dataset'))
        # initialize our lists of extracted facial embeddings and
        # corresponding people names
        knownEmbeddings = []
        knownNames = []
        # initialize the total number of faces processed
        total = 0
        # loop over the image paths
        for (i, imagePath) in enumerate(imagePaths):
            # extract the person name from the image path
            print("[INFO] processing image {}/{}".format(i + 1,
                len(imagePaths)))
            name = imagePath.split(os.path.sep)[-2]

            # load the image, resize it to have a width of 600 pixels (while
            # maintaining the aspect ratio), and then grab the image
            # dimensions
            image = cv2.imread(imagePath)
            image = imutils.resize(image, width=600)
            (h, w) = image.shape[:2]
            # construct a blob from the image
            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(image, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            # apply OpenCV's deep learning-based face detector to localize
            # faces in the input image
            detector.setInput(imageBlob)
            detections = detector.forward()

            # ensure at least one face was found
            if len(detections) > 0:
                # we're making the assumption that each image has only ONE
                # face, so find the bounding box with the largest probability
                i = np.argmax(detections[0, 0, :, 2])
                confidence = detections[0, 0, i, 2]

                # ensure that the detection with the largest probability also
                # means our minimum probability test (thus helping filter out
                # weak detections)
                if confidence > 0.5:
                    # compute the (x, y)-coordinates of the bounding box for
                    # the face
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # extract the face ROI and grab the ROI dimensions
                    face = image[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # ensure the face width and height are sufficiently large
                    if fW < 20 or fH < 20:
                        continue

                    # construct a blob for the face ROI, then pass the blob
                    # through our face embedding model to obtain the 128-d
                    # quantification of the face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                        (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    embedder.setInput(faceBlob)
                    vec = embedder.forward()
       
                    # add the name of the person + corresponding face
                    # embedding to their respective lists
                    knownNames.append(name)
                    knownEmbeddings.append(vec.flatten())
                    total += 1
        # dump the facial embeddings + names to disk
        print("[INFO] serializing {} encodings...".format(total))
        data = {"embeddings": knownEmbeddings, "names": knownNames}
        f = open('output/embeddings.pickle', "wb")
        f.write(pickle.dumps(data))
        f.close()
   
    

    def train_model(self):
        #summary
        print("[INFO] loading face embeddings...")
        data = pickle.loads(open('output/embeddings.pickle', "rb").read())
        le = LabelEncoder()
        labels = le.fit_transform(data["names"])
        # train the model used to accept the 128-d embeddings of the face and
        # then produce the actual face recognition
        print("[INFO] training model...")
        recognizer = SVC(C=1.0, kernel="linear", probability=True)
        recognizer.fit(data["embeddings"], labels)
        # write the actual face recognition model to disk
        f = open('output/recognizer.pickle', "wb")
        f.write(pickle.dumps(recognizer))
        f.close()

        # write the label encoder to disk
        f = open('output/le.pickle', "wb")
        f.write(pickle.dumps(le))
        f.close()
        



    def video_check(self):
        account_number = self.account_entry.get()
        if not account_number:
            messagebox._show("Error", "Please enter your account number!")
            return
        try:
            account_number = int(account_number)
            data = pd.read_csv('bank_details.csv')
            if account_number not in data['account_number'].values:
                messagebox._show("Error", "Invalid account number!")
                return
            self.real_user = data[data['account_number'] == account_number]['unique_id'].values[0]
        except ValueError:
            messagebox._show("Error", "Please enter a valid account number!")
            return

        detector = cv2.dnn.readNetFromCaffe('face_detection_model/deploy.prototxt', 'face_detection_model/res10_300x300_ssd_iter_140000.caffemodel')
        embedder = cv2.dnn.readNetFromTorch('nn4.small2.v1.t7')
        recognizer = pickle.loads(open('output/recognizer.pickle', "rb").read())
        le = pickle.loads(open('output/le.pickle', "rb").read())

        # Initialize video capture
        vs = VideoStream(src=0).start()
        time.sleep(2.0)
        
        # Create camera window with embedded instructions
        camera_window = Toplevel(self.root)
        camera_window.title("Face Verification")
        camera_window.geometry("800x600")
        camera_window.configure(bg="#283593")
        
        # Add instruction text above camera feed
        instruction_label = Label(camera_window,
            text="Position your face within the frame and look directly at the camera",
            bg="#283593",
            fg="white",
            font=("Arial", 12))
        instruction_label.pack(pady=10)
        
        # Create frame for camera feed
        camera_frame = Label(camera_window)
        camera_frame.pack(pady=10)
        
        # Create status label
        status_label = Label(camera_window,
            text="Initializing...",
            bg="#283593",
            fg="white",
            font=("Arial", 12))
        status_label.pack(pady=10)

        timeout = time.time() + 5
        fps = FPS().start()
        real_user_list = []

        cv2.namedWindow("Frame", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Frame", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while True:
            
            #run check for only 15seconds and then stop
            if time.time() > timeout :
                cv2.destroyWindow("Frame")
                break;
               
            # grab the frame from the threaded video stream
            frame = vs.read()
            frame = imutils.resize(frame, width=800, height=200)
            (h, w) = frame.shape[:2]

            # Draw guide circle
            center = (w // 2, h // 2)
            radius = min(w, h) // 3
            cv2.circle(frame, center, radius, (0, 255, 0), 2)

            # construct a blob from the image
            imageBlob = cv2.dnn.blobFromImage(
                cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                (104.0, 177.0, 123.0), swapRB=False, crop=False)

            # apply OpenCV's deep learning-based face detector to localize
            # faces in the input image
            detector.setInput(imageBlob)
            detections = detector.forward()

            #TODO: if 2 faces are detected alert the user of a warning
            # loop over the detections
            for i in range(0, detections.shape[2]):
                # extract the confidence (i.e., probability) associated with
                # the prediction
                confidence = detections[0, 0, i, 2]

                # filter out weak detections
                if confidence > 0.5:
                    # compute the (x, y)-coordinates of the bounding box for
                    # the face
                    box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                    (startX, startY, endX, endY) = box.astype("int")

                    # extract the face ROI
                    face = frame[startY:endY, startX:endX]
                    (fH, fW) = face.shape[:2]

                    # ensure the face width and height are sufficiently large
                    if fW < 20 or fH < 20:
                        continue

                    # construct a blob for the face ROI, then pass the blob
                    # through our face embedding model to obtain the 128-d
                    # quantification of the face
                    faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255,
                        (96, 96), (0, 0, 0), swapRB=True, crop=False)
                    embedder.setInput(faceBlob)
                    vec = embedder.forward()

                    # perform classification to recognize the face
                    preds = recognizer.predict_proba(vec)[0]
                    j = np.argmax(preds)
                    proba = preds[j]
                    name = le.classes_[j]

                    # # draw the bounding box of the face along with the
                    # # associated probability
                    # text = "{}: {:.2f}%".format(name, proba * 100)
                    # y = startY - 10 if startY - 10 > 10 else startY + 10
                    # cv2.rectangle(frame, (startX, startY), (endX, endY),
                    #     (0, 0, 255), 2)
                    # cv2.putText(frame, text, (startX, y),
                    #     cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
                    #TODO: Handle if 2 faces are given.
                    #Decision boundary
                    if (name == 'unknown') or (proba *100) < 50:
                        print("Fraud detected")
                        real_user_list.append(name)
                    else:
                        #cv2.destroyWindow("Frame")
                        real_user_list.append(name)
                        break;
                       

            # update the FPS counter
            fps.update()

            # show the output frame
            cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF

            # if the `q` key was pressed, break from the loop
            if key == ord("q"):
                break

        # stop the timer and display FPS information
        fps.stop()
        print("[INFO] elasped time: {:.2f}".format(fps.elapsed()))
        print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
       

        # do a bit of cleanup
        cv2.destroyAllWindows()
        vs.stop()
        print(real_user_list)
        
        try:
            Counter(real_user_list).most_common(1)[0][0] == 'unknown'
        except IndexError:       
            if self.countter != 0:
                messagebox._show("Verification Info!", "Face Id match failed! You have {} trials left".format(self.countter))
                self.countter = self.countter - 1
                self.video_check()
            else:
                messagebox._show("Verification Info!", "Face Id match failed! You cannot withdraw at this time, try again later")
                self.begin_page()
                self.countter = 2
            
           
        else:
            if Counter(real_user_list).most_common(1)[0][0] == 'unknown':
                if self.countter != 0:
                    messagebox._show("Verification Info!", "Face Id match failed! You have {} trials left".format(self.countter))
                    self.countter = self.countter - 1
                    self.video_check()
                else:
                    messagebox._show("Verification Info!", "Face Id match failed! You cannot withdraw at this time, try again later")
                    self.begin_page()
                    self.countter = 2
                
            else:
                self.real_user = int(Counter(real_user_list).most_common(1)[0][0])
                messagebox._show("Verification Info!", "Face detected!")
                self.password_verification()

       
root = Tk()
root.title("GIET Bank of India")
root.geometry("800x500")
root.configure(bg="blue")
# icon = PhotoImage(file="IMG-f-WA0011 copy.png")
# root.tk.call("wm",'iconphoto',root._w,icon)
obj = BankUi(root)
root.mainloop()
