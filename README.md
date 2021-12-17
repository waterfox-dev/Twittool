# Twittool 

For the moment, this app is under development, it is unusable and this repository exists only to participate in the development of it.

### __Before to continue...__

If you want to dev this app, you need to know some details. 

Firstly, you need your own API key and authentication to test this app. For the system use your API credentials, you will be create a folder in `server` and call it `data`,  and you need to create a file : `twitterApi.json`. Content of `server/data/twitterApi.json`:

```json
{
    "api_key" : "your api key",
    "api_secret_key" : "Your api secret key",
    "bearer_token" : "Your bearer token"
} 
```

Also, you need to install the Flask library (for the moment not any kind of transition to Django are planned). 

### __What can I do ?__

There is a lot of work, and you can work on a specific place :

- #### __HTML template__

You can work on HTML templates, their are based on a Jinja system and you can modified this to adapt django for  a better compatibility. The folder of templates is `server/templates`, you can also work on the CSS, stylesheets are in `server/static/style` folder. 

- #### __Javascript__

Each pages got a specific javascript script. You can add animation and javascript tools to their. Warning, you can't use npm modules and node core, only native javascript are support, but you can work on a update for link  node and flask. Javascript folder is `server/static/script`.

- #### __Python Core__

There is a lot of work on the python core. You can update the modules, and the classes. 