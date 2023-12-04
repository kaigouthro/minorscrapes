  + Organization

* * *
# Organization¶

_class_ `github.Organization.`  `Organization` ¶

This class represents Organizations. The reference can be found here https://docs.github.com/en/rest/reference/orgs

`add_to_members` ( _member: NamedUser_ , _role: Opt[str] = NotSet_ ) → None¶

     Calls:| PUT /orgs/{org}/memberships/{user}

---|---

`add_to_public_members` ( _public_member: NamedUser_ ) → None¶

     Calls:| PUT /orgs/{org}/public_members/{user}

---|---

`create_fork` ( _repo: Repository_ , _name: Opt[str] = NotSet_ , _default_branch_only: Opt[bool] = NotSet_ ) → Repository¶

     Calls:| POST /repos/{owner}/{repo}/forks

---|---

`create_repo_from_template` ( _name: str_ , _repo: Repository_ , _description: Opt[str] = NotSet_ , _private: Opt[bool] = NotSet_ ) → Repository¶

self.name :calls: POST /repos/{template_owner}/{template_repo}/generate

`create_hook` ( _name: str, config: dict[str, str], events: Opt[list[str]] = NotSet, active: Opt[bool] = NotSet_ ) → Hook¶

     Calls:|

POST /orgs/{owner}/hooks

---|---
Parameters:|

  + **name** – string
  + **config** – dict
  + **events** – list of string
  + **active** – bool

Return type:|

 `github.Hook.Hook`

`create_project` ( _name: str_ , _body: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) → github. Project. Project¶

     Calls:| POST /orgs/{org}/projects

---|---

`create_repo` ( _name: str_ , _description: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _homepage: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _private: Union[bool_ , 
_github. GithubObject._NotSetType] = NotSet_ , _visibility: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _has_issues: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ , 
_has_wiki: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ , _has_downloads: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ , _has_projects: Union[bool_ , 
_github. GithubObject._NotSetType] = NotSet_ , _team_id: Union[int_ , _github. GithubObject._NotSetType] = NotSet_ , _auto_init: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ , 
_license_template: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _gitignore_template: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _allow_squash_merge: Union[bool_ , 
_github. GithubObject._NotSetType] = NotSet_ , _allow_merge_commit: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ , _allow_rebase_merge: Union[bool_ , _github. GithubObject._NotSetType] =
NotSet_ , _delete_branch_on_merge: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ , _allow_update_branch: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ ) →
github. Repository. Repository¶

     Calls:| POST /orgs/{org}/repos

---|---

`create_secret` ( _secret_name: str_ , _unencrypted_value: str_ , _visibility: str = 'all'_ , _selected_repositories: Opt[list[github. Repository. Repository]] = NotSet_ ) →
github. OrganizationSecret. OrganizationSecret¶

     Calls:| PUT /orgs/{org}/actions/secrets/{secret_name}

---|---

`get_secrets` () → PaginatedList[OrganizationSecret]¶

Gets all organization secrets :rtype: `PaginatedList` of `github.OrganizationSecret.OrganizationSecret`

`get_secret` ( _secret_name: str_ ) → OrganizationSecret¶

     Calls:| ‘GET /orgs/{org}/actions/secrets/{secret_name} <https://docs.github.com/en/rest/actions/secrets#get-an-organization-secret>`_

---|---
Parameters:|  **secret_name** – string
Return type:| github. OrganizationSecret. OrganizationSecret

`create_team` ( _name: str_ , _repo_names: Opt[list[Repository]] = NotSet_ , _permission: Opt[str] = NotSet_ , _privacy: Opt[str] = NotSet_ , _description: Opt[str] = NotSet_ ) → Team¶

     Calls:|

POST /orgs/{org}/teams

---|---
Parameters:|

  + **name** – string
  + **repo_names** – list of `github.Repository.Repository`
  + **permission** – string
  + **privacy** – string
  + **description** – string

Return type:|

 `github.Team.Team`

`create_variable` ( _variable_name: str_ , _value: str_ , _visibility: str = 'all'_ , _selected_repositories: github. GithubObject. Opt[list[github. Repository. Repository]] = NotSet_ ) →
github. OrganizationVariable. OrganizationVariable¶

     Calls:|

POST /orgs/{org}/actions/variables/

---|---
Parameters:|

  + **variable_name** – string
  + **value** – string
  + **visibility** – string
  + **selected_repositories** – list of `github.Repository.Repository`

Return type:|

github. OrganizationVariable. OrganizationVariable

`get_variables` () → PaginatedList[OrganizationVariable]¶

Gets all organization variables :rtype: `PaginatedList` of `github.OrganizationVariable.OrganizationVariable`

`get_variable` ( _variable_name: str_ ) → OrganizationVariable¶

     Calls:| ‘GET /orgs/{org}/actions/variables/{variable_name} <https://docs.github.com/en/rest/actions/variables#get-an-organization-variable>`_

---|---
Parameters:|  **variable_name** – string
Return type:| github. OrganizationVariable. OrganizationVariable

`delete_hook` ( _id: int_ ) → None¶

     Calls:| DELETE /orgs/{owner}/hooks/{id}

---|---
Parameters:|  **id** – integer
Return type:| None`

`edit` ( _billing_email: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _blog: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _company: Union[str_ , 
_github. GithubObject._NotSetType] = NotSet_ , _description: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _email: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _location:
Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _name: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /orgs/{org}

---|---

`edit_hook` ( _id: int, name: str, config: dict[str, str], events: Opt[list[str]] = NotSet, active: Opt[bool] = NotSet_ ) → Hook¶

     Calls:| PATCH /orgs/{owner}/hooks/{id}

---|---

`get_events` () → PaginatedList[Event]¶

     Calls:| GET /orgs/{org}/events

---|---
Return type:| `PaginatedList` of `github.Event.Event`

`get_hook` ( _id: int_ ) → github. Hook. Hook¶

     Calls:| GET /orgs/{owner}/hooks/{id}

---|---

`get_hooks` () → PaginatedList[Hook]¶

     Calls:| GET /orgs/{owner}/hooks

---|---

`get_hook_delivery` ( _hook_id: int_ , _delivery_id: int_ ) → github. HookDelivery. HookDelivery¶

     Calls:|

GET /orgs/{owner}/hooks/{hook_id}/deliveries/{delivery_id}

---|---
Parameters:|

  + **hook_id** – integer
  + **delivery_id** – integer

Return type:|

 `github.HookDelivery.HookDelivery`

`get_hook_deliveries` ( _hook_id: int_ ) → github. PaginatedList. PaginatedList[github. HookDelivery. HookDeliverySummary][github. HookDelivery. HookDeliverySummary]¶

     Calls:| GET /orgs/{owner}/hooks/{hook_id}/deliveries

---|---
Parameters:|  **hook_id** – integer
Return type:| `PaginatedList` of `github.HookDelivery.HookDeliverySummary`

`get_issues` ( _filter: Opt[str] = NotSet_ , _state: Opt[str] = NotSet_ , _labels: Opt[list[Label]] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _since: Opt[datetime] =
NotSet_ ) → PaginatedList[Issue]¶

     Calls:|

GET /orgs/{org}/issues

---|---
Return type:|

`PaginatedList` of `github.Issue.Issue`

Parameters:|

  + **filter** – string
  + **state** – string
  + **labels** – list of `github.Label.Label`
  + **sort** – string
  + **direction** – string
  + **since** – datetime

Return type:|

`PaginatedList` of `github.Issue.Issue`

`get_members` ( _filter_: Opt[str] = NotSet_ , _role: Opt[str] = NotSet_ ) → PaginatedList[NamedUser]¶

     Calls:| GET /orgs/{org}/members

---|---

`get_projects` ( _state: Opt[str] = NotSet_ ) → PaginatedList[Project]¶

     Calls:| GET /orgs/{org}/projects

---|---

`get_public_members` () → PaginatedList[NamedUser]¶

     Calls:| GET /orgs/{org}/public_members

---|---
Return type:| `PaginatedList` of `github.NamedUser.NamedUser`

`get_outside_collaborators` ( _filter_: Opt[str] = NotSet_ ) → PaginatedList[NamedUser]¶

     Calls:| GET /orgs/{org}/outside_collaborators

---|---

`remove_outside_collaborator` ( _collaborator: NamedUser_ ) → None¶

     Calls:| DELETE /orgs/{org}/outside_collaborators/{username}

---|---
Parameters:|  **collaborator** – `github.NamedUser.NamedUser`

Return type:| None

`convert_to_outside_collaborator` ( _member: NamedUser_ ) → None¶

     Calls:| PUT /orgs/{org}/outside_collaborators/{username}

---|---
Parameters:|  **member** – `github.NamedUser.NamedUser`

Return type:| None

`get_public_key` () → PublicKey¶

     Calls:| GET /orgs/{org}/actions/secrets/public-key

---|---
Return type:| `github.PublicKey.PublicKey`

`get_repo` ( _name: str_ ) → Repository¶

     Calls:| GET /repos/{owner}/{repo}

---|---
Parameters:|  **name** – string
Return type:| `github.Repository.Repository`

`get_repos` ( _type: Opt[str] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ ) → PaginatedList[Repository]¶

     Calls:|

GET /orgs/{org}/repos

---|---
Parameters:|

  + **type** – string (‘all’, ‘public’, ‘private’, ‘forks’, ‘sources’, ‘member’)
  + **sort** – string (‘created’, ‘updated’, ‘pushed’, ‘full_name’)
  + **direction** – string (‘asc’, desc’)

`get_team` ( _id: int_ ) → Team¶

     Calls:| GET /teams/{id}

---|---

`get_team_by_slug` ( _slug: str_ ) → Team¶

     Calls:| GET /orgs/{org}/teams/{team_slug}

---|---

`get_teams` () → PaginatedList[Team]¶

     Calls:| GET /orgs/{org}/teams

---|---

`invitations` () → PaginatedList[NamedUser]¶

     Calls:| GET /orgs/{org}/invitations

---|---

`invite_user` ( _user: Opt[NamedUser] = NotSet_ , _email: Opt[str] = NotSet_ , _role: Opt[str] = NotSet_ , _teams: Opt[list[Team]] = NotSet_ ) → None¶

     Calls:|

POST /orgs/{org}/invitations

---|---
Parameters:|

  + **user** – `github.NamedUser.NamedUser`
  + **email** – string
  + **role** – string
  + **teams** – array of `github.Team.Team`

Return type:|

None

`cancel_invitation` ( _invitee: NamedUser_ ) → bool¶

     Calls:| DELETE /orgs/{org}/invitations/{invitation_id}

---|---
Parameters:|  **invitee** – `github.NamedUser.NamedUser`

Return type:| None

`has_in_members` ( _member: NamedUser_ ) → bool¶

     Calls:| GET /orgs/{org}/members/{user}

---|---
Parameters:|  **member** – `github.NamedUser.NamedUser`

Return type:| bool

`has_in_public_members` ( _public_member: NamedUser_ ) → bool¶

     Calls:| GET /orgs/{org}/public_members/{user}

---|---
Parameters:|  **public_member** – `github.NamedUser.NamedUser`

Return type:| bool

`remove_from_membership` ( _member: NamedUser_ ) → None¶

     Calls:| DELETE /orgs/{org}/memberships/{user}

---|---
Parameters:|  **member** – `github.NamedUser.NamedUser`

Return type:| None

`remove_from_members` ( _member: NamedUser_ ) → None¶

     Calls:| DELETE /orgs/{org}/members/{user}

---|---
Parameters:|  **member** – `github.NamedUser.NamedUser`

Return type:| None

`remove_from_public_members` ( _public_member: NamedUser_ ) → None¶

     Calls:| DELETE /orgs/{org}/public_members/{user}

---|---
Parameters:|  **public_member** – `github.NamedUser.NamedUser`

Return type:| None

`create_migration` ( _repos: list[str], lock_repositories: Opt[bool] = NotSet, exclude_attachments: Opt[bool] = NotSet_ ) → Migration¶

     Calls:|

POST /orgs/{org}/migrations

---|---
Parameters:|

  + **repos** – list or tuple of str
  + **lock_repositories** – bool
  + **exclude_attachments** – bool

Return type:|

 `github.Migration.Migration`

`get_migrations` () → PaginatedList[Migration]¶

     Calls:| GET /orgs/{org}/migrations

---|---
Return type:| `PaginatedList` of `github.Migration.Migration`

`get_installations` () → PaginatedList[Installation]¶

     Calls:| GET /orgs/{org}/installations

---|---
Return type:| `PaginatedList` of `github.Installation.Installation`
