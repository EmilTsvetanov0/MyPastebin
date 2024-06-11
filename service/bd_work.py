import sqlite3

def add_data(id, text, lang):
    try:
        conn = sqlite3.connect('text_data.db')
        cur = conn.cursor()
        # Проверяем, существует ли уже запись с таким id
        cur.execute("SELECT * FROM text_data WHERE id=?", (id,))
        existing_record = cur.fetchone()
        if existing_record:

            return
        # Вставляем данные
        cur.execute("INSERT INTO text_data (id, text, lang) VALUES (?, ?, ?)", (id, text, lang))
        conn.commit()


    finally:
        if conn:
            conn.close()

def delete_data(id):
    try:
        conn = sqlite3.connect('text_data.db')
        cur = conn.cursor()
        cur.execute("DELETE FROM text_data WHERE id=?", (id,))
        conn.commit()



    finally:
        if conn:
            conn.close()

def exist(id):
    try:
        conn = sqlite3.connect('text_data.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM text_data WHERE id=?", (id,))
        existing_record = cur.fetchone()
        if existing_record:
            return True
        else:
            return False
    finally:
        if conn:
            conn.close()



def get_text(id):
    try:
        conn = sqlite3.connect('text_data.db')
        cur = conn.cursor()
        cur.execute("SELECT text FROM text_data WHERE id=?", (id,))
        text_data = cur.fetchone()
        return text_data[0] if text_data else None
    finally:
        if conn:
            conn.close()



def get_lang(id):
    try:
        conn = sqlite3.connect('text_data.db')
        cur = conn.cursor()
        cur.execute("SELECT lang FROM text_data WHERE id=?", (id,))
        lang_data = cur.fetchone()
        return lang_data[0] if lang_data else None
    finally:
        if conn:
            conn.close()

def create_table():
    try:
        conn = sqlite3.connect('text_data.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS text_data (
                        id TEXT PRIMARY KEY,
                        text TEXT,
                        lang TEXT
                        )''')
        print("Таблица успешно создана")
    except sqlite3.Error as e:
        print("Ошибка при создании таблицы:", e)
    finally:
        if conn:
            conn.close()

language_mapping = {
    "C++": "language-cpp",
    "Python": "language-python",
    "JavaScript": "language-javascript",
    "C#": "language-csharp",
    "C": "language-c",
    "Go": "language-go",
    "AppleScript": "language-applescript",
    "Kotlin": "language-kotlin",
    "Pascal": "language-pascal",
    "Java": "language-java",
    "jq": "language-jq",
    "R": "language-r",
    "Mathematica/Wolfram Language": "language-wolfram",
    "Rust": "language-rust",
    "Lua": "language-lua",
    "Visual Basic .NET": "language-vbnet",
    "Swift": "language-swift",
    "Scala": "language-scala",
    "Ruby": "language-ruby",
    "PHP": "language-php",
    "PowerShell": "language-powershell",
    "Perl": "language-perl",
    "COBOL": "language-cobol",
    "ARM Assembly": "language-armasm",
    "Fortran": "language-fortran",
    "Erlang": "language-erlang"
}