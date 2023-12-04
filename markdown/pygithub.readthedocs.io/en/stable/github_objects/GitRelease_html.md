  + GitRelease

* * *
# GitRelease¶

_class_ `github.GitRelease.`  `GitRelease` ¶

This class represents GitReleases. The reference can be found here https://docs.github.com/en/rest/reference/repos#releases

`delete_release` () → None¶

     Calls:| DELETE /repos/{owner}/{repo}/releases/{release_id}

---|---

`update_release` ( _name: str_ , _message: str_ , _draft: bool = False_ , _prerelease: bool = False_ , _tag_name: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _target_commitish:
Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) → github. GitRelease. GitRelease¶

     Calls:| PATCH /repos/{owner}/{repo}/releases/{release_id}

---|---

`upload_asset` ( _path: str_ , _label: str = ''_ , _content_type: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _name: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ ) →
github. GitReleaseAsset. GitReleaseAsset¶

     Calls:| POST https://<upload_url>/repos/{owner}/{repo}/releases/{release_id}/assets

---|---

`upload_asset_from_memory` ( _file_like: BinaryIO_ , _file_size: int_ , _name: str_ , _content_type: Union[str_ , _github. GithubObject._NotSetType] = NotSet_ , _label: str = ''_ ) →
github. GitReleaseAsset. GitReleaseAsset¶

Uploads an asset. Unlike `upload_asset()` this method allows you to pass in a file-like object to upload. Note that this method is more strict and requires you to specify the `name` , since there’s no
file name to infer these from. :calls: POST https://<upload_url>/repos/{owner}/{repo}/releases/{release_id}/assets :param file_like: binary file-like object, such as those returned by
`open("file_name", "rb")` . At the very minimum, this object must implement `read()` . :param file_size: int, size in bytes of `file_like`

`get_assets` () → github. PaginatedList. PaginatedList[github. GitReleaseAsset. GitReleaseAsset][github. GitReleaseAsset. GitReleaseAsset]¶

     Calls:| GET /repos/{owner}/{repo}/releases/{release_id}/assets

---|---
