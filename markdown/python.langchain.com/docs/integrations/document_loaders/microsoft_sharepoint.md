

Skip to main content

On this page

# Microsoft SharePoint

> Microsoft SharePoint is a website-based collaboration system that uses workflow applications, “list” databases, and other web parts and security features to empower business teams to work together
> developed by Microsoft.

This notebook covers how to load documents from the SharePoint Document Library. Currently, only docx, doc, and pdf files are supported.

## Prerequisites​

  1. Register an application with the Microsoft identity platform instructions.
  2. When registration finishes, the Azure portal displays the app registration's Overview pane. You see the Application (client) ID. Also called the `client ID`, this value uniquely identifies your application in the Microsoft identity platform.
  3. During the steps you will be following at **item 1** , you can set the redirect URI as `https://login.microsoftonline.com/common/oauth2/nativeclient`
  4. During the steps you will be following at **item 1** , generate a new password (`client_secret`) under Application Secrets section.
  5. Follow the instructions at this document to add the following `SCOPES` (`offline_access` and `Sites.Read.All`) to your application.
  6. To retrieve files from your **Document Library** , you will need its ID. To obtain it, you will need values of `Tenant Name`, `Collection ID`, and `Subsite ID`.
  7. To find your `Tenant Name` follow the instructions at this document. Once you got this, just remove `.onmicrosoft.com` from the value and hold the rest as your `Tenant Name`.
  8. To obtain your `Collection ID` and `Subsite ID`, you will need your **SharePoint** `site-name`. Your `SharePoint` site URL has the following format `https://<tenant-name>.sharepoint.com/sites/<site-name>`. The last part of this URL is the `site-name`.
  9. To Get the Site `Collection ID`, hit this URL in the browser: `https://<tenant>.sharepoint.com/sites/<site-name>/_api/site/id` and copy the value of the `Edm.Guid` property.
  10. To get the `Subsite ID` (or web ID) use: `https://<tenant>.sharepoint.com/<site-name>/_api/web/id` and copy the value of the `Edm.Guid` property.
  11. The `SharePoint site ID` has the following format: `<tenant-name>.sharepoint.com,<Collection ID>,<subsite ID>`. You can hold that value to use in the next step.
  12. Visit the Graph Explorer Playground to obtain your `Document Library ID`. The first step is to ensure you are logged in with the account associated with your **SharePoint** site. Then you need to make a request to `https://graph.microsoft.com/v1.0/sites/<SharePoint site ID>/drive` and the response will return a payload with a field `id` that holds the ID of your `Document Library ID`.

## 🧑 Instructions for ingesting your documents from SharePoint Document Library​

### 🔑 Authentication​

By default, the `SharePointLoader` expects that the values of `CLIENT_ID` and `CLIENT_SECRET` must be stored as environment variables named `O365_CLIENT_ID` and `O365_CLIENT_SECRET` respectively. You
could pass those environment variables through a `.env` file at the root of your application or using the following command in your script.

```python




    os.environ['O365_CLIENT_ID'] = "YOUR CLIENT ID"
    os.environ['O365_CLIENT_SECRET'] = "YOUR CLIENT SECRET"



```


This loader uses an authentication called _on behalf of a user_. It is a 2 step authentication with user consent. When you instantiate the loader, it will call will print a url that the user must
visit to give consent to the app on the required permissions. The user must then visit this url and give consent to the application. Then the user must copy the resulting page url and paste it back on
the console. The method will then return True if the login attempt was succesful.

```python




    from langchain.document_loaders.sharepoint import SharePointLoader

    loader = SharePointLoader(document_library_id="YOUR DOCUMENT LIBRARY ID")



```


Once the authentication has been done, the loader will store a token (`o365_token.txt`) at `~/.credentials/` folder. This token could be used later to authenticate without the copy/paste steps
explained earlier. To use this token for authentication, you need to change the `auth_with_token` parameter to True in the instantiation of the loader.

```python




    from langchain.document_loaders.sharepoint import SharePointLoader

    loader = SharePointLoader(document_library_id="YOUR DOCUMENT LIBRARY ID", auth_with_token=True)



```


### 🗂️ Documents loader​

#### 📑 Loading documents from a Document Library Directory​

`SharePointLoader` can load documents from a specific folder within your Document Library. For instance, you want to load all documents that are stored at `Documents/marketing` folder within your
Document Library.

```python




    from langchain.document_loaders.sharepoint import SharePointLoader

    loader = SharePointLoader(document_library_id="YOUR DOCUMENT LIBRARY ID", folder_path="Documents/marketing", auth_with_token=True)
    documents = loader.load()



```


#### 📑 Loading documents from a list of Documents IDs​

Another possibility is to provide a list of `object_id` for each document you want to load. For that, you will need to query the Microsoft Graph API to find all the documents ID that you are
interested in. This link provides a list of endpoints that will be helpful to retrieve the documents ID.

For instance, to retrieve information about all objects that are stored at `data/finance/` folder, you need make a request to: `https://graph.microsoft.com/v1.0/drives/<document-library-
id>/root:/data/finance:/children`. Once you have the list of IDs that you are interested in, then you can instantiate the loader with the following parameters.

```python




    from langchain.document_loaders.sharepoint import SharePointLoader

    loader = SharePointLoader(document_library_id="YOUR DOCUMENT LIBRARY ID", object_ids=["ID_1", "ID_2"], auth_with_token=True)
    documents = loader.load()



```
