  + Commit

* * *
# Commit¶

_class_ `github.Commit.`  `Commit` ¶

This class represents Commits. The reference can be found here https://docs.github.com/en/rest/reference/git#commits

`create_comment` ( _body: str_ , _line: Opt[int] = NotSet_ , _path: Opt[str] = NotSet_ , _position: Opt[int] = NotSet_ ) → CommitComment¶

     Calls:| POST /repos/{owner}/{repo}/commits/{sha}/comments

---|---

`create_status` ( _state: str_ , _target_url: Opt[str] = NotSet_ , _description: Opt[str] = NotSet_ , _context: Opt[str] = NotSet_ ) → CommitStatus¶

     Calls:| POST /repos/{owner}/{repo}/statuses/{sha}

---|---

`get_comments` () → PaginatedList[CommitComment]¶

     Calls:| GET /repos/{owner}/{repo}/commits/{sha}/comments

---|---

`get_statuses` () → PaginatedList[CommitStatus]¶

     Calls:| GET /repos/{owner}/{repo}/statuses/{ref}

---|---

`get_combined_status` () → CommitCombinedStatus¶

     Calls:| GET /repos/{owner}/{repo}/commits/{ref}/status/

---|---

`get_pulls` () → PaginatedList[PullRequest]¶

     Calls:| GET /repos/{owner}/{repo}/commits/{sha}/pulls

---|---

`get_check_runs` ( _check_name: Opt[str] = NotSet_ , _status: Opt[str] = NotSet_ , _filter: Opt[str] = NotSet_ ) → PaginatedList[CheckRun]¶

     Calls:| GET /repos/{owner}/{repo}/commits/{sha}/check-runs

---|---

`get_check_suites` ( _app_id: Opt[int] = NotSet_ , _check_name: Opt[str] = NotSet_ ) → PaginatedList[CheckSuite]¶

     Class:| GET /repos/{owner}/{repo}/commits/{ref}/check-suites

---|---
