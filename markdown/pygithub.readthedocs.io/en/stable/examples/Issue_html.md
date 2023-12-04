  + Docs »
  + Examples »
  + Issues

* * *
# Issues¶

## Get issue¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.get_issue(number=874)
        Issue(title="PyGithub example usage", number=874)

```

[/code]

## Create comment on issue¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> issue = repo.get_issue(number=874)
    >>> issue.create_comment("Test")
        IssueComment(user=NamedUser(login="user"), id=36763078)

```

[/code]

## Create issue¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.create_issue(title="This is a new issue")
        Issue(title="This is a new issue", number=XXX)

```

[/code]

## Create issue with body¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.create_issue(title="This is a new issue", body="This is the issue body")
        Issue(title="This is a new issue", number=XXX)

```

[/code]

## Create issue with labels¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> label = repo.get_label("My Label")
    >>> repo.create_issue(title="This is a new issue", labels=[label])
        Issue(title="This is a new issue", number=XXX)

```

[/code]

## Create issue with assignee¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> repo.create_issue(title="This is a new issue", assignee="github-username")
        Issue(title="This is a new issue", number=XXX)

```

[/code]

## Create issue with milestone¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> milestone = repo.create_milestone("New Issue Milestone")
    >>> repo.create_issue(title="This is a new issue", milestone=milestone)
        Issue(title="This is a new issue", number=XXX)

```

[/code]

## Close all issues¶

[code]

```

    >>> repo = g.get_repo("PyGithub/PyGithub")
    >>> open_issues = repo.get_issues(state='open')
    >>> for issue in open_issues:
    ...     issue.edit(state='closed')

```

[/code]
