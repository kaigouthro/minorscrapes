  + Docs »
  + Reference »
  + APIs

* * *
# APIs¶
  + `/app`
    - GET: `github.GithubIntegration.GithubIntegration.get_app()` or `github.MainClass.Github.get_app()`
  + `/app/installations/{installation_id}`
    - GET: `github.GithubIntegration.GithubIntegration.get_app_installation()`
  + `/app/installations/{installation_id}/access_tokens`
    - POST: `github.GithubIntegration.GithubIntegration.get_access_token()`
  + `/apps/{slug}`
    - GET: `github.MainClass.Github.get_app()`
  + `/authorizations`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_authorizations()`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_authorization()`
  + `/authorizations/{id}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_authorization()`
    - PATCH: `github.Authorization.Authorization.edit()`
    - DELETE: `github.Authorization.Authorization.delete()`
  + `/emojis`
    - GET: `github.MainClass.Github.get_emojis()`
  + `/enterprises/{enterprise}`
    - GET: `github.MainClass.Github.get_enterprise()`
  + `/enterprises/{enterprise}/consumed-licenses`
    - GET: `github.Enterprise.Enterprise.get_consumed_licenses()` or `github.EnterpriseConsumedLicenses.EnterpriseConsumedLicenses.get_users()`
  + `/events`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_events()` or `github.MainClass.Github.get_events()`
  + `/gists`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_gists()`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_gist()`
  + `/gists/public`
    - GET: `github.MainClass.Github.get_gists()`
  + `/gists/starred`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_starred_gists()`
  + `/gists/{gist_id}/comments`
    - GET: `github.Gist.Gist.get_comments()`
    - POST: `github.Gist.Gist.create_comment()`
  + `/gists/{gist_id}/comments/{id}`
    - GET: `github.Gist.Gist.get_comment()`
    - PATCH: `github.GistComment.GistComment.edit()`
    - DELETE: `github.GistComment.GistComment.delete()`
  + `/gists/{id}`
    - GET: `github.MainClass.Github.get_gist()`
    - PATCH: `github.Gist.Gist.edit()`
    - DELETE: `github.Gist.Gist.delete()`
  + `/gists/{id}/forks`
    - POST: `github.Gist.Gist.create_fork()`
  + `/gists/{id}/star`
    - GET: `github.Gist.Gist.is_starred()`
    - PUT: `github.Gist.Gist.set_starred()`
    - DELETE: `github.Gist.Gist.reset_starred()`
  + `/gitignore/templates`
    - GET: `github.MainClass.Github.get_gitignore_templates()`
  + `/gitignore/templates/{name}`
    - GET: `github.MainClass.Github.get_gitignore_template()`
  + `/hooks`
    - GET: `github.MainClass.Github.get_hooks()`
  + `/hooks/{hook_id}/deliveries`
    - GET: `github.MainClass.Github.get_hook_deliveries()`
  + `/hooks/{hook_id}/deliveries/{delivery_id}`
    - GET: `github.MainClass.Github.get_hook_delivery()`
  + `/hooks/{name}`
    - GET: `github.MainClass.Github.get_hook()`
  + `/hub`
    - POST: `github.Repository.Repository.subscribe_to_hub()` or `github.Repository.Repository.unsubscribe_from_hub()`
  + `/installation/repositories`
    - GET: `github.Installation.Installation.get_repos()`
  + `/issues`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_issues()`
  + `/legacy/issues/search/{owner}/{repository}/{state}/{keyword}`
    - GET: `github.Repository.Repository.legacy_search_issues()`
  + `/license/{license}`
    - GET: `github.MainClass.Github.get_license()`
  + `/licenses`
    - GET: `github.MainClass.Github.get_licenses()`
  + `/login/oauth/access_token`
    - POST: `github.ApplicationOAuth.ApplicationOAuth.get_access_token()` or `github.ApplicationOAuth.ApplicationOAuth.refresh_access_token()`
  + `/markdown`
    - POST: `github.MainClass.Github.render_markdown()`
  + `/markdown/raw`
    - POST: Not implemented, see `/markdown`
  + `/networks/{owner}/{repo}/events`
    - GET: `github.Repository.Repository.get_network_events()`
  + `/notifications`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_notifications()`
    - PUT: `github.AuthenticatedUser.AuthenticatedUser.mark_notifications_as_read()`
  + `/notifications/threads/{id}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_notification()`
    - PATCH: `github.Notification.Notification.mark_as_read()`
  + `/organizations`
    - GET: `github.MainClass.Github.get_organizations()`
  + `/orgs/{org}`
    - GET: `github.MainClass.Github.get_organization()`
    - PATCH: `github.Organization.Organization.edit()`
  + `/orgs/{org}/actions/secrets/public-key`
    - GET: `github.Organization.Organization.get_public_key()`
  + `/orgs/{org}/actions/secrets/{secret_name}`
    - PUT: `github.Organization.Organization.create_secret()`
  + `/orgs/{org}/actions/secrets/{variable_name}`
    - PATCH: `github.OrganizationSecret.OrganizationSecret.edit()`
  + `/orgs/{org}/actions/variables/`
    - POST: `github.Organization.Organization.create_variable()`
  + `/orgs/{org}/actions/variables/{variable_name}`
    - PATCH: `github.OrganizationVariable.OrganizationVariable.edit()`
  + `/orgs/{org}/events`
    - GET: `github.Organization.Organization.get_events()`
  + `/orgs/{org}/installation`
    - GET: `github.GithubIntegration.GithubIntegration.get_org_installation()`
  + `/orgs/{org}/installations`
    - GET: `github.Organization.Organization.get_installations()`
  + `/orgs/{org}/invitations`
    - GET: `github.Organization.Organization.invitations()`
    - POST: `github.Organization.Organization.invite_user()`
  + `/orgs/{org}/invitations/{invitation_id}`
    - DELETE: `github.Organization.Organization.cancel_invitation()`
  + `/orgs/{org}/issues`
    - GET: `github.Organization.Organization.get_issues()`
  + `/orgs/{org}/members`
    - GET: `github.Organization.Organization.get_members()`
  + `/orgs/{org}/members/{user}`
    - GET: `github.Organization.Organization.has_in_members()`
    - DELETE: `github.Organization.Organization.remove_from_members()`
  + `/orgs/{org}/memberships/team/{team_id}/{username}`
    - GET: `github.Team.Team.get_team_membership()`
  + `/orgs/{org}/memberships/{username}`
    - GET: `github.NamedUser.NamedUser.get_organization_membership()`
  + `/orgs/{org}/memberships/{user}`
    - PUT: `github.Organization.Organization.add_to_members()`
    - DELETE: `github.Organization.Organization.remove_from_membership()`
  + `/orgs/{org}/migrations`
    - GET: `github.Organization.Organization.get_migrations()`
    - POST: `github.Organization.Organization.create_migration()`
  + `/orgs/{org}/outside_collaborators`
    - GET: `github.Organization.Organization.get_outside_collaborators()`
  + `/orgs/{org}/outside_collaborators/{username}`
    - PUT: `github.Organization.Organization.convert_to_outside_collaborator()`
    - DELETE: `github.Organization.Organization.remove_outside_collaborator()`
  + `/orgs/{org}/projects`
    - GET: `github.Organization.Organization.get_projects()`
    - POST: `github.Organization.Organization.create_project()`
  + `/orgs/{org}/public_members`
    - GET: `github.Organization.Organization.get_public_members()`
  + `/orgs/{org}/public_members/{user}`
    - GET: `github.Organization.Organization.has_in_public_members()`
    - PUT: `github.Organization.Organization.add_to_public_members()`
    - DELETE: `github.Organization.Organization.remove_from_public_members()`
  + `/orgs/{org}/repos`
    - GET: `github.Organization.Organization.get_repos()`
    - POST: `github.Organization.Organization.create_repo()`
  + `/orgs/{org}/teams`
    - GET: `github.Organization.Organization.get_teams()`
    - POST: `github.Organization.Organization.create_team()`
  + `/orgs/{org}/teams/{team_slug}`
    - GET: `github.Organization.Organization.get_team_by_slug()`
  + `/orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}`
    - PUT: `github.Team.Team.update_team_repository()`
  + `/orgs/{owner}/hooks`
    - GET: `github.Organization.Organization.get_hooks()`
    - POST: `github.Organization.Organization.create_hook()`
  + `/orgs/{owner}/hooks/{hook_id}/deliveries`
    - GET: `github.Organization.Organization.get_hook_deliveries()`
  + `/orgs/{owner}/hooks/{hook_id}/deliveries/{delivery_id}`
    - GET: `github.Organization.Organization.get_hook_delivery()`
  + `/orgs/{owner}/hooks/{id}`
    - GET: `github.Organization.Organization.get_hook()`
    - PATCH: `github.Organization.Organization.edit_hook()`
    - DELETE: `github.Organization.Organization.delete_hook()`
  + `/projects/columns/cards/{card_id}`
    - PATCH: `github.ProjectCard.ProjectCard.edit()`
    - DELETE: `github.ProjectCard.ProjectCard.delete()`
  + `/projects/columns/cards/{card_id}/moves`
    - POST: `github.ProjectCard.ProjectCard.move()`
  + `/projects/columns/{column_id}`
    - GET: `github.MainClass.Github.get_project_column()`
    - PATCH: `github.ProjectColumn.ProjectColumn.edit()`
    - DELETE: `github.ProjectColumn.ProjectColumn.delete()`
  + `/projects/columns/{column_id}/cards`
    - GET: `github.ProjectColumn.ProjectColumn.get_cards()`
    - POST: `github.ProjectColumn.ProjectColumn.create_card()`
  + `/projects/{project_id}`
    - GET: `github.MainClass.Github.get_project()`
    - PATCH: `github.Project.Project.edit()`
    - DELETE: `github.Project.Project.delete()`
  + `/projects/{project_id}/columns`
    - GET: `github.Project.Project.get_columns()`
  + `/rate_limit`
    - GET: Not implemented, see Github.rate_limiting
  + `/reactions/{id}`
    - DELETE: `github.Reaction.Reaction.delete()`
  + `/repos/:owner/:repo/pulls/:number/reviews/:review_id`
    - DELETE: `github.PullRequestReview.PullRequestReview.delete()`
  + `/repos/{owner}/deployments/{deployment_id}/statuses`
    - GET: `github.Deployment.Deployment.get_statuses()`
  + `/repos/{owner}/deployments/{deployment_id}/statuses/{status_id}`
    - GET: `github.Deployment.Deployment.get_status()`
  + `/repos/{owner}/{repo}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_repo()` or `github.MainClass.Github.get_repo()` or `github.NamedUser.NamedUser.get_repo()` or `github.Organization.Organization.get_repo()`
    - PATCH: `github.Repository.Repository.edit()`
    - DELETE: `github.Repository.Repository.delete()`
  + `/repos/{owner}/{repo}/actions/artifacts`
    - GET: `github.Repository.Repository.get_artifacts()`
  + `/repos/{owner}/{repo}/actions/artifacts/{artifact_id}`
    - GET: `github.Repository.Repository.get_artifact()`
    - DELETE: `github.Artifact.Artifact.delete()`
  + `/repos/{owner}/{repo}/actions/runners`
    - GET: `github.Repository.Repository.get_self_hosted_runners()`
  + `/repos/{owner}/{repo}/actions/runners/{id}`
    - GET: `github.Repository.Repository.get_self_hosted_runner()`
  + `/repos/{owner}/{repo}/actions/runners/{runner_id}`
    - DELETE: `github.Repository.Repository.remove_self_hosted_runner()`
  + `/repos/{owner}/{repo}/actions/runs`
    - GET: `github.Repository.Repository.get_workflow_runs()`
  + `/repos/{owner}/{repo}/actions/runs/{run_id}`
    - GET: `github.Repository.Repository.get_workflow_run()`
    - DELETE: `github.WorkflowRun.WorkflowRun.delete()`
  + `/repos/{owner}/{repo}/actions/runs/{run_id}/cancel`
    - POST: `github.WorkflowRun.WorkflowRun.cancel()`
  + `/repos/{owner}/{repo}/actions/runs/{run_id}/rerun`
    - POST: `github.WorkflowRun.WorkflowRun.rerun()`
  + `/repos/{owner}/{repo}/actions/runs/{run_id}/timing`
    - GET: `github.WorkflowRun.WorkflowRun.timing()`
  + `/repos/{owner}/{repo}/actions/secrets/public-key`
    - GET: `github.Repository.Repository.get_public_key()`
  + `/repos/{owner}/{repo}/actions/secrets/{secret_name}`
    - PUT: `github.Repository.Repository.create_secret()`
    - DELETE: `github.Repository.Repository.delete_secret()`
  + `/repos/{owner}/{repo}/actions/variables/{variable_name}`
    - PATCH: `github.Variable.Variable.edit()`
    - POST: `github.Repository.Repository.create_variable()`
    - DELETE: `github.Repository.Repository.delete_variable()`
  + `/repos/{owner}/{repo}/actions/workflows`
    - GET: `github.Repository.Repository.get_workflows()`
  + `/repos/{owner}/{repo}/actions/workflows/{workflow_id}`
    - GET: `github.Repository.Repository.get_workflow()`
  + `/repos/{owner}/{repo}/actions/workflows/{workflow_id}/dispatches`
    - POST: `github.Workflow.Workflow.create_dispatch()`
  + `/repos/{owner}/{repo}/actions/workflows/{workflow_id}/runs`
    - GET: `github.Workflow.Workflow.get_runs()`
  + `/repos/{owner}/{repo}/assignees`
    - GET: `github.Repository.Repository.get_assignees()`
  + `/repos/{owner}/{repo}/assignees/{assignee}`
    - GET: `github.Repository.Repository.has_in_assignees()`
  + `/repos/{owner}/{repo}/autolinks`
    - GET: `github.Repository.Repository.get_autolinks()`
    - POST: `github.Repository.Repository.create_autolink()`
  + `/repos/{owner}/{repo}/autolinks/{id}`
    - DELETE: `github.Repository.Repository.remove_autolink()`
  + `/repos/{owner}/{repo}/automated-security-fixes`
    - PUT: `github.Repository.Repository.enable_automated_security_fixes()`
    - DELETE: `github.Repository.Repository.disable_automated_security_fixes()`
  + `/repos/{owner}/{repo}/branches`
    - GET: `github.Repository.Repository.get_branches()`
  + `/repos/{owner}/{repo}/branches/{branch}`
    - GET: `github.Repository.Repository.get_branch()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection`
    - GET: `github.Branch.Branch.get_protection()`
    - PUT: `github.Branch.Branch.edit_protection()`
    - DELETE: `github.Branch.Branch.remove_protection()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection/enforce_admins`
    - GET: `github.Branch.Branch.get_admin_enforcement()`
    - POST: `github.Branch.Branch.set_admin_enforcement()`
    - DELETE: `github.Branch.Branch.remove_admin_enforcement()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection/required_pull_request_reviews`
    - GET: `github.Branch.Branch.get_required_pull_request_reviews()`
    - PATCH: `github.Branch.Branch.edit_required_pull_request_reviews()`
    - DELETE: `github.Branch.Branch.remove_required_pull_request_reviews()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection/required_signatures`
    - GET: `github.Branch.Branch.get_required_signatures()`
    - POST: `github.Branch.Branch.add_required_signatures()`
    - DELETE: `github.Branch.Branch.remove_required_signatures()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection/required_status_checks`
    - GET: `github.Branch.Branch.get_required_status_checks()`
    - PATCH: `github.Branch.Branch.edit_required_status_checks()`
    - DELETE: `github.Branch.Branch.remove_required_status_checks()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection/restrictions`
    - DELETE: `github.Branch.Branch.remove_push_restrictions()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/teams`
    - GET: `github.Branch.Branch.get_team_push_restrictions()`
    - POST: `github.Branch.Branch.add_team_push_restrictions()`
    - PUT: `github.Branch.Branch.replace_team_push_restrictions()`
    - DELETE: `github.Branch.Branch.remove_team_push_restrictions()`
  + `/repos/{owner}/{repo}/branches/{branch}/protection/restrictions/users`
    - GET: `github.Branch.Branch.get_user_push_restrictions()`
    - POST: `github.Branch.Branch.add_user_push_restrictions()`
    - PUT: `github.Branch.Branch.replace_user_push_restrictions()`
    - DELETE: `github.Branch.Branch.remove_user_push_restrictions()`
  + `/repos/{owner}/{repo}/branches/{branch}/rename`
    - POST: `github.Repository.Repository.rename_branch()`
  + `/repos/{owner}/{repo}/check-runs`
    - POST: `github.Repository.Repository.create_check_run()`
  + `/repos/{owner}/{repo}/check-runs/{check_run_id}`
    - GET: `github.Repository.Repository.get_check_run()`
    - PATCH: `github.CheckRun.CheckRun.edit()`
  + `/repos/{owner}/{repo}/check-runs/{check_run_id}/annotations`
    - GET: `github.CheckRun.CheckRun.get_annotations()`
  + `/repos/{owner}/{repo}/check-suites`
    - POST: `github.Repository.Repository.create_check_suite()`
  + `/repos/{owner}/{repo}/check-suites/preferences`
    - PATCH: `github.Repository.Repository.update_check_suites_preferences()`
  + `/repos/{owner}/{repo}/check-suites/{check_suite_id}`
    - GET: `github.Repository.Repository.get_check_suite()`
  + `/repos/{owner}/{repo}/check-suites/{check_suite_id}/check-runs`
    - GET: `github.CheckSuite.CheckSuite.get_check_runs()`
  + `/repos/{owner}/{repo}/check-suites/{check_suite_id}/rerequest`
    - POST: `github.CheckSuite.CheckSuite.rerequest()`
  + `/repos/{owner}/{repo}/collaborators`
    - GET: `github.Repository.Repository.get_collaborators()`
  + `/repos/{owner}/{repo}/collaborators/{username}/permission`
    - GET: `github.Repository.Repository.get_collaborator_permission()`
  + `/repos/{owner}/{repo}/collaborators/{user}`
    - GET: `github.Repository.Repository.has_in_collaborators()`
    - PUT: `github.Repository.Repository.add_to_collaborators()`
    - DELETE: `github.Repository.Repository.remove_from_collaborators()`
  + `/repos/{owner}/{repo}/comments`
    - GET: `github.Repository.Repository.get_comments()`
  + `/repos/{owner}/{repo}/comments/{comment_id}/reactions/{reaction_id}`
    - DELETE: `github.CommitComment.CommitComment.delete_reaction()`
  + `/repos/{owner}/{repo}/comments/{id}`
    - GET: `github.Repository.Repository.get_comment()`
    - PATCH: `github.CommitComment.CommitComment.edit()`
    - DELETE: `github.CommitComment.CommitComment.delete()`
  + `/repos/{owner}/{repo}/comments/{id}/reactions`
    - GET: `github.CommitComment.CommitComment.get_reactions()`
    - POST: `github.CommitComment.CommitComment.create_reaction()`
  + `/repos/{owner}/{repo}/commits`
    - GET: `github.Repository.Repository.get_commits()`
  + `/repos/{owner}/{repo}/commits/{ref}/status/`
    - GET: `github.Commit.Commit.get_combined_status()`
  + `/repos/{owner}/{repo}/commits/{sha}`
    - GET: `github.Repository.Repository.get_commit()`
  + `/repos/{owner}/{repo}/commits/{sha}/check-runs`
    - GET: `github.Commit.Commit.get_check_runs()`
  + `/repos/{owner}/{repo}/commits/{sha}/comments`
    - GET: `github.Commit.Commit.get_comments()`
    - POST: `github.Commit.Commit.create_comment()`
  + `/repos/{owner}/{repo}/commits/{sha}/pulls`
    - GET: `github.Commit.Commit.get_pulls()`
  + `/repos/{owner}/{repo}/compare/{base...:head}`
    - GET: `github.Repository.Repository.compare()`
  + `/repos/{owner}/{repo}/contents/{path}`
    - GET: `github.Repository.Repository.get_contents()` or `github.Repository.Repository.get_dir_contents()`
    - PUT: `github.Repository.Repository.create_file()` or `github.Repository.Repository.update_file()`
    - DELETE: `github.Repository.Repository.delete_file()`
  + `/repos/{owner}/{repo}/contributors`
    - GET: `github.Repository.Repository.get_contributors()`
  + `/repos/{owner}/{repo}/deployments`
    - GET: `github.Repository.Repository.get_deployments()`
    - POST: `github.Repository.Repository.create_deployment()`
  + `/repos/{owner}/{repo}/deployments/{deployment_id}`
    - GET: `github.Repository.Repository.get_deployment()`
  + `/repos/{owner}/{repo}/deployments/{deployment_id}/statuses`
    - POST: `github.Deployment.Deployment.create_status()`
  + `/repos/{owner}/{repo}/downloads`
    - GET: `github.Repository.Repository.get_downloads()`
  + `/repos/{owner}/{repo}/downloads/{id}`
    - GET: `github.Repository.Repository.get_download()`
    - DELETE: `github.Download.Download.delete()`
  + `/repos/{owner}/{repo}/environments`
    - GET: `github.Repository.Repository.get_environments()`
  + `/repos/{owner}/{repo}/environments/{environment_name}`
    - GET: `github.Repository.Repository.get_environment()`
    - PUT: `github.Repository.Repository.create_environment()`
    - DELETE: `github.Repository.Repository.delete_environment()`
  + `/repos/{owner}/{repo}/events`
    - GET: `github.Repository.Repository.get_events()`
  + `/repos/{owner}/{repo}/forks`
    - GET: `github.Repository.Repository.get_forks()`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_fork()` or `github.Organization.Organization.create_fork()` or `github.Repository.Repository.create_fork()`
  + `/repos/{owner}/{repo}/git/blobs`
    - POST: `github.Repository.Repository.create_git_blob()`
  + `/repos/{owner}/{repo}/git/blobs/{sha}`
    - GET: `github.Repository.Repository.get_git_blob()`
  + `/repos/{owner}/{repo}/git/commits`
    - POST: `github.Repository.Repository.create_git_commit()`
  + `/repos/{owner}/{repo}/git/commits/{sha}`
    - GET: `github.Repository.Repository.get_git_commit()`
  + `/repos/{owner}/{repo}/git/matching-refs/{ref}`
    - GET: `github.Repository.Repository.get_git_matching_refs()`
  + `/repos/{owner}/{repo}/git/refs`
    - GET: `github.Repository.Repository.get_git_refs()`
    - POST: `github.Repository.Repository.create_git_ref()`
  + `/repos/{owner}/{repo}/git/refs/{ref}`
    - GET: `github.Repository.Repository.get_git_ref()`
    - PATCH: `github.GitRef.GitRef.edit()`
    - DELETE: `github.GitRef.GitRef.delete()`
  + `/repos/{owner}/{repo}/git/tags`
    - POST: `github.Repository.Repository.create_git_tag()`
  + `/repos/{owner}/{repo}/git/tags/{sha}`
    - GET: `github.Repository.Repository.get_git_tag()`
  + `/repos/{owner}/{repo}/git/trees`
    - POST: `github.Repository.Repository.create_git_tree()`
  + `/repos/{owner}/{repo}/git/trees/{sha}`
    - GET: `github.Repository.Repository.get_git_tree()`
  + `/repos/{owner}/{repo}/hooks`
    - GET: `github.Repository.Repository.get_hooks()`
    - POST: `github.Repository.Repository.create_hook()`
  + `/repos/{owner}/{repo}/hooks/{hook_id}/deliveries`
    - GET: `github.Repository.Repository.get_hook_deliveries()`
  + `/repos/{owner}/{repo}/hooks/{hook_id}/deliveries/{delivery_id}`
    - GET: `github.Repository.Repository.get_hook_delivery()`
  + `/repos/{owner}/{repo}/hooks/{id}`
    - GET: `github.Repository.Repository.get_hook()`
    - PATCH: `github.Hook.Hook.edit()`
    - DELETE: `github.Hook.Hook.delete()`
  + `/repos/{owner}/{repo}/hooks/{id}/pings`
    - POST: `github.Hook.Hook.ping()`
  + `/repos/{owner}/{repo}/hooks/{id}/tests`
    - POST: `github.Hook.Hook.test()`
  + `/repos/{owner}/{repo}/import`
    - GET: `github.Repository.Repository.get_source_import()`
    - PUT: `github.Repository.Repository.create_source_import()`
  + `/repos/{owner}/{repo}/installation`
    - GET: `github.GithubIntegration.GithubIntegration.get_installation()` or `github.GithubIntegration.GithubIntegration.get_repo_installation()`
  + `/repos/{owner}/{repo}/invitations`
    - GET: `github.Repository.Repository.get_pending_invitations()`
  + `/repos/{owner}/{repo}/invitations/{invitation_id}`
    - DELETE: `github.Repository.Repository.remove_invitation()`
  + `/repos/{owner}/{repo}/issues`
    - GET: `github.Repository.Repository.get_issues()`
    - POST: `github.Repository.Repository.create_issue()`
  + `/repos/{owner}/{repo}/issues/comments`
    - GET: `github.Repository.Repository.get_issues_comments()`
  + `/repos/{owner}/{repo}/issues/comments/{comment_id}/reactions/{reaction_id}`
    - DELETE: `github.IssueComment.IssueComment.delete_reaction()`
  + `/repos/{owner}/{repo}/issues/comments/{id}`
    - GET: `github.Issue.Issue.get_comment()` or `github.PullRequest.PullRequest.get_issue_comment()`
    - PATCH: `github.IssueComment.IssueComment.edit()`
    - DELETE: `github.IssueComment.IssueComment.delete()`
  + `/repos/{owner}/{repo}/issues/comments/{id}/reactions`
    - GET: `github.IssueComment.IssueComment.get_reactions()`
    - POST: `github.IssueComment.IssueComment.create_reaction()`
  + `/repos/{owner}/{repo}/issues/events`
    - GET: `github.Repository.Repository.get_issues_events()`
  + `/repos/{owner}/{repo}/issues/events/{id}`
    - GET: `github.Repository.Repository.get_issues_event()`
  + `/repos/{owner}/{repo}/issues/{issue_number}/events`
    - GET: `github.Issue.Issue.get_events()` or `github.PullRequest.PullRequest.get_issue_events()`
  + `/repos/{owner}/{repo}/issues/{issue_number}/lock`
    - PUT: `github.Issue.Issue.lock()`
    - DELETE: `github.Issue.Issue.unlock()`
  + `/repos/{owner}/{repo}/issues/{issue_number}/reactions/{reaction_id}`
    - DELETE: `github.Issue.Issue.delete_reaction()`
  + `/repos/{owner}/{repo}/issues/{number}`
    - GET: `github.PullRequest.PullRequest.as_issue()` or `github.Repository.Repository.get_issue()`
    - PATCH: `github.Issue.Issue.edit()`
  + `/repos/{owner}/{repo}/issues/{number}/assignees`
    - POST: `github.Issue.Issue.add_to_assignees()` or `github.PullRequest.PullRequest.add_to_assignees()`
    - DELETE: `github.Issue.Issue.remove_from_assignees()` or `github.PullRequest.PullRequest.remove_from_assignees()`
  + `/repos/{owner}/{repo}/issues/{number}/comments`
    - GET: `github.Issue.Issue.get_comments()` or `github.PullRequest.PullRequest.get_issue_comments()`
    - POST: `github.Issue.Issue.create_comment()` or `github.PullRequest.PullRequest.create_issue_comment()`
  + `/repos/{owner}/{repo}/issues/{number}/labels`
    - GET: `github.Issue.Issue.get_labels()` or `github.PullRequest.PullRequest.get_labels()`
    - POST: `github.Issue.Issue.add_to_labels()` or `github.PullRequest.PullRequest.add_to_labels()`
    - PUT: `github.Issue.Issue.set_labels()` or `github.PullRequest.PullRequest.set_labels()`
    - DELETE: `github.Issue.Issue.delete_labels()` or `github.PullRequest.PullRequest.delete_labels()`
  + `/repos/{owner}/{repo}/issues/{number}/labels/{name}`
    - DELETE: `github.Issue.Issue.remove_from_labels()` or `github.PullRequest.PullRequest.remove_from_labels()`
  + `/repos/{owner}/{repo}/issues/{number}/reactions`
    - GET: `github.Issue.Issue.get_reactions()`
    - POST: `github.Issue.Issue.create_reaction()`
  + `/repos/{owner}/{repo}/issues/{number}/timeline`
    - GET: `github.Issue.Issue.get_timeline()`
  + `/repos/{owner}/{repo}/keys`
    - GET: `github.Repository.Repository.get_keys()`
    - POST: `github.Repository.Repository.create_key()`
  + `/repos/{owner}/{repo}/keys/{id}`
    - GET: `github.Repository.Repository.get_key()`
    - DELETE: `github.RepositoryKey.RepositoryKey.delete()`
  + `/repos/{owner}/{repo}/labels`
    - GET: `github.Repository.Repository.get_labels()`
    - POST: `github.Repository.Repository.create_label()`
  + `/repos/{owner}/{repo}/labels/{name}`
    - GET: `github.Repository.Repository.get_label()`
    - PATCH: `github.Label.Label.edit()`
    - DELETE: `github.Label.Label.delete()`
  + `/repos/{owner}/{repo}/languages`
    - GET: `github.Repository.Repository.get_languages()`
  + `/repos/{owner}/{repo}/license`
    - GET: `github.Repository.Repository.get_license()`
  + `/repos/{owner}/{repo}/merges`
    - POST: `github.Repository.Repository.merge()`
  + `/repos/{owner}/{repo}/milestones`
    - GET: `github.Repository.Repository.get_milestones()`
    - POST: `github.Repository.Repository.create_milestone()`
  + `/repos/{owner}/{repo}/milestones/{number}`
    - GET: `github.Repository.Repository.get_milestone()`
    - PATCH: `github.Milestone.Milestone.edit()`
    - DELETE: `github.Milestone.Milestone.delete()`
  + `/repos/{owner}/{repo}/milestones/{number}/labels`
    - GET: `github.Milestone.Milestone.get_labels()`
  + `/repos/{owner}/{repo}/notifications`
    - GET: `github.Repository.Repository.get_notifications()`
    - PUT: `github.Repository.Repository.mark_notifications_as_read()`
  + `/repos/{owner}/{repo}/projects`
    - GET: `github.Repository.Repository.get_projects()`
    - POST: `github.Repository.Repository.create_project()`
  + `/repos/{owner}/{repo}/pulls`
    - GET: `github.Repository.Repository.get_pulls()`
    - POST: `github.Repository.Repository.create_pull()`
  + `/repos/{owner}/{repo}/pulls/comments`
    - GET: `github.Repository.Repository.get_pulls_comments()` or `github.Repository.Repository.get_pulls_review_comments()`
  + `/repos/{owner}/{repo}/pulls/comments/{comment_id}/reactions/{reaction_id}`
    - DELETE: `github.PullRequestComment.PullRequestComment.delete_reaction()`
  + `/repos/{owner}/{repo}/pulls/comments/{number}`
    - GET: `github.PullRequest.PullRequest.get_comment()` or `github.PullRequest.PullRequest.get_review_comment()`
    - PATCH: `github.PullRequestComment.PullRequestComment.edit()`
    - DELETE: `github.PullRequestComment.PullRequestComment.delete()`
  + `/repos/{owner}/{repo}/pulls/comments/{number}/reactions`
    - GET: `github.PullRequestComment.PullRequestComment.get_reactions()`
    - POST: `github.PullRequestComment.PullRequestComment.create_reaction()`
  + `/repos/{owner}/{repo}/pulls/{number}`
    - GET: `github.Issue.Issue.as_pull_request()` or `github.ProjectCard.ProjectCard.get_content()` or `github.Repository.Repository.get_pull()`
    - PATCH: `github.PullRequest.PullRequest.edit()`
  + `/repos/{owner}/{repo}/pulls/{number}/comments`
    - GET: `github.PullRequest.PullRequest.get_comments()` or `github.PullRequest.PullRequest.get_review_comments()`
    - POST: `github.PullRequest.PullRequest.create_comment()` or `github.PullRequest.PullRequest.create_review_comment()`
  + `/repos/{owner}/{repo}/pulls/{number}/commits`
    - GET: `github.PullRequest.PullRequest.get_commits()`
  + `/repos/{owner}/{repo}/pulls/{number}/files`
    - GET: `github.PullRequest.PullRequest.get_files()`
  + `/repos/{owner}/{repo}/pulls/{number}/merge`
    - GET: `github.PullRequest.PullRequest.is_merged()`
    - PUT: `github.PullRequest.PullRequest.merge()`
  + `/repos/{owner}/{repo}/pulls/{number}/requested_reviewers`
    - GET: `github.PullRequest.PullRequest.get_review_requests()`
    - POST: `github.PullRequest.PullRequest.create_review_request()`
    - DELETE: `github.PullRequest.PullRequest.delete_review_request()`
  + `/repos/{owner}/{repo}/pulls/{number}/review/{id}/comments`
    - GET: `github.PullRequest.PullRequest.get_single_review_comments()`
  + `/repos/{owner}/{repo}/pulls/{number}/reviews`
    - GET: `github.PullRequest.PullRequest.get_reviews()`
    - POST: `github.PullRequest.PullRequest.create_review()`
  + `/repos/{owner}/{repo}/pulls/{number}/reviews/{id}`
    - GET: `github.PullRequest.PullRequest.get_review()`
  + `/repos/{owner}/{repo}/pulls/{number}/reviews/{review_id}/dismissals`
    - PUT: `github.PullRequestReview.PullRequestReview.dismiss()`
  + `/repos/{owner}/{repo}/pulls/{pull_number}/comments/{comment_id}/replies`
    - POST: `github.PullRequest.PullRequest.create_review_comment_reply()`
  + `/repos/{owner}/{repo}/readme`
    - GET: `github.Repository.Repository.get_readme()`
  + `/repos/{owner}/{repo}/releases`
    - GET: `github.Repository.Repository.get_releases()`
    - POST: `github.Repository.Repository.create_git_release()`
  + `/repos/{owner}/{repo}/releases/latest`
    - GET: `github.Repository.Repository.get_latest_release()`
  + `/repos/{owner}/{repo}/releases/{id}`
    - GET: `github.Repository.Repository.get_release()`
  + `/repos/{owner}/{repo}/releases/{release_id}`
    - PATCH: `github.GitRelease.GitRelease.update_release()`
    - DELETE: `github.GitRelease.GitRelease.delete_release()`
  + `/repos/{owner}/{repo}/releases/{release_id}/assets`
    - GET: `github.GitRelease.GitRelease.get_assets()`
  + `/repos/{owner}/{repo}/security-advisories`
    - GET: `github.Repository.Repository.get_repository_advisories()`
    - POST: `github.Repository.Repository.create_repository_advisory()`
  + `/repos/{owner}/{repo}/security-advisories/:advisory_id`
    - PATCH: `github.RepositoryAdvisory.RepositoryAdvisory.accept_report()` or `github.RepositoryAdvisory.RepositoryAdvisory.add_vulnerabilities()` or `github.RepositoryAdvisory.RepositoryAdvisory.add_vulnerability()` or `github.RepositoryAdvisory.RepositoryAdvisory.clear_credits()` or `github.RepositoryAdvisory.RepositoryAdvisory.close()` or `github.RepositoryAdvisory.RepositoryAdvisory.edit()` or `github.RepositoryAdvisory.RepositoryAdvisory.offer_credit()` or `github.RepositoryAdvisory.RepositoryAdvisory.offer_credits()` or `github.RepositoryAdvisory.RepositoryAdvisory.publish()` or `github.RepositoryAdvisory.RepositoryAdvisory.revoke_credit()`
  + `/repos/{owner}/{repo}/security-advisories/reports`
    - POST: `github.Repository.Repository.report_security_vulnerability()`
  + `/repos/{owner}/{repo}/security-advisories/{ghsa}`
    - GET: `github.Repository.Repository.get_repository_advisory()`
  + `/repos/{owner}/{repo}/stargazers`
    - GET: `github.Repository.Repository.get_stargazers_with_dates()` or `github.Repository.Repository.get_stargazers()`
  + `/repos/{owner}/{repo}/stats/code_frequency`
    - GET: `github.Repository.Repository.get_stats_code_frequency()`
  + `/repos/{owner}/{repo}/stats/commit_activity`
    - GET: `github.Repository.Repository.get_stats_commit_activity()`
  + `/repos/{owner}/{repo}/stats/contributors`
    - GET: `github.Repository.Repository.get_stats_contributors()`
  + `/repos/{owner}/{repo}/stats/participation`
    - GET: `github.Repository.Repository.get_stats_participation()`
  + `/repos/{owner}/{repo}/stats/punch_card`
    - GET: `github.Repository.Repository.get_stats_punch_card()`
  + `/repos/{owner}/{repo}/statuses/{ref}`
    - GET: `github.Commit.Commit.get_statuses()`
  + `/repos/{owner}/{repo}/statuses/{sha}`
    - POST: `github.Commit.Commit.create_status()`
  + `/repos/{owner}/{repo}/subscribers`
    - GET: `github.Repository.Repository.get_subscribers()`
  + `/repos/{owner}/{repo}/subscription`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.has_in_watched()`
    - PUT: `github.AuthenticatedUser.AuthenticatedUser.add_to_watched()`
    - DELETE: `github.AuthenticatedUser.AuthenticatedUser.remove_from_watched()`
  + `/repos/{owner}/{repo}/tags`
    - GET: `github.Repository.Repository.get_tags()`
  + `/repos/{owner}/{repo}/teams`
    - GET: `github.Repository.Repository.get_teams()`
  + `/repos/{owner}/{repo}/topics`
    - GET: `github.Repository.Repository.get_topics()`
    - PUT: `github.Repository.Repository.replace_topics()`
  + `/repos/{owner}/{repo}/traffic/clones`
    - GET: `github.Repository.Repository.get_clones_traffic()`
  + `/repos/{owner}/{repo}/traffic/popular/paths`
    - GET: `github.Repository.Repository.get_top_paths()`
  + `/repos/{owner}/{repo}/traffic/popular/referrers`
    - GET: `github.Repository.Repository.get_top_referrers()`
  + `/repos/{owner}/{repo}/traffic/views`
    - GET: `github.Repository.Repository.get_views_traffic()`
  + `/repos/{owner}/{repo}/vulnerability-alerts`
    - GET: `github.Repository.Repository.get_vulnerability_alert()`
    - PUT: `github.Repository.Repository.enable_vulnerability_alert()`
    - DELETE: `github.Repository.Repository.disable_vulnerability_alert()`
  + `/repos/{owner}/{repo}/watchers`
    - GET: `github.Repository.Repository.get_watchers()`
  + `/repos/{owner}/{repo}/{archive_format}/{ref}`
    - GET: `github.Repository.Repository.get_archive_link()`
  + `/repos/{template_owner}/{template_repo}/generate`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_repo_from_template()` or `github.Organization.Organization.create_repo_from_template()`
  + `/repositories`
    - GET: `github.MainClass.Github.get_repos()`
  + `/repositories/{id}`
    - GET: `github.MainClass.Github.get_repo()`
  + `/search/code`
    - GET: `github.MainClass.Github.search_code()`
  + `/search/commits`
    - GET: `github.MainClass.Github.search_commits()`
  + `/search/issues`
    - GET: `github.MainClass.Github.search_issues()`
  + `/search/repositories`
    - GET: `github.MainClass.Github.search_repositories()`
  + `/search/topics`
    - GET: `github.MainClass.Github.search_topics()`
  + `/search/users`
    - GET: `github.MainClass.Github.search_users()`
  + `/teams/{id}`
    - GET: `github.Organization.Organization.get_team()`
    - PATCH: `github.Team.Team.edit()`
    - DELETE: `github.Team.Team.delete()`
  + `/teams/{id}/discussions`
    - GET: `github.Team.Team.get_discussions()`
  + `/teams/{id}/invitations`
    - GET: `github.Team.Team.invitations()`
  + `/teams/{id}/members`
    - GET: `github.Team.Team.get_members()`
  + `/teams/{id}/members/{user}`
    - GET: `github.Team.Team.has_in_members()`
    - PUT: `github.Team.Team.add_to_members()`
    - DELETE: `github.Team.Team.remove_from_members()`
  + `/teams/{id}/memberships/{user}`
    - PUT: `github.Team.Team.add_membership()`
  + `/teams/{id}/repos`
    - GET: `github.Team.Team.get_repos()`
  + `/teams/{id}/repos/{org}/{repo}`
    - GET: `github.Team.Team.get_repo_permission()`
    - PUT: `github.Team.Team.add_to_repos()` or `github.Team.Team.set_repo_permission()`
  + `/teams/{id}/repos/{owner}/{repo}`
    - GET: `github.Team.Team.has_in_repos()`
    - DELETE: `github.Team.Team.remove_from_repos()`
  + `/teams/{id}/teams`
    - GET: `github.Team.Team.get_teams()`
  + `/teams/{team_id}/memberships/{username}`
    - DELETE: `github.Team.Team.remove_membership()`
  + `/user`
    - GET: `github.MainClass.Github.get_user()`
    - PATCH: `github.AuthenticatedUser.AuthenticatedUser.edit()`
  + `/user/emails`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_emails()`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.add_to_emails()`
    - DELETE: `github.AuthenticatedUser.AuthenticatedUser.remove_from_emails()`
  + `/user/followers`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_followers()`
  + `/user/following`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_following()`
  + `/user/following/{user}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.has_in_following()`
    - PUT: `github.AuthenticatedUser.AuthenticatedUser.add_to_following()`
    - DELETE: `github.AuthenticatedUser.AuthenticatedUser.remove_from_following()`
  + `/user/installations`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_installations()`
  + `/user/issues`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_user_issues()`
  + `/user/keys`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_keys()`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_key()`
  + `/user/keys/{id}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_key()`
    - DELETE: `github.UserKey.UserKey.delete()`
  + `/user/memberships/orgs/{org}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_organization_membership()`
  + `/user/migrations`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_migrations()`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_migration()`
  + `/user/migrations/{migration_id}`
    - GET: `github.Migration.Migration.get_status()`
  + `/user/migrations/{migration_id}/archive`
    - GET: `github.Migration.Migration.get_archive_url()`
    - DELETE: `github.Migration.Migration.delete()`
  + `/user/migrations/{migration_id}/repos/{repo_name}/lock`
    - DELETE: `github.Migration.Migration.unlock_repo()`
  + `/user/orgs`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_orgs()`
  + `/user/projects`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_project()`
  + `/user/repos`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_repos()`
    - POST: `github.AuthenticatedUser.AuthenticatedUser.create_repo()`
  + `/user/repository_invitations`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_invitations()`
  + `/user/repository_invitations/{invitation_id}`
    - PATCH: `github.AuthenticatedUser.AuthenticatedUser.accept_invitation()`
  + `/user/starred`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_starred()`
  + `/user/starred/{owner}/{repo}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.has_in_starred()`
    - PUT: `github.AuthenticatedUser.AuthenticatedUser.add_to_starred()`
    - DELETE: `github.AuthenticatedUser.AuthenticatedUser.remove_from_starred()`
  + `/user/subscriptions`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_subscriptions()` or `github.AuthenticatedUser.AuthenticatedUser.get_watched()`
  + `/user/subscriptions/{owner}/{repo}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.has_in_subscriptions()`
    - PUT: `github.AuthenticatedUser.AuthenticatedUser.add_to_subscriptions()`
    - DELETE: `github.AuthenticatedUser.AuthenticatedUser.remove_from_subscriptions()`
  + `/user/teams`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_teams()`
  + `/user/{id}`
    - GET: `github.MainClass.Github.get_user_by_id()`
  + `/users`
    - GET: `github.MainClass.Github.get_users()`
  + `/users/{username}/installation`
    - GET: `github.GithubIntegration.GithubIntegration.get_user_installation()`
  + `/users/{user}`
    - GET: `github.MainClass.Github.get_user()`
  + `/users/{user}/events`
    - GET: `github.NamedUser.NamedUser.get_events()`
  + `/users/{user}/events/orgs/{org}`
    - GET: `github.AuthenticatedUser.AuthenticatedUser.get_organization_events()`
  + `/users/{user}/events/public`
    - GET: `github.NamedUser.NamedUser.get_public_events()`
  + `/users/{user}/followers`
    - GET: `github.NamedUser.NamedUser.get_followers()`
  + `/users/{user}/following`
    - GET: `github.NamedUser.NamedUser.get_following()`
  + `/users/{user}/following/{target_user}`
    - GET: `github.NamedUser.NamedUser.has_in_following()`
  + `/users/{user}/gists`
    - GET: `github.NamedUser.NamedUser.get_gists()`
  + `/users/{user}/keys`
    - GET: `github.NamedUser.NamedUser.get_keys()`
  + `/users/{user}/orgs`
    - GET: `github.NamedUser.NamedUser.get_orgs()`
  + `/users/{user}/projects`
    - GET: `github.NamedUser.NamedUser.get_projects()`
  + `/users/{user}/received_events`
    - GET: `github.NamedUser.NamedUser.get_received_events()`
  + `/users/{user}/received_events/public`
    - GET: `github.NamedUser.NamedUser.get_public_received_events()`
  + `/users/{user}/repos`
    - GET: `github.NamedUser.NamedUser.get_repos()`
  + `/users/{user}/starred`
    - GET: `github.NamedUser.NamedUser.get_starred()`
  + `/users/{user}/subscriptions`
    - GET: `github.NamedUser.NamedUser.get_subscriptions()`
  + `/users/{user}/watched`
    - GET: `github.NamedUser.NamedUser.get_watched()`
  + `POST`
    - POST: `github.ProjectColumn.ProjectColumn.move()`
  + `https://<upload_url>/repos/{owner}/{repo}/releases/{release_id}/assets`
    - POST: `github.GitRelease.GitRelease.upload_asset_from_memory()` or `github.GitRelease.GitRelease.upload_asset()`
  + `https://api.github.com/repos/{owner}/{repo}/code-scanning/alerts`
    - GET: `github.Repository.Repository.get_codescan_alerts()`
  + `on`
  + `{secret_url}`
    - DELETE: `github.Secret.Secret.delete()`
  + `{variable_url}`
    - DELETE: `github.Variable.Variable.delete()`
