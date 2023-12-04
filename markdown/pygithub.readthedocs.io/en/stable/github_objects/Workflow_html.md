  + Workflow

* * *
# Workflow¶

_class_ `github.Workflow.`  `Workflow` ¶

This class represents Workflows. The reference can be found here https://docs.github.com/en/rest/reference/actions#workflows

`create_dispatch` ( _ref: github. Branch. Branch | github. Tag. Tag | github. Commit. Commit | str_ , _inputs: Opt[dict] = NotSet_ ) → bool¶

     Calls:| POST /repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches

---|---

`get_runs` ( _actor: Union[github. NamedUser. NamedUser_ , _github. GithubObject._NotSetType] = NotSet_ , _branch: Union[github. Branch. Branch_ , _github. GithubObject._NotSetType] = NotSet_ , _event:
Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _status: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _created: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , 
_exclude_pull_requests: Union[bool_ , _github. GithubObject._NotSetType] = NotSet_ , _check_suite_id: Union[int_ , _github. GithubObject._NotSetType] = NotSet_ , _head_sha: Union[str_ , 
_github. GithubObject._NotSetType] = NotSet_ ) → github. PaginatedList. PaginatedList[github. WorkflowRun. WorkflowRun][github. WorkflowRun. WorkflowRun]¶

     Calls:| GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs

---|---
