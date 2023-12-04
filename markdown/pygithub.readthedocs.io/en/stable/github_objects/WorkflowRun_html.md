  + WorkflowRun

* * *
# WorkflowRun¶

_class_ `github.WorkflowRun.`  `WorkflowRun` ¶

This class represents Workflow Runs. The reference can be found here https://docs.github.com/en/rest/reference/actions#workflow-runs

`cancel` () → bool¶

     Calls:| POST /repos/{owner}/{repo}/actions/runs/{run_id}/cancel

---|---

`rerun` () → bool¶

     Calls:| POST /repos/{owner}/{repo}/actions/runs/{run_id}/rerun

---|---

`timing` () → github. WorkflowRun. TimingData¶

     Calls:| GET /repos/{owner}/{repo}/actions/runs/{run_id}/timing

---|---

`delete` () → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/actions/runs/{run_id}

---|---

`jobs` ( __filter: Opt[str] = NotSet_ ) → PaginatedList[WorkflowJob]¶

:calls “GET /repos/{owner}/{repo}/actions/runs/{run_id}/jobs :param _filter: string latest, or all
