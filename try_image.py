import logging
from dotenv import load_dotenv

load_dotenv()

if __name__ == "__main__":
    import imgkit

    options = {
    }
    imgkit.from_file('html/build/index.html', 'var/out.jpg', options=options)
