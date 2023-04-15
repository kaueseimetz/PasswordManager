from cx_Freeze import setup, Executable

options = {
    'build_exe': {
        'packages': ['tkinter', 'cryptography', 'messagebox', 'fernet'],
        'include_files': [
#            'caminho/para/o/seu/arquivo/de/configuracao.cfg',
#            'caminho/para/o/seu/arquivo/de/log.log',
            'chave.key',
            'dados.json',
            'Entry.json'
        ],
#        'excludes': ['tkinter'] # se você não estiver usando tkinter
    }
}

executables = [
    Executable(
        "start.py",
        base="Win32GUI",
        icon="icons/key.ico",
    ),
    Executable(
        "main.py",
        base="Win32GUI",
        icon="icons/key.ico",
    ),
    # adicione quantos scripts desejar
]

setup(
    name='Password Manager',
    version='1.0',
    description='Manage Your Passwords',
    author='Kaues',
    author_email='Kaues@example.com',
    options={"build_exe": options},
    executables=executables,
)
