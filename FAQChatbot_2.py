import customtkinter as ctk
from tkinter import Menu, messagebox
from difflib import get_close_matches
import math
import random
import datetime
import time
import os
import json
import re
import webbrowser
import sqlite3
import tkinter
import ast
questions_answered = 0



ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")




faqs = {
    "What is your name?":
        " My name is AlphaBot. I'm here to help answer your questions and assist you with various tasks.",

    "What can you do?":
        "I can answer questions, explain concepts, provide coding help, solve math problems, and assist with general information.",

    "How do I use this chatbot?":
        "Simply type your question into the chat box and press Enter or click Send.",

    "Are you available 24/7?":
        "Yes, I'm available anytime to assist you.",

    "Yes, I'm available anytime to assist you.":
        "Yes! I can help with Python, Java, C++, JavaScript, HTML, CSS, SQL, and many other programming languages.",

    "Can you solve math problems?":
        "Yes, I can solve arithmetic, algebra, calculus, statistics, and many other mathematical problems.",

    "Do you store my personal information?":
        "The placement cell is located in Block C.",

    "Can you help me write emails or resumes?":
        "Yes, I can help write emails, resumes, cover letters, reports, and other documents.",

    "What should I do if you don't know the answer?":
        "Try rephrasing your question or providing more details. I'll do my best to help.",

    "Is this chatbot free to use?":
        "That depends on the application you're using. Please check the platform's pricing or subscription details.",
        
    "Can you tell me a joke?":
        "Of course! Here's one: Why do programmers prefer dark mode? Because light attracts bugs!",
   
        
    "What languages do you support?":
        "I can understand and communicate in many languages, including English, Hindi, Spanish, French, German, Tamil, Telugu, Kannada, and more.",
    "Can you translate text?":
        "Yes, I can translate text between multiple languages accurately.",
    "Can you explain programming concepts?":
        "Yes, I can explain programming concepts from beginner to advanced levels with examples.",
    "Can you help me prepare for interviews?":
        "Yes, I can provide interview questions, mock interviews, coding challenges, and career tips.",
    "Can you generate code?":
        "Yes, I can generate code in Python, Java, C++, JavaScript, C#, SQL, HTML, CSS, and many other languages.",
    "Can you debug my code?":
        "Yes, paste your code and I'll help identify and fix errors.",
    "Can you summarize documents?":
        "Yes, I can summarize articles, reports, essays, and long pieces of text.",
    "Can you recommend books?":
        "Yes, I can recommend books based on your interests and goals.",
    "Can you recommend movies?":
        "Absolutely! Tell me your favorite genre and I'll suggest some great movies.",
    "Can you help with homework?":
        "Yes, I can explain concepts and guide you through solving problems step by step.",
    "Can you explain science topics?":
        "Yes, I can explain physics, chemistry, biology, astronomy, and other science subjects.",
    "Can you help me improve my English?":
        "Yes, I can help with grammar, vocabulary, pronunciation tips, and writing practice.",
    "Can you create quizzes?":
        "Yes, I can generate quizzes with multiple-choice or descriptive questions on any topic.",
    "Can you provide career advice?":
        "Yes, I can suggest career paths, required skills, certifications, and learning resources.",
    "Can you help me learn AI and Machine Learning?":
        "Yes, I can explain AI/ML concepts, algorithms, projects, and coding examples.",
    "Can you help me with databases?":
        "Yes, I can explain SQL, NoSQL, database design, normalization, and queries.",
    "Can you assist with project ideas?":
        "Yes, I can suggest beginner, intermediate, and advanced project ideas for various technologies.",
    "How can I contact support?":
        "Please contact the application's support team or administrator for technical assistance and account-related issues.",
    "What is Artificial Intelligence (AI)?":
        "Artificial Intelligence is the simulation of human intelligence in machines that can learn, reason, and solve problems.",
    "What is Machine Learning?":
        "Machine Learning is a branch of AI that enables computers to learn from data and improve their performance without being explicitly programmed.",
    "What is Python?":
        "Python is a popular, easy-to-learn programming language used for web development, AI, automation, and data science.",
    "What is Java?":
        "Java is an object-oriented programming language widely used for developing desktop, web, and Android applications",
    "What is C++?":
        "C++ is a powerful programming language commonly used for system software, games, and high-performance applications.",
    "What is HTML?":
        "HTML (HyperText Markup Language) is the standard language used to create web pages.",
    "What is CSS?":
        "CSS (Cascading Style Sheets) is used to style and design web pages.",
    "What is JavaScript?":
        "JavaScript is a scripting language used to make web pages interactive and dynamic.",
    "What is SQL?":
        "SQL (Structured Query Language) is used to manage and retrieve data from databases.",
    "What is a database?":
        "A database is an organized collection of data that can be stored, managed, and accessed efficiently.",
    "What is cloud computing?":
        "Cloud computing provides computing resources such as storage and servers over the internet instead of local hardware.",
    "What is cybersecurity?":
        "Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.",
    "What is Git?":
        "Git is a version control system that helps developers track changes in their code.",
    "What is GitHub?":
        "GitHub is a platform for hosting Git repositories and collaborating on software projects.",
    "What is an API?":
        "An API (Application Programming Interface) allows different software applications to communicate with each other.",
    "What is a chatbot?":
        "A chatbot is a software application that simulates conversations with users using text or voice.",
    "What is the Internet?":
        "The Internet is a global network that connects computers and allows them to share information.",
    "What is an operating system?":
        "An operating system manages a computer's hardware and software resources and provides services for applications.",
    "Can you motivate me?":
        "Absolutely! Every expert was once a beginner. Keep learning, stay consistent, Never Give Up!, and you'll achieve your goals!.",
    "Can you solve math problems?":
        "Yes. Enter your math expression or describe the problem, and I'll help solve it step by step if supported by my capabilities."  ,  
    "Can you solve algebra equations?":
        "Yes. I can help solve linear and quadratic equations and explain each step."  ,  
    "Can you calculate percentages?":
        "Yes. I can calculate percentages, discounts, profit/loss, tax, and percentage increases or decreases." ,   
    "Can you calculate areas and volumes?":
        "Yes. I can calculate the area, perimeter, surface area, and volume of common geometric shapes.",
    "Can you perform unit conversions?":
        "Yes. I can convert units such as length, weight, temperature, time, and speed." ,   
    "Can you help with coding problems?":
        "Yes. Describe the problem or share the code, and I'll help explain or debug it."  ,  
    "Can you solve LeetCode problems?":
        "Yes. I can explain algorithms, discuss approaches, and help write or improve solutions for LeetCode problems.",
    "Can you explain data structures?":
        "Yes. I can explain arrays, linked lists, stacks, queues, trees, graphs, heaps, hash tables, and more.",
    "Can you explain algorithms?":
        "es. I can explain sorting, searching, dynamic programming, graph algorithms, recursion, and other common techniques." ,   
    "Can you help me prepare for coding interviews?":
        "Yes. I can provide interview questions, coding exercises, and tips for technical interviews." ,   
    "Can you help in an emergency?":
        "I can provide general guidance and first-aid information, but if there is immediate danger or a life-threatening emergency, contact your local emergency services immediately." ,   
    "Someone is unconscious. What should I do?":
        "Call your local emergency services immediately. If you are trained, begin appropriate first aid or CPR while waiting for professional help.",    
    "What should I do if someone is choking?":
        "Encourage them to cough if they can. If they cannot breathe or speak, seek emergency medical help immediately and follow recognized first-aid guidance if you are trained.",    
    "What should I do during a fire?":
        "Leave the building immediately using the safest exit, stay low if there is smoke, and call the fire department once you are safe." ,   
    "What should I do during an earthquake?":
        "Drop, Cover, and Hold On. Stay away from windows, and once the shaking stops, move to a safe area if needed."  ,  
    "What should I do if I forget my password?":
        "Use the application's password reset option or contact the service's support team.",    
    "Can you help me write a resume or cover letter?":
        "Yes. I can help create or improve resumes, cover letters, and professional documents.",    
    "Can you explain science and technology concepts?":
        "Yes. I can explain topics from physics, chemistry, biology, computer science, and engineering.",    
    "Can you help me make decisions?":
        "I can compare options, explain trade-offs, and help you think through a decision, but the final choice is yours.",    
    "What should I do if you cannot answer my question?":
        "Try asking with more details or rephrasing the question. If it's outside my capabilities, I may suggest other reliable resources.",    
    
    "Thank you":
        "You're welcome! 😊 I'm always here to help. Have a Great day!",
    "Hello":
        "Hello! How can I assist you today?",
    "can you be my friend?":
        "Of course! I'm here to chat and help you with anything you need. Let's be friends!",
    "Good morning":
        "Good morning! How can I assist you today?",
    "thank you so much":
        "You're very welcome! I'm glad I could help. If you have any more questions or need assistance, feel free to ask!",
    "i am feeling sad":
        "I'm sorry to hear that. Is there anything I can do to help you feel better?",
    "i am feeling happy":
        "That's great to hear! Is there anything I can do for you today?",
        
    "Good afternoon":
        "Good afternoon! How can I assist you today?",
    "good evening":
        "Good evening! How can I assist you tonight?",
    "good night":
        "Good night! Sleep well and wake up refreshed!",
    "i am feeling angry":
        "I'm sorry to hear that. Is there anything I can do to help you feel better?"
        
}

def preprocess(text):
    return text.lower().strip()


def get_response(user_question):

    processed_input = preprocess(user_question)

    faq_questions = list(faqs.keys())

    processed_faqs = [
        preprocess(question)
        for question in faq_questions
    ]

    match = get_close_matches(
        processed_input,
        processed_faqs,
        n=1,
        cutoff=0.7
    )

    if match:

        matched_index = processed_faqs.index(match[0])

        original_question = faq_questions[matched_index]

        return faqs[original_question]

    return "Sorry, I couldn't find a suitable answer."

def send_message():

    global questions_answered
    user_text = user_entry.get().strip()

    if user_text == "":
        return
    status_text.set("⌛ AlphaBot is thinking...")
    app.update()
    text = user_text.lower()

    if "open google" in text:
        webbrowser.open("https://www.google.com")
        response = "Opening Google..."

    elif "open youtube" in text:
        webbrowser.open("https://www.youtube.com")
        response = "Opening YouTube..."

    elif "open github" in text:
        webbrowser.open("https://github.com")
        response = "Opening GitHub..."

    elif "open chatgpt" in text:
        webbrowser.open("https://chatgpt.com")
        response = "Opening ChatGPT..."
    elif "open gmail" in text:
        webbrowser.open("https://mail.google.com")
        response = "Opening Gmail..."
    
    elif "open linkedin" in text:
        webbrowser.open("https://www.linkedin.com")
        response = "Opening LinkedIn..."

    elif "open wikipedia" in text:
        webbrowser.open("https://www.wikipedia.org")
        response = "Opening Wikipedia..."

    elif "open amazon" in text:
        webbrowser.open("https://www.amazon.in")
        response = "Opening Amazon..."

    else:
        try:
            allowed = {
                "__builtins__": None,
                "sqrt": math.sqrt,
                "pow": pow,
                "abs": abs,
                "round": round
            }

            result = eval(user_text, allowed)
            response = f"The answer is {result}"

        except Exception:
            response = get_response(user_text)

    chat_box.configure(state="normal")
    
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    
    chat_box.insert(
        "end",
        f"\n[{current_time}] 👤 You: {user_text}\n",
        "user"
    )

    current_time = datetime.datetime.now().strftime("%I:%M %p")

    chat_box.insert(
        "end",
        f"[{current_time}] 🤖 AlphaBot: {response}\n",
        "bot"
    )
    questions_answered += 1
    
    chat_box.configure(state="disabled")
    user_entry.delete(0, "end")
    chat_box.see("end")
    user_entry.focus()
    update_status_bar()

def update_chat_colors():

    current = ctk.get_appearance_mode()

    if current == "Dark":
        chat_box.tag_config("user", foreground="yellow")
        chat_box.tag_config("bot", foreground="light green")
    else:
        chat_box.tag_config("user", foreground="blue")
        chat_box.tag_config("bot", foreground="green")


def clear_chat():

    chat_box.configure(state="normal")

    chat_box.delete("1.0", "end")

    chat_box.insert(
        "end",
        "🤖 AlphaBot is Ready...\n"
    )

    chat_box.configure(state="disabled")
    update_chat_colors()


   
# Create the main window

app = ctk.CTk()


# Create the input frame FIRST

def update_chat_colors():

    current = ctk.get_appearance_mode()

    if current == "Dark":

        chat_box.tag_config("user", foreground="yellow")
        chat_box.tag_config("bot", foreground="light green")

    else:

        chat_box.tag_config("user", foreground="blue")
        chat_box.tag_config("bot", foreground="green")


def toggle_theme():

    if ctk.get_appearance_mode() == "Light":
        ctk.set_appearance_mode("dark")
    else:
        ctk.set_appearance_mode("light")

    app.after(100, update_chat_colors)
    app.after(100, update_status_bar)
    
app.title("Smart FAQ Chatbot")

app.geometry("1000x700")


title = ctk.CTkLabel(
    app,
    text="🤖 Smart FAQ AlphaBot v2.0",
    font=("Segoe UI", 30, "bold")
)

title.pack(pady=15)

subtitle = ctk.CTkLabel(
    app,
    text="AI Powered Smart FAQ & Utility Assistant",
    font=("Segoe UI", 14)
)

subtitle.pack()


chat_frame = ctk.CTkFrame(app)

chat_frame.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

chat_box = ctk.CTkTextbox(
    chat_frame,
    font=("Segoe UI", 15)
)

chat_box.pack(
    fill="both",
    expand=True,
    padx=10,
    pady=10
)
update_chat_colors()
chat_box.insert(
    "end",
    "🤖 AlphaBot is Ready...\n"
)


chat_box.configure(state="disabled")
input_frame = ctk.CTkFrame(app)

input_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

    
user_entry = ctk.CTkEntry(
    input_frame,
    placeholder_text="Ask a question...",
    height=45,
    font=("Segoe UI", 14)
)

user_entry.pack(
    side="left",
    fill="x",
    expand=True,
    padx=10,
    pady=10
)


user_entry.bind("<Return>", lambda event: send_message())
user_entry.focus()

send_btn = ctk.CTkButton(
    input_frame,
    text="Send",
    width=120,
    command=send_message
)
send_btn.pack(
    side="left",
    padx=10
)

bottom_frame = ctk.CTkFrame(app)

bottom_frame.pack(
    fill="x",
    padx=20,
    pady=10
)

clear_btn = ctk.CTkButton(
    bottom_frame,
    text="🗑 Clear Chat",
    command=clear_chat
)

clear_btn.pack(
    side="left",
    padx=10,
    pady=10
)

theme_btn = ctk.CTkButton(
    bottom_frame,
    text="Change Theme",
    command=toggle_theme
)

theme_btn.pack(
    side="right",
    padx=10
)

def show_about():

    about = ctk.CTkToplevel(app)

    about.title("About Smart FAQ AlphaBot")

    about.geometry("500x380")

    about.resizable(False, False)

    ctk.CTkLabel(
        about,
        text="🤖 Smart FAQ AlphaBot v2.0",
        font=("Segoe UI",24,"bold")
    ).pack(pady=20)

    ctk.CTkLabel(
        about,
        text="""Developed by
       
 Dheeraj Suriya
        
AI Powered Smart FAQ & Utility Assistant
        
CodeAlpha Internship Project""",
        font=("Segoe UI",16),
        justify="center"
    ).pack(pady=25)

    ctk.CTkButton(
        about,
        text="Close",
        command=about.destroy
    ).pack(pady=25)

menu_bar = Menu(app)

app.configure(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="File",
    menu=file_menu
)

file_menu.add_command(
    label="Clear Chat",
    command=clear_chat
)

file_menu.add_separator()

file_menu.add_command(
    label="Exit",
    command=app.quit
)

settings_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="Settings",
    menu=settings_menu
)

settings_menu.add_command(
    label="Toggle Theme",
    command=toggle_theme
)

help_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="Help",
    menu=help_menu
)

help_menu.add_command(
    label="How to Use",
    command=lambda: messagebox.showinfo(
        "Help",
        """Type your question and press Enter
or click Send.

Examples:

Hello
Who created Python?
25 + 18
sqrt(64)
Open Google
Open YouTube
What is AI?
"""
    )
)

about_menu = Menu(menu_bar, tearoff=0)

menu_bar.add_cascade(
    label="About",
    menu=about_menu
)

about_menu.add_command(
    label="About AlphaBot",
    command=show_about
)
# ---------------- Status Bar ----------------

status_text = ctk.StringVar()

status_bar = ctk.CTkLabel(
    app,
    textvariable=status_text,
    height=28,
    anchor="w",
    font=("Segoe UI", 11)
)

status_bar.pack(
    side="bottom",
    fill="x",
    padx=10,
    pady=(0, 8)
)
questions_answered = 0
def update_status_bar():
    current_time = datetime.datetime.now().strftime("%I:%M %p")
    theme = ctk.get_appearance_mode()

    status_text.set(
        f"🟢 Ready  |  🕒 {current_time}  |  🌙 {theme} Mode  |  💬 Questions Answered: {questions_answered}  |  🤖 AlphaBot v2.0  |  👨‍💻 Developed by Dheeraj Suriya"
    )
update_status_bar()

app.mainloop()