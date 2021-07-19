
**login_project**

A login dialog for your apps, made with PySide2(PyQt5)

To run this project, please make sure you have python installed on your computer.

How to run this project:

1. Make a virtual environment and activate it.
    There are many detailed tutorials on how   to do so.

2. Run `pip install -r requirements.txt`
3. You can now run login_project. Internet connection is required

Feel free to adapt this project to your needs.

Please report any issue and if you have ideas or suggestions, make an issue or a pull request

Notes:

the program first checks if the folder where main.py is has a data.json file with the credentials stored. If not, it prompts the user.

The data.json file structure should be like this:

`{
    username:"username", 
    password:"password"
}
`
