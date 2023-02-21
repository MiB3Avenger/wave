# wave

Install virtualenv
``` pip3 install virtualenv ```
``` python3 -m venv venv ```

For mac, enter virtualenv by:
``` source venv/bin/activate ```

For windows, enter virtualenv by:
``` .\env\Scripts\activate ```

Use following command to install required python packages:
``` pip3 install -r requirements.txt ```

Start server by:
``` cd django ```
``` python manage.py migrate ```
``` python manage.py runserver ```

For front-end, install node and npm. Then enter vue project director by:
``` cd vue/wave ```

Install node packages by:
``` npm run install ```

Run front-end server by \[developmental\]:
``` npm run dev ```