  + Docs »
  + Reference »
  + Utilities

* * *
# Utilities¶

## Logging¶

`github.`  `enable_console_debug_logging` () → None¶

This function sets up a very simple logging configuration (log everything on standard output) that is useful for troubleshooting.

## Error Handling¶

_exception_ `github.GithubException.`  `GithubException` ( _status: int_ , _data: Any = None_ , _headers: Optional[Dict[str_ , _str]] = None_ , _message: Optional[str] = None_ )¶

Error handling in PyGithub is done with exceptions. This class is the base of all exceptions raised by PyGithub (but `github.GithubException.BadAttributeException` ).

Some other types of exceptions might be raised by underlying libraries, for example for network-related issues.

`status` ¶

The status returned by the Github API

`data` ¶

The (decoded) data returned by the Github API

`headers` ¶

The headers returned by the Github API

_exception_ `github.GithubException.`  `BadCredentialsException` ( _status: int_ , _data: Any = None_ , _headers: Optional[Dict[str_ , _str]] = None_ , _message: Optional[str] = None_ )¶

Exception raised in case of bad credentials (when Github API replies with a 401 or 403 HTML status)

_exception_ `github.GithubException.`  `UnknownObjectException` ( _status: int_ , _data: Any = None_ , _headers: Optional[Dict[str_ , _str]] = None_ , _message: Optional[str] = None_ )¶

Exception raised when a non-existing object is requested (when Github API replies with a 404 HTML status)

_exception_ `github.GithubException.`  `BadUserAgentException` ( _status: int_ , _data: Any = None_ , _headers: Optional[Dict[str_ , _str]] = None_ , _message: Optional[str] = None_ )¶

Exception raised when request is sent with a bad user agent header (when Github API replies with a 403 bad user agent HTML status)

_exception_ `github.GithubException.`  `RateLimitExceededException` ( _status: int_ , _data: Any = None_ , _headers: Optional[Dict[str_ , _str]] = None_ , _message: Optional[str] = None_ )¶

Exception raised when the rate limit is exceeded (when Github API replies with a 403 rate limit exceeded HTML status)

_exception_ `github.GithubException.`  `BadAttributeException` ( _actualValue: Any, expectedType: Union[Dict[Tuple[Type[str], Type[str]], Type[dict]], Tuple[Type[str], Type[str]], List[Type[dict]], 
List[Tuple[Type[str], Type[str]]]], transformationException: Optional[Exception]_ )¶

Exception raised when Github returns an attribute with the wrong type.

`actual_value` ¶

The value returned by Github

`expected_type` ¶

The type PyGithub expected

`transformation_exception` ¶

The exception raised when PyGithub tried to parse the value

_exception_ `github.GithubException.`  `TwoFactorException` ( _status: int_ , _data: Any = None_ , _headers: Optional[Dict[str_ , _str]] = None_ , _message: Optional[str] = None_ )¶

Exception raised when Github requires a onetime password for two-factor authentication

_exception_ `github.GithubException.`  `IncompletableObject` ( _status: int_ , _data: Any = None_ , _headers: Optional[Dict[str_ , _str]] = None_ , _message: Optional[str] = None_ )¶

Exception raised when we can not request an object from Github because the data returned did not include a URL

## Default argument¶

`github.NotSet` is a special value for arguments you don’t want to provide. You should not have to manipulate it directly, because it’s the default value of all parameters accepting it. Just note that
it is different from `None` , which is an allowed value for some parameters.

## Pagination¶

_class_ `github.PaginatedList.`  `PaginatedList` ¶

This class abstracts the pagination of the API.

You can simply enumerate through instances of this class:

[code]

```python

    for repo in user.get_repos():
        print(repo.name)

```

[/code]

If you want to know the total number of items in the list:

[code]

```python

    print(user.get_repos().totalCount)

```

[/code]

You can also index them or take slices:

[code]

```python

    second_repo = user.get_repos()[1]
    first_repos = user.get_repos()[:10]

```

[/code]

If you want to iterate in reversed order, just do:

[code]

```python

    for repo in user.get_repos().reversed:
        print(repo.name)

```

[/code]

And if you really need it, you can explicitly access a specific page:

[code]

```python

    some_repos = user.get_repos().get_page(0)
    some_other_repos = user.get_repos().get_page(3)

```

[/code]

## Input classes¶

_class_ `github.InputFileContent.`  `InputFileContent` ( _content: str_ , _new_name: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ )¶

This class represents InputFileContents

_class_ `github.InputGitAuthor.`  `InputGitAuthor` ( _name: str_ , _email: str_ , _date: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ )¶

This class represents InputGitAuthors

_class_ `github.InputGitTreeElement.`  `InputGitTreeElement` ( _path: str_ , _mode: str_ , _type: str_ , _content: Opt[str] = NotSet_ , _sha: Opt[str | None] = NotSet_ )¶

This class represents InputGitTreeElements
