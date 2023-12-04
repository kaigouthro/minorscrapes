  + Branch

* * *
# Branch¶

_class_ `github.Branch.`  `Branch` ¶

This class represents Branches. The reference can be found here https://docs.github.com/en/rest/reference/repos#branches

`get_protection` () → BranchProtection¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}/protection

---|---

`edit_protection` ( _strict: Opt[bool] = NotSet_ , _contexts: Opt[list[str]] = NotSet_ , _enforce_admins: Opt[bool] = NotSet_ , _dismissal_users: Opt[list[str]] = NotSet_ , _dismissal_teams:
Opt[list[str]] = NotSet_ , _dismissal_apps: Opt[list[str]] = NotSet_ , _dismiss_stale_reviews: Opt[bool] = NotSet_ , _require_code_owner_reviews: Opt[bool] = NotSet_ , 
_required_approving_review_count: Opt[int] = NotSet_ , _user_push_restrictions: Opt[list[str]] = NotSet_ , _team_push_restrictions: Opt[list[str]] = NotSet_ , _app_push_restrictions: Opt[list[str]] =
NotSet_ , _required_linear_history: Opt[bool] = NotSet_ , _allow_force_pushes: Opt[bool] = NotSet_ , _required_conversation_resolution: Opt[bool] = NotSet_ , _lock_branch: Opt[bool] = NotSet_ , 
_allow_fork_syncing: Opt[bool] = NotSet_ , _users_bypass_pull_request_allowances: Opt[list[str]] = NotSet_ , _teams_bypass_pull_request_allowances: Opt[list[str]] = NotSet_ , 
_apps_bypass_pull_request_allowances: Opt[list[str]] = NotSet_ , _block_creations: Opt[bool] = NotSet_ ) → BranchProtection¶

     Calls:| PUT /repos/{owner}/{repo}/branches/{branch}/protection

---|---

NOTE: The GitHub API groups strict and contexts together, both must be submitted. Take care to pass both as arguments even if only one is changing. Use edit_required_status_checks() to avoid this.

`remove_protection` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection

---|---

`get_required_status_checks` () → RequiredStatusChecks¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks

---|---
Return type:| `github.RequiredStatusChecks.RequiredStatusChecks`

`edit_required_status_checks` ( _strict: Opt[bool] = NotSet_ , _contexts: Opt[list[str]] = NotSet_ ) → RequiredStatusChecks¶

     Calls:| PATCH /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks

---|---

`remove_required_status_checks` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks

---|---

`get_required_pull_request_reviews` () → RequiredPullRequestReviews¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews

---|---

`edit_required_pull_request_reviews` ( _dismissal_users: Opt[list[str]] = NotSet_ , _dismissal_teams: Opt[list[str]] = NotSet_ , _dismissal_apps: Opt[list[str]] = NotSet_ , _dismiss_stale_reviews:
Opt[bool] = NotSet_ , _require_code_owner_reviews: Opt[bool] = NotSet_ , _required_approving_review_count: Opt[int] = NotSet_ ) → RequiredStatusChecks¶

     Calls:| PATCH /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews

---|---

`remove_required_pull_request_reviews` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews

---|---

`get_admin_enforcement` () → bool¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins

---|---

`set_admin_enforcement` () → None¶

     Calls:| POST /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins

---|---

`remove_admin_enforcement` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins

---|---

`get_user_push_restrictions` () → PaginatedList[NamedUser]¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users

---|---

`get_team_push_restrictions` () → PaginatedList[Team]¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams

---|---

`add_user_push_restrictions` ( _*users_ ) → None¶

     Calls:| POST /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users

---|---
Users:| list of strings (user names)

`replace_user_push_restrictions` ( _*users_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users

---|---
Users:| list of strings (user names)

`remove_user_push_restrictions` ( _*users_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users

---|---
Users:| list of strings (user names)

`add_team_push_restrictions` ( _*teams_ ) → None¶

     Calls:| POST /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams

---|---
Teams:| list of strings (team slugs)

`replace_team_push_restrictions` ( _*teams_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams

---|---
Teams:| list of strings (team slugs)

`remove_team_push_restrictions` ( _*teams_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams

---|---
Teams:| list of strings (team slugs)

`remove_push_restrictions` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection/restrictions

---|---

`get_required_signatures` () → bool¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures

---|---

`add_required_signatures` () → None¶

     Calls:| POST /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures

---|---

`remove_required_signatures` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/branches/{branch}/protection/required_signatures

---|---
