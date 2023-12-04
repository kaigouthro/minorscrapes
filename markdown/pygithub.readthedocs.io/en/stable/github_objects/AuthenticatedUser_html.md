  + AuthenticatedUser

* * *
# AuthenticatedUser¶

_class_ `github.AuthenticatedUser.`  `AuthenticatedUser` ¶

This class represents AuthenticatedUsers as returned by https://docs.github.com/en/rest/reference/users#get-the-authenticated-user

An AuthenticatedUser object can be created by calling `get_user()` on a Github object.

`add_to_emails` ( _*emails_ ) → None¶

     Calls:| POST /user/emails

---|---

`add_to_following` ( _following: NamedUser_ ) → None¶

     Calls:| PUT /user/following/{user}

---|---

`add_to_starred` ( _starred: Repository_ ) → None¶

     Calls:| PUT /user/starred/{owner}/{repo}

---|---

`add_to_subscriptions` ( _subscription: Repository_ ) → None¶

     Calls:| PUT /user/subscriptions/{owner}/{repo}

---|---

`add_to_watched` ( _watched: Repository_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/subscription

---|---

`create_authorization` ( _scopes: Opt[list[str]] = NotSet_ , _note: Opt[str] = NotSet_ , _note_url: Opt[str] = NotSet_ , _client_id: Opt[str] = NotSet_ , _client_secret: Opt[str] = NotSet_ , 
_onetime_password: str | None = None_ ) → Authorization¶

     Calls:| POST /authorizations

---|---

_static_ `create_fork` ( _repo: Repository_ , _name: Opt[str] = NotSet_ , _default_branch_only: Opt[bool] = NotSet_ ) → Repository¶

     Calls:| POST /repos/{owner}/{repo}/forks

---|---

`create_repo_from_template` ( _name: str_ , _repo: Repository_ , _description: Opt[str] = NotSet_ , _private: Opt[bool] = NotSet_ ) → Repository¶

     Calls:| POST /repos/{template_owner}/{template_repo}/generate

---|---

`create_gist` ( _public: bool, files: dict[str, InputFileContent], description: Opt[str] = NotSet_ ) → Gist¶

     Calls:| POST /gists

---|---

`create_key` ( _title: str_ , _key: str_ ) → UserKey¶

     Calls:|

POST /user/keys

---|---
Parameters:|

  + **title** – string
  + **key** – string

Return type:|

 `github.UserKey.UserKey`

`create_project` ( _name: str_ , _body: Opt[str] = NotSet_ ) → Project¶

     Calls:|

POST /user/projects

---|---
Parameters:|

  + **name** – string
  + **body** – string

Return type:|

 `github.Project.Project`

`create_repo` ( _name: str_ , _description: Opt[str] = NotSet_ , _homepage: Opt[str] = NotSet_ , _private: Opt[bool] = NotSet_ , _has_issues: Opt[bool] = NotSet_ , _has_wiki: Opt[bool] = NotSet_ , 
_has_downloads: Opt[bool] = NotSet_ , _has_projects: Opt[bool] = NotSet_ , _auto_init: Opt[bool] = NotSet_ , _license_template: Opt[str] = NotSet_ , _gitignore_template: Opt[str] = NotSet_ , 
_allow_squash_merge: Opt[bool] = NotSet_ , _allow_merge_commit: Opt[bool] = NotSet_ , _allow_rebase_merge: Opt[bool] = NotSet_ , _delete_branch_on_merge: Opt[bool] = NotSet_ ) → Repository¶

     Calls:| POST /user/repos

---|---

`edit` ( _name: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _email: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _blog: Union[str_ , _github. GithubObject._NotSetType] =
NotSet_ , _company: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _location: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _hireable: Union[bool_ , 
_github. GithubObject._NotSetType] = NotSet_ , _bio: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /user

---|---

`get_authorization` ( _id: int_ ) → Authorization¶

     Calls:| GET /authorizations/{id}

---|---

`get_authorizations` () → PaginatedList[Authorization]¶

     Calls:| GET /authorizations

---|---

`get_emails` () → list[EmailData]¶

     Calls:| GET /user/emails

---|---

`get_events` () → PaginatedList[Event]¶

     Calls:| GET /events

---|---

`get_followers` () → PaginatedList[NamedUser]¶

     Calls:| GET /user/followers

---|---

`get_following` () → PaginatedList[NamedUser]¶

     Calls:| GET /user/following

---|---

`get_gists` ( _since: Opt[datetime] = NotSet_ ) → PaginatedList[Gist]¶

     Calls:| GET /gists

---|---
Parameters:|  **since** – datetime format YYYY-MM-DDTHH: MM: SSZ
Return type:| `PaginatedList` of `github.Gist.Gist`

`get_issues` ( _filter: Opt[str] = NotSet_ , _state: Opt[str] = NotSet_ , _labels: Opt[list[Label]] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _since: Opt[datetime] =
NotSet_ ) → PaginatedList[Issue]¶

     Calls:| GET /issues

---|---

`get_user_issues` ( _filter: Opt[str] = NotSet_ , _state: Opt[str] = NotSet_ , _labels: Opt[list[Label]] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _since: Opt[datetime] =
NotSet_ ) → PaginatedList[Issue]¶

     Calls:| GET /user/issues

---|---

`get_key` ( _id: int_ ) → UserKey¶

     Calls:| GET /user/keys/{id}

---|---

`get_keys` () → PaginatedList[UserKey]¶

     Calls:| GET /user/keys

---|---

`get_notification` ( _id: str_ ) → Notification¶

     Calls:| GET /notifications/threads/{id}

---|---

`get_notifications` ( _all: Opt[bool] = NotSet_ , _participating: Opt[bool] = NotSet_ , _since: Opt[datetime] = NotSet_ , _before: Opt[datetime] = NotSet_ ) → PaginatedList[Notification]¶

     Calls:| GET /notifications

---|---

`get_organization_events` ( _org: Organization_ ) → PaginatedList[Event]¶

     Calls:| GET /users/{user}/events/orgs/{org}

---|---

`get_orgs` () → PaginatedList[Organization]¶

     Calls:| GET /user/orgs

---|---

`get_repo` ( _name: str_ ) → Repository¶

     Calls:| GET /repos/{owner}/{repo}

---|---

`get_repos` ( _visibility: Opt[str] = NotSet_ , _affiliation: Opt[str] = NotSet_ , _type: Opt[str] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ ) → PaginatedList[Repository]¶

     Calls:| GET /user/repos

---|---

`get_starred` () → PaginatedList[Repository]¶

     Calls:| GET /user/starred

---|---

`get_starred_gists` () → PaginatedList[Gist]¶

     Calls:| GET /gists/starred

---|---

`get_subscriptions` () → PaginatedList[Repository]¶

     Calls:| GET /user/subscriptions

---|---

`get_teams` () → PaginatedList[Team]¶

     Calls:| GET /user/teams

---|---

`get_watched` () → PaginatedList[Repository]¶

     Calls:| GET /user/subscriptions

---|---

`get_installations` () → PaginatedList[Installation]¶

     Calls:| GET /user/installations

---|---

`has_in_following` ( _following: NamedUser_ ) → bool¶

     Calls:| GET /user/following/{user}

---|---

`has_in_starred` ( _starred: Repository_ ) → bool¶

     Calls:| GET /user/starred/{owner}/{repo}

---|---

`has_in_subscriptions` ( _subscription: Repository_ ) → bool¶

     Calls:| GET /user/subscriptions/{owner}/{repo}

---|---

`has_in_watched` ( _watched: Repository_ ) → bool¶

     Calls:| GET /repos/{owner}/{repo}/subscription

---|---

`mark_notifications_as_read` ( _last_read_at: datetime | None = None_ ) → None¶

     Calls:| PUT /notifications

---|---

`remove_from_emails` ( _*emails_ ) → None¶

     Calls:| DELETE /user/emails

---|---

`remove_from_following` ( _following: NamedUser_ ) → None¶

     Calls:| DELETE /user/following/{user}

---|---

`remove_from_starred` ( _starred: Repository_ ) → None¶

     Calls:| DELETE /user/starred/{owner}/{repo}

---|---

`remove_from_subscriptions` ( _subscription: Repository_ ) → None¶

     Calls:| DELETE /user/subscriptions/{owner}/{repo}

---|---

`remove_from_watched` ( _watched: Repository_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/subscription

---|---

`accept_invitation` ( _invitation: Invitation | int_ ) → None¶

     Calls:| PATCH /user/repository_invitations/{invitation_id}

---|---

`get_invitations` () → PaginatedList[Invitation]¶

     Calls:| GET /user/repository_invitations

---|---

`create_migration` ( _repos: list[Repository] | tuple[Repository], lock_repositories: Opt[bool] = NotSet, exclude_attachments: Opt[bool] = NotSet_ ) → Migration¶

     Calls:| POST /user/migrations

---|---

`get_migrations` () → PaginatedList[Migration]¶

     Calls:| GET /user/migrations

---|---

`get_organization_membership` ( _org: str_ ) → Membership¶

     Calls:| GET /user/memberships/orgs/{org}

---|---
