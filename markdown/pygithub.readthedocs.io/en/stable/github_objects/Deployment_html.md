  + Deployment

* * *
# Deployment¶

_class_ `github.Deployment.`  `Deployment` ¶

This class represents Deployments. The reference can be found here https://docs.github.com/en/rest/reference/repos#deployments

`get_statuses` () → github. PaginatedList. PaginatedList[github. DeploymentStatus. DeploymentStatus][github. DeploymentStatus. DeploymentStatus]¶

     Calls:| GET /repos/{owner}/deployments/{deployment_id}/statuses

---|---

`get_status` ( _id_: int_ ) → github. DeploymentStatus. DeploymentStatus¶

     Calls:| GET /repos/{owner}/deployments/{deployment_id}/statuses/{status_id}

---|---

`create_status` ( _state: str_ , _target_url: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _description: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _environment:
Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _environment_url: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _auto_inactive: Union[bool_ , _github. GithubObject._NotSetType]
= NotSet_ ) → github. DeploymentStatus. DeploymentStatus¶

     Calls:| POST /repos/{owner}/{repo}/deployments/{deployment_id}/statuses

---|---
