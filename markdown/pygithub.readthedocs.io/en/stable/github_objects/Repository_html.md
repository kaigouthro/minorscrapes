

  * Docs »
  * Reference »
  * Github objects »
  * Repository
  * Edit on GitHub

* * *

# Repository¶

_class_`github.Repository.``Repository`¶

    

This class represents Repositories. The reference can be found here https://docs.github.com/en/rest/reference/repos

`allow_auto_merge`¶

     Type:| bool  
---|---  
  
`allow_forking`¶

     Type:| bool  
---|---  
  
`allow_merge_commit`¶

     Type:| bool  
---|---  
  
`allow_rebase_merge`¶

     Type:| bool  
---|---  
  
`allow_squash_merge`¶

     Type:| bool  
---|---  
  
`allow_update_branch`¶

     Type:| bool  
---|---  
  
`archived`¶

     Type:| bool  
---|---  
  
`archive_url`¶

     Type:| string  
---|---  
  
`assignees_url`¶

     Type:| string  
---|---  
  
`blobs_url`¶

     Type:| string  
---|---  
  
`branches_url`¶

     Type:| string  
---|---  
  
`clone_url`¶

     Type:| string  
---|---  
  
`collaborators_url`¶

     Type:| string  
---|---  
  
`comments_url`¶

     Type:| string  
---|---  
  
`commits_url`¶

     Type:| string  
---|---  
  
`compare_url`¶

     Type:| string  
---|---  
  
`contents_url`¶

     Type:| string  
---|---  
  
`contributors_url`¶

     Type:| string  
---|---  
  
`created_at`¶

     Type:| datetime  
---|---  
  
`default_branch`¶

     Type:| string  
---|---  
  
`delete_branch_on_merge`¶

     Type:| bool  
---|---  
  
`deployments_url`¶

     Type:| string  
---|---  
  
`description`¶

     Type:| string  
---|---  
  
`downloads_url`¶

     Type:| string  
---|---  
  
`events_url`¶

     Type:| string  
---|---  
  
`fork`¶

     Type:| bool  
---|---  
  
`forks`¶

     Type:| integer  
---|---  
  
`forks_count`¶

     Type:| integer  
---|---  
  
`forks_url`¶

     Type:| string  
---|---  
  
`full_name`¶

     Type:| string  
---|---  
  
`git_commits_url`¶

     Type:| string  
---|---  
  
`git_refs_url`¶

     Type:| string  
---|---  
  
`git_tags_url`¶

     Type:| string  
---|---  
  
`git_url`¶

     Type:| string  
---|---  
  
`has_downloads`¶

     Type:| bool  
---|---  
  
`has_issues`¶

     Type:| bool  
---|---  
  
`has_pages`¶

     Type:| bool  
---|---  
  
`has_projects`¶

     Type:| bool  
---|---  
  
`has_wiki`¶

     Type:| bool  
---|---  
  
`homepage`¶

     Type:| string  
---|---  
  
`hooks_url`¶

     Type:| string  
---|---  
  
`html_url`¶

     Type:| string  
---|---  
  
`id`¶

     Type:| integer  
---|---  
  
`is_template`¶

     Type:| bool  
---|---  
  
`issue_comment_url`¶

     Type:| string  
---|---  
  
`issue_events_url`¶

     Type:| string  
---|---  
  
`issues_url`¶

     Type:| string  
---|---  
  
`keys_url`¶

     Type:| string  
---|---  
  
`labels_url`¶

     Type:| string  
---|---  
  
`language`¶

     Type:| string  
---|---  
  
`languages_url`¶

     Type:| string  
---|---  
  
`merge_commit_message`¶

     Type:| string  
---|---  
  
`merge_commit_title`¶

     Type:| string  
---|---  
  
`merges_url`¶

     Type:| string  
---|---  
  
`milestones_url`¶

     Type:| string  
---|---  
  
`mirror_url`¶

     Type:| string  
---|---  
  
`name`¶

     Type:| string  
---|---  
  
`network_count`¶

     Type:| integer  
---|---  
  
`notifications_url`¶

     Type:| string  
---|---  
  
`open_issues`¶

     Type:| integer  
---|---  
  
`open_issues_count`¶

     Type:| integer  
---|---  
  
`organization`¶

     Type:| `github.Organization.Organization`  
---|---  
  
`owner`¶

     Type:| `github.NamedUser.NamedUser`  
---|---  
  
`parent`¶

     Type:| `github.Repository.Repository`  
---|---  
  
`permissions`¶

     Type:| `github.Permissions.Permissions`  
---|---  
  
`private`¶

     Type:| bool  
---|---  
  
`pulls_url`¶

     Type:| string  
---|---  
  
`pushed_at`¶

     Type:| datetime  
---|---  
  
`releases_url`¶

     Type:| string  
---|---  
  
`size`¶

     Type:| integer  
---|---  
  
`source`¶

     Type:| `github.Repository.Repository`  
---|---  
  
`squash_merge_commit_message`¶

     Type:| string  
---|---  
  
`squash_merge_commit_title`¶

     Type:| string  
---|---  
  
`ssh_url`¶

     Type:| string  
---|---  
  
`stargazers_count`¶

     Type:| integer  
---|---  
  
`stargazers_url`¶

     Type:| string  
---|---  
  
`statuses_url`¶

     Type:| string  
---|---  
  
`subscribers_url`¶

     Type:| string  
---|---  
  
`subscribers_count`¶

     Type:| integer  
---|---  
  
`subscription_url`¶

     Type:| string  
---|---  
  
`svn_url`¶

     Type:| string  
---|---  
  
`tags_url`¶

     Type:| string  
---|---  
  
`teams_url`¶

     Type:| string  
---|---  
  
`topics`¶

     Type:| list of strings  
---|---  
  
`trees_url`¶

     Type:| string  
---|---  
  
`updated_at`¶

     Type:| datetime  
---|---  
  
`web_commit_signoff_required`¶

     Type:| bool  
---|---  
  
`add_to_collaborators`( _collaborator: str | NamedUser_ , _permission: Opt[str] = NotSet_ ) → Invitation | None¶

     Calls:| PUT /repos/{owner}/{repo}/collaborators/{user}  
---|---  
Parameters:|  **permission** – string ‘pull’, ‘push’ or ‘admin’  
  
`get_collaborator_permission`( _collaborator: str | NamedUser_ ) → str¶

     Calls:| GET /repos/{owner}/{repo}/collaborators/{username}/permission  
---|---  
Parameters:|  **collaborator** – string or `github.NamedUser.NamedUser`  
Return type:| string  
  
`get_pending_invitations`() → PaginatedList[Invitation]¶

     Calls:| GET /repos/{owner}/{repo}/invitations  
---|---  
Return type:| `PaginatedList` of `github.Invitation.Invitation`  
  
`remove_invitation`( _invite_id: int_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/invitations/{invitation_id}  
---|---  
Return type:| None  
  
`compare`( _base: str_ , _head: str_ ) → Comparison¶

     Calls:| 

GET /repos/{owner}/{repo}/compare/{base…:head}  
  
---|---  
Parameters:|

  * **base** – string
  * **head** – string

  
Return type:|

`github.Comparison.Comparison`  
  
`create_autolink`( _key_prefix: str_ , _url_template: str_ , _is_alphanumeric: Union[bool_ , _github.GithubObject._NotSetType] = NotSet_ ) → github.Autolink.Autolink¶

     Calls:| 

POST /repos/{owner}/{repo}/autolinks  
  
---|---  
Parameters:|

  * **key_prefix** – string
  * **url_template** – string
  * **is_alphanumeric** – bool

  
Return type:|

`github.Autolink.Autolink`  
  
`create_git_blob`( _content: str_ , _encoding: str_ ) → GitBlob¶

     Calls:| 

POST /repos/{owner}/{repo}/git/blobs  
  
---|---  
Parameters:|

  * **content** – string
  * **encoding** – string

  
Return type:|

`github.GitBlob.GitBlob`  
  
`create_git_commit`( _message: str, tree: GitTree, parents: list[GitCommit], author: Opt[InputGitAuthor] = NotSet, committer: Opt[InputGitAuthor] = NotSet_ ) → GitCommit¶

     Calls:| 

POST /repos/{owner}/{repo}/git/commits  
  
---|---  
Parameters:|

  * **message** – string
  * **tree** – `github.GitTree.GitTree`
  * **parents** – list of `github.GitCommit.GitCommit`
  * **author** – `github.InputGitAuthor.InputGitAuthor`
  * **committer** – `github.InputGitAuthor.InputGitAuthor`

  
Return type:|

`github.GitCommit.GitCommit`  
  
`create_git_ref`( _ref: str_ , _sha: str_ ) → GitRef¶

     Calls:| 

POST /repos/{owner}/{repo}/git/refs  
  
---|---  
Parameters:|

  * **ref** – string
  * **sha** – string

  
Return type:|

`github.GitRef.GitRef`  
  
`create_git_tag_and_release`( _tag: str_ , _tag_message: str_ , _release_name: str_ , _release_message: str_ , _object: str_ , _type: str_ , _tagger: Opt[InputGitAuthor] = NotSet_ , _draft: bool =
False_ , _prerelease: bool = False_ , _generate_release_notes: bool = False_ ) → GitRelease¶

    

Convenience function that calls `Repository.create_git_tag()` and `Repository.create_git_release()`. :param tag: string :param tag_message: string :param release_name: string :param release_message:
string :param object: string :param type: string :param tagger: :class:github.InputGitAuthor.InputGitAuthor :param draft: bool :param prerelease: bool :param generate_release_notes: bool :rtype:
`github.GitRelease.GitRelease`

`create_git_release`( _tag: str_ , _name: str_ , _message: str_ , _draft: bool = False_ , _prerelease: bool = False_ , _generate_release_notes: bool = False_ , _target_commitish: Opt[str] = NotSet_ )
→ GitRelease¶

     Calls:| 

POST /repos/{owner}/{repo}/releases  
  
---|---  
Parameters:|

  * **tag** – string
  * **name** – string
  * **message** – string
  * **draft** – bool
  * **prerelease** – bool
  * **generate_release_notes** – bool
  * **target_commitish** – string or `github.Branch.Branch` or `github.Commit.Commit` or `github.GitCommit.GitCommit`

  
Return type:|

`github.GitRelease.GitRelease`  
  
`create_git_tag`( _tag: str_ , _message: str_ , _object: str_ , _type: str_ , _tagger: Opt[InputGitAuthor] = NotSet_ ) → GitTag¶

     Calls:| POST /repos/{owner}/{repo}/git/tags  
---|---  
  
`create_git_tree`( _tree: list[InputGitTreeElement], base_tree: Opt[GitTree] = NotSet_ ) → GitTree¶

     Calls:| 

POST /repos/{owner}/{repo}/git/trees  
  
---|---  
Parameters:|

  * **tree** – list of `github.InputGitTreeElement.InputGitTreeElement`
  * **base_tree** – `github.GitTree.GitTree`

  
Return type:|

`github.GitTree.GitTree`  
  
`create_hook`( _name: str, config: dict[str, str], events: Opt[list[str]] = NotSet, active: Opt[bool] = NotSet_ ) → Hook¶

     Calls:| 

POST /repos/{owner}/{repo}/hooks  
  
---|---  
Parameters:|

  * **name** – string
  * **config** – dict
  * **events** – list of string
  * **active** – bool

  
Return type:|

`github.Hook.Hook`  
  
`create_issue`( _title: str_ , _body: Opt[str] = NotSet_ , _assignee: NamedUser | Opt[str] = NotSet_ , _milestone: Opt[Milestone] = NotSet_ , _labels: list[Label] | Opt[list[str]] = NotSet_ ,
_assignees: Opt[list[str]] | list[NamedUser] = NotSet_ ) → Issue¶

     Calls:| 

POST /repos/{owner}/{repo}/issues  
  
---|---  
Parameters:|

  * **title** – string
  * **body** – string
  * **assignee** – string or `github.NamedUser.NamedUser`
  * **assignees** – list of string or `github.NamedUser.NamedUser`
  * **milestone** – `github.Milestone.Milestone`
  * **labels** – list of `github.Label.Label`

  
Return type:|

`github.Issue.Issue`  
  
`create_key`( _title: str_ , _key: str_ , _read_only: bool = False_ ) → RepositoryKey¶

     Calls:| 

POST /repos/{owner}/{repo}/keys  
  
---|---  
Parameters:|

  * **title** – string
  * **key** – string
  * **read_only** – bool

  
Return type:|

`github.RepositoryKey.RepositoryKey`  
  
`create_label`( _name: str_ , _color: str_ , _description: Opt[str] = NotSet_ ) → Label¶

     Calls:| 

POST /repos/{owner}/{repo}/labels  
  
---|---  
Parameters:|

  * **name** – string
  * **color** – string
  * **description** – string

  
Return type:|

`github.Label.Label`  
  
`create_milestone`( _title: str_ , _state: Opt[str] = NotSet_ , _description: Opt[str] = NotSet_ , _due_on: Opt[date] = NotSet_ ) → Milestone¶

     Calls:| 

POST /repos/{owner}/{repo}/milestones  
  
---|---  
Parameters:|

  * **title** – string
  * **state** – string
  * **description** – string
  * **due_on** – datetime

  
Return type:|

`github.Milestone.Milestone`  
  
`create_project`( _name: str_ , _body: Opt[str] = NotSet_ ) → Project¶

     Calls:| 

POST /repos/{owner}/{repo}/projects  
  
---|---  
Parameters:|

  * **name** – string
  * **body** – string

  
Return type:|

`github.Project.Project`  
  
`create_pull`( _base: str_ , _head: str_ , _*_ , _title: Union[str_ , _github.GithubObject._NotSetType] = NotSet_ , _body: Union[str_ , _github.GithubObject._NotSetType] = NotSet_ ,
_maintainer_can_modify: Union[bool_ , _github.GithubObject._NotSetType] = NotSet_ , _draft: Union[bool_ , _github.GithubObject._NotSetType] = NotSet_ , _issue: Union[github.Issue.Issue_ ,
_github.GithubObject._NotSetType] = NotSet_ ) → github.PullRequest.PullRequest¶

     Calls:| POST /repos/{owner}/{repo}/pulls  
---|---  
  
`create_repository_advisory`( _summary: str_ , _description: str_ , _severity_or_cvss_vector_string: str_ , _cve_id: str | None = None_ , _vulnerabilities:
Iterable[github.RepositoryAdvisoryVulnerability.AdvisoryVulnerability] | None = None_ , _cwe_ids: Iterable[str] | None = None_ , _credits:
Iterable[github.RepositoryAdvisoryCredit.RepositoryAdvisoryCredit] | None = None_ ) → github.RepositoryAdvisory.RepositoryAdvisory¶

     Calls:| 

POST /repos/{owner}/{repo}/security-advisories  
  
---|---  
Parameters:|

  * **summary** – string
  * **description** – string
  * **severity_or_cvss_vector_string** – string
  * **cve_id** – string
  * **vulnerabilities** – iterable of `github.RepositoryAdvisoryVulnerability.AdvisoryVulnerability`
  * **cwe_ids** – iterable of string
  * **credits** – iterable of `github.RepositoryAdvisoryCredit.RepositoryAdvisoryCredit`

  
Return type:|

`github.RepositoryAdvisory.RepositoryAdvisory`  
  
`report_security_vulnerability`( _summary: str_ , _description: str_ , _severity_or_cvss_vector_string: str_ , _cve_id: str | None = None_ , _vulnerabilities:
Iterable[github.RepositoryAdvisoryVulnerability.AdvisoryVulnerability] | None = None_ , _cwe_ids: Iterable[str] | None = None_ , _credits:
Iterable[github.RepositoryAdvisoryCredit.RepositoryAdvisoryCredit] | None = None_ ) → github.RepositoryAdvisory.RepositoryAdvisory¶

     Calls:| 

POST /repos/{owner}/{repo}/security-advisories/reports  
  
---|---  
Parameters:|

  * **summary** – string
  * **description** – string
  * **severity_or_cvss_vector_string** – string
  * **cve_id** – string
  * **vulnerabilities** – iterable of `github.RepositoryAdvisoryVulnerability.AdvisoryVulnerability`
  * **cwe_ids** – iterable of string
  * **credits** – iterable of `github.RepositoryAdvisoryCredit.RepositoryAdvisoryCredit`

  
Return type:|

`github.RepositoryAdvisory.RepositoryAdvisory`  
  
`create_repository_dispatch`( _event_type: str_ , _client_payload: Opt[dict[str_ , _Any]] = NotSet_ ) → bool¶

     Calls:| 

POST /repos/{owner}/{repo}/dispatches <https://docs.github.com/en/rest/repos#create-a-repository-dispatch-event>  
  
---|---  
Parameters:|

  * **event_type** – string
  * **client_payload** – dict

  
Return type:|

bool  
  
`create_secret`( _secret_name: str_ , _unencrypted_value: str_ ) → github.Secret.Secret¶

     Calls:| PUT /repos/{owner}/{repo}/actions/secrets/{secret_name}  
---|---  
  
`get_secrets`() → github.PaginatedList.PaginatedList[github.Secret.Secret][github.Secret.Secret]¶

    

Gets all repository secrets

`get_secret`( _secret_name: str_ ) → github.Secret.Secret¶

     Calls:| ‘GET /repos/{owner}/{repo}/actions/secrets/{secret_name} <https://docs.github.com/en/rest/actions/secrets#get-an-organization-secret>`_  
---|---  
  
`create_variable`( _variable_name: str_ , _value: str_ ) → github.Variable.Variable¶

     Calls:| POST /repos/{owner}/{repo}/actions/variables/{variable_name}  
---|---  
  
`get_variables`() → github.PaginatedList.PaginatedList[github.Variable.Variable][github.Variable.Variable]¶

    

Gets all repository variables :rtype: `PaginatedList` of `github.Variable.Variable`

`get_variable`( _variable_name: str_ ) → github.Variable.Variable¶

     Calls:| ‘GET /orgs/{org}/actions/variables/{variable_name} <https://docs.github.com/en/rest/actions/variables#get-an-organization-variable>`_  
---|---  
Parameters:|  **variable_name** – string  
Return type:| github.Variable.Variable  
  
`delete_secret`( _secret_name: str_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/actions/secrets/{secret_name}  
---|---  
Parameters:|  **secret_name** – string  
Return type:| bool  
  
`delete_variable`( _variable_name: str_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/actions/variables/{variable_name}  
---|---  
Parameters:|  **variable_name** – string  
Return type:| bool  
  
`create_source_import`( _vcs: str_ , _vcs_url: str_ , _vcs_username: Opt[str] = NotSet_ , _vcs_password: Opt[str] = NotSet_ ) → SourceImport¶

     Calls:| 

PUT /repos/{owner}/{repo}/import  
  
---|---  
Parameters:|

  * **vcs** – string
  * **vcs_url** – string
  * **vcs_username** – string
  * **vcs_password** – string

  
Return type:|

`github.SourceImport.SourceImport`  
  
`delete`() → None¶

     Calls:| DELETE /repos/{owner}/{repo}  
---|---  
Return type:| None  
  
`edit`( _name: str | None = None_ , _description: Opt[str] = NotSet_ , _homepage: Opt[str] = NotSet_ , _private: Opt[bool] = NotSet_ , _visibility: Opt[str] = NotSet_ , _has_issues: Opt[bool] =
NotSet_ , _has_projects: Opt[bool] = NotSet_ , _has_wiki: Opt[bool] = NotSet_ , _is_template: Opt[bool] = NotSet_ , _default_branch: Opt[str] = NotSet_ , _allow_squash_merge: Opt[bool] = NotSet_ ,
_allow_merge_commit: Opt[bool] = NotSet_ , _allow_rebase_merge: Opt[bool] = NotSet_ , _allow_auto_merge: Opt[bool] = NotSet_ , _delete_branch_on_merge: Opt[bool] = NotSet_ , _allow_update_branch:
Opt[bool] = NotSet_ , _use_squash_pr_title_as_default: Opt[bool] = NotSet_ , _squash_merge_commit_title: Opt[str] = NotSet_ , _squash_merge_commit_message: Opt[str] = NotSet_ , _merge_commit_title:
Opt[str] = NotSet_ , _merge_commit_message: Opt[str] = NotSet_ , _archived: Opt[bool] = NotSet_ , _allow_forking: Opt[bool] = NotSet_ , _web_commit_signoff_required: Opt[bool] = NotSet_ ) → None¶

     Calls:| 

PATCH /repos/{owner}/{repo}  
  
---|---  
Parameters:|

  * **name** – string
  * **description** – string
  * **homepage** – string
  * **private** – bool
  * **visibility** – string
  * **has_issues** – bool
  * **has_projects** – bool
  * **has_wiki** – bool
  * **is_template** – bool
  * **default_branch** – string
  * **allow_squash_merge** – bool
  * **allow_merge_commit** – bool
  * **allow_rebase_merge** – bool
  * **allow_auto_merge** – bool
  * **delete_branch_on_merge** – bool
  * **allow_update_branch** – bool
  * **use_squash_pr_title_as_default** – bool

  
  
:param squash_merge_commit_title : string :param squash_merge_commit_message : string :param merge_commit_title : string :param merge_commit_message : string :param archived: bool :param
allow_forking: bool :param web_commit_signoff_required: bool :rtype: None

`get_archive_link`( _archive_format: str_ , _ref: Union[str_ , _github.GithubObject._NotSetType] = NotSet_ ) → str¶

     Calls:| 

GET /repos/{owner}/{repo}/{archive_format}/{ref}  
  
---|---  
Parameters:|

  * **archive_format** – string
  * **ref** – string

  
Return type:|

string  
  
`get_assignees`() → PaginatedList[NamedUser]¶

     Calls:| GET /repos/{owner}/{repo}/assignees  
---|---  
Return type:| `PaginatedList` of `github.NamedUser.NamedUser`  
  
`get_branch`( _branch: str_ ) → Branch¶

     Calls:| GET /repos/{owner}/{repo}/branches/{branch}  
---|---  
Parameters:|  **branch** – string  
Return type:| `github.Branch.Branch`  
  
`rename_branch`( _branch: str | Branch_ , _new_name: str_ ) → bool¶

     Calls:| 

POST /repos/{owner}/{repo}/branches/{branch}/rename  
  
---|---  
Parameters:|

  * **branch** – `github.Branch.Branch` or string
  * **new_name** – string

  
Return type:|

bool  
  
NOTE: This method does not return the branch since it may take some time to fully complete server-side.

`get_branches`() → PaginatedList[Branch]¶

     Calls:| GET /repos/{owner}/{repo}/branches  
---|---  
Return type:| `PaginatedList` of `github.Branch.Branch`  
  
`get_collaborators`( _affiliation: Opt[str] = NotSet_ ) → PaginatedList[NamedUser]¶

     Calls:| GET /repos/{owner}/{repo}/collaborators  
---|---  
Parameters:|  **affiliation** – string  
Return type:| `PaginatedList` of `github.NamedUser.NamedUser`  
  
`get_comment`( _id: int_ ) → CommitComment¶

     Calls:| GET /repos/{owner}/{repo}/comments/{id}  
---|---  
Parameters:|  **id** – integer  
Return type:| `github.CommitComment.CommitComment`  
  
`get_comments`() → PaginatedList[CommitComment]¶

     Calls:| GET /repos/{owner}/{repo}/comments  
---|---  
Return type:| `PaginatedList` of `github.CommitComment.CommitComment`  
  
`get_commit`( _sha: str_ ) → Commit¶

     Calls:| GET /repos/{owner}/{repo}/commits/{sha}  
---|---  
Parameters:|  **sha** – string  
Return type:| `github.Commit.Commit`  
  
`get_commits`( _sha: Opt[str] = NotSet_ , _path: Opt[str] = NotSet_ , _since: Opt[datetime] = NotSet_ , _until: Opt[datetime] = NotSet_ , _author: Opt[AuthenticatedUser | NamedUser | str] = NotSet_ )
→ PaginatedList[Commit]¶

     Calls:| 

GET /repos/{owner}/{repo}/commits  
  
---|---  
Parameters:|

  * **sha** – string
  * **path** – string
  * **since** – datetime
  * **until** – datetime
  * **author** – string or `github.NamedUser.NamedUser` or `github.AuthenticatedUser.AuthenticatedUser`

  
Return type:|

`PaginatedList` of `github.Commit.Commit`  
  
`get_contents`( _path: str_ , _ref: Opt[str] = NotSet_ ) → list[ContentFile] | ContentFile¶

     Calls:| 

GET /repos/{owner}/{repo}/contents/{path}  
  
---|---  
Parameters:|

  * **path** – string
  * **ref** – string

  
Return type:|

`github.ContentFile.ContentFile` or a list of them  
  
`get_deployments`( _sha: Opt[str] = NotSet_ , _ref: Opt[str] = NotSet_ , _task: Opt[str] = NotSet_ , _environment: Opt[str] = NotSet_ ) → PaginatedList[Deployment]¶

     Calls:| GET /repos/{owner}/{repo}/deployments  
---|---  
Param:| sha: string  
Param:| ref: string  
Param:| task: string  
Param:| environment: string  
Return type:| `PaginatedList` of `github.Deployment.Deployment`  
  
`get_deployment`( _id_: int_ ) → Deployment¶

     Calls:| GET /repos/{owner}/{repo}/deployments/{deployment_id}  
---|---  
Param:| id_: int  
Return type:| `github.Deployment.Deployment`  
  
`create_deployment`( _ref: str_ , _task: Opt[str] = NotSet_ , _auto_merge: Opt[bool] = NotSet_ , _required_contexts: Opt[list[str]] = NotSet_ , _payload: Opt[dict[str_ , _Any]] = NotSet_ ,
_environment: Opt[str] = NotSet_ , _description: Opt[str] = NotSet_ , _transient_environment: Opt[bool] = NotSet_ , _production_environment: Opt[bool] = NotSet_ ) → Deployment¶

     Calls:| POST /repos/{owner}/{repo}/deployments  
---|---  
Param:| ref: string  
Param:| task: string  
Param:| auto_merge: bool  
Param:| required_contexts: list of status contexts  
Param:| payload: dict  
Param:| environment: string  
Param:| description: string  
Param:| transient_environment: bool  
Param:| production_environment: bool  
Return type:| `github.Deployment.Deployment`  
  
`get_top_referrers`() → None | list[Referrer]¶

     Calls:| GET /repos/{owner}/{repo}/traffic/popular/referrers  
---|---  
  
`get_top_paths`() → None | list[Path]¶

     Calls:| GET /repos/{owner}/{repo}/traffic/popular/paths  
---|---  
Return type:| `list` of `github.Path.Path`  
  
`get_views_traffic`( _per: Opt[str] = NotSet_ ) → None | dict[str, int | list[View]]¶

     Calls:| GET /repos/{owner}/{repo}/traffic/views  
---|---  
Parameters:|  **per** – string, must be one of day or week, day by default  
  
`get_clones_traffic`( _per: Opt[str] = NotSet_ ) → dict[str, int | list[Clones]] | None¶

     Calls:| GET /repos/{owner}/{repo}/traffic/clones  
---|---  
Parameters:|  **per** – string, must be one of day or week, day by default  
Return type:| None or list of `github.Clones.Clones`  
  
`get_projects`( _state: Opt[str] = NotSet_ ) → PaginatedList[Project]¶

     Calls:| GET /repos/{owner}/{repo}/projects  
---|---  
Return type:| `PaginatedList` of `github.Project.Project`  
Parameters:|  **state** – string  
  
`get_autolinks`() → PaginatedList[Autolink]¶

     Calls:| GET /repos/{owner}/{repo}/autolinks  
---|---  
Return type:| `PaginatedList` of `github.Autolink.Autolink`  
  
`create_file`( _path: str_ , _message: str_ , _content: str | bytes_ , _branch: Opt[str] = NotSet_ , _committer: Opt[InputGitAuthor] = NotSet_ , _author: Opt[InputGitAuthor] = NotSet_ ) → dict[str,
ContentFile | Commit]¶

    

Create a file in this repository.

Calls:|

PUT /repos/{owner}/{repo}/contents/{path}  
  
---|---  
Parameters:|

  * **path** – string, (required), path of the file in the repository
  * **message** – string, (required), commit message
  * **content** – string, (required), the actual data in the file
  * **branch** – string, (optional), branch to create the commit on. Defaults to the default branch of the repository
  * **committer** – InputGitAuthor, (optional), if no information is given the authenticated user’s information will be used. You must specify both a name and email.
  * **author** – InputGitAuthor, (optional), if omitted this will be filled in with committer information. If passed, you must specify both a name and email.

  
Return type:|

{ ‘content’: `ContentFile`:, ‘commit’: `Commit`}  
  
`get_repository_advisories`() → github.PaginatedList.PaginatedList[github.RepositoryAdvisory.RepositoryAdvisory][github.RepositoryAdvisory.RepositoryAdvisory]¶

     Calls:| GET /repos/{owner}/{repo}/security-advisories  
---|---  
Return type:| `PaginatedList` of `github.RepositoryAdvisory.RepositoryAdvisory`  
  
`get_repository_advisory`( _ghsa: str_ ) → github.RepositoryAdvisory.RepositoryAdvisory¶

     Calls:| GET /repos/{owner}/{repo}/security-advisories/{ghsa}  
---|---  
Parameters:|  **ghsa** – string  
Return type:| `github.RepositoryAdvisory.RepositoryAdvisory`  
  
`update_file`( _path: str_ , _message: str_ , _content: bytes | str_ , _sha: str_ , _branch: Opt[str] = NotSet_ , _committer: Opt[InputGitAuthor] = NotSet_ , _author: Opt[InputGitAuthor] = NotSet_ ) →
dict[str, ContentFile | Commit]¶

    

This method updates a file in a repository

Calls:|

PUT /repos/{owner}/{repo}/contents/{path}  
  
---|---  
Parameters:|

  * **path** – string, Required. The content path.
  * **message** – string, Required. The commit message.
  * **content** – string, Required. The updated file content, either base64 encoded, or ready to be encoded.
  * **sha** – string, Required. The blob SHA of the file being replaced.
  * **branch** – string. The branch name. Default: the repository’s default branch (usually master)
  * **committer** – InputGitAuthor, (optional), if no information is given the authenticated user’s information will be used. You must specify both a name and email.
  * **author** – InputGitAuthor, (optional), if omitted this will be filled in with committer information. If passed, you must specify both a name and email.

  
Return type:|

{ ‘content’: `ContentFile`:, ‘commit’: `Commit`}  
  
`delete_file`( _path: str_ , _message: str_ , _sha: str_ , _branch: Opt[str] = NotSet_ , _committer: Opt[InputGitAuthor] = NotSet_ , _author: Opt[InputGitAuthor] = NotSet_ ) → dict[str, Commit |
_NotSetType]¶

    

This method deletes a file in a repository

Calls:|

DELETE /repos/{owner}/{repo}/contents/{path}  
  
---|---  
Parameters:|

  * **path** – string, Required. The content path.
  * **message** – string, Required. The commit message.
  * **sha** – string, Required. The blob SHA of the file being replaced.
  * **branch** – string. The branch name. Default: the repository’s default branch (usually master)
  * **committer** – InputGitAuthor, (optional), if no information is given the authenticated user’s information will be used. You must specify both a name and email.
  * **author** – InputGitAuthor, (optional), if omitted this will be filled in with committer information. If passed, you must specify both a name and email.

  
Return type:|

{ ‘content’: `null`:, ‘commit’: `Commit`}  
  
`get_dir_contents`( _path: str_ , _ref: Opt[str] = NotSet_ ) → list[ContentFile]¶

     Calls:| GET /repos/{owner}/{repo}/contents/{path}  
---|---  
  
`get_contributors`( _anon: Opt[str] = NotSet_ ) → PaginatedList[NamedUser]¶

     Calls:| GET /repos/{owner}/{repo}/contributors  
---|---  
Parameters:|  **anon** – string  
Return type:| `PaginatedList` of `github.NamedUser.NamedUser`  
  
`get_download`( _id: int_ ) → Download¶

     Calls:| GET /repos/{owner}/{repo}/downloads/{id}  
---|---  
Parameters:|  **id** – integer  
Return type:| `github.Download.Download`  
  
`get_downloads`() → PaginatedList[Download]¶

     Calls:| GET /repos/{owner}/{repo}/downloads  
---|---  
Return type:| `PaginatedList` of `github.Download.Download`  
  
`get_events`() → PaginatedList[Event]¶

     Calls:| GET /repos/{owner}/{repo}/events  
---|---  
Return type:| `PaginatedList` of `github.Event.Event`  
  
`get_forks`() → github.PaginatedList.PaginatedList[github.Repository.Repository][github.Repository.Repository]¶

     Calls:| GET /repos/{owner}/{repo}/forks  
---|---  
Return type:| `PaginatedList` of `github.Repository.Repository`  
  
`create_fork`( _organization: Organization | Opt[str] = NotSet_ , _name: Opt[str] = NotSet_ , _default_branch_only: Opt[bool] = NotSet_ ) → Repository¶

     Calls:| 

POST /repos/{owner}/{repo}/forks  
  
---|---  
Parameters:|

  * **organization** – `github.Organization.Organization` or string
  * **name** – string
  * **default_branch_only** – bool

  
Return type:|

`github.Repository.Repository`  
  
`get_git_blob`( _sha: str_ ) → GitBlob¶

     Calls:| GET /repos/{owner}/{repo}/git/blobs/{sha}  
---|---  
Parameters:|  **sha** – string  
Return type:| `github.GitBlob.GitBlob`  
  
`get_git_commit`( _sha: str_ ) → GitCommit¶

     Calls:| GET /repos/{owner}/{repo}/git/commits/{sha}  
---|---  
Parameters:|  **sha** – string  
Return type:| `github.GitCommit.GitCommit`  
  
`get_git_ref`( _ref: str_ ) → GitRef¶

     Calls:| GET /repos/{owner}/{repo}/git/refs/{ref}  
---|---  
Parameters:|  **ref** – string  
Return type:| `github.GitRef.GitRef`  
  
`get_git_refs`() → PaginatedList[GitRef]¶

     Calls:| GET /repos/{owner}/{repo}/git/refs  
---|---  
Return type:| `PaginatedList` of `github.GitRef.GitRef`  
  
`get_git_matching_refs`( _ref: str_ ) → PaginatedList[GitRef]¶

     Calls:| GET /repos/{owner}/{repo}/git/matching-refs/{ref}  
---|---  
Return type:| `PaginatedList` of `github.GitRef.GitRef`  
  
`get_git_tag`( _sha: str_ ) → GitTag¶

     Calls:| GET /repos/{owner}/{repo}/git/tags/{sha}  
---|---  
Parameters:|  **sha** – string  
Return type:| `github.GitTag.GitTag`  
  
`get_git_tree`( _sha: str_ , _recursive: Opt[bool] = NotSet_ ) → GitTree¶

     Calls:| 

GET /repos/{owner}/{repo}/git/trees/{sha}  
  
---|---  
Parameters:|

  * **sha** – string
  * **recursive** – bool

  
Return type:|

`github.GitTree.GitTree`  
  
`get_hook`( _id: int_ ) → Hook¶

     Calls:| GET /repos/{owner}/{repo}/hooks/{id}  
---|---  
Parameters:|  **id** – integer  
Return type:| `github.Hook.Hook`  
  
`get_hooks`() → PaginatedList[Hook]¶

     Calls:| GET /repos/{owner}/{repo}/hooks  
---|---  
Return type:| `PaginatedList` of `github.Hook.Hook`  
  
`get_hook_delivery`( _hook_id: int_ , _delivery_id: int_ ) → github.HookDelivery.HookDelivery¶

     Calls:| 

GET /repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}  
  
---|---  
Parameters:|

  * **hook_id** – integer
  * **delivery_id** – integer

  
Return type:|

`github.HookDelivery.HookDelivery`  
  
`get_hook_deliveries`( _hook_id: int_ ) → github.PaginatedList.PaginatedList[github.HookDelivery.HookDeliverySummary][github.HookDelivery.HookDeliverySummary]¶

     Calls:| GET /repos/{owner}/{repo}/hooks/{hook_id}/deliveries  
---|---  
Parameters:|  **hook_id** – integer  
Return type:| `PaginatedList` of `github.HookDelivery.HookDeliverySummary`  
  
`get_issue`( _number: int_ ) → Issue¶

     Calls:| GET /repos/{owner}/{repo}/issues/{number}  
---|---  
Parameters:|  **number** – integer  
Return type:| `github.Issue.Issue`  
  
`get_issues`( _milestone: Milestone | Opt[str] = NotSet_ , _state: Opt[str] = NotSet_ , _assignee: NamedUser | Opt[str] = NotSet_ , _mentioned: Opt[NamedUser] = NotSet_ , _labels: Opt[list[str] |
list[Label]] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _since: Opt[datetime] = NotSet_ , _creator: Opt[NamedUser] = NotSet_ ) → PaginatedList[Issue]¶

     Calls:| 

GET /repos/{owner}/{repo}/issues  
  
---|---  
Parameters:|

  * **milestone** – `github.Milestone.Milestone` or “none” or “*”
  * **state** – string. open, closed, or all. If this is not set the GitHub API default behavior will be used. At the moment this is to return only open issues. This might change anytime on GitHub API side and it could be clever to explicitly specify the state value.
  * **assignee** – string or `github.NamedUser.NamedUser` or “none” or “*”
  * **mentioned** – `github.NamedUser.NamedUser`
  * **labels** – list of string or `github.Label.Label`
  * **sort** – string
  * **direction** – string
  * **since** – datetime
  * **creator** – string or `github.NamedUser.NamedUser`

  
Return type:|

`PaginatedList` of `github.Issue.Issue`  
  
`get_issues_comments`( _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _since: Opt[datetime] = NotSet_ ) → PaginatedList[IssueComment]¶

     Calls:| 

GET /repos/{owner}/{repo}/issues/comments  
  
---|---  
Parameters:|

  * **sort** – string
  * **direction** – string
  * **since** – datetime

  
Return type:|

`PaginatedList` of `github.IssueComment.IssueComment`  
  
`get_issues_event`( _id: int_ ) → IssueEvent¶

     Calls:| GET /repos/{owner}/{repo}/issues/events/{id}  
---|---  
Parameters:|  **id** – integer  
Return type:| `github.IssueEvent.IssueEvent`  
  
`get_issues_events`() → PaginatedList[IssueEvent]¶

     Calls:| GET /repos/{owner}/{repo}/issues/events  
---|---  
Return type:| `PaginatedList` of `github.IssueEvent.IssueEvent`  
  
`get_key`( _id: int_ ) → RepositoryKey¶

     Calls:| GET /repos/{owner}/{repo}/keys/{id}  
---|---  
Parameters:|  **id** – integer  
Return type:| `github.RepositoryKey.RepositoryKey`  
  
`get_keys`() → PaginatedList[RepositoryKey]¶

     Calls:| GET /repos/{owner}/{repo}/keys  
---|---  
Return type:| `PaginatedList` of `github.RepositoryKey.RepositoryKey`  
  
`get_label`( _name: str_ ) → Label¶

     Calls:| GET /repos/{owner}/{repo}/labels/{name}  
---|---  
Parameters:|  **name** – string  
Return type:| `github.Label.Label`  
  
`get_labels`() → PaginatedList[Label]¶

     Calls:| GET /repos/{owner}/{repo}/labels  
---|---  
Return type:| `PaginatedList` of `github.Label.Label`  
  
`get_languages`() → dict[str, int]¶

     Calls:| GET /repos/{owner}/{repo}/languages  
---|---  
Return type:| dict of string to integer  
  
`get_license`() → ContentFile¶

     Calls:| GET /repos/{owner}/{repo}/license  
---|---  
Return type:| `github.ContentFile.ContentFile`  
  
`get_milestone`( _number: int_ ) → Milestone¶

     Calls:| GET /repos/{owner}/{repo}/milestones/{number}  
---|---  
Parameters:|  **number** – integer  
Return type:| `github.Milestone.Milestone`  
  
`get_milestones`( _state: Opt[str] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ ) → PaginatedList[Milestone]¶

     Calls:| 

GET /repos/{owner}/{repo}/milestones  
  
---|---  
Parameters:|

  * **state** – string
  * **sort** – string
  * **direction** – string

  
Return type:|

`PaginatedList` of `github.Milestone.Milestone`  
  
`get_network_events`() → PaginatedList[Event]¶

     Calls:| GET /networks/{owner}/{repo}/events  
---|---  
Return type:| `PaginatedList` of `github.Event.Event`  
  
`get_public_key`() → PublicKey¶

     Calls:| GET /repos/{owner}/{repo}/actions/secrets/public-key  
---|---  
Return type:| `github.PublicKey.PublicKey`  
  
`get_pull`( _number: int_ ) → PullRequest¶

     Calls:| GET /repos/{owner}/{repo}/pulls/{number}  
---|---  
Parameters:|  **number** – integer  
Return type:| `github.PullRequest.PullRequest`  
  
`get_pulls`( _state: Opt[str] = NotSet_ , _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _base: Opt[str] = NotSet_ , _head: Opt[str] = NotSet_ ) → PaginatedList[PullRequest]¶

     Calls:| 

GET /repos/{owner}/{repo}/pulls  
  
---|---  
Parameters:|

  * **state** – string
  * **sort** – string
  * **direction** – string
  * **base** – string
  * **head** – string

  
Return type:|

`PaginatedList` of `github.PullRequest.PullRequest`  
  
`get_pulls_comments`( _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _since: Opt[datetime] = NotSet_ ) → PaginatedList[PullRequestComment]¶

     Calls:| 

GET /repos/{owner}/{repo}/pulls/comments  
  
---|---  
Parameters:|

  * **sort** – string
  * **direction** – string
  * **since** – datetime

  
Return type:|

`PaginatedList` of `github.PullRequestComment.PullRequestComment`  
  
`get_pulls_review_comments`( _sort: Opt[str] = NotSet_ , _direction: Opt[str] = NotSet_ , _since: Opt[datetime] = NotSet_ ) → PaginatedList[PullRequestComment]¶

     Calls:| 

GET /repos/{owner}/{repo}/pulls/comments  
  
---|---  
Parameters:|

  * **sort** – string ‘created’, ‘updated’, ‘created_at’
  * **direction** – string ‘asc’ or ‘desc’
  * **since** – datetime

  
Return type:|

`PaginatedList` of `github.PullRequestComment.PullRequestComment`  
  
`get_readme`( _ref: Opt[str] = NotSet_ ) → ContentFile¶

     Calls:| GET /repos/{owner}/{repo}/readme  
---|---  
Parameters:|  **ref** – string  
Return type:| `github.ContentFile.ContentFile`  
  
`get_self_hosted_runner`( _runner_id: int_ ) → SelfHostedActionsRunner¶

     Calls:| GET /repos/{owner}/{repo}/actions/runners/{id}  
---|---  
Parameters:|  **runner_id** – int  
Return type:| `github.SelfHostedActionsRunner.SelfHostedActionsRunner`  
  
`get_self_hosted_runners`() → PaginatedList[SelfHostedActionsRunner]¶

     Calls:| GET /repos/{owner}/{repo}/actions/runners  
---|---  
Return type:| `PaginatedList` of `github.SelfHostedActionsRunner.SelfHostedActionsRunner`  
  
`get_source_import`() → SourceImport | None¶

     Calls:| GET /repos/{owner}/{repo}/import  
---|---  
  
`get_stargazers`() → PaginatedList[NamedUser]¶

     Calls:| GET /repos/{owner}/{repo}/stargazers  
---|---  
Return type:| `PaginatedList` of `github.NamedUser.NamedUser`  
  
`get_stargazers_with_dates`() → PaginatedList[Stargazer]¶

     Calls:| GET /repos/{owner}/{repo}/stargazers  
---|---  
Return type:| `PaginatedList` of `github.Stargazer.Stargazer`  
  
`get_stats_contributors`() → list[StatsContributor] | None¶

     Calls:| GET /repos/{owner}/{repo}/stats/contributors  
---|---  
Return type:| None or list of `github.StatsContributor.StatsContributor`  
  
`get_stats_commit_activity`() → list[StatsCommitActivity] | None¶

     Calls:| GET /repos/{owner}/{repo}/stats/commit_activity  
---|---  
Return type:| None or list of `github.StatsCommitActivity.StatsCommitActivity`  
  
`get_stats_code_frequency`() → list[StatsCodeFrequency] | None¶

     Calls:| GET /repos/{owner}/{repo}/stats/code_frequency  
---|---  
Return type:| None or list of `github.StatsCodeFrequency.StatsCodeFrequency`  
  
`get_stats_participation`() → StatsParticipation | None¶

     Calls:| GET /repos/{owner}/{repo}/stats/participation  
---|---  
Return type:| None or `github.StatsParticipation.StatsParticipation`  
  
`get_stats_punch_card`() → StatsPunchCard | None¶

     Calls:| GET /repos/{owner}/{repo}/stats/punch_card  
---|---  
Return type:| None or `github.StatsPunchCard.StatsPunchCard`  
  
`get_subscribers`() → PaginatedList[NamedUser]¶

     Calls:| GET /repos/{owner}/{repo}/subscribers  
---|---  
Return type:| `PaginatedList` of `github.NamedUser.NamedUser`  
  
`get_tags`() → PaginatedList[Tag]¶

     Calls:| GET /repos/{owner}/{repo}/tags  
---|---  
Return type:| `PaginatedList` of `github.Tag.Tag`  
  
`get_releases`() → PaginatedList[GitRelease]¶

     Calls:| GET /repos/{owner}/{repo}/releases  
---|---  
Return type:| `PaginatedList` of `github.GitRelease.GitRelease`  
  
`get_release`( _id: int | str_ ) → GitRelease¶

     Calls:| GET /repos/{owner}/{repo}/releases/{id}  
---|---  
Parameters:|  **id** – int (release id), str (tag name)  
Return type:| None or `github.GitRelease.GitRelease`  
  
`get_latest_release`() → GitRelease¶

     Calls:| GET /repos/{owner}/{repo}/releases/latest  
---|---  
Return type:| `github.GitRelease.GitRelease`  
  
`get_teams`() → PaginatedList[Team]¶

     Calls:| GET /repos/{owner}/{repo}/teams  
---|---  
Return type:| `PaginatedList` of `github.Team.Team`  
  
`get_topics`() → list[str]¶

     Calls:| GET /repos/{owner}/{repo}/topics  
---|---  
Return type:| list of strings  
  
`get_watchers`() → PaginatedList[NamedUser]¶

     Calls:| GET /repos/{owner}/{repo}/watchers  
---|---  
Return type:| `PaginatedList` of `github.NamedUser.NamedUser`  
  
`get_workflows`() → PaginatedList[Workflow]¶

     Calls:| GET /repos/{owner}/{repo}/actions/workflows  
---|---  
Return type:| `PaginatedList` of `github.Workflow.Workflow`  
  
`get_workflow`( _id_or_file_name: str | int_ ) → Workflow¶

     Calls:| GET /repos/{owner}/{repo}/actions/workflows/{workflow_id}  
---|---  
Parameters:|  **id_or_file_name** – int or string. Can be either a workflow ID or a filename.  
Return type:| `github.Workflow.Workflow`  
  
`get_workflow_runs`( _actor: Opt[NamedUser] = NotSet_ , _branch: Opt[Branch] = NotSet_ , _event: Opt[str] = NotSet_ , _status: Opt[str] = NotSet_ , _exclude_pull_requests: Opt[bool] = NotSet_ ,
_head_sha: Opt[str] = NotSet_ ) → PaginatedList[WorkflowRun]¶

     Calls:| 

GET /repos/{owner}/{repo}/actions/runs  
  
---|---  
Parameters:|

  * **actor** – `github.NamedUser.NamedUser` or string
  * **branch** – `github.Branch.Branch` or string
  * **event** – string
  * **status** – string queued, in_progress, completed, success, failure, neutral, cancelled, skipped, timed_out, or action_required
  * **exclude_pull_requests** – bool
  * **head_sha** – string

  
Return type:|

`PaginatedList` of `github.WorkflowRun.WorkflowRun`  
  
`get_workflow_run`( _id_: int_ ) → WorkflowRun¶

     Calls:| GET /repos/{owner}/{repo}/actions/runs/{run_id}  
---|---  
Parameters:|  **id** – int  
Return type:| `github.WorkflowRun.WorkflowRun`  
  
`has_in_assignees`( _assignee: str | NamedUser_ ) → bool¶

     Calls:| GET /repos/{owner}/{repo}/assignees/{assignee}  
---|---  
Parameters:|  **assignee** – string or `github.NamedUser.NamedUser`  
Return type:| bool  
  
`has_in_collaborators`( _collaborator: str | NamedUser_ ) → bool¶

     Calls:| GET /repos/{owner}/{repo}/collaborators/{user}  
---|---  
Parameters:|  **collaborator** – string or `github.NamedUser.NamedUser`  
Return type:| bool  
  
`legacy_search_issues`( _state: str_ , _keyword: str_ ) → list[Issue]¶

     Calls:| 

GET /legacy/issues/search/{owner}/{repository}/{state}/{keyword}  
  
---|---  
Parameters:|

  * **state** – “open” or “closed”
  * **keyword** – string

  
Return type:|

List of `github.Issue.Issue`  
  
`get_notifications`( _all: Opt[bool] = NotSet_ , _participating: Opt[bool] = NotSet_ , _since: Opt[datetime] = NotSet_ , _before: Opt[datetime] = NotSet_ ) → PaginatedList[Notification]¶

     Calls:| 

GET /repos/{owner}/{repo}/notifications  
  
---|---  
Parameters:|

  * **all** – bool
  * **participating** – bool
  * **since** – datetime
  * **before** – datetime

  
Return type:|

`PaginatedList` of `github.Notification.Notification`  
  
`mark_notifications_as_read`( _last_read_at: datetime.datetime = datetime.datetime(2023_ , _9_ , _30_ , _10_ , _50_ , _33_ , _795946_ , _tzinfo=datetime.timezone.utc)_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/notifications  
---|---  
Parameters:|  **last_read_at** – datetime  
  
`merge`( _base: str_ , _head: str_ , _commit_message: Opt[str] = NotSet_ ) → Commit | None¶

     Calls:| 

POST /repos/{owner}/{repo}/merges  
  
---|---  
Parameters:|

  * **base** – string
  * **head** – string
  * **commit_message** – string

  
Return type:|

`github.Commit.Commit`  
  
`replace_topics`( _topics: list[str]_ ) → None¶

     Calls:| PUT /repos/{owner}/{repo}/topics  
---|---  
Parameters:|  **topics** – list of strings  
Return type:| None  
  
`get_vulnerability_alert`() → bool¶

     Calls:| GET /repos/{owner}/{repo}/vulnerability-alerts  
---|---  
Return type:| bool  
  
`enable_vulnerability_alert`() → bool¶

     Calls:| PUT /repos/{owner}/{repo}/vulnerability-alerts  
---|---  
Return type:| bool  
  
`disable_vulnerability_alert`() → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/vulnerability-alerts  
---|---  
Return type:| bool  
  
`enable_automated_security_fixes`() → bool¶

     Calls:| PUT /repos/{owner}/{repo}/automated-security-fixes  
---|---  
Return type:| bool  
  
`disable_automated_security_fixes`() → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/automated-security-fixes  
---|---  
Return type:| bool  
  
`remove_from_collaborators`( _collaborator: str | NamedUser_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/collaborators/{user}  
---|---  
Parameters:|  **collaborator** – string or `github.NamedUser.NamedUser`  
Return type:| None  
  
`remove_self_hosted_runner`( _runner: SelfHostedActionsRunner | int_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/actions/runners/{runner_id}  
---|---  
Parameters:|  **runner** – int or `github.SelfHostedActionsRunner.SelfHostedActionsRunner`  
Return type:| bool  
  
`remove_autolink`( _autolink: Autolink | int_ ) → bool¶

     Calls:| DELETE /repos/{owner}/{repo}/autolinks/{id}  
---|---  
Parameters:|  **autolink** – int or `github.Autolink.Autolink`  
Return type:| None  
  
`subscribe_to_hub`( _event: str_ , _callback: str_ , _secret: Union[str_ , _github.GithubObject._NotSetType] = NotSet_ ) → None¶

     Calls:| 

POST /hub  
  
---|---  
Parameters:|

  * **event** – string
  * **callback** – string
  * **secret** – string

  
Return type:|

None  
  
`unsubscribe_from_hub`( _event: str_ , _callback: str_ ) → None¶

     Calls:| 

POST /hub  
  
---|---  
Parameters:|

  * **event** – string
  * **callback** – string
  * **secret** – string

  
Return type:|

None  
  
`create_check_suite`( _head_sha: str_ ) → CheckSuite¶

     Calls:| POST /repos/{owner}/{repo}/check-suites  
---|---  
Parameters:|  **head_sha** – string  
Return type:| `github.CheckSuite.CheckSuite`  
  
`get_check_suite`( _check_suite_id: int_ ) → CheckSuite¶

     Calls:| GET /repos/{owner}/{repo}/check-suites/{check_suite_id}  
---|---  
Parameters:|  **check_suite_id** – int  
Return type:| `github.CheckSuite.CheckSuite`  
  
`update_check_suites_preferences`( _auto_trigger_checks: list[dict[str, bool | int]]_ ) → RepositoryPreferences¶

     Calls:| PATCH /repos/{owner}/{repo}/check-suites/preferences  
---|---  
Parameters:|  **auto_trigger_checks** – list of dict  
Return type:| `github.RepositoryPreferences.RepositoryPreferences`  
  
`create_check_run`( _name: str_ , _head_sha: str_ , _details_url: Opt[str] = NotSet_ , _external_id: Opt[str] = NotSet_ , _status: Opt[str] = NotSet_ , _started_at: Opt[datetime] = NotSet_ ,
_conclusion: Opt[str] = NotSet_ , _completed_at: Opt[datetime] = NotSet_ , _output: Opt[dict[str_ , _str | list[dict[str_ , _str | int]]]] = NotSet_ , _actions: Opt[list[dict[str_ , _str]]] = NotSet_
) → CheckRun¶

     Calls:| 

POST /repos/{owner}/{repo}/check-runs  
  
---|---  
Parameters:|

  * **name** – string
  * **head_sha** – string
  * **details_url** – string
  * **external_id** – string
  * **status** – string
  * **started_at** – datetime
  * **conclusion** – string
  * **completed_at** – datetime
  * **output** – dict
  * **actions** – list of dict

  
Return type:|

`github.CheckRun.CheckRun`  
  
`get_check_run`( _check_run_id: int_ ) → CheckRun¶

     Calls:| GET /repos/{owner}/{repo}/check-runs/{check_run_id}  
---|---  
Parameters:|  **check_run_id** – int  
Return type:| `github.CheckRun.CheckRun`  
  
`get_artifacts`( _name: Opt[str] = NotSet_ ) → PaginatedList[Artifact]¶

     Calls:| GET /repos/{owner}/{repo}/actions/artifacts  
---|---  
Parameters:|  **name** – str  
Return type:| `PaginatedList` of `github.Artifact.Artifact`  
  
`get_artifact`( _artifact_id: int_ ) → Artifact¶

     Calls:| GET /repos/{owner}/{repo}/actions/artifacts/{artifact_id}  
---|---  
Parameters:|  **artifact_id** – int  
Return type:| `github.Artifact.Artifact`  
  
`get_codescan_alerts`() → PaginatedList[CodeScanAlert]¶

     Calls:| GET https://api.github.com/repos/{owner}/{repo}/code-scanning/alerts  
---|---  
Return type:| `PaginatedList` of `github.CodeScanAlert.CodeScanAlert`  
  
`get_environments`() → PaginatedList[Environment]¶

     Calls:| GET /repos/{owner}/{repo}/environments  
---|---  
Return type:| `PaginatedList` of `github.Environment.Environment`  
  
`get_environment`( _environment_name: str_ ) → Environment¶

     Calls:| GET /repos/{owner}/{repo}/environments/{environment_name}  
---|---  
Return type:| `github.Environment.Environment`  
  
`create_environment`( _environment_name: str_ , _wait_timer: int = 0_ , _reviewers: list[ReviewerParams] = []_ , _deployment_branch_policy: EnvironmentDeploymentBranchPolicyParams | None = None_ ) →
Environment¶

     Calls:| 

PUT /repos/{owner}/{repo}/environments/{environment_name}  
  
---|---  
Parameters:|

  * **environment_name** – string
  * **wait_timer** – int
  * **reviews** – List[:class:github.EnvironmentDeploymentBranchPolicy.EnvironmentDeploymentBranchPolicyParams]
  * **deployment_branch_policy** – Optional[:class:github.EnvironmentDeploymentBranchPolicy.EnvironmentDeploymentBranchPolicyParams`]

  
Return type:|

`github.Environment.Environment`  
  
`update_environment`( _environment_name: str_ , _wait_timer: int = 0_ , _reviewers: list[ReviewerParams] = []_ , _deployment_branch_policy: EnvironmentDeploymentBranchPolicyParams | None = None_ ) →
Environment¶

     Calls:| 

PUT /repos/{owner}/{repo}/environments/{environment_name}  
  
---|---  
Parameters:|

  * **environment_name** – string
  * **wait_timer** – int
  * **reviews** – List[:class:github.EnvironmentDeploymentBranchPolicy.EnvironmentDeploymentBranchPolicyParams]
  * **deployment_branch_policy** – Optional[:class:github.EnvironmentDeploymentBranchPolicy.EnvironmentDeploymentBranchPolicyParams`]

  
Return type:|

`github.Environment.Environment`  
  
`delete_environment`( _environment_name: str_ ) → None¶

     Calls:| DELETE /repos/{owner}/{repo}/environments/{environment_name}  
---|---  
Parameters:|  **environment_name** – string  
Return type:| None  
  
Read the Docs v: stable

Versions

     latest
     stable
     v2.1.1
     v2.1.0.post0
     v2.1.0
     v2.0.1-preview
     v2.0.0-preview.1
     v2.0.0-preview
     v1.59.1
     v1.59.0
     v1.58.2
     v1.58.1
     v1.58.0
     v1.57

On Read the Docs

     Project Home
     Builds
     Downloads

On GitHub

     View

Search

    

* * *

Hosted by Read the Docs ·  Privacy Policy

