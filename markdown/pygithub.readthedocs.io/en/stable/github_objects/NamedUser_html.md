  + NamedUser

* * *
# NamedUser¶

_class_ `github.NamedUser.`  `NamedUser` ¶

This class represents NamedUsers. The reference can be found here https://docs.github.com/en/rest/reference/users#get-a-user

`get_events` () → PaginatedList[Event]¶

     Calls:| GET /users/{user}/events

---|---

`get_followers` () → github. PaginatedList. PaginatedList[github. NamedUser. NamedUser][github. NamedUser. NamedUser]¶

     Calls:| GET /users/{user}/followers

---|---

`get_following` () → github. PaginatedList. PaginatedList[github. NamedUser. NamedUser][github. NamedUser. NamedUser]¶

     Calls:| GET /users/{user}/following

---|---

`get_gists` ( _since: Opt[datetime] = NotSet_ ) → PaginatedList[Gist]¶

     Calls:| GET /users/{user}/gists

---|---

`get_keys` () → PaginatedList[UserKey]¶

     Calls:| GET /users/{user}/keys

---|---

`get_orgs` () → PaginatedList[Organization]¶

     Calls:| GET /users/{user}/orgs

---|---

`get_projects` ( _state: str = 'open'_ ) → PaginatedList[Project]¶

     Calls:| GET /users/{user}/projects

---|---

`get_public_events` () → PaginatedList[Event]¶

     Calls:| GET /users/{user}/events/public

---|---

`get_public_received_events` () → PaginatedList[Event]¶

     Calls:| GET /users/{user}/received_events/public

---|---

`get_received_events` () → PaginatedList[Event]¶

     Calls:| GET /users/{user}/received_events

---|---

`get_repo` ( _name: str_ ) → Repository¶

     Calls:| GET /repos/{owner}/{repo}

---|---

`get_repos` ( _type: Opt[str] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ ) → PaginatedList[Repository]¶

     Calls:| GET /users/{user}/repos

---|---

`get_starred` () → PaginatedList[Repository]¶

     Calls:| GET /users/{user}/starred

---|---

`get_subscriptions` () → PaginatedList[Repository]¶

     Calls:| GET /users/{user}/subscriptions

---|---

`get_watched` () → PaginatedList[Repository]¶

     Calls:| GET /users/{user}/watched

---|---

`has_in_following` ( _following: github. NamedUser. NamedUser_ ) → bool¶

     Calls:| GET /users/{user}/following/{target_user}

---|---

`get_organization_membership` ( _org: str | Organization_ ) → Membership¶

     Calls:| GET /orgs/{org}/memberships/{username}

---|---
