

Skip to main content

# TOML

> TOML is a file format for configuration files. It is intended to be easy to read and write, and is designed to map unambiguously to a dictionary. Its specification is open-source. `TOML` is
> implemented in many programming languages. The name `TOML` is an acronym for "Tom's Obvious, Minimal Language" referring to its creator, Tom Preston-Werner.

If you need to load `Toml` files, use the `TomlLoader`.

[code]
```python




    from langchain.document_loaders import TomlLoader  
    


```
[/code]


[code]
```python




    loader = TomlLoader("example_data/fake_rule.toml")  
    


```
[/code]


[code]
```python




    rule = loader.load()  
    


```
[/code]


[code]
```python




    rule  
    


```
[/code]


[code]
```python




        [Document(page_content='{"internal": {"creation_date": "2023-05-01", "updated_date": "2022-05-01", "release": ["release_type"], "min_endpoint_version": "some_semantic_version", "os_list": ["operating_system_list"]}, "rule": {"uuid": "some_uuid", "name": "Fake Rule Name", "description": "Fake description of rule", "query": "process where process.name : \\"somequery\\"\\n", "threat": [{"framework": "MITRE ATT&CK", "tactic": {"name": "Execution", "id": "TA0002", "reference": "https://attack.mitre.org/tactics/TA0002/"}}]}}', metadata={'source': 'example_data/fake_rule.toml'})]  
    


```
[/code]


