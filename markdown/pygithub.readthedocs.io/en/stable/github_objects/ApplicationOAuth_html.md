  + ApplicationOAuth

* * *
# ApplicationOAuth¶

_class_ `github.ApplicationOAuth.`  `ApplicationOAuth` ¶

This class is used for identifying and authorizing users for Github Apps. The reference can be found at https://docs.github.com/en/developers/apps/building-github-apps/identifying-and-authorizing-
users-for-github-apps

`get_login_url` ( _redirect_uri: str | None = None_ , _state: str | None = None_ , _login: str | None = None_ ) → str¶

Return the URL you need to redirect a user to in order to authorize your App.

`get_access_token` ( _code: str_ , _state: str | None = None_ ) → AccessToken¶

     Calls:| POST /login/oauth/access_token

---|---

`refresh_access_token` ( _refresh_token: str_ ) → AccessToken¶

     Calls:| POST /login/oauth/access_token

---|---
Parameters:|  **refresh_token** – string
