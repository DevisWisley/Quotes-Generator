import tkinter as tk
from tkinter import messagebox
import random
import threading

quotes = [
    "Jangan pernah menyimpan dua orang dalam satu hati ❤️. Fisik bisa diubah 💪, materi bisa dicari 💰, tapi orang yang tulus mencintaimu 💖 tidak akan datang dua kali 🔁...!!!",
    "Jangan merasa paling tersakiti 😢. Kadang kamu juga sering melukai orang lain 💔 tapi tidak menyadarinya 🤷‍♂️🤷‍♀️.",
    "Rindu tidak oleh jarak 🌍, akan tetapi oleh perasaan 💭. Kamu merindukannya bukan karena ia jauh 🚶‍♂️, namun karena ia telah ada di hatimu ❤️.",
    "Yakinlah 🙏, se deras apa pun hujan 🌧️ pasti ada redanya 🌤️. Demikian juga ujian dan masalah hidup 💼😔 tak selamanya berderai air mata 😢. Akan ada masanya penuh canda 🤭 tertawa 😂, hingga akhirnya tercipta bahagia 😊❤️.",
    "Jika sudah ditakdirkan bersama 💑, semua pasti ada jalannya 🚶‍♂️🛤️.",
    "Mencintaimu adalah hak istimewa 💖, tapi dicinta olehmu adalah berkah 🌟. Bersamamu adalah keinginan yang menjadi nyata 💑✨. Dan aku berharap semua keinginanmu 🎁 menjadi kenyataan di hari istimewa ini 🎂🎉.",
    "Jangan kolam renang yang panjang 🏊‍♂️, lautan aja ku sebrangi 🌊⛵ asal ujungnya ada kamu ❤️.",
    "Terkadang kita butuh jarak 🛤️, agar memahami rasa sebenarnya 💭❤️. Seperti kata-kata ✍️ yang butuh spasi 🔠, agar bisa terbaca dengan baik 📖✨.",
    "Tak perlu memaksa seseorang untuk selalu ada buat kita 🙅‍♂️💬, sebab yang tulus 💖 akan selalu ada 🫂, tanpa kita minta sekalipun 🤲.",
    "Aku mungkin tak melihatmu setiap hari 👀📆, tapi aku senantiasa merindukanmu setiap saat 💭❤️. Semoga jarak ini 🌍 membuat kita semakin dekat 🤝, walaupun jarak antara kita terbentang jauh 🚶‍♀️🌏🚶‍♂️. Percayalah bahwa hati ini terjaga rapi untukmu seorang 💌🔐.",
    "Di balik kata lelah 😮‍💨, ada kamu 💖 yang selalu menjadi alasanku untuk tidak menyerah 💪✨.",
    "Tanpa rasa sakit 😣, kita tidak akan belajar menjadi kuat 💪. Tanpa rasa kecewa 😔, kita tidak akan belajar menjadi dewasa 🧠. Tanpa kehilangan 💔, kita tidak akan belajar arti ikhlas 🤲✨",
    "Awalnya, manis 🍬 pada akhirnya membuat hati ini terluka 💔. Maka, akan ku hancurkan mereka semua 💣🔥.",
    "Aku selalu berjanji pada diriku 🤞. Aku selalu menyayangi 💖 dan melindungimu 🛡️. Dan bila ada yang berani menyakitimu 😠💢.",
    "Yang lalu biarlah berlalu ⏳💨. Sekarang, masa depan menanti yang lebih baik 🌅🚀.",
    "Hidup ini terasa milik kita berdua 💑 kalau kita satu desa 🏡❤️.",
    "Cincin ini 💍 janjiku seumur hidup untukmu 💖, Name, menikahlah denganku 💌👰‍♀️🤵‍♂️.",
    "Banyak yang bilang cinta bangku sekolah 🎒💌 nggak akan sampai akhir ⏳, tapi dia menjadikanku satu-satunya 💑❤️.",
    "Cinta terbaik 💖 akan memberiku cinta yang aman dan cukup 🛡️💫, tapi aku memberimu kepercayaan 🤝🔐.",
    "Perjanjian hitam 📝⚫ di atas putih ✍️⚪.",
    "Ada sebuah perasaan 💖 yang selamanya tak bisa kalah dengan waktu ⏳❤️.",
    "Hal yang paling menyakitkan 😢 adalah sebuah perpisahan 💔 yang tak akan ada pertemuan kembali 🚶‍♂️💨.",
    "Mengapa berbagi kesulitan itu mudah 🤝😔, tetapi kamu tidak menjaga hati 💔. Yang aku mau hanyalah cinta 💖.",
    "Sakit 😢 juga bisa disebabkan oleh kehilangan sahabat 👥💔 sekaligus orang yang kita cintai 💖.",
    "Semarah-marahnya aku 😠, aku tetap mencintaimu 💖, tetap menjaga 🛡️ dan menyayangimu 🤗, karena sejatinya hubungan yaitu mempertahankan 🤝❤️.",
    "Cinta 💖 nggak akan tersakiti 😢, kalau emang sama-sama saling mengerti 🤝 dan menyayangi 🤗.",
    "Ternyata 😔 tidak semua kesalahan ❌ bisa dimaafkan 🙏.",
    "Terkadang 🤐 memendam adalah pilihan satu-satunya ☝️ agar semua terlihat baik-baik saja 🙂💔.",
    "Terkadang 🕰️ kita diuji 🧪 bukan untuk menunjukkan kelemahan kita 😞, tetapi untuk menemukan kekuatan kita 💪✨.",
    "Cinta itu diperjuangin 💪💖, bukan ditunggu ⏳🙇‍♀️.",
    "Jadilah, hubungan yang dewasa 🧠💞 — jarang bertemu 🚶‍♂️🌍🚶‍♀️, tapi saling percaya 🤝 dan setia 💖. Karena setia adalah seni tertinggi 🎨 dalam mencintai ❤️.",
    "Dipertemukan oleh virtual 💻📱, disatukan oleh kehidupan nyata 🤝❤️, dan dipisahkan oleh bedanya kepercayaan 🙏⚖️💔.",
    "Berani berbuat 💪, berani bertanggung jawab 🛡️⚖️ itu namanya kesatria 🗡️🛡️.",
    "Bahwa kelak 🕰️, ketika kita miskin atau kaya 💸💰, sehat ataupun sakit 💪🤒, kita nggak akan pernah berpisah 🤝❤️."
]

is_dark_mode = False

def apply_theme():
    bg = "#1e1e1e" if is_dark_mode else "#f2f2f2"
    fg = "#ffffff" if is_dark_mode else "#333333"
    card_bg = "#2e2e2e" if is_dark_mode else "white"
    btn_bg = "#3e8e41" if is_dark_mode else "#4CAF50"
    quote_fg = "#f2f2f2" if is_dark_mode else "#333"

    root.config(bg=bg)
    title.config(bg=bg, fg=fg)
    footer.config(bg=bg, fg="gray")
    card.config(bg=card_bg)
    quote_display.config(bg=card_bg, fg=quote_fg)
    generate_btn.config(bg=btn_bg)

def toggle_dark_mode():
    global is_dark_mode
    is_dark_mode = not is_dark_mode
    apply_theme()

def generate_quote():
    quote = random.choice(quotes)
    quote_display.config(state='normal')
    quote_display.delete(1.0, tk.END)
    quote_display.insert(tk.END, quote)
    quote_display.config(state='disabled')

def confirm_exit():
    result = messagebox.askyesno("Konfirmasi Keluar", "Apakah Anda yakin ingin keluar dari aplikasi?")
    if result:
        root.quit()

def show_about():
    messagebox.showinfo(
        "Tentang Aplikasi",
        "❤️ Quotes Generator\n\nKutipan cinta & kehidupan dengan emoji 💖\n\nDeveloper: Devis Wisley © 2025"
    )

def show_splash():
    splash = tk.Toplevel()
    splash.overrideredirect(True)
    splash.geometry("400x250+500+250")
    splash.configure(bg="#ffffff")

    label = tk.Label(
        splash,
        text="✨ Quote Generator ✨",
        font=("Segoe UI", 20, "bold"),
        bg="white",
        fg="#333"
    )
    label.pack(expand=True)

    developer = tk.Label(
        splash,
        text="Dibuat oleh Devis Wisley",
        font=("Segoe UI", 12),
        bg="white",
        fg="gray"
    )
    developer.pack(pady=10)

    splash.after(2500, splash.destroy)

def start_main_app():
    global root, quote_display, title, footer, card, generate_btn

    root = tk.Tk()
    root.title("✨ Quote Generator ✨")
    root.geometry("700x450")
    root.resizable(False, False)
    root.configure(bg="#f2f2f2")

    # Menu bar
    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="🎲 Generate Quote", command=generate_quote)
    file_menu.add_separator()
    file_menu.add_command(label="❌ Exit", command=confirm_exit)
    menu_bar.add_cascade(label="File", menu=file_menu)

    view_menu = tk.Menu(menu_bar, tearoff=0)
    view_menu.add_command(label="🌓 Toggle Dark Mode", command=toggle_dark_mode)
    menu_bar.add_cascade(label="View", menu=view_menu)

    help_menu = tk.Menu(menu_bar, tearoff=0)
    help_menu.add_command(label="ℹ️ About", command=show_about)
    menu_bar.add_cascade(label="Help", menu=help_menu)

    title = tk.Label(
        root,
        text="✨ Quote Generator ✨",
        font=("Segoe UI", 22, "bold"),
        bg="#f2f2f2",
        fg="#333"
    )
    title.pack(pady=15)

    card = tk.Frame(root, bg="white", highlightbackground="#ccc", highlightthickness=1)
    card.pack(padx=30, pady=10, fill="both", expand=False)

    quote_display = tk.Text(
        card,
        height=7,
        width=70,
        wrap="word",
        font=("Segoe UI Emoji", 14),
        bg="white",
        fg="#333",
        relief="flat",
        borderwidth=0
    )
    quote_display.insert(tk.END, "Klik tombol di bawah atau menu File → Generate Quote untuk mendapatkan kutipan! ❤️")
    quote_display.config(state='disabled')
    quote_display.pack(padx=20, pady=20)

    def on_enter(e):
        generate_btn.config(bg="#3e8e41" if not is_dark_mode else "#2a7b36")
    def on_leave(e):
        generate_btn.config(bg="#4CAF50" if not is_dark_mode else "#3e8e41")

    generate_btn = tk.Button(
        root,
        text="🎲 Generate Quote",
        command=generate_quote,
        font=("Segoe UI", 13, "bold"),
        bg="#4CAF50",
        fg="white",
        padx=20,
        pady=10,
        relief="flat",
        cursor="hand2"
    )
    generate_btn.pack(pady=10)
    generate_btn.bind("<Enter>", on_enter)
    generate_btn.bind("<Leave>", on_leave)

    footer = tk.Label(
        root,
        text="Dibuat oleh Devis Wisley © 2025",
        font=("Segoe UI", 10),
        bg="#f2f2f2",
        fg="gray"
    )
    footer.pack(pady=(10, 5))

    apply_theme()
    root.mainloop()

if __name__ == "__main__":
    app = tk.Tk()
    app.withdraw()
    show_splash()
    threading.Timer(2.6, start_main_app).start()
    app.mainloop()
