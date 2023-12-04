  + Docs »
  + Reference »
  + Github objects

* * *
# Github objects¶

_class_ `github.GithubObject.`  `GithubObject` ¶

Base class for all classes representing objects returned by the API.

`raw_data` ¶

     Type:| dict

---|---

`raw_headers` ¶

     Type:| dict

---|---

`etag` ¶

     Type:| str

---|---

`last_modified` ¶

     Type:| str

---|---

`get__repr__` ( _params: Dict[str, Any]_ ) → str¶

Converts the object to a nicely printable string.

  + AccessToken
  + AppAuthentication
  + ApplicationOAuth
  + Artifact
  + Auth
  + AuthenticatedUser
  + Authorization
  + AuthorizationApplication
  + Autolink
  + Branch
  + BranchProtection
  + CWE
  + CheckRun
  + CheckRunAnnotation
  + CheckRunOutput
  + CheckSuite
  + Clones
  + CodeScanAlert
  + CodeScanAlertInstance
  + CodeScanAlertInstanceLocation
  + CodeScanRule
  + CodeScanTool
  + Commit
  + CommitCombinedStatus
  + CommitComment
  + CommitStats
  + CommitStatus
  + Comparison
  + ContentFile
  + Deployment
  + DeploymentStatus
  + Download
  + Enterprise
  + EnterpriseConsumedLicenses
  + Environment
  + EnvironmentDeploymentBranchPolicy
  + EnvironmentProtectionRule
  + EnvironmentProtectionRuleReviewer
  + Event
  + File
  + Gist
  + GistComment
  + GistFile
  + GistHistoryState
  + GitAuthor
  + GitBlob
  + GitCommit
  + GitObject
  + GitRef
  + GitRelease
  + GitReleaseAsset
  + GitTag
  + GitTree
  + GitTreeElement
  + GithubApp
  + GithubIntegration
  + GithubRetry
  + GitignoreTemplate
  + Hook
  + HookDelivery
  + HookDescription
  + HookResponse
  + Installation
  + InstallationAuthorization
  + Invitation
  + Issue
  + IssueComment
  + IssueEvent
  + IssuePullRequest
  + Label
  + License
  + Membership
  + Migration
  + Milestone
  + NamedEnterpriseUser
  + NamedUser
  + Notification
  + NotificationSubject
  + Organization
  + OrganizationSecret
  + OrganizationVariable
  + Path
  + Permissions
  + Plan
  + Project
  + ProjectCard
  + ProjectColumn
  + PublicKey
  + PullRequest
  + PullRequestComment
  + PullRequestMergeStatus
  + PullRequestPart
  + PullRequestReview
  + Rate
  + RateLimit
  + Reaction
  + Referrer
  + Repository
  + RepositoryAdvisory
  + RepositoryAdvisoryCredit
  + RepositoryAdvisoryCreditDetailed
  + RepositoryAdvisoryVulnerability
  + RepositoryAdvisoryVulnerabilityPackage
  + RepositoryKey
  + RepositoryPreferences
  + RequiredPullRequestReviews
  + RequiredStatusChecks
  + Secret
  + SelfHostedActionsRunner
  + SourceImport
  + Stargazer
  + StatsCodeFrequency
  + StatsCommitActivity
  + StatsContributor
  + StatsParticipation
  + StatsPunchCard
  + Tag
  + Team
  + TeamDiscussion
  + TimelineEvent
  + TimelineEventSource
  + Topic
  + UserKey
  + Variable
  + View
  + Workflow
  + WorkflowJob
  + WorkflowRun
  + WorkflowStep
