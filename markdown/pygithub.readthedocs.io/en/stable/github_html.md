  + Docs »
  + Reference »
  + Main class: Github

* * *
# Main class: Github¶

_class_ `github.MainClass.`  `Github` ( _login_or_token: str | None = None_ , _password: str | None = None_ , _jwt: str | None = None_ , _app_auth: AppAuthentication | None = None_ , _base_url: str =
'https://api.github.com'_ , _timeout: int = 15_ , _user_agent: str = 'PyGithub/Python'_ , _per_page: int = 30_ , _verify: bool | str = True_ , _retry: int | Retry | None = GithubRetry(total=10_ , 
_connect=None_ , _read=None_ , _redirect=None_ , _status=None)_ , _pool_size: int | None = None_ , _seconds_between_requests: float | None = 0.25_ , _seconds_between_writes: float | None = 1.0_ , 
_auth: github. Auth. Auth | None = None_ )¶

This is the main class you instantiate to access the Github API v3. Optional parameters allow different authentication methods.

Parameters:|

  + **login_or_token** – string deprecated, use auth=github. Auth. Login(…) or auth=github. Auth. Token(…) instead
  + **password** – string deprecated, use auth=github. Auth. Login(…) instead
  + **jwt** – string deprecated, use auth=github. Auth. AppAuth(…) or auth=github. Auth. AppAuthToken(…) instead
  + **app_auth** – github. AppAuthentication deprecated, use auth=github. Auth. AppInstallationAuth(…) instead
  + **base_url** – string
  + **timeout** – integer
  + **user_agent** – string
  + **per_page** – int
  + **verify** – boolean or string
  + **retry** – int or urllib3.util.retry. Retry object, defaults to github. Github.default_retry, set to None to disable retries
  + **pool_size** – int
  + **seconds_between_requests** – float
  + **seconds_between_writes** – float
  + **auth** – authentication method

---|---

`close` () → None¶

Close connections to the server. Alternatively, use the Github object as a context manager:

[code]

```python

    with github.Github(...) as gh:
      # do something

```

[/code]

`rate_limiting` ¶

First value is requests remaining, second value is request limit.

`rate_limiting_resettime` ¶

Unix timestamp indicating when rate limiting will reset.

`get_rate_limit` () → github. RateLimit. RateLimit¶

Rate limit status for different resources (core/search/graphql).

Calls:| GET /rate_limit
---|---

`oauth_scopes` ¶

     Type:| list of string

---|---

`get_license` ( _key: Opt[str] = NotSet_ ) → License¶

     Calls:| GET /license/{license}

---|---

`get_licenses` () → PaginatedList[License]¶

     Calls:| GET /licenses

---|---

`get_events` () → PaginatedList[Event]¶

     Calls:| GET /events

---|---

`get_user` ( _login: Opt[str] = NotSet_ ) → NamedUser | AuthenticatedUser¶

     Calls:| GET /users/{user} or GET /user

---|---

`get_user_by_id` ( _user_id: int_ ) → NamedUser¶

     Calls:| GET /user/{id}

---|---
Parameters:|  **user_id** – int
Return type:| `github.NamedUser.NamedUser`

`get_users` ( _since: Opt[int] = NotSet_ ) → PaginatedList[NamedUser]¶

     Calls:| GET /users

---|---

`get_organization` ( _login: str_ ) → Organization¶

     Calls:| GET /orgs/{org}

---|---

`get_organizations` ( _since: Opt[int] = NotSet_ ) → PaginatedList[Organization]¶

     Calls:| GET /organizations

---|---

`get_enterprise` ( _enterprise: str_ ) → github. Enterprise. Enterprise¶

     Calls:| GET /enterprises/{enterprise}

---|---
Parameters:|  **enterprise** – string
Return type:| `Enterprise`

`get_repo` ( _full_name_or_id: int | str_ , _lazy: bool = False_ ) → Repository¶

     Calls:| GET /repos/{owner}/{repo} or GET /repositories/{id}

---|---

`get_repos` ( _since: Opt[int] = NotSet_ , _visibility: Opt[str] = NotSet_ ) → PaginatedList[Repository]¶

     Calls:|

GET /repositories

---|---
Parameters:|

  + **since** – integer
  + **visibility** – string (‘all’, ’public’)

`get_project` ( _id: int_ ) → Project¶

     Calls:| GET /projects/{project_id}

---|---

`get_project_column` ( _id: int_ ) → ProjectColumn¶

     Calls:| GET /projects/columns/{column_id}

---|---

`get_gist` ( _id: str_ ) → Gist¶

     Calls:| GET /gists/{id}

---|---

`get_gists` ( _since: Opt[datetime] = NotSet_ ) → PaginatedList[Gist]¶

     Calls:| GET /gists/public

---|---

`search_repositories` ( _query: str_ , _sort: Opt[str] = NotSet_ , _order: Opt[str] = NotSet_ , _**qualifiers_ ) → PaginatedList[Repository]¶

     Calls:|

GET /search/repositories

---|---
Parameters:|

  + **query** – string
  + **sort** – string (‘stars’, ‘forks’, ‘updated’)
  + **order** – string (‘asc’, ‘desc’)
  + **qualifiers** – keyword dict query qualifiers

`search_users` ( _query: str_ , _sort: Opt[str] = NotSet_ , _order: Opt[str] = NotSet_ , _**qualifiers_ ) → PaginatedList[NamedUser]¶

     Calls:|

GET /search/users

---|---
Parameters:|

  + **query** – string
  + **sort** – string (‘followers’, ‘repositories’, ‘joined’)
  + **order** – string (‘asc’, ‘desc’)
  + **qualifiers** – keyword dict query qualifiers

Return type:|

`PaginatedList` of `github.NamedUser.NamedUser`

`search_issues` ( _query: str_ , _sort: Opt[str] = NotSet_ , _order: Opt[str] = NotSet_ , _**qualifiers_ ) → PaginatedList[Issue]¶

     Calls:|

GET /search/issues

---|---
Parameters:|

  + **query** – string
  + **sort** – string (‘comments’, ‘created’, ‘updated’)
  + **order** – string (‘asc’, ‘desc’)
  + **qualifiers** – keyword dict query qualifiers

Return type:|

`PaginatedList` of `github.Issue.Issue`

`search_code` ( _query: str_ , _sort: Opt[str] = NotSet_ , _order: Opt[str] = NotSet_ , _highlight: bool = False_ , _**qualifiers_ ) → PaginatedList[ContentFile]¶

     Calls:|

GET /search/code

---|---
Parameters:|

  + **query** – string
  + **sort** – string (‘indexed’)
  + **order** – string (‘asc’, ‘desc’)
  + **highlight** – boolean (True, False)
  + **qualifiers** – keyword dict query qualifiers

Return type:|

`PaginatedList` of `github.ContentFile.ContentFile`

`search_commits` ( _query: str_ , _sort: Opt[str] = NotSet_ , _order: Opt[str] = NotSet_ , _**qualifiers_ ) → PaginatedList[Commit]¶

     Calls:|

GET /search/commits

---|---
Parameters:|

  + **query** – string
  + **sort** – string (‘author-date’, ‘committer-date’)
  + **order** – string (‘asc’, ‘desc’)
  + **qualifiers** – keyword dict query qualifiers

Return type:|

`PaginatedList` of `github.Commit.Commit`

`search_topics` ( _query: str_ , _**qualifiers_ ) → PaginatedList[Topic]¶

     Calls:|

GET /search/topics

---|---
Parameters:|

  + **query** – string
  + **qualifiers** – keyword dict query qualifiers

Return type:|

`PaginatedList` of `github.Topic.Topic`

`render_markdown` ( _text: str_ , _context: Opt[Repository] = NotSet_ ) → str¶

     Calls:|

POST /markdown

---|---
Parameters:|

  + **text** – string
  + **context** – `github.Repository.Repository`

Return type:|

string

`get_hook` ( _name: str_ ) → github. HookDescription. HookDescription¶

     Calls:| GET /hooks/{name}

---|---

`get_hooks` () → list[HookDescription]¶

     Calls:| GET /hooks

---|---
Return type:| list of `github.HookDescription.HookDescription`

`get_hook_delivery` ( _hook_id: int_ , _delivery_id: int_ ) → github. HookDelivery. HookDelivery¶

     Calls:|

GET /hooks/{hook_id}/deliveries/{delivery_id}

---|---
Parameters:|

  + **hook_id** – integer
  + **delivery_id** – integer

Return type:|

 `HookDelivery`

`get_hook_deliveries` ( _hook_id: int_ ) → list[HookDeliverySummary]¶

     Calls:| GET /hooks/{hook_id}/deliveries

---|---
Parameters:|  **hook_id** – integer
Return type:| list of `HookDeliverySummary`

`get_gitignore_templates` () → list[str]¶

     Calls:| GET /gitignore/templates

---|---

`get_gitignore_template` ( _name: str_ ) → GitignoreTemplate¶

     Calls:| GET /gitignore/templates/{name}

---|---

`get_emojis` () → dict[str, str]¶

     Calls:| GET /emojis

---|---
Return type:| dictionary of type => url for emoji`

`create_from_raw_data` ( _klass: type[TGithubObject], raw_data: dict[str, Any], headers: dict[str, str | int] | None = None_ ) → TGithubObject¶

Creates an object from raw_data previously obtained by `GithubObject.raw_data` , and optionally headers previously obtained by `GithubObject.raw_headers` .

Parameters:|

  + **klass** – the class of the object to create
  + **raw_data** – dict
  + **headers** – dict

---|---
Return type:|

instance of class `klass`

`dump` ( _obj: github. GithubObject. GithubObject_ , _file: BinaryIO_ , _protocol: int = 0_ ) → None¶

Dumps (pickles) a PyGithub object to a file-like object. Some effort is made to not pickle sensitive information like the Github credentials used in the `Github` instance. But NO EFFORT is made to
remove sensitive information from the object’s attributes.

Parameters:|

  + **obj** – the object to pickle
  + **file** – the file-like object to pickle to
  + **protocol** – the pickling protocol

---|---

`load` ( _f: BinaryIO_ ) → Any¶

Loads (unpickles) a PyGithub object from a file-like object.

Parameters:|  **f** – the file-like object to unpickle from
---|---
Returns:| the unpickled object

`get_app` ( _slug: Opt[str] = NotSet_ ) → GithubApp¶

     Calls:| GET /apps/{slug} or GET /app

---|---
