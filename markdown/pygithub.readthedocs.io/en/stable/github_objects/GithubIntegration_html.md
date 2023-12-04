  + GithubIntegration

* * *
# GithubIntegration¶

_class_ `github.GithubIntegration.`  `GithubIntegration` ¶

Main class to obtain tokens for a GitHub integration.

Parameters:|

  + **integration_id** – int deprecated, use auth=github. Auth. AppAuth(…) instead
  + **private_key** – string deprecated, use auth=github. Auth. AppAuth(…) instead
  + **base_url** – string
  + **timeout** – integer
  + **user_agent** – string
  + **per_page** – int
  + **verify** – boolean or string
  + **retry** – int or urllib3.util.retry. Retry object
  + **pool_size** – int
  + **seconds_between_requests** – float
  + **seconds_between_writes** – float
  + **jwt_expiry** – int deprecated, use auth=github. Auth. AppAuth(…) instead
  + **jwt_issued_at** – int deprecated, use auth=github. Auth. AppAuth(…) instead
  + **jwt_algorithm** – string deprecated, use auth=github. Auth. AppAuth(…) instead
  + **auth** – authentication method

---|---

`close` () → None¶

Close connections to the server. Alternatively, use the GithubIntegration object as a context manager:

[code]

```python

    with github.GithubIntegration(...) as gi:
      # do something

```

[/code]

`create_jwt` ( _expiration: int | None = None_ ) → str¶

Create a signed JWT https://docs.github.com/en/developers/apps/building-github-apps/authenticating-with-github-apps#authenticating-as-a-github-app

`get_access_token` ( _installation_id: int_ , _permissions: dict[str_ , _str] | None = None_ ) → InstallationAuthorization¶

     Calls:| POST /app/installations/{installation_id}/access_tokens <https://docs.github.com/en/rest/apps/apps#create-an-installation-access-token-for-an-app>

---|---

`get_installation` ( _owner: str_ , _repo: str_ ) → github. Installation. Installation¶

Deprecated by get_repo_installation

Calls:| GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app>
---|---

`get_installations` () → github. PaginatedList. PaginatedList[github. Installation. Installation][github. Installation. Installation]¶

     Calls:| GET /app/installations <https://docs.github.com/en/rest/reference/apps#list-installations-for-the-authenticated-app>

---|---

`get_org_installation` ( _org: str_ ) → github. Installation. Installation¶

     Calls:| GET /orgs/{org}/installation <https://docs.github.com/en/rest/apps/apps#get-an-organization-installation-for-the-authenticated-app>

---|---

`get_repo_installation` ( _owner: str_ , _repo: str_ ) → github. Installation. Installation¶

     Calls:| GET /repos/{owner}/{repo}/installation <https://docs.github.com/en/rest/reference/apps#get-a-repository-installation-for-the-authenticated-app>

---|---

`get_user_installation` ( _username: str_ ) → github. Installation. Installation¶

     Calls:| GET /users/{username}/installation <https://docs.github.com/en/rest/apps/apps#get-a-user-installation-for-the-authenticated-app>

---|---

`get_app_installation` ( _installation_id: int_ ) → github. Installation. Installation¶

     Calls:| GET /app/installations/{installation_id} <https://docs.github.com/en/rest/apps/apps#get-an-installation-for-the-authenticated-app>

---|---

`get_app` () → github. GithubApp. GithubApp¶

     Calls:| GET /app

---|---
