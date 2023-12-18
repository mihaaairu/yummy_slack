## Slack-App creation manual

> We need to collect some data for our `app_auth.conf` file, which is being created on `Yummy Slack` first launch and looks like this:
> 
> ```
> app_auth.conf
> {
>     "File validation": "Replace this text with a single word 'complete', after you update Slack-App auth data below.",
>     "Client ID": "Replace this text with your Slack-App 'Client ID'.",
>     "Client Secret": "Replace this text with your Slack-App 'Client Secret'.",
>     "Signing Secret": "Replace this text with your Slack-App 'Signing Secret'.",
>     "Sharable URL": "Replace this text with your Slack-App 'Sharable URL'."
> }
> ```
>  
> To fill your file with data, you need to create your own Slack-App.  
> ***So, let's get started.***  
 
> Got to [Slack applications space](https://api.slack.com/apps) and create your Slack-App.  
> 
> ![app_register_1.png](/app/resources/images/app_register_1.png)  

> Choose `From scratch` option.  
> 
> ![app_register_2.png.png](/app/resources/images/app_register_2.png)

> Name your Slack-App, choose your target workspace and press `Create App`.   
> 
> ![app_register_3.png.png](/app/resources/images/app_register_3.png)

> Provide the required `User Token Scopes` in `Features/OAuth & Permissions/Scopes` side menu section.  
> 
> ![app_register_4.png.png](/app/resources/images/app_register_4.png)  
> 
> Here are the required scopes:
> - channels:history
> - channels:read
> - files:read
> - groups:history
> - groups:read
> - im:history
> - im:read
> - mpim:history
> - mpim:read
> - users:read

> Set up redirect URL with `https://127.0.0.1:5000/` in `Features/OAuth & Permissions/Redirect URLs` side menu section.  
>  
> ![app_register_5.png.png](/app/resources/images/app_register_5.png)

> <span style="color: orange;">OPTIONAL</span>   
> You can `Activate Public Distribution` in case you want to share your Slack-App with other workspaces (add the same slack-backend to your another workspace a.e.).  
> 
> Confirm that you have removed all personal data from the code in `Settings/Manage Distribution/Share Your App with Other Workspaces` side menu section.  
> 
> ![app_register_6.png.png](/app/resources/images/app_register_6.png)

> Copy `Sharable URL` from `Settings/Manage Distribution/Share Your App with Your Workspace` side menu section.  
> 
> (You need to copy `Sharable URL` from `Share Your App with Any Workspaces` instead, in case you choose to `Activate Public Distribution` on previous step).
> 
> ![app_register_7.1.png.png](/app/resources/images/app_register_7.1.png)

> Copy `Client ID`, `Client Secret`, `Signing Secret` from `Settings/Basic Information/App Credentials` side menu section.   
> 
> ![app_register_8.png.png](/app/resources/images/app_register_8.png)

> Fill out the `app_auth.conf` file with copied data.  
> After filing the config with necessary information you should end up with a similar file but with your own data:
> ```
> app_auth.conf
> {
>     "FILE_VALIDATION": "complete",
>     "CLIENT_ID": "1234567890123.4567890123456",
>     "CLIENT_SECRET": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
>     "SIGNING_SECRET": "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p",
>     "AUTH_URL": "https://slack.com/oauth/v2/authorize?client_id=1234567890123.4567890123456&scope=&user_scope=channels:history,channels:read,files:read,groups:history,groups:read,im:history,im:read,mpim:history,mpim:read,users:read"
> }
> ```
> Save the file and continue the main flow from the manual.