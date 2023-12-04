  + Team

* * *
# Team¶

_class_ `github.Team.`  `Team` ¶

This class represents Teams. The reference can be found here https://docs.github.com/en/rest/reference/teams

`add_to_members` ( _member: NamedUser_ ) → None¶

This API call is deprecated. Use add_membership instead. https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy

Calls:| PUT /teams/{id}/members/{user}
---|---

`add_membership` ( _member: NamedUser_ , _role: Opt[str] = NotSet_ ) → None¶

     Calls:| PUT /teams/{id}/memberships/{user}

---|---

`get_team_membership` ( _member: str | NamedUser_ ) → Membership¶

     Calls:| GET /orgs/{org}/memberships/team/{team_id}/{username}

---|---

`add_to_repos` ( _repo: Repository_ ) → None¶

     Calls:| PUT /teams/{id}/repos/{org}/{repo}

---|---

`get_repo_permission` ( _repo: Repository_ ) → Permissions | None¶

     Calls:| GET /teams/{id}/repos/{org}/{repo}

---|---

`set_repo_permission` ( _repo: Repository_ , _permission: str_ ) → None¶

     Calls:|

PUT /teams/{id}/repos/{org}/{repo}

---|---
Parameters:|

  + **repo** – `github.Repository.Repository`
  + **permission** – string

Return type:|

None

`update_team_repository` ( _repo: Repository_ , _permission: str_ ) → bool¶

     Calls:| PUT /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}

---|---

`delete` () → None¶

     Calls:| DELETE /teams/{id}

---|---

`edit` ( _name: str_ , _description: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _permission: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _privacy: Union[str_ , 
_github. GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| PATCH /teams/{id}

---|---

`get_teams` () → PaginatedList[Team]¶

     Calls:| GET /teams/{id}/teams

---|---

`get_discussions` () → PaginatedList[TeamDiscussion]¶

     Calls:| GET /teams/{id}/discussions

---|---

`get_members` ( _role: Opt[str] = NotSet_ ) → PaginatedList[NamedUser]¶

     Calls:| GET /teams/{id}/members

---|---

`get_repos` () → PaginatedList[Repository]¶

     Calls:| GET /teams/{id}/repos

---|---

`invitations` () → PaginatedList[NamedUser]¶

     Calls:| GET /teams/{id}/invitations

---|---

`has_in_members` ( _member: NamedUser_ ) → bool¶

     Calls:| GET /teams/{id}/members/{user}

---|---

`has_in_repos` ( _repo: Repository_ ) → bool¶

     Calls:| GET /teams/{id}/repos/{owner}/{repo}

---|---

`remove_membership` ( _member: NamedUser_ ) → None¶

     Calls:| DELETE /teams/{team_id}/memberships/{username}

---|---

`remove_from_members` ( _member: NamedUser_ ) → None¶

This API call is deprecated. Use remove_membership instead: https://docs.github.com/en/rest/reference/teams#add-or-update-team-membership-for-a-user-legacy

Calls:| DELETE /teams/{id}/members/{user}
---|---

`remove_from_repos` ( _repo: Repository_ ) → None¶

     Calls:| DELETE /teams/{id}/repos/{owner}/{repo}

---|---
