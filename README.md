# Yummy Slack
### About the project

"Yummy Slack" is an open-source project for creating backups of Slack messenger public / private channels and direct messages.  
It needs a [Slack-App](https://api.slack.com/apps) as a backend, so you need to create your own in your Slack-workspace. Read about this [here](create_slack_app.md) or further.

### Useful links:
- [Slack API docs](https://api.slack.com/docs)
- [Slack Apps control center](https://api.slack.com/apps)
- [Qt for Python](https://doc.qt.io/qtforpython-6/)

### Useful commands for binaries and resources:  
- Convert `.ui` file to `.py` with PySide6 - `pyside6-uic app/resources/ui_files/main_window.ui -o main_window_ui.py`
- Convert `.qrc` file to `.py` with PySide6 - `pyside6-rcc app/resources/resource.qrc -o resource_rc.py`
- Compile project to executable file with pyinstaller - `pyinstaller app.py -F --noconsole --icon=app/resources/icons/candy.ico --name "Yummy Slack"`

### Support the developer
In development for now :>

# Getting stated

## File structure
 - "Yummy Slack" (hereinafter simply app) is a program for the Windows system (for now).  
App creates its file structure described below at the first launch of the program:  
    ```
    |-- user_named_folder/
        |-- Yummy Slack.exe  
        |-- Backups/
            |-- direct chats/
            |-- public channels/
            |-- private channels/
        |-- AppData/
            |-- cache
                |-- user.cache
            |-- config/
                |-- app_auth.conf
            |-- logs/
    ```

 - Folders inside `Backups/` folder (`direct chats/`, `public channels/` and `private channels/`) contain the similar structure, that is created after successful backup process.  
Here the `direct chats` folder, as example:
    ```
    |-- Backups/
        |-- direct chats/
            |-- chat_name/
                |-- attachments/
                |-- chat_name.html
    ```

 - Folders inside `AppData/` folder (`cache/`, `config/` and `logs/`) contains app-settings and log-files.  
User should edit `./AppData/config/app_auth.conf` only. Read about this further.  
Logging files, stored in `./AppData/logs/` is useful for troubleshooting.  

> ___Please report errors that occur while using the program to this GitHub in the issues section, attaching the corresponding log-files.___  

## The first launch
*__The application has a fairly user-friendly interface and informative messages, so carefully read the messages provided by the program and follow its instructions.__*  

At the first start the application will create its file structure (which is described in previous chapter). The same behaviour will be in case of deleting the `AppData/` or `Backups/` folders later. They wil be recreated.
> <span style="color:orange;">IMPORTANT</span>  
> The application doesn't have any authentication data at the first start and in case of deleting the `AppData/` folder. 
> 
> ![no_conf.png](/app/resources/images/no_conf.png)  
> 
> It needs `app_auth.conf` file, whose template will be created and stored in `./AppData/config/` after the first launch of the program.  
> Fill the file according to the instructions in [Slack app creation manual](create_slack_app.md). 

## Authorisation in Application
After completing the app-registration and filing the `app_auth.conf` you can finally `Authorise in Slack`.  

![auth.png](/app/resources/images/auth.png)  

If you did everything correctly on previous steps, the login web-page for the Slack-App will open in your browser. (Authentication browser-session exists only one minute, so don't waste time).  

![log_in_example.png](/app/resources/images/log_in_example.png)  

Choose your Slack-Workspace and allow permissions-request.  

> <span style="color: orange;">DON'T PANIC</span>  
> Due to the fact that the application is open-source, it does not have pre-installed certificates and security keys for browsers (`pyopenssl` and `werkzeug server` with `adhoc` are used instead). 
> For this reason, your browser will warn you that a secure connection cannot be established. Make an exception for the current web-page in your browser and continue logging in (anyway this web-page is hosted locally). 

> 🎉 ___Congratulations!___ 🎉  
> You have successfully logged into the app (if all worked as expected ofc). The hardest part is over. Your user-authorisation data will be stored in `AppData/cache/user.cache` on the program closing.

## Basic usage

After logging in, you will see the apps main page instead of previous info-page with single button.  

App has pretty simple GUI.  
![GUI.png](/app/resources/images/GUI.png)  
Interface elements are listed below:
1. `Info-field` - contains user and team name which are loaded after successful authorisation.
2. `Chat-list` - list of available chats / channels.
3. `Backup status` - each chat or channel has its own personal backup-status indicator next to the name. 
4. `Log out button` - log-out from the app and erase `user.cache`.
5. `Start backup button` - start backup for selected chats and channels.
6. `Search field` - find necessary chats or channels by their name.
7. `Chat-groups buttons` - switch between chats / channels lists. (Search results are different for different list).

> The app shows a pop-up window with backup global-status and info.  
> Unlike the chat or channel backup-status, which shows the status of a specific chat, the backup global-status shows the status of the entire backup process.
> 
>![start_pop_up.png](/app/resources/images/start_pop_up.png)  ![complete_pop_up.png](/app/resources/images/complete_pop_up.png) ![warning_pop_up.png](/app/resources/images/warning_pop_up.png)  

>___To start backup, choose necessary chats / channels from the relevant groups and press `Start Backup`.___

That's all. Feel free to use this App as it is / fork / modify. 











