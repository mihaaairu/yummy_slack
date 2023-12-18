# Slack-App creation manual

We need to collect some data for our `app_auth.conf` file, which is being created on `Yummy Slack` first launch and looks like this:

```
app_auth.conf
{
    "File validation": "Replace this text with a single word 'complete', after you update Slack-App auth data below.",
    "Client ID": "Replace this text with your Slack-App 'Client ID'.",
    "Client Secret": "Replace this text with your Slack-App 'Client Secret'.",
    "Signing Secret": "Replace this text with your Slack-App 'Signing Secret'.",
    "Sharable URL": "Replace this text with your Slack-App 'Sharable URL'."
}
```
 
__To fill your file with data, you need to create your own Slack-App.__  
So, let's get started.   

## Slack-App creation

To create a bare application go to [Slack applications space](https://api.slack.com/apps) and create your Slack-App.

<kbd> <img src="/app/resources/images/app_register_1.png" /> </kbd>

Choose `From scratch` option.  

<kbd> <img src="/app/resources/images/app_register_2.png" /> </kbd>

Name your Slack-App, choose your target workspace and press `Create App`.   

<kbd> <img src="/app/resources/images/app_register_3.png" /> </kbd>

## OAuth & Permissions
To allow the application to interact with our workspace we need to provide the required `User Token Scopes` in `Features/OAuth & Permissions/Scopes` side menu section.  

<kbd> <img src="/app/resources/images/app_register_4.png" /> </kbd>

Here are the required scopes:
- channels:history
- channels:read
- files:read
- groups:history
- groups:read
- im:history
- im:read
- mpim:history
- mpim:read
- users:read

Set up redirect URL with `https://127.0.0.1:5000/` in `Features/OAuth & Permissions/Redirect URLs` side menu section. It's used in OAuth process in Slack auth-response receiving. "Yummy Slack" will listen to this address and receive a response from the Slack through it.  
 
<kbd> <img src="/app/resources/images/app_register_5.png" /> </kbd>  

> [!TIP]  
> If you want to use another redirect URL, you need to redeclare it in code. In addition, you should use `https` protocol, as long as Slack doesn't work with `http` protocol at all.

## Manage Distribution

Now we need to save a `Sharable URL`, which will be used in workspace authorisation process.  

> [!Note]   
> You can `Activate Public Distribution` in case you want to share your Slack-App with other workspaces (add the same slack-backend to your another workspace a.e.).  
> 
> Confirm that you have removed all personal data from the code in `Settings/Manage Distribution/Share Your App with Other Workspaces` side menu section.  
> 
> <kbd> <img src="/app/resources/images/app_register_6.png" /> </kbd>

Copy `Sharable URL` from `Settings/Manage Distribution/Share Your App with Your Workspace` side menu section.  

<kbd> <img src="/app/resources/images/app_register_7.1.png" /> </kbd>

> [!TIP]
> You need to copy `Sharable URL` from `Share Your App with Any Workspaces` instead, in case you choose to `Activate Public Distribution` on previous step.

## App Credentials
Copy `Client ID`, `Client Secret`, `Signing Secret` from `Settings/Basic Information/App Credentials` side menu section, which will be used in workspace authorisation process either.  

<kbd> <img src="/app/resources/images/app_register_8.png" /> </kbd>

## Complete the config file
Fill out the `app_auth.conf` file with data, copied on previous steps.  
After filing the config with necessary information you should end up with a similar file but with your own data:
```
app_auth.conf
{
    "FILE_VALIDATION": "complete",
    "CLIENT_ID": "1234567890123.4567890123456",
    "CLIENT_SECRET": "a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6",
    "SIGNING_SECRET": "1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p",
    "AUTH_URL": "https://slack.com/oauth/v2/authorize?client_id=1234567890123.4567890123456&scope=&user_scope=channels:history,channels:read,files:read,groups:history,groups:read,im:history,im:read,mpim:history,mpim:read,users:read"
}
```
Save the file and continue the main flow from the manual.
