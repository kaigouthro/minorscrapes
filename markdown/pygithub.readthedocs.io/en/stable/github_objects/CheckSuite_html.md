  + CheckSuite

* * *
# CheckSuite¶

_class_ `github.CheckSuite.`  `CheckSuite` ¶

This class represents check suites. The reference can be found here https://docs.github.com/en/rest/reference/checks#check-suites

`after` ¶

     Type:| string

---|---

`app` ¶

     Type:| `github.GithubApp.GithubApp`

---|---

`before` ¶

     Type:| string

---|---

`check_runs_url` ¶

     Type:| string

---|---

`conclusion` ¶

     Type:| string

---|---

`created_at` ¶

     Type:| datetime.datetime

---|---

`head_branch` ¶

     Type:| string

---|---

`head_commit` ¶

     Type:| `github.GitCommit.GitCommit`

---|---

`head_sha` ¶

     Type:| string

---|---

`id` ¶

     Type:| int

---|---

`latest_check_runs_count` ¶

     Type:| int

---|---

`pull_requests` ¶

     Type:| list of `github.PullRequest.PullRequest`

---|---

`repository` ¶

     Type:| `github.Repository.Repository`

---|---

`status` ¶

     Type:| string

---|---

`updated_at` ¶

     Type:| datetime.datetime

---|---

`url` ¶

     Type:| string

---|---

`rerequest` () → bool¶

     Calls:| POST /repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest

---|---
Return type:| bool

`get_check_runs` ( _check_name: Opt[str] = NotSet_ , _status: Opt[str] = NotSet_ , _filter: Opt[str] = NotSet_ ) → PaginatedList[CheckRun]¶

     Calls:| GET /repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs

---|---
