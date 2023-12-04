  + GithubRetry

* * *
# GithubRetry¶

_class_ `github.GithubRetry.`  `GithubRetry` ¶

A Github-specific implementation of urllib3. Retry

This retries 403 responses if they are retry-able. Github requests are retry-able when the response provides a “Retry-After” header, or the content indicates a rate limit error.

By default, response codes 403, and 500 up to 599 are retried. This can be configured via the status_forcelist argument.

By default, all methods defined in Retry. DEFAULT_ALLOWED_METHODS are retried, plus GET and POST. This can be configured via the allowed_methods argument.

Parameters:|

  + **secondary_rate_wait** – seconds to wait before retrying secondary rate limit errors
  + **kwargs** – see urllib3. Retry for more arguments

---|---

`increment` ( _method: Optional[str] = None_ , _url: Optional[str] = None_ , _response: Optional[urllib3.response. HTTPResponse] = None_ , _error: Optional[Exception] = None_ , __pool:
Optional[urllib3.connectionpool. ConnectionPool] = None_ , __stacktrace: Optional[traceback] = None_ ) → urllib3.util.retry. Retry¶

Return a new Retry object with incremented retry counters.

Parameters:|

  + **response** (`BaseHTTPResponse`) – A response object, or None, if the server did not return a response.
  + **error** ( _Exception_ ) – An error encountered during the request, or None if the response was received successfully.

---|---
Returns:|

A new `Retry` object.
